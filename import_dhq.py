#!/usr/bin/env python

import glob
import os.path
import subprocess
from pathlib import Path
import yaml


# make param
# use base path?
path = "../dhq-journal/articles/"


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
        completed = subprocess.run(["saxon", article, "tei-to-hugo.xslt"])
        if completed.returncode != 0:
            print("error transforming %s" % article)

        # create issue index files for each issue dir
        # create vol files for each vol
        # - use archetypes?


def to_hugo_metadata(info):
    return "---\n%s---\n\n" % yaml.safe_dump(info)


def create_issue_indexes():
    vol_index = "content/vol/_index.md"
    # if not os.path.exists(vol_index):
    # update whether exists it or not
    vol_index_info = {"title": "Volumes"}
    Path(vol_index).write_text(to_hugo_metadata(vol_index_info))

    # numeric volume dirs
    for voldir in Path("content/vol").iterdir():
        if voldir.is_dir():
            vol_number = int(os.path.basename(voldir))
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
                if issue.is_dir():
                    print(issue)
                    issue_index = issue / "_index.md"
                    issue_number = int(os.path.basename(issue))
                    issue_title = "%d.%d" % (vol_number, issue_number)
                    issue_info = {
                        "type": "issue",
                        "layout": "single",
                        "title": "Issue %s" % issue_title,
                        "number": issue_title,
                        # TODO: get date from articles
                    }
                    issue_index.write_text(to_hugo_metadata(issue_info))


if __name__ == "__main__":
    # convert_articles()
    create_issue_indexes()
