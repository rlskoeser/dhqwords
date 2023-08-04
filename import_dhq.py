#!/usr/bin/env python

import glob
import os.path
import shutil
import subprocess
from pathlib import Path
import yaml

from eulxml import xmlmap


# make param
# use base path?
path = "../dhq-journal/articles/"


class TocCluster(xmlmap.XmlObject):
    title = xmlmap.StringField("title", normalize=True)
    editors = xmlmap.StringField("editors", normalize=True)


class TocIssue(xmlmap.XmlObject):
    vol = xmlmap.StringField("@vol")
    issue = xmlmap.StringField("@issue")
    preview = xmlmap.StringField("@preview")
    title = xmlmap.StringField("title")
    clusters = xmlmap.NodeListField("cluster", TocCluster)


class DhqToc(xmlmap.XmlObject):
    issues = xmlmap.NodeListField("//journal", TocIssue)

    def get_issue(self, vol, issue):
        for i in self.issues:
            if i.vol == str(vol) and i.issue == str(issue):
                return i


def convert_articles():
    for article in glob.iglob(f"{path}/*/*.xml", recursive=True):
        print(article)
        # some articles have a duplicate, #### and ###_name.xml;
        # ignore the second file
        if "_" in article:
            print("Skipping %s" % article)
            continue
        # all 0s and almost all 9s are test articles
        article_id = os.path.splitext(os.path.basename(article))[0]
        if article_id == "000000" or article_id.startswith("999"):
            print("Skipping %s (test/template)" % article)
            continue

        # convert xslt to article markdown
        # completed = subprocess.run(["saxon", article, "tei-to-hugo.xslt"])
        completed = subprocess.run(
            ["node_modules/.bin/xslt3", "-s:%s" % article, "-xsl:tei-to-hugo.xslt"],
            capture_output=True,
            text=True,
        )
        if completed.returncode != 0:
            print("error transforming %s" % article)
        else:
            # print xslt output
            print(completed.stdout)
            article_resource_dir = os.path.join(os.path.dirname(article), "resources")
            if os.path.exists(article_resource_dir):
                print("resource directory %s exists" % article_resource_dir)

                lines = completed.stdout.split("\n")
                # xslt outputs markdown file(s); use to get directory
                try:
                    markdown_file = [l for l in lines if l.endswith(".md")][0]
                    output_dir = os.path.dirname(markdown_file)
                    print("markdown: %s; output_dir: %s" % (markdown_file, output_dir))
                    # for now, assume if it exists we already copied it
                    if not os.path.exists(output_dir):
                        # copy entire resource directory
                        shutil.copytree(
                            article_resource_dir, "%s/resources" % output_dir
                        )
                except IndexError:
                    print("** could not determine output directory")

        # create issue index files for each issue dir
        # create vol files for each vol
        # - use archetypes?


def to_hugo_metadata(info):
    return "---\n%s---\n\n" % yaml.safe_dump(info)


def create_issue_indexes():
    dhqtoc = xmlmap.load_xmlobject_from_file(
        "../dhq-journal/toc/toc.xml", xmlclass=DhqToc
    )

    vol_index = "content/vol/_index.md"
    # if not os.path.exists(vol_index):
    # update whether exists it or not
    vol_index_info = {"title": "Volumes"}
    Path(vol_index).write_text(to_hugo_metadata(vol_index_info))

    # numeric volume dirs
    for voldir in Path("content/vol").iterdir():
        if voldir.is_dir():
            try:
                vol_number = int(os.path.basename(voldir))
            except ValueError:
                # if not numeric, we don't want it
                # (NaN folder created from some articles; preview/vol unset?)
                print("removing %s" % voldir)
                shutil.rmtree(voldir)
                continue

            print(voldir, vol_number)
            vol_index = voldir / "_index.md"
            vol_info = {
                "title": "Volume %d" % vol_number,
                "volume": vol_number,
                # volume 1 was 2007; one volume per year
                # hugo needs a full date
                "date": "%s-01-01" % (vol_number + 2007 - 1,),
            }
            vol_index.write_text(to_hugo_metadata(vol_info))

            for issue in voldir.iterdir():
                # TODO: need to make translated issue indexes
                # for issues with articles in other languages
                if issue.is_dir():
                    print(issue)
                    # TODO: need an index for each language in the issue?
                    issue_index = issue / "_index.md"
                    issue_number = int(os.path.basename(issue))
                    issue_title = "%d.%d" % (vol_number, issue_number)
                    issue_info = {
                        "type": "issue",
                        "layout": "single",
                        "title": "Issue %s" % issue_title,
                        "number": issue_title,
                        # TODO: get actual date from articles?
                    }
                    tocinfo = dhqtoc.get_issue(vol_number, issue_number)
                    # get cluster and preview/draft from toc
                    if tocinfo:
                        if tocinfo.preview:
                            issue_info["draft"] = "true"
                        if tocinfo.clusters:
                            clusters = {}
                            theme = []
                            for i, c in enumerate(tocinfo.clusters):
                                theme.append(str(c.title))
                                # output a number for use in templates
                                clusters[f"{i + 1}"] = {
                                    "title": str(c.title),
                                    "editors": str(c.editors),
                                }

                            issue_info["clusters"] = clusters
                            # use cluser title(s) as issue theme
                            issue_info["theme"] = ", ".join(theme)
                    issue_index.write_text(to_hugo_metadata(issue_info))


if __name__ == "__main__":
    # convert_articles()  # NOTE: this is slow
    create_issue_indexes()
