---
type: article
dhqtype: article
title: "Reference Rot in the Digital Humanities Literature: An Analysis of Citations Containing Website Links in DHQ"
date: 2023-05-26
article_id: "000662"
volume: 017
issue: 1
authors:
- Zach Coble
- Jojo Karlin
translationType: original
categories:
- citation analysis
- information retrieval
- information standards
- publishing
tags:
- project resiliency
- link rot
- Digital Humanities Quarterly
abstract: |
   The ubiquity of the web has dramatically transformed scholarly communication. The shift toward digital publishing has brought great advantages, including an increased speed of knowledge dissemination and a greater uptake in open scholarship. There is also an increasing range of scholarly material being communicated and referenced. References have expanded beyond books and articles to include a broad array of assets consulted or created during the research process, such as datasets, social media content like tweets and blogs, and digital exhibitions. There are, however, numerous challenges posed by the transition to a constantly evolving digital scholarly infrastructure. This paper examines one of those challenges: link rot. Link rot is likely most familiar in the form of 404 Not Found error messages, but there are other less prominent obstacles to accessing web content. Our study examines instances of link rot in Digital Humanities Quarterly articles and its impact on the ability to access the online content referenced in these articles after their publication.
teaser: "Link rot in DHQ"
order: 9
cluster: "Project Resiliency"
---



## Introduction

The ubiquity of the web has dramatically transformed scholarly communication. The shift toward digital publishing has brought great advantages, including an increased speed of knowledge dissemination and a greater uptake in open scholarship. There is also an increasing range of scholarly material being communicated and referenced. References have expanded beyond books and articles to include a broad array of assets consulted or created during the research process, such as datasets, social media content like tweets and blogs, and digital exhibitions. There are, however, numerous challenges posed by the transition to a constantly evolving digital scholarly infrastructure. This paper examines one of those challenges: link rot, which serves as a way towards understanding its corollary, reference rot. Link rot is likely most familiar in the form of404 Not Founderror messages, but there are other less prominent obstacles to accessing web content. Our study examines instances of reference rot in _Digital Humanities Quarterly_ articles and its impact on the ability to access the online content referenced in these articles after their publication. We also look at the extent to which article references rely on links in order to gain a more complete understanding of the threat posed.

This study provides an important step in assessing remediative actions as well as a broader examination of perceptions of cohesion and integrity in the digital humanities literature. As the Endings Project team mentions in their DH2019 paper,HTML is the most popular standard output for DH projects,meaning that websites continue to be a key mechanism for delivering digital humanities (DH) outputs<a class="footnote-ref" href="#arneil2019"> [arneil2019] </a>. The ongoing costs and resources required to maintain and repair web-based DH outputs is well known, as shown by efforts such as the Endings Project and the Socio-Technical Sustainability Roadmap<a class="footnote-ref" href="#sociotechnical"> [sociotechnical] </a><a class="footnote-ref" href="#ending2022"> [ending2022] </a>. Our research contributes to this area of knowledge from a particular angle: the impact on the stability of the DH scholarly record.




## Literature Review

Looking at the literature, we observe three main categories relevant to this article: theory of citation, evolving guidelines for proper citation, and studies of the practice of link preservation. Citation theory describes the continuous tug between the ideals of citation and the disciplinary administrative function of scholarly discourse<a class="footnote-ref" href="#zuckerman1987"> [zuckerman1987] </a>. Broadly speaking, a reference is a piece of information provided in a scholarly work that specifies the work of another person used in the creation of the former. A citation is a paraphrase, quotation or allusion to a source, a specific instance of a reference such as a paraphrase or quotation. The scholarly literature rests on the premise that citations and references exist to pay homage and give credit to prior work, to substantiate claims and maintain intellectual honesty, and to provide leads and background reading<a class="footnote-ref" href="#garfield1994"> [garfield1994] </a>. Consequently, if readers cannot access the referenced material, then they are unable to uphold these standards or corroborate the scholarly record. The arguments of individual articles are weakened, and the integrity of the scholarly literature is threatened. Recent efforts have contributed critical approaches to citation theory, such as citation justice, that seek to expand understanding of social systems of credit within academia<a class="footnote-ref" href="#knowledgeequity"> [knowledgeequity] </a>.

Hyperlinks are a critical component of scholarly discourse in the digital era, and in the late 1990s and early 2000s, we see researchers beginning to adapt citation guidelines to accommodate new online resources. Janice Walker created MLA-Style Citations of Electronic Sources for referencing emerging formats such as Telnet, listservs, and video games<a class="footnote-ref" href="#walker1995"> [walker1995] </a>, whereas Anita Greenhill and Gordon Fletcher sought to catalog citation recommendations in the World Wide Web Virtual Library<a class="footnote-ref" href="#greenhill2003"> [greenhill2003] </a>, and the Library of Congress’sLearning Pagedemonstrates the concern for capturing appropriate links. Across disciplines, citation guidelines have grown to accommodate, and hustled to keep up with, shifts in web practices. As of the 7th edition, the APA Handbook ([2020](#apa2020)) offers examples for 27 types of electronic resources, from websites to Wikipedia to datasets to podcasts. This range of electronic resources points to the widening understanding of viable source materials as well as the complex set of standards that authors and stewards of scholarly output must reconcile.

In “Scholarly Context Not Found: One in Five Articles Suffers from Reference Rot,” <a class="footnote-ref" href="#klein2014"> [klein2014] </a>studied science, technology, and medicine articles to document the extent of reference rot, which they define as a combination of link rot and content drift. They define content drift as a resource changing or evolving over time, up to the point where it no longer reflects the originally referenced content. Attributing the lagging system of link preservation to the swift adoption of web-based scholarly communications, the expanding capacity to reference different types of things, and the challenge of bridging digital reference systems and paper-based communications, the authors call for robust solutions to ensure integrity of the web-based scholarly record. To Klein and co-authors, the integrity of the link maintains the context necessary to ensure sound scholarship, for “as references rot or as the content they originally referred to changes, it becomes impossible to revisit the intellectual context that surrounded the referencing article at the time of its publication” <a class="footnote-ref" href="#klein2014"> [klein2014] </a>.

Zhou et al.[2015](#zhou2015)studied the persistence of web resource citations by developing a machine-learning model for assessing link rot in scholarly articles. They propose establishing a system of priority for archival preservation of links by proactively predicting links more prone to rot.<a class="footnote-ref" href="#brunelle2015"> [brunelle2015] </a>attempt to measure the impact of missing resources through web user experience interviews that evaluate how the loss of embedded resources affects user trust in archived websites. The Hiberlink and Robust Links projects have contributed valuable research framing the problem of reference rot in the scholarly literature. While their recommendations rely on a specific set of digital publishing tools that has not yet been widely adopted across the academy, the project has contributed a more sophisticated understanding of how link preservation requires attending not only to the ideals of citation and web maintenance best practices but also to the social expectations concerning who is responsible for these linkages<a class="footnote-ref" href="#robustify"> [robustify] </a>.

Our study joins these and others that have examined instances of link rot in the scholarly literature. Our aim here is not only to document the amount of link rot but also to understand the extent to which citations rely on links. To do so we also looked at the percentage of articles that contain links, the average number of links per article, and the percentage of citations that are links. Only two other studies to date have examined all of these topics together.<a class="footnote-ref" href="#aronsky2007"> [aronsky2007] </a>examines PubMed articles immediately after publication, and<a class="footnote-ref" href="#yang2010"> [yang2010] </a>provide a comprehensive study of Chinese humanities and social science journals. Several studies examine one or two of these topics, and are used in the Analysis section to contextualize our data and to understand how the DH literature compares to other disciplines.




## Methodology

Our study examines the prevalence of websites listed as citations in _DHQ_ articles and the status of those websites. _DHQ_ is one of the most long-standing, well known journals within the field of digital humanities and is listed in the Directory of Open Access Journals as well as indexed in the Clarivate Analytics “Emerging Sources Citation Index” <a class="footnote-ref" href="#dhqabout"> [dhqabout] </a>. All types of articles were included in the analysis (e.g. Introductions, Articles, Reviews) as each article type consistently contained references. Our analysis examined only citations appearing in the Works Cited section and excluded citations in the Notes section as well as in-text links. When analyzing an individual link, we manually opened the link in a new browser tab, observed any changes in the URL as the page loaded, and once the page loaded (or not) placed it into one of seven categories. In a small number of cases, the link was correctly displayed but the HTML code contained a minor formatting error. We chose to follow the (correctly) displayed link, under the assumption that a reader interested in following the citation would do the same. Beyond this, we did not perform any additional searching to track down if a page had been relocated or archived, since the object of study is the link as it appears in the citation. The browser environments used for analysis were free of ad blockers and similar browser extensions, which can significantly alter how URLs and pages perform. The analysis was performed in the United States, and we acknowledge that results will likely differ depending on geographic location due to Internet Protocol (IP) address restrictions.

We examined articles published in _DHQ_ from its inception in 2007 up to 2019. To make the data collection process more manageable, we used systematic sampling to determine which articles to analyze. Systematic sampling uses a fixed interval, and fits this particular dataset because the citations and links within the articles in _DHQ_ are sufficiently normally distributed. This method ensures even representation of the characteristics of the articles published per year that we want to observe (i.e., number of citations, number of links and working status of the links), which was important in allowing us to reliably track trends over time<a class="footnote-ref" href="#hibberts2012"> [hibberts2012] </a>. Since the population size is known, we chose the sampling interval based on our desired confidence interval, 95%, and margin of error, 5%, for the proportion of citations that are links, assuming a variance of 25%. In order to achieve this, the target sample size would be 205 with a sampling interval of 0.47. We rounded up the sample interval to 0.50, meaning that we analyzed every other article (226 total), which slightly improves the margin of error to 4.55% while maintaining the 95% confidence interval.1 We decided that defining the population as the total number of articles, rather than total number of citations, would better foster future re-use of the data set, which is openly available online<a class="footnote-ref" href="#coble2021"> [coble2021] </a>.

Each citation that appeared as a link in the sample was labeled using one of seven categories:

 _Link resolves correctly_ :

1. Page exists2. Redirected, to the same page


 _Link does not resolve correctly_ :

3. Page exists, but is different4. Redirected, to same site5. Redirected, but page or site is different6. Page does not exist, site exists7. Page does not exist, site does not exist




## 1. Page Exists

The link resolves as expected and it resolves to a page with content that is clearly the cited source. This category includes Handles and DOIs, paywalled content with previews (e.g. _New York Times_ ), and pages with SSL certificate issues that still resolve.




## 2. Redirected, to the same page

The link redirects automatically and takes you to a page with content that is clearly the cited source. It is important to note that, for all categories, determinations of whether a page is the _same_ or _different_ are based primarily on clues given in the citation — most notably the page title, creator, and similar URL structure. Some assumptions were made based on information available, and this is a potential source of error in the study.




## 3. Page exists, but is different

The link resolves but the page content is obviously and significantly different from what was cited, such as web technologies that are no longer supported by browsers (e.g. Abode Flash).




## 4. Redirected, to same site

The link redirects, although the user is taken to a different page on the same top-level domain (typically the homepage) rather than the page specified in the citation. This outcome was common in cases where a site migration had occurred. Though this is not the most worrisome category, since the intended page often still exists and is findable with additional effort, technically speaking the link does not resolve correctly.




## 5. Redirected, but page or site is different

Redirected to a page or site that is obviously and significantly different from the cited source.




## 6. Page does not exist, site exists

The page no longer exists but the site it was part of still resolves. One challenge with our approach of differentiating a web page and a website is determining what exactly is the “site.” Practices can vary widely, particularly in citations of non-academic works, and we used discretion when it was obvious from contextual clues in the content and URL structure, otherwise we defaulted to using the top-level domain.




## 7. Page does not exist, site does not exist

Neither the page nor the site it was part of still resolves. This is the most worrying category, as there is effectively no original trace left of the cited source. Such pages might be captured in the Internet Archive or other web archives, but that outcome was outside the scope of this study.





## Findings
Summary of Sampled DataTotal articles analyzed (including articles without links)226Total articles analyzed (only articles with links)180Articles in sample without any citations containing links46Total citations analyzed (only links)1,924Total citations in sample (links & non-links)6,934
Table 1 provides general information about the sample. There were 226 total articles in the sample. Of these, 180 articles contained links and 46 articles did not contain any citations with links. There were 6,934 total citations in the sample (links and non-links) and 1,924 of those citations contained links.

{{< figure src="images/figure01.jpeg" caption="" alt="Image of a bar chart in orange and blue. The blue bar shows citations per article and the orange links per citation."  >}}


Figure 1 breaks down this information by year, where the first column (in blue) shows the average number of total references (links and non-links) contained in the sampled articles published that year. For instance, on average, an article published in 2007 contains twenty-three citations, which includes both references to print sources and links to websites. This data was collected using web scraping and it maps onto the primary axis (i.e., the y axis on the left, with the range 0 - 45). The second column (in yellow) shows the percentage of citations that are links for that year. For example, for all sampled articles published in 2007, 32% of the citations are links. Conversely, 68% of the citations point tonon-websitesources, such as print materials, interviews, and other types of media. This number is calculated by dividing the total number of citations that are links by the total number of citations overall (links and non-links), and it maps onto the secondary axis (i.e., the y axis on the right, with the range 0% - 100%).
Totals for Link Status CategoriesPage exists1131 (58.8%)Redirected, to the same page197 (10.2%) _Total links that work correctly_  _1328 (69%)_ Page exists, but is different37 (1.9%)Redirected, to same site53 (2.8%)Redirected, but page or site is different22 (1.1%)Page does not exist, site exists333 (17.3%)Pages does not exist, site does not exist151 (7.8%) _Total links that do not work correctly_  _596 (31%)_ 
Table 2 provides totals for the link status categories analyzed in the sample. Figure 2 visualizes this data, where each column is one year and contains the total percentage for each category, represented by color. The total number of sampled citations analyzed each year is given at the top of each bar. The sections in blue represent links that work correctly (i.e., the link resolves to the cited source). The sections in green represent links that do not work correctly (i.e., the link does not resolve to the cited source). While the data is not entirely uniform — for instance, there are only nine citations in the sample for 2008 — a clear trend is observable where over time it becomes increasingly likely that a link will not resolve correctly.

{{< figure src="images/figure02.jpeg" caption="" alt="Image of a bar chart in shades of green and blue."  >}}





## Analysis
Percentage of links in citations that do not resolve _Field_  _Link Source_  _Years_  _N_ Journalism & CommunicationURLs contained in citations in 5 journals<a class="footnote-ref" href="#dimitrova2007"> [dimitrova2007] </a>2000-200339%Library & Information ScienceOnline resources cited in 4 journals<a class="footnote-ref" href="#sadatmoosavi2012"> [sadatmoosavi2012] </a>2005-200836%Digital HumanitiesWorks cited containing links in _Digital Humanities Quarterly_ 1997-201931%NursingLinks in citations from 20 journals<a class="footnote-ref" href="#oermann2008"> [oermann2008] </a>2004-200528%Science, Technology, & MedicineURLs in references in 3 databases<a class="footnote-ref" href="#klein2014"> [klein2014] </a>1997-201213-22%PubMedInternet references in bibliographies<a class="footnote-ref" href="#aronsky2007"> [aronsky2007] </a>200612%
We know that link rot exists on the web, and Figure 2 demonstrates that there is something significant at stake as it relates to the integrity of the DH literature. Within the sample, there are 596 works cited that are links that do not work correctly. This count means that 31% of citations containing links, and 8.7% of all sampled citations, including non-link citations, no longer work correctly. Conversely, 69% of links still resolve to the cited source.

These numbers become more troubling when compared to other disciplines. Table 3 compares our data to other studies examining links that appear in references or works cited section and reveals that _DHQ_ has a comparable and relatively high percentage of link rot. Since we looked only at the works cited section, we excluded comparison studies that analyzed links in other areas, such as abstracts or entire articles.
Percentage of articles that contain links _Field_  _Link Source_  _Years_  _N_ Humanities and Social SciencesCitation links from articles in the Chinese Social Sciences Index<a class="footnote-ref" href="#yang2010"> [yang2010] </a>1998-200782%Library & Information ScienceURLs in references from 9 journals<a class="footnote-ref" href="#veena2008"> [veena2008] </a>2000-200681%Digital HumanitiesWorks cited containing links in _Digital Humanities Quarterly_ 1997-201980%ScienceLinks in citations from 3 high impact journals<a class="footnote-ref" href="#dellavale2003"> [dellavale2003] </a>200330%PubMedInternet references in bibliographies<a class="footnote-ref" href="#aronsky2007"> [aronsky2007] </a>20069%
Compounding the threat of link rot is the extent to which references in the DH literature rely on internet resources. According to sampled data, 80% of articles in _DHQ_ contain at least one reference with a URL. As Table 4 indicates, this percentage is relatively high compared to other fields where data is available. Additionally, Table 5 shows that _DHQ_ articles contain an average of 8.5 links per article, which is significantly higher compared to other disciplines. This suggests that the problem of link rot is spread across a high proportion of articles. The higher frequency of links as citations indicates a greater reliance on links compared to other fields.
Average number of links per article _Field_  _Link Source_  _Years_  _N_ Digital HumanitiesWorks cited containing links in _Digital Humanities Quarterly_ 1997-20198.5HistoryLinks in articles from 2 journals<a class="footnote-ref" href="#russell2008"> [russell2008] </a>1999-20063.9NursingLinks in citations from 20 journals<a class="footnote-ref" href="#oermann2008"> [oermann2008] </a>2004-20053.1EcologyCitation to material on the internet<a class="footnote-ref" href="#duda2008"> [duda2008] </a>1997-20052.0Computer science & engineeringArticles containing URLs in 2 journal databases<a class="footnote-ref" href="#spinellis2003"> [spinellis2003] </a>1995-19991.7Humanities and Social SciencesCitation links from articles in the Chinese Social Sciences Index<a class="footnote-ref" href="#yang2010"> [yang2010] </a>1998-20070.37PubMedInternet references in bibliographies<a class="footnote-ref" href="#aronsky2007"> [aronsky2007] </a>20060.18
Overall, 27% of sampled citations in _DHQ_ are links. Table 6 shows that _DHQ_ ranks high among studies that calculate the percentage of citations that contain links; only library and information science contain more (44%). This figure shows that, more than most disciplines, the DH literature relies heavily on links.
Percentage of citations that are links _Field_  _Link Source_  _Years_  _N_ Library & Information ScienceURLs in references from 9 journals<a class="footnote-ref" href="#veena2008"> [veena2008] </a>2000-200644%Digital HumanitiesWorks cited containing links in _Digital Humanities Quarterly_ 1997-201927%Humanities and Social SciencesCitation links from articles in the Chinese Social Sciences Index<a class="footnote-ref" href="#yang2010"> [yang2010] </a>1998-20073.60%ScienceLinks in citations from 3 high impact journals<a class="footnote-ref" href="#dellavale2003"> [dellavale2003] </a>20032.60%PubMedInternet references in bibliographies<a class="footnote-ref" href="#aronsky2007"> [aronsky2007] </a>20060.60%
There are some caveats to our findings. For instance, even if a link does not work, the page might still exist at a different link. The web is fluid, and our study is only a snapshot of a particular moment from a particular geographic location. Also, a broken link does not necessarily mean a non-existent page. A simple search could reveal the new URL, a site may only be temporarily unavailable, or it might be available in the Internet Archive or another web archive. A study of library and information science literature found that employing these two strategies decreased the rate of inaccessible URLs from 36% to 5%<a class="footnote-ref" href="#sadatmoosavi2012"> [sadatmoosavi2012] </a>.




## Discussion

Our data shows that a significant number of works cited no longer exist, are inaccessible, or have additional barriers to access. Instances of link rot increase with time. Additionally, there is a higher frequency and higher proportion of links contained in _DHQ_ articles, showing that internet resources are a critical part of the DH literature. Taken together, the combined result is a persistent and cumulative threat to the integrity and stability of the DH literature, and one that is even more alarming when compared to other disciplines.

Just as there are multiple causes of link rot, there is no single or simple solution to this threat. Here we revisit the three categories presented in the literature review to use as a framework for discussion: theory of citation, evolving guidelines for proper citation, and studies of the practice of link preservation. We focus on recent initiatives as well as overlooked aspects that we believe are worth greater attention.

The area of citation theory has much potential for reframing our understanding of the problem. Many technical solutions have been proffered, but after almost three decades the problem of link rot is as persistent as ever and there has not yet emerged a convincing full-scale solution. Thus, perhaps we need new lenses through which to view this phenomenon. For instance, it may be worth revisiting the broad assumption that scholarly literature should be accessible for the long term. Put differently, are there wider epistemological shifts or perceptions toward academic systems of credit that are being reflected in our commitment to widening the scope of verifiable sources?

In _Digital Diaspora: A Race for Cyberspace_ <a class="footnote-ref" href="#everett2009"> [everett2009] </a>, Anna Everett lays out the critical ways a Black digital public sphere developed parallel to the white, masculinist domain of the early Internet. Kelly Baker Josephs and Roopika Risam continue this thread in their introduction to _Digital Black Atlantic_ <a class="footnote-ref" href="#josephs2021"> [josephs2021] </a>and work to name these digital spaces of resistance. Josephs and Risam, in pursuit of the objective “to create a provisional space and framework for academic conversation that could emerge by virtue of acts of citational and conceptual juxtaposition,” gesture toward alternative acts of scholarly activation. Current pedagogies of writing also point to a shifting sense of how to cite sources. In “Web Writing and Citation: The Authority of Communities,” <a class="footnote-ref" href="#switaj2015"> [switaj2015] </a>, Elizabeth Switaj lists the variations on retweet (RT), modified tweet (MT), via, and hat-tip (h/t) that indicate a move on social media to gestural citation, its paths to conversation, and its social system of credit.

The second area, guidelines for citation, has the potential for incremental improvements to the health of the scholarly record. For authors, Sadat-Moosavi et al.[2012](#sadatmoosavi2012)suggest best practices for constructing links, such as citing documents in repositories (which typically use persistent identifiers) rather than private for-profit platforms such as Academia.edu and ResearchGate. When available, using persistent identifiers is a key practice. Of the 108 DOI links in our data, 107 resolved correctly (99.1%). Some publishers use DOIs in the URL string (e.g.[https://onlinelibrary.wiley.com/doi/10.1002/9781118680605.ch23](https://onlinelibrary.wiley.com/doi/10.1002/9781118680605.ch23)) but such links are not persistent (i.e. the persistent link is[https://doi.org/10.1002/9781118680605.ch23](https://doi.org/10.1002/9781118680605.ch23)). Seemingly minor details make a difference, and ideally such strategies would be more widely incorporated into citation manuals in an effort to provide authoritative guidance to researchers.

There are a number of approaches to the third area, the practice of link preservation. Building on Aronsky et al.[2007](#aronsky2007)finding that 12% of links in PubMed were already broken two days after publication, journals should incorporate link-checking as a regular part of the editorial process. Further, scanning all article links on a regular basis would make this work more manageable for journals and also help to identify patterns or issues specific to their field. Another option would be to implement measures such as those of the _Review Journal of the IDE_ , which also requires authors to use the Internet Archive’sSave Page Nowservice<a class="footnote-ref" href="#ride"> [ride] </a>for referenced links. This helps ensure that a record exists of the site as it was originally referenced, which Jones et al.[2021](#jones2021)identify as a core issue but one that is not inherently guaranteed by web archiving services such as the Internet Archive, Archive-It, or Conifer. The on-demand service Perma.cc was specifically designed to address reference rot by generating permanent links to affix web citations used in publishing<a class="footnote-ref" href="#permacc"> [permacc] </a>. Perma.cc comes the closest to providing a turnkey solution, although its approach is to replace the original resource with a replica. Each of these web archiving strategies show different approaches that can be employed by journals, although it is worth noting that they rely on external service providers.

Finally, there are several recent initiatives providing resources for website creators and maintainers as well as a growing general awareness of the labor and craft required to build and sustain web-based DH outputs. Page-level redirects, or URL forwarding, is a proven and established technique for ensuring that links resolve correctly, and is particularly important when migrating a site or performing other updates that alter the URL structure of references. Best practices for this are thoughtfully articulated in Guidelines for Preserving New Forms of Scholarship<a class="footnote-ref" href="#greenberg2021"> [greenberg2021] </a>.

More broadly, the Socio-Technical Sustainability Roadmap gives a practical framework and holistic approach for the range of work involved in the entire lifecycle of a project<a class="footnote-ref" href="#sociotechnical"> [sociotechnical] </a>. And the Endings Project has produced a valuable set of tools, principles, and body of knowledge that advances our ability to create “accessible, stable, long-lasting resources in the humanities” <a class="footnote-ref" href="#ending2022"> [ending2022] </a>. Additionally,<a class="footnote-ref" href="#minimalNd"> [minimalNd] </a>provides an ethos that undergirds this work, and tools like Wax directly put these principles into practice by generating static sites<a class="footnote-ref" href="#minimalNd"> [minimalNd] </a><a class="footnote-ref" href="#nyrop2021"> [nyrop2021] </a>. None of these will inherently ensure long-term access to websites, and it is crucial to acknowledge that all require real and sustained institutional investments in staff and technical resources (see the articles by Otis and Cummings in this issue). However, there is some room for optimism given the overlap and shared history between DH and scholarly communication<a class="footnote-ref" href="#coble2014"> [coble2014] </a>. The practitioners of the latter, who share a keen interest in the stewardship of the scholarly record and have already taken great strides to address this phenomenon, are well positioned in terms of expertise and resources to continue these efforts. Taken together, they constitute an engaged community bringing necessary advancements to digital scholarly infrastructure.




## Conclusion

Scholarly discourse depends on the practice of referencing sources. Our study shows that over a quarter of sampled citations are links to websites. Over 30% of these references are inaccessible or have additional access barriers. When compared to other fields, articles in _DHQ_ contain the highest number of links per article, a high proportion of citations that are links, and a high proportion of articles that contain links. This problem is persistent and gets worse over time, creating a significant threat to the stability and integrity of the DH literature.

Even when we acknowledge that link rot and content drift present a risk to the DH literature, it is worth exploring to what extent this is a problem. It is unwise to simply assert that all websites should be accessible forever. Rather, within the context of scholarly literature, we should consider what criteria or considerations would be helpful to better understand which sites require longer term access. Preserving the record of a resource does not inherently preserve access to that resource, and understanding the social expectations of citation practice within a given field should be taken into account as DH citations are created. Maintaining access to websites is different from maintaining links to those websites, and it is always worth emphasizing that implementing such approaches at scale requires significant investments of labor and resources from institutional coalitions of publishers, libraries, and archives.




## Notes

Three main characteristics were observed in our analysis: number of citations per article, percentage of citations that are links and percent of links that work. Our sample size was chosen to ensure confidence about the percentage of citations that were links and we observed the status of all of those. Given the observed standard deviations of our sample characteristics we are able to calculate the margin of error for a 95% and a 99% confidence interval. The results are presented on the following table:

Citation data statisticsLinks per articlePercent citations that are linksPercent of links that workMean8.528%69%Standard Deviation11.324%29%Sample size226213*180**Population438438438Margin of error (95% confidence interval)1.473%4%Margin of error (99% confidence interval)1.934%5%* For this we only consider papers that have citations** For this we only consider the papers where at least one citation is a link



## Acknowledgements

The authors give thanks to Luiza Nassif Pires.

## Bibliography

<ul>
<li id="apa2020">American Psychological Association. (2020). Publication manual of the American Psychological Association 2020: the official guide to APA style (7th ed.). American Psychological Association.
</li>
<li id="arneil2019">Arneil et al. (2019) “Project Endings: Early Impressions from Our Recent Survey On Project Longevity In DH”  _DH2019_ , Utrecht, Netherlands. Available at:<a href="https://doi.org/10.34894/SIKOBN">https://doi.org/10.34894/SIKOBN</a>.
</li>
<li id="aronsky2007">Aronsky, D., Madani, S., Carnevale, R. J., et al. (2007) “The prevalence and inaccessibility of Internet references in the biomedical literature at the time of publication” , _Journal of the American Medical Informatics Association_ , 14(2), pp. 232–234. Available at:<a href="https://doi.org/10.1197/jamia.M2243">https://doi.org/10.1197/jamia.M2243</a>.
</li>
<li id="brunelle2015">Brunelle, J. F., Kelly, M., SalahEldeen, H. et al. (2015) “Not all mementos are created equal: measuring the impact of missing resources” , _International Journal on Digital Libraries_ , 16, pp. 283–301. Available at:<a href="https://doi.org/10.1007/s00799-015-0150-6">https://doi.org/10.1007/s00799-015-0150-6</a>.
</li>
<li id="burnhill2015">Burnhill, P., Mewissen, M., & Wincewicz, R. (2015) “Reference rot in scholarly statement: threat and remedy” , _Insights_ , 28:2, 55–61. Available at:<a href="http://doi.org/10.1629/uksg.237">http://doi.org/10.1629/uksg.237</a>.
</li>
<li id="coble2014">Coble, Z., Potvin, S., and Shirazi, R. (2014) “Process as Product: Scholarly Communication Experiments in the Digital Humanities” , _Journal of Librarianship and Scholarly Communication_ , 2:3. Available at:<a href="https://doi.org/10.7710/2162-3309.1137">https://doi.org/10.7710/2162-3309.1137</a>.
</li>
<li id="coble2021">Coble, Z and Karlin, K. (2021) “Reference Rot in the DH Literature” . Available at:<a href="https://github.com/nyu-dss/dh-citation-links">https://github.com/nyu-dss/dh-citation-links</a>.
</li>
<li id="dellavale2003">Dellavalle, R. P., Hester, E. J., Heilig, L. F., et al. (2003) “Going, Going, Gone: Lost Internet References” , _Science_ , 302:5646, 787-788. Available at:<a href="https://doi.org/10.1126/science.1088234">https://doi.org/10.1126/science.1088234</a>.
</li>
<li id="dimitrova2007">Dimitrova, D. V. and Bugeja, M. (2007) “The half-life of internet references cited in communication journals” , _New Media & Society_ , 9:5, 811–826. Available at:<a href="https://doi.org/10.1177/1461444807081226">https://doi.org/10.1177/1461444807081226</a>.
</li>
<li id="dhqabout"> _Digital Humanities Quarterly_ , “About” . The Alliance of Digital Humanities Organizations and The Association for Computers and the Humanities. Available at:<a href="http://digitalhumanities.org/dhq/about/about.html">http://digitalhumanities.org/dhq/about/about.html</a>.
</li>
<li id="duda2008">Duda, J. J., and Camp, R. J. (2008) “Ecology in the information age: patterns of use and attrition rates of internet-based citations in ESA journals, 1997–2005” , _Frontiers in Ecology and the Environment_ , 6(3), pp. 145–151. Available at:<a href="https://doi.org/10.1890/070022">https://doi.org/10.1890/070022</a>.
</li>
<li id="ending2022"> “The Endings Project” , University of Victoria, 2022. Available at:<a href="https://endings.uvic.ca/about.html">https://endings.uvic.ca/about.html</a>.
</li>
<li id="everett2009">Everett, A., (2009) _Digital Diaspora_ . Albany, NY: State University of New York Press.
</li>
<li id="garfield1994">Garfield, E. (1994) “When to Cite” , _Library Quarterly_ , 66(4), pp. 449–58.
</li>
<li id="greenberg2021">Greenberg, J., Hanson, K., & Verhoff, D. (2021) “Guidelines for Preserving New Forms of Scholarship” , _NYU Libraries_ . Available at:<a href="https://doi.org/10.33682/221c-b2xj">https://doi.org/10.33682/221c-b2xj</a>and<a href="https://preservingnewforms.dlib.nyu.edu/guidelines">https://preservingnewforms.dlib.nyu.edu/guidelines</a>.
</li>
<li id="greenhill2003">Greenhill, A., and Fletcher, G. (eds.) (2003) “Electronic References & Scholarly Citations of Internet Sources” , _The World-Wide Web Virtual Library_ . Available at:<a href="http://www.spaceless.com/WWWVL/">http://www.spaceless.com/WWWVL/</a>.
</li>
<li id="hibberts2012">Hibberts M., Burke Johnson R., and Hudson K. (2012) “Common Survey Sampling Techniques” In L. Gideon (ed.), _Handbook of Survey Methodology for the Social Sciences_ . New York, pp. 53–74. Available at:<a href="https://doi.org/10.1007/978-1-4614-3876-2_5">https://doi.org/10.1007/978-1-4614-3876-2_5</a>.
</li>
<li id="jones2021">Jones, S. M., Klein, M., Sompel, H. V. D. (2021) “Robustifying Links To Combat Reference Rot” , _Code4Lib_ , 50. Available at:<a href="https://journal.code4lib.org/articles/15509">https://journal.code4lib.org/articles/15509</a>.
</li>
<li id="josephs2021">Josephs, K. B., and Risam, R. (eds.) (2021) _Digital Black Atlantic_ . Minneapolis: University of Minnesota Press. Available at:<a href="https://doi.org/10.5749/9781452965321">https://doi.org/10.5749/9781452965321</a>.
</li>
<li id="klein2014">Klein M, Van de Sompel H, Sanderson R, et al. (2014) “Scholarly Context Not Found: One in Five Articles Suffers from Reference Rot” , _PLoS ONE_ 9(12), e115253. Available at:<a href="https://doi.org/10.1371/journal.pone.0115253">https://doi.org/10.1371/journal.pone.0115253</a>.
</li>
<li id="knowledgeequity"> “Knowledge Equity Lab” University of Toronto Scarborough. Available at:<a href="https://knowledgeequitylab.ca/">https://knowledgeequitylab.ca/</a>.
</li>
<li id="minimalNd"> “Minimal Computing” , Global Outlook::Digital Humanities. Available at:<a href="https://go-dh.github.io/mincomp/">https://go-dh.github.io/mincomp/</a>.
</li>
<li id="nyrop2021">Nyröp, M. “What is Wax?” Available at:<a href="https://minicomp.github.io/wax/about/">https://minicomp.github.io/wax/about/</a>.
</li>
<li id="oermann2008">Oermann, M. H., Nordstrom, C. K., Ineson, V., and Wilmes, N. A. (2008) “Web Citations in the Nursing Literature: How Accurate Are They?”  _Journal of Professional Nursing_ , 24(6), pp. 347–351. Available at:<a href="https://doi.org/10.1016/j.profnurs.2007.12.004">https://doi.org/10.1016/j.profnurs.2007.12.004</a>.
</li>
<li id="permacc"> “Perma.cc”  _Harvard Library Innovation Lab_ . Available at:<a href="https://perma.cc/">https://perma.cc/</a>.
</li>
<li id="ride">Review Journal of the IDE. “Writing Guidelines” , _Institute for Documentology and Scholarly Editing_ . Available at:<a href="https://ride.i-d-e.de/reviewers/writing-guidelines/#links">https://ride.i-d-e.de/reviewers/writing-guidelines/#links</a>.
</li>
<li id="robustify"> “Make Your Links Robust” , _Memento Project_ . Available at:<a href="https://robustlinks.mementoweb.org/">https://robustlinks.mementoweb.org/</a>.
</li>
<li id="russell2008">Russell, E., & Kane, J. (2008) “The Missing Link: Assessing the Reliability of Internet Citations in History Journals” , _Technology and Culture_ , 49(2), pp. 420–429. Available at:<a href="https://doi.org/10.1353/tech.0.0028">https://doi.org/10.1353/tech.0.0028</a>.
</li>
<li id="sadatmoosavi2012">Sadat-Moosavi A., Isfandyari-Moghaddam A., and Tajeddini O. (2012) “Accessibility of online resources cited in scholarly LIS journals: A study of emerald ISI-ranked journals” , _Aslib Proceedings_ , 64(2), pp. 178–192.
</li>
<li id="sociotechnical">Visual Media Workshop at the University of Pittsburgh. “The Socio-Technical Sustainability Roadmap” . Available at:<a href="http://sustainingdh.net/">http://sustainingdh.net</a>.
</li>
<li id="spinellis2003">Spinellis, D. (2003) “The decay and failures of web references” , _Communications of the ACM_ , 46(1), pp. 71–77. Available at:<a href="https://doi.org/10.1145/602421.602422">https://doi.org/10.1145/602421.602422</a>.
</li>
<li id="switaj2015">Switaj, Elizabeth. (2015) “Web Writing and Citation: The Authority of Communities” In Dougherty, J and O'Donnell T (eds.), _Web Writing: Why and How for Liberal Arts Teaching and Learning_ . Ann Arbor: University of Michigan Press, pp. 223–32. Available at:<a href="https://doi.org/10.2307/j.ctv65sxgk.24">https://doi.org/10.2307/j.ctv65sxgk.24</a>.
</li>
<li id="veena2008">Veena, SVR and Sampath Kumar, B. T. (2008) “Web citation behaviour in scholarly electronic journals in the field of library and information science” , _Webology_ , 5(2). Available at:<a href="https://www.webology.org/data-cms/articles/20200515041147pma57.pdf">https://www.webology.org/data-cms/articles/20200515041147pma57.pdf</a>.
</li>
<li id="walker1995">Walker, J. R. (1995) “MLA-Style Citations of Electronic Sources” Ver.1.0. Cited in: Harnack, A and G. Kleppinger. (1996) K A I R O S: 1.2. Kairos.technorhetoric.net. Available at:<a href="https://kairos.technorhetoric.net/1.2/binder.html?inbox/mla.html">https://kairos.technorhetoric.net/1.2/binder.html?inbox/mla.html</a>.
</li>
<li id="yang2010">Yang, S., Qiu, J. and Xiong, Z. (2010) “An Empirical Study on the Utilization of Web Academic Resources in Humanities and Social Sciences Based on Web Citations” , _Scientometrics_ , 84, pp. 1–19. Available at:<a href="https://doi.org/10.1007/s11192-009-0142-7">https://doi.org/10.1007/s11192-009-0142-7</a>.
</li>
<li id="zhou2015">Zhou, K, Grover, C, Klein, M, and Tobin, R. (2015) “No More 404s: Predicting Referenced Link Rot in Scholarly Articles for Pro-Active Archiving” , _JCDL '15: Proceedings of the 15th ACM/IEEE-CS Joint Conference on Digital Libraries_ , New York, pp. 233–236. Available at:<a href="https://doi.org/10.1145/2756406.2756940">https://doi.org/10.1145/2756406.2756940</a>.
</li>
<li id="zuckerman1987">Zuckerman, H. (1987) “Citation analysis and the complex problem of intellectual influence” , _Scientometrics_ , 12(5), pp. 329–38.
</li>

</ul>
