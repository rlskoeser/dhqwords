---
type: article
dhqtype: article
title: "Computational Paremiology: Charting the temporal, ecological dynamics of proverb use in books, news articles, and tweets"
date: 2023-05-26
article_id: "000676"
volume: 017
issue: 2
authors:
- Ethan Davis
- Christopher Danforth
- Wolfgang Mieder
- Peter Sheridan Dodds
translationType: original
abstract: |
   Proverbs are an essential component of language and culture, and though much attention has been paid to their history and currency, there has been comparatively little quantitative work on changes in the frequency with which they are used over time. With wider availability of large corpora reflecting many diverse genres of documents, it is now possible to take a broad and dynamic view of the importance of the proverb. Here, we measure temporal changes in the relevance of proverbs within four corpora, differing in kind, scale, and time frame: Millions of books over centuries; thousands of books over centuries; millions of news articles over twenty years; and billions of tweets over a decade. While similar methodologies abound lately, they have not yet been performed using comprehensive phraseological lexica (here, The Dictionary of American Proverbs). We show that beyond simple partitioning of texts into words, searches for culturally significant phrases can yield distinct insights from the same corpora. Comparative analysis between four commonly used corpora show that each reveals its own relationship to the phenomena being studied. We also find that the frequency with which proverbs appear in texts follows a similar distribution to that of individual words.
teaser: "This article measures temporal changes in the relevance of proverbs within four corpora,differing in kind, scale, and time frame: Millions of books over centuries; thousands of books over centuries; millions of news articles over twenty years; and billions of tweets over a decade."
order: 1
draft: true
---



## Introduction

Our goal here is to advancecomputational paremiology: The data-driven study of proverbs, and in general to examine the utility of frequency-based studies of common phrases in large corpora. In particular, we hope to answer the following: Can a computational study of proverbs in large corpora offer unique insight in the study of those proverbs? And is this novel kind of approach appropriate to corpus linguistics and studies using corpora broadly? We first build a quantitative foundation by searching for and counting instances of an ecology of proverbs, and estimating their frequency of use over time in several large corpora from different domains. We then characterize basic temporal dynamics allowing us to address fundamental questions such as whether or not proverbs appear in texts according to a similar probability distribution to words<a class="footnote-ref" href="#zipf2012"> [zipf2012] </a><a class="footnote-ref" href="#balasubrahmanyan1996"> [balasubrahmanyan1996] </a><a class="footnote-ref" href="#williams2015b"> [williams2015b] </a><a class="footnote-ref" href="#cancho2001"> [cancho2001] </a>.

In studies of phraseology, data on frequency of use is often conspicuously absent<a class="footnote-ref" href="#cermak2014"> [cermak2014] </a>. The recent proliferation of large machine-readable corpora has enabled new frequency-informed studies of words and _n_ -grams (phrases of length _n_ ) that have expanded our knowledge of language use in a variety of settings, from the Google Books _n_ -gram Corpus and the introduction ofculturomics<a class="footnote-ref" href="#michel2011"> [michel2011] </a><a class="footnote-ref" href="#pechenick2015a"> [pechenick2015a] </a>, to availability and analysis of Twitter data<a class="footnote-ref" href="#alshaabi2020"> [alshaabi2020] </a>. Routine formulae, or multi-word expressions that cannot be reduced to a literal reading of their semantic components, remain notoriously averse to reliable identification despite carrying high degrees of symbolic and indexical meaning<a class="footnote-ref" href="#sag2002"> [sag2002] </a>. It is, for instance, much easier to chart a probability distribution of single words or _n_ -grams than phrases like proverbs, conventional metaphors, or idioms, which must be associated with a lexicon – a set of meaningful linguistic units.

Studies of words alone can generally assume that each word is lexically represented as such, but the study of phrases with a particular cultural use may require a lexicon in addition to the text being studied. Here, we use Mieder’s _Dictionary of American Proverbs_ as such a resource. Assuming words orgramsas fundamental components of texts risks flattening the complex interrelations between common phrases that might place a text in a historical or literary context, by de-emphasizing or omitting altogether culturally significant phrases. We show a case (proverbs) in which established computational methods may be applied to a class of culturally meaningful phrases, with results that paint a valid and substantially unique picture of language use in the corpora studied.

Perhaps the most recognizable routine formulae are proverbs and their close cousin, idioms. Centuries of the study of proverbs – paremiology – have shown their importance in language and culture, and that they are immensely popular among the folk (the people for whom these phrases are culturally relevant)<a class="footnote-ref" href="#mieder2012"> [mieder2012] </a>. Proverbs are generally metaphorical in their use, and map a generic situation described by the proverb to an immediate context. In light of challenges in developing reliable instruments for measurement and quantification of figurative language, research would greatly benefit, as it has with words, from a better understanding of the frequency and dynamics of proverb use in texts. By applying new methodologies in measuring frequency and probability distributions, this study seeks to contribute to this endeavor.

Before going any further, we must detail a more precise definition of the proverb. Though there is still some debate, it is widely agreed that proverbs are popular sayings that offer general advice or wisdom. Naturally, not all such sayings are proverbs. Mieder’s definition is perhaps the most useful for our present purposes: “Proverbs [are] concise traditional statements of apparent truths with currency among the folk. More elaborately stated, proverbs are short, generally known sentences of the folk that contain wisdom, truths, morals, and traditional views in a metaphorical, fixed, and memorizable form and that are handed down from generation to generation” <a class="footnote-ref" href="#mieder2008"> [mieder2008] </a>.

Proverbs maintain a particular relationship with their context of use that provides a fruitful domain for frequency and probability analysis. An important part of the proverb is the context in which it is used. The metaphorical property of a proverb need not only have to do with the proverb itself (as in the proverb/metaphorwar is hell,in which war is compared to hell within the proverb). In general, the use of a proverb is metaphorical in context, meaning that the proverb offers wisdom about a current situation via a metaphoric comparison to a proverbial one<a class="footnote-ref" href="#mieder2008"> [mieder2008] </a>. For instance, while the proverb “still waters run deep” might be used to caution someone against taking a seeming calm for granted, as it may belie unseen dangers. As with many other proverbs, it is hard to imagine anyone using the proverb “you can’t put lipstick on a pig” in any literal or pragmatic context. Rather, these phrases offer wisdom embodied in the culture as opposed to that of the speaker. In this way proverbs may be used generically without proffering personal expertise.

Proverbs are necessarily ambiguous enough to offer wisdom in any number of situations. Michael Lieber argued that this ambiguity paradoxically gives proverbs the function of disambiguating situations in which they are used. In part due to their role as cultural rather than individual wisdom, they can be invoked impersonally as a way of clarifying a complex reality<a class="footnote-ref" href="#lieber1994"> [lieber1994] </a>. As such, part of Winick’s definition of the proverb is that they “address recurrent social situations in a strategic way” <a class="footnote-ref" href="#mieder2008"> [mieder2008] </a>.

It is important to note the distinction between proverbs and idioms. An example of an idiom would be the phrasered herringdenoting a mislead. The meanings of idioms, like proverbs, often cannot be ascertained from the meanings of their component words. But unlike proverbs, idioms are often not complete sentences, require context, and need not reference a paradigmatic situation. Proverbs on the other hand represent a complete situation and offer some sort of general wisdom. The boundary between the two is rather fuzzy and contains many idioms and proverbial expressions. For instance, the proverb “every cloud has its silver lining” is perhaps more well known by its idiomatic reductionsilver lining.In fact, people may use an idiom without any knowledge of its proverbial context. Our intent here is to focus on expressions of full proverbs, and not their idiomatic uses. As previous work has shown, it is possible to investigate the manipulations and idiomizations of individual proverbs<a class="footnote-ref" href="#cermak2014"> [cermak2014] </a><a class="footnote-ref" href="#moon1998"> [moon1998] </a>. Our approach has limitations, and further research into flexible searches or other identification methods will be essential in future work.

Metaphor and idiom identification and comprehension are an open area of research in machine learning and NLP (Natural Language Processing)<a class="footnote-ref" href="#fazly2009"> [fazly2009] </a><a class="footnote-ref" href="#shutova2010"> [shutova2010] </a>. In general, metaphors and metaphorical speech are difficult to identify, and do not occur in consistent, repeated phrasings. Whereas in the study of individual words, one is allowed the tacit assumption that most of these words are represented in the lexicon of the language, in the search for routine formulae, one must access the lexicon as an essential step in verifying a phrase’s meaningfulness. Furthermore, the source and target domains of their metaphoric mapping are seldom explicit, as laid out by Lakoff and Johnson in their _Conceptual Metaphor Theory_ <a class="footnote-ref" href="#lakoff1985"> [lakoff1985] </a><a class="footnote-ref" href="#andersson2013"> [andersson2013] </a>. Proverbs generally appear in the same recognizable format, and in the form of a full, self-contained sentence. Prospectively, understanding of the conceptual mapping involved in proverb use may provide a useful step towards general understanding of metaphors in the above fields<a class="footnote-ref" href="#ozbal2016a"> [ozbal2016a] </a><a class="footnote-ref" href="#ozbal2016b"> [ozbal2016b] </a>.

Arguably, the proverb’s flexibility of use has helped make them an essential part of language and communication, literature, discourse, and media<a class="footnote-ref" href="#mieder2012"> [mieder2012] </a>. Interest in the collection and study of proverbs dates back to at least the ancient Greeks and Sumerians. Erasmus famously collected proverbs. In English literature, the proverb has been an important device for many famous authors, among them Geoffrey Chaucer, William Shakespeare, Oscar Wilde, and Agatha Christie<a class="footnote-ref" href="#abrams1994"> [abrams1994] </a><a class="footnote-ref" href="#obelkevich1994"> [obelkevich1994] </a>.




## Quantitative Approaches

This is by no means the first quantitative study of proverb use. Permiakov called for demographic studies of proverb knowledge to gather an impression of which proverbs were being used by the folk, in the interest of establishing a paremiological minimum: A minimum lexicon of proverbs for understanding a language<a class="footnote-ref" href="#permiakov1989"> [permiakov1989] </a>. Subsequent interest in proverb knowledge in psychology and folklore resulted in several studies conducted in the United States. Early studies by Albig and Bain in the 1930s found that American college students could recall on average between 25 and 27 distinct proverbs, many of which were common among participants<a class="footnote-ref" href="#albig1931"> [albig1931] </a><a class="footnote-ref" href="#bain1939"> [bain1939] </a>. A more recent study by Haas observed proverb familiarity among college students in several regions of the US. They performed experiments in both proverb generation and proverb recognition. Notably, students could recognize more proverbs than they could recall on their own<a class="footnote-ref" href="#haas2008"> [haas2008] </a>.

Apart from the lexicographic collection of proverbs from texts, several attempts have been made to quantify and characterize their use. Whiting, in his assiduous collection of proverbs from texts in “Modern Proverbs and Proverbial Sayings” <a class="footnote-ref" href="#whiting2014"> [whiting2014] </a>, kept track of the frequency with which they were encountered. Norrick attempted a manual search for proverb frequency, though he was constrained to only using proverbs starting with the letter _f_ , and used a relatively small text sample<a class="footnote-ref" href="#norrick1985"> [norrick1985] </a>. In the first serious computational analysis of proverb frequency, Lau searched for and counted instances of proverbs in newspapers in the Lexis/Nexis ALLNWS database<a class="footnote-ref" href="#lau1996"> [lau1996] </a>.

David Cram theorized that proverbs, acting as self-contained lexical units, were employed much in the same way that words are, and that their use involved alexical loopwhere the speaker accesses the lexicon in addition to the syntax when forming a text. As such, in the case of proverbs (and phrasal idioms), one ought to “analyze a syntactic string as a single lexical item” <a class="footnote-ref" href="#cram1994"> [cram1994] </a>.

Moon’s exhaustive early study of fixed expressions and idioms (denoted FEIs) in the Oxford Hector Pilot Corpus (OHPC) did just that<a class="footnote-ref" href="#moon1998"> [moon1998] </a>. His study represents the first serious attempt to apply the new tools of computational linguistics to routine formulae. He searched the OHPC (a precursor to the British National Corpus or BNC) for instances of 6776 FEIs from the _Collins Cobuild English Language Dictionary_ . It is worth noting that at the time, there were few machine-readable English phraseological lexica. Though proverbs consisted of only 3.5% of the searched phrases (240), 19% of the expressions found in the corpus were proverbial expressions, the second most common subtype behindsimple expressions(70%). Of the proverbs found, 59% were deemed metaphorical. Moon notes that exploitation of FEIs are easy to miss, and uses the proverb “a bird in the hand is worth two in the bush” as an example.

Significantly, Moon noted that journalism was over-represented in the corpus, and that the results did not represent the distributions of these FEIs in English as a whole. This and other similar caveats inspired the present study to observe genre-specific corpora separately, and compare after analysis.

Čermák’s essay collection _Proverbs: Their Lexical and Semantic Features_ contains several essays that deal with the distribution of proverbs in the British National Corpus<a class="footnote-ref" href="#cermak2014"> [cermak2014] </a>. In Čermák’s pioneering essays, he searches for occurrences of English proverbs in the BNC corpus (100 million words)<a class="footnote-ref" href="#bnc2001"> [bnc2001] </a>. In his study, even the most common proverbs seem to occur relatively infrequently. For example, “easier said than done” is the most common, appearing 62 times in the entire corpus. His study discusses the relevance of corpus occurrence to a paremiological minimum (he uses a limited proverb list from Wiktionary). Another study focuses on text introducers to various proverbs using collocation analysis. (Čermák notably created/spearheaded one of the first machine-readable phrasaeological lexica in the “Czech Idiom Dictionary” (1994).)

Čermák relates frequency dictionaries to discussions of a paremeological minimum. Should proverb frequency in large corpora be considered when judging that minimum? Of course, there are problems with this approach as well: proverbs rely heavily on oral tradition, and are prone to frequent corruptions and purposeful exploitations. As such there is no guarantee that a search of a given phrasing of a proverb will capture all, if any, of its occurrences in a text. There are ways around this on an individual basis, but it depends on the proverb: some employ parallel structures (likegood X make good Y), or have popular idiomizations (likesilver lining). Longer proverbs are more likely to appear in more than one form, as words and clauses can be swapped rearranged, or omitted without changing their overall meaning, which makes computational identification more difficult. Shorter proverbs will more reliably appear in a consistent form because there are fewer words to manipulate, and any manipulation is likely to change their meaning.

In a recent introductory paremiology textbook, Steyer (2015) outlined a process general corpus linguistic method for studying proverbs, similar to Moon and Čermák. Most recently, Haas (2022) used Google Trends to analyze the frequency of Google searches of proverbs included in discourse around the COVID-19 pandemic. Here, we expand on the above literature, including much larger corpora and proverb data sets.

Should the ambition be to find these distributions in English as a whole? We contend that there is no such universal corpus for any language. Clearly use of these phrases is context-dependent, it seems unlikely inter-contextual searches will yield greater insight than single-genre searches. Instead, frequency dynamics and distributions in separate corpora from differing contexts may be more informative.




## From Data on Language to Culture

Our present study of proverbs from a corpus linguistic point of view examines proverb frequency using several methods that are well established in the study of words, though rarely used in conjunction: namely the dynamics of frequency over time, and the relationship between frequency and relative popularity (rank). We illustrate that moving beyond words to the study of significant phrases provides worthwhile insight that cannot be captured by word-based methods, and yet reproduces some of the expected behavior of words.

One of the foundational achievements in the study of complex systems was Zipf’s identification of scaling laws in language and other social phenomena<a class="footnote-ref" href="#zipf2012"> [zipf2012] </a>. Studies of scaling can help us understand the relationship between common and uncommon observations, and are particularly suited to studies of language, which relies both on the utility of some elements, and the specificity of others. A rank distribution describes the relationship between the frequency of a word’s appearance, and its resulting rank among all words in the text. Zipf’s law shows that there is an inverse relationship between the frequency and rank of words in a text, and that the most common 20% of the unique words in a text account for 80% of overall word frequency. It was first observed by Zipf that the rank distribution of words in a text follows a _power law_ Fr=cr-α,whereris a word’s rank,Fris its frequency, withα≃1. As early as 1996, natural language (in the context of computational linguistics) was cited explicitly as an example of the recently coined “complex adaptive systems” <a class="footnote-ref" href="#balasubrahmanyan1996"> [balasubrahmanyan1996] </a>.

While primary interest here is paid to its appearance and seeming ubiquity in language, the same class of distributions have been observed in phenomena across a wide range of fields including physics, biology, psychology, sociology, urban studies, and engineering<a class="footnote-ref" href="#clauset2009"> [clauset2009] </a><a class="footnote-ref" href="#martinezmekler2009"> [martinezmekler2009] </a>.

One shortcoming noted in many evaluations of Zipf's law in text is that power law scaling breaks down toward the tails of these empirical distributions, meaning that the lowest ranked words do not seem to follow Zipf’s law. Recent work by Williams et al.<a class="footnote-ref" href="#williams2015b"> [williams2015b] </a>showed that power law scaling holds over more orders of magnitude when randomly partitioned phrases are used rather than individual words. That study also suggested a refocusing of corpus linguistic attention from words to phrases as essential elements of language. Further work by Williams et al. ([2015a](#williams2015a)) suggested that changes in scaling in Zipf distributions of large corpora can be attributed to text mining. Few, if any, attempts have been made to apply Zipf's law to phraseological lexica.

With large amounts of newly digitized text, corpus linguistics and lexicology/lexicography have seen renewed wider interest, and new results. Can these methods be used to tell new stories that are of interest to those working in the humanities? And in particular, how can that work embed itself into the existing wealth of knowledge accrued by those disciplines. In this case, how can computational work on proverbs situate itself in the existing knowledge-base of paremiology?

In their seminal 2011 paper, Michel et al. discussed the newly created Google Books corpus, and coined the termculturomicsto describe the nascent discipline concerned with observable trends in the use of _n_ -grams over time<a class="footnote-ref" href="#michel2011"> [michel2011] </a>. They present several case studies, among them trends in the use of “influenza” with historical outbreaks, and the use of geographical and antagonistic terms alongside the history of the American Civil War. These case studies make use of time series data and relative frequency to tell complex stories of interest from simple queries.

Pechenick et al. note that there are serious issues with assertions that Google Books offers a reliable representation of culture. For one, books are not indexed by popularity, and each book appears only once. As a result, the linguistic contributions of the most popular books are weighted equally with the least popular<a class="footnote-ref" href="#pechenick2015a"> [pechenick2015a] </a>. Secondly, the increase in volume of scientific publications in the last century causes the last century of English as a whole to be relatively skewed towards that genre. For instance, enormously influential books like _To Kill a Mockingbird_ , _I Know Why the Caged Bird Sings_ , _Mockingjay_ , or _Harry Potter and the Order of the Phoenix_ are only represented once, and share the same weight as even the most obscure books. In the last century, the rise in volume of scientific and academic publication drastically increased the relative influence of this type of writing. Here, we examine only the English Fiction subset of the corpus, which is a less problematic subset<a class="footnote-ref" href="#pechenick2015b"> [pechenick2015b] </a>.

Other work by Reagan et al. utilized the timelines _within_ texts to evaluate theemotional arcof a text, given word valence (sentiment) data. Emotional arcs were created by plotting the changing sentiment of words in a text as it progresses: from beginning to end, how positive or negative is the overall languge in a given section? Inspired by Kurt Vonnegut's rejected Master's thesis (in anthropology) on the shapes of stories, they found that the emotional arcs of most stories in the Gutenberg corpus could be reduced to a handful of paradigmatic shapes<a class="footnote-ref" href="#reagan2016"> [reagan2016] </a>.

Work by Underwood et al. used historical use of gendered names and words to reveal trends in gender representation in literature using data from the HathiTrust digital library<a class="footnote-ref" href="#underwood2018"> [underwood2018] </a>.

StoryWrangler, a tool recently developed by Alshaabi et al. allows users to explore the temporal dynamics of _n_ -grams found on Twitter<a class="footnote-ref" href="#alshaabi2020"> [alshaabi2020] </a>. Using a data set reflecting a random 10% of Twitter since 2008 (presently over 150 billion tweets), Storywrangler tracks the prevalence of _n_ -grams on a daily scale. _n_ -grams are portrayed via rank by popularity, and convey the rise/dynamics of President Trump (further depicted in the PoTUSometer)<a class="footnote-ref" href="#dodds2021"> [dodds2021] </a>, or the meteoric rise, and continued influence of Justin Bieber (of surprising relevance to this work). Unlike the Google Books _n_ -gram Corpus, StoryWrangler is notable in its ability to track phrases in both original tweets and retweets, conveying aspects of popularity through amplification.

Beyond simple words and phrases, data have been used to track the progression of ideas. For instance, Leskovec et al.'s paper onmeme-trackingtracked the progression and mutation of popular sayings as they proliferated through news reporting and blogging<a class="footnote-ref" href="#leskovec2009"> [leskovec2009] </a>.

Recently,Computational Folkloristicshas gained recognition as an area of study, with a 2016 issue of the _Journal of American Folklore_ being devoted to the subject<a class="footnote-ref" href="#tangherlini2016"> [tangherlini2016] </a>. Using classification, networks, geographical data, temporal data, and digitized text, folklorists and other interested academics have explored new possibilities in understanding texts and cultural history. The _Danish Folklore Nexus_ developed by Abello et al. provides tools for large-scale analysis of Danish folk tales and stories, aiding in classification of stories, or mapping their similarity to others through networks. Tools like this can augment traditional methods of studying folklore, using data-driven methodology to guide future avenues of folklore research<a class="footnote-ref" href="#abello2012"> [abello2012] </a>. This represents a paradigmatic example of a computational tool participating in the continued discourse around folklore, without being an end in and of itself.




## Data and Methods

In an effort to quantify the ecology of proverbial language, a list of over 14,000 proverbs was obtained from Mieder's _Dictionary of American Proverbs_ <a class="footnote-ref" href="#mieder1992"> [mieder1992] </a>. Proverbs were stored in an SQL database for ease of access, and matched for frequency with four distinct corpora:

The Gutenberg Corpus (English)The _New York Times_ (1988-2007)The Google Books _n_ -gram Corpus (1800-2000)Twitter (2008-2020)


For Google Books, the proverbshit happenswas added to the set of proverbs to illustrate the emergence of a modern proverb.

Individual corpora were collected as follows.



## A. Gutenberg

The Gutenberg corpus comprises over 60,000 collected published documents spanning several centuries. The present study restricts its use to the subset of documents in English. As the metadata for the Gutenberg corpus does not consistently encode the date of original publication, temporal data was collected using author birth dates (gathered from the gutenbergr library for R)<a class="footnote-ref" href="#robinson2020"> [robinson2020] </a>. These were used in place of publication dates, as the publication dates in the corpus seldom represent the original publication, instead they represent the digitized edition. For temporal analysis, documents without authors and their birth dates were omitted.

The Gutenberg corpus comes with several caveats. Firstly, works were curated by perceived importance. Works also disproportionately represent the 18th and 19th centuries, and for this reason much of our work with Gutenberg focuses on this period. Several authors have much of their extensive oeuvre represented in the corpus (e.g., Anthony Trollope, Mark Twain), which could compromise a more objective view of English writing tendencies of the period.




## B. The _New York Times_ 

Data from the _New York Times_ were gathered from the _New York Times_ Annotated Corpus of 1.8 million articles from 1987-2007 [Sandhaus 2008]. The data are organized in NTIF (News Industry Text Format) formatted XML-readable documents. The corpus includes obituaries and other short pieces in addition to more traditional news articles.




## C. Google Books

The 2020 English Fiction Google _n_ -grams corpus consists of every _n_ -gram that appears at least 40 times in its set of millions of digitized books. For each _n_ -gram the corpus provides on each year it appears in the data set, the frequency with which it appeared that year, and the number of documents it appeared in that year<a class="footnote-ref" href="#michel2011"> [michel2011] </a>. Unlike Gutenberg and the _New York Times_ , Google Books does not contain the raw text of the concerned documents, rather it displays the counts for popular _n_ -grams in the corpus, organized by _n-_ gram length. This creates an obvious limitation, where only phrases of the same length can be studied together.




## Twitter

Data from Twitter was accessed through the Vermont Complex Systems Center's StoryWrangler API<a class="footnote-ref" href="#alshaabi2020"> [alshaabi2020] </a>. StoryWrangler receives a randomly selected 1/10th of each day's tweets from Twitter's Decahose API (including retweets), and organizes _n_ -grams by rank and frequency. Data for 2-gram and 3-gram proverbs were obtained though the tool, and were aggregated so the collection was case insensitive. Similar to Google Books, this corpus is organized by _n-_ gram counts rather than full texts.




## D. Data Processing and Visualization

The data from all four corpora were processed using Python, and the libraries pandas and matplotlib were used for organization and visualization respectively<a class="footnote-ref" href="#pandas2020"> [pandas2020] </a><a class="footnote-ref" href="#hunter2007"> [hunter2007] </a>.

In our processing of Gutenberg and the _New York Times_ , punctuation in both proverbs and texts was removed. Twitter data were punctuation insensitive. Regular expressions were used to capture variations in punctuation when processing the Google Books _n_ -gram Corpus.

Estimating the frequency of a proverb’s use is essential to this work. Simple counts don’t lend themselves to comparing results between corpora of different sizes, and do not capture the frequency of the proverb in relation to the size of a single corpus. Relative frequency can be calculated simply by dividing the raw frequency by a quantity describing the size of a corpus (number of articles, number of _n_ -grams, number of books, etc.) Expressed mathematically, it is calculated as:frel=ft/ntwhich is the frequencyffor time periodtdivided by the number of documentsnfound during time periodt.

Zipf distributions were plotted using ranks of proverbs in a corpus, with rank 1 being the most frequent against their frequency. Zipf distribution plots are shown on a log-log scale as is standard, which displays less intuitive power law functions as more intuitive linear functions. For results and analysis, see Appendix A.

A network approach will be useful in exploring how different books are connected by the proverbs they share. In this case, a connection is drawn between two books if they share at least one proverb. The resulting network emerges after this step is performed for each possible pair of books. In network analysis, an important metric is _centrality_ , which in this case describes how well-connected a book is in the larger network. Specifically, we calculate _betweenness centrality_ , which assesses how often a given book appears in the shortest path between any other two books in the network. A book with high betweenness centrality in this network appears in the path between many pairs of books in the network. For results and analysis, see Appendix B.

Betweenness centrality in these networks is calculated asbv=∑s≠v≠tσstvσst,whereσstdenotes the number of shortest paths between books _s_ and _t_ , andσstvdenotes the number of those paths that also pass through book _v_ .

Most processing was performed using the Vermont Advanced Computing Core (VACC) located at the University of Vermont.





## Results



## Gutenberg

While the most popular entry in the Gutenberg corpus and the Google Books _n_ -gram corpus was the phrase “hold your tongue,” this phrase is classified as a proverbial expression rather than a proverb (its use requires outside context). For clarity of focus the phrase has been excluded from figures in this section.Sink or swim,another proverbial expression, has been left in. In light of the limitations of the Gutenberg corpus detailed in Methods, it is difficult to make claims about the trends of proverb use over time (Figure 1). It is clear from the data shown in Figure 1 that proverbs appear in a remarkable portion of the documents in the corpus. “The sooner the better” for example, appears in nearly one in every ten documents in the early 1800s.

{{< figure src="images/figure01.png" caption="Time series for the 16 most popular proverbs in the Gutenberg corpus, ranked by overall count. These most common proverbs occur in a large portion of documents in the corpus for most of the period studied. For instance,the sooner the betterregularly appeared in at least 5% of documents from the 19th century. Plots are ordered in the grid by rank first left to right, then top to bottom. Note that the vertical axis ranges vary across plots to highlight individual variation in time." alt="sixteen frequency charts showing frequencies on the y axes and years on the x axes. The years go from 1800-1950"  >}}





## The _New York Times_ 

Figure 2 shows time series plots for the 16 most common proverbs in The _New York Times_ Annotated Corpus. Shown are frequency binned by month and year, and normalized by article count. All articles are included in the count including smaller articles like obituaries (the average article count is 248 per issue). It is by no means a surprise that proverbs appear frequently in journalism; in fact Lau's study found as much<a class="footnote-ref" href="#lau1996"> [lau1996] </a>. Not present in that work, is a temporal dimension (not to mention a different time period). It is clear in Figure 2 that the proverbs represented are used on a monthly or semi-monthly basis, and are rarely if ever absent in a year's publications. In these representations of proverb use, it is easier to identify use patterns and perhaps to extract narratives from their dynamics. The easiest, if somewhat trivial case is “to delay may mean to forget” owes its yearly rhythm to its role as the NYT's charity tagline. Its frequency of use increased markedly over the period studied, though stayed confined to the winter holiday months.

{{< figure src="images/figure02.png" caption="Time series plots for the 16 most popular proverbs in the _New York Times_ from 1997-2007 (ranked by overall count). The gray represent the data binned by month, and the orange represent the data binned by year. The proverbto delay may mean to forgetowes its yearly rhythm to its role as the NYT's charity tagline. The frequencies are normalized by article count (obits, and non-body included). Plots are ordered in the grid by rank first left to right, then top to bottom." alt="sixteen frequency charts showing frequency counts for key phrases over time. the y-axes show frequencies and the x-axes show years from 1988-2008"  >}}


With the exception of “to delay may mean to forget,” and consistent with accepted definitions of the proverb, the consistency with which proverbs are used in the _New York Times_ suggests they are employed widely for their utility in mapping general wisdom to a specific context.

Nonetheless, prominent spikes in frequency can be associated with historical events. For instance, the brief several-fold increase in the use ofboys will be boysaround November of 1992 is likely attributed to a contentious and widely publicized sexual assault case at the time, which prompted additional discussion of rape culture. Before the trial, the president of the New Jersey chapter of the National Organization for Women was reported as saying, “We're going to stop this 'boys will be boys' attitude from continuing in this country.” Meanwhile in the trial, the lawyer for the defense excused the rapists’ actions, telling the jury, “boys will be boys” <a class="footnote-ref" href="#glaberson1992"> [glaberson1992] </a><a class="footnote-ref" href="#hanley1992"> [hanley1992] </a>.

The maximum in use of “pay as you go” in 2004 seems to correspond with discussion around President Bush and the Republican party’s budget plans, referencing the “pay as you go” budget policy from the 1990's by which tax cuts and spending increases must not increase the defecit. Its increase in use in 1996 seems to owe to discussion of the Environmental Bond Act being proposed in New York at the time, which proponents argued would cause fewer delays than “pay as you go” funding for environmental clean-up<a class="footnote-ref" href="#voteyes1996"> [voteyes1996] </a><a class="footnote-ref" href="#henry1996"> [henry1996] </a>.




## Google Books

In Figure 3 are time series plots for the 12 most common 2-gram proverbs in the Google _n_ -grams corpus. Here the gray represents yearly frequency (counted once per volume), and the orange represents the five-year rolling average, normalized by the number of volumes in a given year. One can see clearly from the figure the emergence of several more recent proverbs:safety first,money talks,andshit happens.

{{< figure src="images/figure03.png" caption="Time series plots for the 12 most popular 2-gram proverbs in the Google Books n-gram Corpus (ranked by overall count). The gray represent the yearly frequency, while the orange represent the five-year rolling average. The dramatic increase in use of the proverbsshit happensandsafety firstcorrespond with previous scholarship on their emergence. Plots are ordered in the grid by rank first left to right, then top to bottom." alt="nine frequency charts showing the frequencies of key phrases over time. The y axes all show frequencies and the x axes show years from 1800-2000"  >}}


Safety firstexhibits a precipitous rise in usage in the early 20th century. Specifically, in 1912, the National Safety Council (NSC) in the US adopted the phrase as its slogan to promote standards of worker safety, though the Safety First Movement was initiated by US Steel in 1906. Its origin has been traced back to at least 1818<a class="footnote-ref" href="#mieder2019"> [mieder2019] </a>. The data shown in Figure 3 support the history of its popularization<a class="footnote-ref" href="#swuste2010"> [swuste2010] </a><a class="footnote-ref" href="#mieder1992"> [mieder1992] </a>.

Previous scholarship on the proverbshit happens(which does not appear in _The Dictionary of American Proverbs_ ) traced its origin to the year 1944, and its rise in popularity corresponds to its humorous use as a bumper sticker, and cultural controversy (and legal battles) associated with it<a class="footnote-ref" href="#mieder2004"> [mieder2004] </a><a class="footnote-ref" href="#georgia1991"> [georgia1991] </a>. It’s increasing currency is illustrated in its appearance in Tom Clancy’s popular novel, _Clear and Present Danger_ : “Look, in field operations anything can go wrong … We are not immune. Shit happens, as they say” <a class="footnote-ref" href="#clancy1990"> [clancy1990] </a>. It also famously appeared in the movie _Forrest Gump_ <a class="footnote-ref" href="#zemeckis1994"> [zemeckis1994] </a>.

Figure 4 shows time series plots for the 16 most popular 3-gram proverbs in the Google Books _n_ -gram corpus. Though the proverbnever say neveroriginated in 1887<a class="footnote-ref" href="#mieder1992"> [mieder1992] </a>, it is evident that it gained far wider popularity in the late 1900s. Though the proverbenough is enoughdates at least to 1546<a class="footnote-ref" href="#mieder1992"> [mieder1992] </a>, its popularity seems to vastly increase throughout the 20th century. The proverbdivide and conquerseems to have briefly gained popularity around the World War II era.

{{< figure src="images/figure04.png" caption="Time series plots for the 16 most popular 3-gram proverbs in the Google Books Ngram Corpus (ranked by overall count). The gray represents the yearly frequency, while the orange represents the 5 year rolling average. The rise in popularity of the proverbnever say neveris shown. A period of increased usage of the proverbdivide and conquercorresponds with the World War II era. Plots are ordered in the grid by rank first left to right, then top to bottom." alt="sixteen frequency charts showing the frequencies of key phrases over time. The y-axes show frequency counts and the x-axes show years from 1800 to 2000"  >}}





## Twitter

On Twitter, the four most common 2-gram proverbs, on average, don't seem to exhibit much variability in their usage (Figure 5). The proverbsbe yourselfandtime fliesseem to remain above10-6, or 1 in every million 2-grams on Twitter during the period studied. An increase in usage of “safety first” in early 2020 may be related to the onset of the coronavirus pandemic during the same period.

{{< figure src="images/figure05.png" caption="Time series plots for the nine most popular 2-gram proverbs on Twitter (ranked by overall count). The gray represents the daily frequency, while the orange represents the 30 day rolling average. The proverbsbe yourselfandtime fliesmaintain popularity over the period studied. Notably, thesafety firstshows an increase in popularity in early 2020, possibly relating to the coronavirus pandemic. Plots are ordered in the grid by rank first left to right, then top to bottom." alt="screenshot of nine frequency charts showing 2-grams of key phrases over time on Twitter. Charts are arranged by rank withbe yourselfranking first. The graphs are colored with orange and gray to display frequiencies"  >}}


Exhibited on Twitter (Figure 6), the convenience of proverbs as succinct narratives has made them useful in several titular media events in the past decade. Of note, Figure 6 shows marked shifts in frequency ofnever say never,andlove is blind.Never say neverowes its initial attention in 2010 to Justin Bieber's single of the same title ( _Justin Bieber: Never Say Never_ ), repeated as his slogan and title of a biographical documentary. This was not the first film to utilize the proverb in its title; Sean Connery's final performance as James Bond was titled _Never Say Never Again_ (1983).

{{< figure src="images/figure06.png" caption="Time series plots for 3-gram proverbs on Twitter (ranked by overall count). The gray represents the daily frequency, while the orange represents the 30 day rolling average. The proverbnever say neverowes its meteoric rise in popularity in 2010 to popular musician Justin Bieber's single and biographical documentary of the same name.never say neverremains the most popular proverb on Twitter until 2016, when it is supplanted byenough is enoughwhich has steadily gained popularity in the last decade, owed in part to its constant use by Senator Bernie Sanders, and punctuated by reactions to tragedies related to gun and police violence. Plots are ordered in the grid by rank first left to right, then top to bottom." alt="screenshot of sixteen frequency charts showing 3-grams of key phrases over time on Twitter. Charts are arranged by rank withnever say neverranking first. The graphs are colored with orange and gray to display frequiencies"  >}}


Figure 7 shows the dynamics ofnever say neveron Twitter in more detail. We observe first its meteoric rise in popularity at the time of _Never Say Never_ 's (song) release as the lead single off the soundtrack for a modern remake of the _Karate Kid_ movie (roughly two magnitudes in a single day). At the time of the single's official release on June 8th, 2010,never say neverwas the 63rd most used 3-gram on Twitter. When _Justin Bieber: Never Say Never_ was released on January 31, 2011,never say neverwas the 34th most common 3-gram on Twitter; for comparison,I love youwas 22nd at the time.

{{< figure src="images/figure07.png" caption="Daily relative frequency of the 3-gramnever say neveron Twitter. Whilenever say neverwas already popular on Twitter as of 2008, its popularity was amplified in 2010 by the release of Justin Bieber's single entitled “Never say never,” and his subsequent biographical documentary of the same name. Remarkably, it remained the most popular proverb on Twitter for almost six years, punctuated by anniversaries and reruns of the movie, until it was surpassed byenough is enoughin 2016." alt="screenshot of one frequency chart showing 3-grams of key phrases over time on Twitter. The chart shows the frequency of the phrasenever say neverwith the highest peak in 2010. The graphs are colored with orange and gray to display frequiencies"  >}}


Remarkably, the popularity ofnever say neveron Twitter decayed so slowly that it did not reach its pre-Bieber frequency until 2016. The continued presence of the proverb in Twitter discourse suggests that in the wake of its initial rise, it was more frequently adopted to general non-Bieber usage. (A similarly popular 3-gram, non-proverbial song of that year, “Rock That Body” appeared and disappeared from the Twitter discourse in the span of a few months). While the enormity and fervor of Bieber's fanbase at the time (a period calledBieber fever<a class="footnote-ref" href="#tweedle2012"> [tweedle2012] </a>) certainly contributed to its popularity, its continued use over a five-year period is compelling evidence that the proverb became a more integral part of the Twitter lexicon for a time.

In 2020, “Love is Blind” became the title of a literally minded reality dating show in which participants were quarantined in private rooms, only communicating via audio interfaces. In this instance, the proverb was not only an apt description of the show's narrative, but a template for its formation. Additionally, it came to represent a narrative solution to the isolation imposed by the concurrent pandemic. The increase in the phrase's popularity seems only to have lasted for the month of the show's release, after which it seems to settle at its former rate of use. The proverb itself is ancient, and translations exist nearly every European language.

While withnever say never(the most popular proverb on Twitter), we see a sudden rise and slow decay, we see a different pattern in the second most popular proverb,enough is enough.

From 2016 to the present, we see a steady increase in the frequency ofenough is enoughon Twitter (Figure 8). Recent work by Mieder attributes its renewed popularity in part to its constant use by Bernie Sanders<a class="footnote-ref" href="#mieder2019"> [mieder2019] </a>. Unlikenever say neverthere does not seem to be a single event that precipitates this trend. An investigation into the several local maxima (brief spikes in occurrence) suggests a possible narrative correspondence. Many of these local maxima correspond to events related to either police violence or mass shootings.

{{< figure src="images/figure08.png" caption="Daily relative frequency of the 3-gramenough is enoughon Twitter. The popularity ofenough is enoughon Twitter grew steadily over the last decade, and it has been the most popular proverb on Twitter since 2016, perhaps originating from its consistent use by Senator Bernie Sanders<a class=\"footnote-ref\" href=\"#mieder2019\"> [mieder2019] </a>. It has since become associated with growing protests against police brutality and gun violence. Annotations reflect widely reported violent events and protests (with the exception of the 2018 US midterm elections). The stark simplicity of this sixteenth century proverb evokes a narrative of repetition past the point of tolerance<a class=\"footnote-ref\" href=\"#mieder1992\"> [mieder1992] </a>. In this instance, beginning as a condemnation of the continued reaffirmation of the status quo in US politics by Senator Sanders, it is now popular as collective outcry against political inaction in the wake of regular mass shootings in the US, and a lack of accountability in the killing of black Americans by police. The changing significance and popularity of the proverb in the past decade displays the aptitude of proverbial speech to be successfully employed in varying contexts, and its potential to illustrate narrative commonalities between phenomena." alt="screenshot of one frequency chart showing 3-grams of key phrases over time on Twitter. The chart shows the frequency of the phraseenough is enoughsteady useage from 2010-2020 and peaks around major international events such as the Pulse nightclub shooting and the Parkland school shooting. The graph is colored with orange and gray to display frequiencies"  >}}


Famously, survivors of the Parkland shooting in 2018 appeared on the cover of _Time_ magazine with a simple title: “Enough.” <a class="footnote-ref" href="#alter2018"> [alter2018] </a>. Coverage of the March for Our Lives against gun violence in the _New York Times_ included the title: _March for Our Lives Highlights: Students Protesting Guns Say Enough Is Enough _ <a class="footnote-ref" href="#marchforourlives2018"> [marchforourlives2018] </a>. When protesters marched in DC in the wake of the murder of George Floyd, Politico's coverage was titled: _ Enough is enough : Thousands descend on D.C. for largest George Floyd protest yet_ <a class="footnote-ref" href="#semones2020"> [semones2020] </a>. Inasmuch as proverbs can create metaphorical mappings from a paradigmatic situation (or narrative) onto a present one,enough is enoughrepresents a compelling narrative of continued injustice, and a critical point of retaliation. The data from Twitter display a narrative of repeated tragedy in spite of public outcry. The proverb was most popular during the 2018 US midterm elections, during which gun control was a major issue.





## Concluding remarks

In this study, four corpora reveal four markedly different patterns of proverb use, which taken each within the limits of their methods of collection, can offer piecemeal insight into the relationship between phrases and the written record. Observing all four side by side, it should become clear that generalizing linguistic tendencies from individual corpora may not be a good idea. Even among corpora with significant temporal overlap the results differ due to both the scope of each corpus, and the way in which data are collected from texts. The present approach of studying data from distinct domains allows for both a more limited and more useful interpretation of the results: We can only claim that results are representative of proverb use on Twitter for instance, rather than proverb use in English as a whole — an impossible achievement.

So, rather than using the results to speak about _all proverbs_ or all of language, we may use it as lens by which to identify areas (within a corpus) that warrant a closer look. In studies of common words, the concept the word represents is often dependent on its context, and evaluating context for each instance in a large corpus is generally not feasible. Proverbs carry with them a paradigmatic context

Unlike studies of common words, whose interpretation is often dependent on their context, we show that proverbs allow us to perform a different kind of analysis that focuses on the historical use of a stable paradigmatic narrative.

While much work up to this point uses computational methods to take a broader view of text than traditional methods of humanities scholarship, that broader view often necessarily obscures the context in which linguistic elements are used. A single word or short sequence of words may carry any number of meanings dependent on the words or concepts around it. Proverbs carry their own paradigmatic context which makes their meaning and use fairly consistent. While proverbs may be employed in many different practical situations, the paradigmatic situation they represent remains the same. In searching for proverbs, we are able to see how a paradigmatic context is applied to different practical contexts. The results of this search show not only the frequency of some sequence of words, but also the frequency with which a particular cultural concept is employed.

 _N_ -gram based methods of analyzing common phrases in texts suffer from the inclusion of many sequences of words which do not have any self-contained meaning. Our work, in which phrases must be represented in the lexicon, ensures that each phrase studied is meaningful. In an analysis of all 3-grams in a text, a very common phrase without a fixed meaning, likeand this iscould obscure a far less common meaningful phrase likelove is blind,even though it is common among phrases with fixed meanings. Our study of a specific cultural-linguistic phenomenon highlights the utility of using an extensive lexicon to isolate the phenomenon being studied.

We demonstrate that lexically significant phrases (here proverbs), which are relatively stable and self-contained, can discern trends that words or _n_ -grams would likely miss. In each corpus studied, evidence of proverbs’ changing use over time is shown to validate previous scholarship, reflect cultural events, and offer a quantitative, longitudinal perspective unable to be achieved by traditional methods in the study of proverbs.

The study of common and flexible phrases seems to lend itself to this mode of inquiry. Through novel or context-specific words and phrases, we are able to observe discourse around specific phenomena (pizzagate,pandemic,orMake America Great Again). In contrast, through more generic culturally significant phrases, we may be able to observe how we organize specific phenomena into the paradigmatic narratives they represent.

Much attention has been paid to the use of words and _n_ -grams in general in large corpora, but it is difficult to extract from them instances of individual narrative or metaphorical language use. Proverbs, in their tendency to act as both narrative and metaphor, and in their often relatively fixed structure, are an ideal test case for our ability to observe broader cultural narratives through the piecemeal, routine stories employed by the folk. Studies of n-grams tend to organize their interpretation around n-grams which attain a specific historical use-case. In our study of proverbs, we are able to trace the progression of a paradigm and its varying application to historical changes and events.

A natural limitation of this study, and any study that uses extant data to study language, is the issue of representativeness. In this study that limitation is twofold: Both the lexicon for directing the search, and the data being searched are inherently limited. While _The Dictionary of American Proverbs_ is extensive, and represents much that is known of proverbs in America, it naturally excludes new proverbs and does not account for many ways in which the structure of the proverbs it contains may be manipulated in their practical use. There are lexical resources that address recent proverbs, for example _The Dictionary of Modern Proverbs_ , and the methodology of this study may be readily applied to such lexica<a class="footnote-ref" href="#doyle2012"> [doyle2012] </a>. Previous studies on proverb frequency have relied on composite corpora, namely variations of the BNC (British National Corpus), which contains manually curated selections from several domains of text. As shown in this study, composite corpora may miss important differences in proverb usage between domains.

Fieldwork (digital and otherwise) continues to be important in identifying new proverbs and changing structures of existing proverbs. This task may be aided in the future by tools like StoryWrangler, that track _n_ -gram rank, likely capturing new proverbs in the process. The task then would be extracting likely proverbs from these data, which would require linguistic, cultural, and computational expertise.

Much of proverb scholarship has been concerned with the idea of aparemiological minimum: A minimum proverbial lexicon for a language and culture. As shown by Lau (1996), and again in the present study, computational studies of the frequency of proverb use can contribute to the understanding of these minima, as those proverbs which seem ubiquitous in large corpora ought to be understood by speakers of a language. Temporal analysis of their frequency may further validate that their frequency is related to enduring currency among the folk, rather than correspondence with a specific occurrence. Another concern in paremiology and phraeseology is the origins of sayings. Work like the present study can serve to both validate and expand on previous scholarship on the history of phrases.

In the study of the statistical distribution of natural language, there exists the idea of a kernel lexicon, a subset of words that are essential to communication using a given language. Much literature on the study of culture and education has focused on what one might consider aminimum of cultural literacy. Special attention has been paid to which proverbs constitute part of that minimum. It is clear from this study that the most common proverbs vary considerably between corpora. Given the prevalence of these popular proverbs in their respective contexts, we can posit that English learners would benefit in their comprehension of the language if they were familiar with these proverbs.

Analyses of the frequency and rank of proverbs in this study (shown in Appendix A) verify that with ever increasing amounts of machine-readable textual data, we may produce longitudinal phraseological studies.

Traditionally, the study of metaphor in language has relied on theoretical interpretations<a class="footnote-ref" href="#lakoff1985"> [lakoff1985] </a>. This study opens up the possibility for new avenues in the study of metaphor that incorporate the currency of specific metaphors among the folk. A natural extension of this study would be employing a similar method to study idioms and conventional metaphors.

As machine comprehension of natural language becomes increasingly important, this area too, would benefit from an expanded lexicon that includes proverbs and routine formulae, and understanding of metaphor may be assisted by a more basic understanding of the mapping from general to specific situations that exists in the use of proverbs.




## Acknowledgements

Thank you to David Dewhurst, Josh Minot, Michael Arnold, Nicholas Allgaier, Thayer Alshaabi for providing invaluable guidance in the writing of this paper. The authors are grateful for the computing resources provided by the Vermont Advanced Computing Core which was supported in part by NSF award No. OAC-1827314, and financial support from the Massachusetts Mutual Life Insurance Company to CMD and PSD.




## Appendix A

Figure 9 shows Zipf distributions for entries from Mieder's _Dictionary of American Proverbs_ (1992) for each of the four corpora studied, using 3-gram proverbs for Google Books and Twitter. While the distributions exhibit some Zipf’s Law-like behavior (heavy tails), we do not observe robust power-law scaling for all proverbs. We find the largest number of distinct proverbs appearing in Gutenberg and the _New York Times_ , on the order of thousands, with the Google Books and Twitter examples showing many fewer. We note that Zipf's law for words does not itself extend over many orders of magnitude<a class="footnote-ref" href="#williams2015a"> [williams2015a] </a>, typically only 2 or 3, and that it is meaningful, mixed length phrases that present many orders of magnitude of scaling<a class="footnote-ref" href="#williams2015b"> [williams2015b] </a>. The Zipf distributions for proverbs are thus comparable to what we see for single words.

With a more sophisticated method of proverb detection, one that captures minor variations in phrase structure, we would expect to see some adjustments to the Zipf distributions we have observed, though a priori it is not clear how. Short, robust proverbs (time flies) will be well counted, while longer ones for which, say, constituent function words might be changed based on context or era (he/she/they who hesitates…) would only see their apparent observed frequency of usage grow.

{{< figure src="images/figure09.png" caption="Zipf distributions for entries from Mieder's _Dictionary of American Proverbs_ <a class=\"footnote-ref\" href=\"#mieder1992\"> [mieder1992] </a>. For each corpus, proverbs are enumerated and shown on logarithmic axes as a function of rank, withhold your tongue,todelay may mean to forget,time will tell,andnever say nevertopping the charts in Gutenberg, NYT, Google, and Twitter respectively. Each distribution exhibits heavy-tailed behavior, more prominently for Gutenberg and NYT." alt="frequency charts for for the phraseshold your tongue,todelay may mean to forget,time will tell,andnever say neverin the Project Gutenberg, NYT, Google Books, and Twitter"  >}}





## Appendix B

The data for proverbs in the Gutenberg corpus were used to construct a network with documents as nodes, connected if a given proverb appears in both documents. When betweenness centrality was calculated for nodes in the network, surprisingly James Joyce's _Ulysses_ had the 14th highest centrality, close to several dictionaries of proverbs and quotations, and the collected works of Mark Twain (Table B-1). Creasy (2008) documented Joyce's use of proverbs in _Ulysses_ from a critical perspective, noting that they are often altered, and blend high and low culture in the work. As Joyce uses many fewer proverbs than a comprehensive proverbial dictionary, the book's centrality in this network implies that Joyce's use of proverbs is far from arbitrary, and that his choice of proverbs is purposefully situated in the broader context of English proverbial knowledge.
The 20 most central books by betweenness centrality, from a network of books connected by shared proverbs in Gutenberg. Notably, James Joyce's _Ulysses_ appears alongside several proverb and quotations collections, and the collected works of Mark Twain.Bookbtwn centrality1Dictionary of Quotations0.0430482Familiar Quotations0.0228213Dictionary of English Proverbs and Proverbial Phrases0.0142744A Polyglot of Foreign Proverbs0.0130615The Entire Project Gutenberg Works of Mark Twain0.0130416French Idioms and Proverbs0.0100837Roget's Thesaurus0.0097858Webster's Unabridged Dictionary0.0079789U.S. Copyright Renewals 1950 – 19770.00670910The Project Gutenberg Complete Works of Gilbert Parker0.00627811Proverb Lore0.00602812Complete Project Gutenberg John Galsworthy Works0.00389713Complete Project Gutenberg Works of George Meredith0.00366014Ulysses0.00318415The Historical Romances of Georg Ebers0.00316816Familiar Quotations0.00300717The Circle of Knowledge0.00288618The Complete Poetic and Dramatic Works of Robert Browning0.00274919Complete Project Gutenberg Oliver Wendell Holmes, Sr. Works0.00265720Motion Pictures, 1960-1969: Catalog of Copyright Entries0.002578



## Appendix C

Tables 2-4 show the total count of the 50 most popular proverbs in

their respective corpora.
The top 50 proverbs and proverbial expressions (from the _Dictionary of American Proverbs_ ) in the entire Gutenberg Corpus.ProverbCount1hold your tongue2,2842the sooner the better1,5363be yourself7394let bygones be bygones6855time flies6036alls well that ends well5887one thing at a time5808business is business5349sink or swim53110forgive and forget47711take it or leave it43612nothing is impossible42113better late than never41914every man for himself41415know thyself39416share and share alike37217slow but sure36318live and let live35619the more the merrier35220the die is cast34821honesty is the best policy33922to be or not to be33523do or die32224never say die31925extremes meet28926art for arts sake28627all men are created equal26528let well enough alone26029time is money25030no accounting for taste24931peace at any price24432tastes differ24133history repeats itself23534boys will be boys23535charity begins at home23136love is blind22837the end justifies the means22738one good turn deserves another22439blood is thicker than water22140not wisely but too well21941all things work together for good21342first come first served20143keep the wolf from the door19644dead men tell no tales19545the wages of sin is death19146seeing is believing18747keep a stiff upper lip18648ignorance is bliss18549where theres a will theres a way18350murder will out179The top 50 proverbs and proverbial expressions (from the _Dictionary of American Proverbs_ ) in the _New York Times_ from 1987-2007.ProverbCount1to delay may mean to forget1,0752enough is enough8913time will tell8644pay as you go5975take it or leave it5656do or die5287first come first served4638be yourself3489father knows best30710never say never27611live and let live27212money talks24413the sooner the better24014better late than never22415sink or swim21816boys will be boys21317time flies20518time is of the essence20419divide and conquer19820gentlemen prefer blondes19221to be or not to be18722the show must go on18523time is money17424talk is cheap16725every man for himself16626leave well enough alone16327put up or shut up16128business is business15929accentuate the positive15730forgive and forget15131you get what you pay for14232safety first14233too little and too late14034there is no easy way13235let the chips fall where they may13136all men are created equal12937the more the merrier12838history repeats itself12239let bygones be bygones11740one thing at a time11341let nature take its course10642never say die10643seeing is believing10244nothing is impossible10045war is hell9546the worst is yet to come8547actions speak louder than words8248gone but not forgotten8249to each his own8050let the buyer beware80The top 50 3-gram proverbs and proverbial expressions (from the _Dictionary of American Proverbs_ ) in the Google Books Ngram Corpus.ProverbCount1hold your tongue131,4262time will tell65,6403forgive and forget45,1894enough is enough43,1495business is business30,1016sink or swim26,3157nothing is impossible25,6958easy does it23,6559do or die21,67210time is money18,85611practice makes perfect17,46912never say never16,64913divide and conquer15,67314love is blind14,43915seeing is believing12,95116never say die12,32917ignorance is bliss11,83818history repeats itself11,52919fair is fair10,45620slow but sure9,89821forewarned is forearmed9,86022love conquers all9,83923misery loves company9,65424facts are facts8,94425time will pass8,38926orders are orders7,62027the truth hurts7,29228blood will tell6,84029father knows best6,78330try anything once6,38831murder will out6,34932silence is golden6,27833war is hell6,13634business before pleasure5,81135talk is cheap5,72336revenge is sweet5,40037familiarity breeds contempt5,09538might makes right4,76839consider the source4,67740toe the mark4,54941every little helps4,13942time marches on4,01943nothing is perfect4,00744money is power3,75745circumstances alter cases3,66846respect your elders3,64447gentlemen prefer blondes2,92248mother knows best2,90849love never fails2,84850nobody is perfect2,801The top 50 proverbs and proverbial expressions (from the _Dictionary of American Proverbs_ ) on Twitter from 2008-2021.ProverbCount1never say never2,549,0952enough is enough2,182,4603nothing is impossible978,5334time will tell869,6625the truth hurts748,2856forgive and forget557,2947talk is cheap465,6088love is blind426,0109practice makes perfect405,63510nobody is perfect399,32411time is money383,63212ignorance is bliss377,03713do or die316,32814history repeats itself307,46715love never fails255,79516misery loves company226,21717divide and conquer94,08518facts are facts90,51319respect your elders89,37220seeing is believing86,16921time will pass84,43222silence is golden82,34623love conquers all80,96424revenge is sweet69,82025health is wealth66,27426never say die65,11527prayer changes things63,75728iron sharpens iron57,06529sink or swim50,36130tomorrow never comes50,29731business is business39,52532hold your tongue34,34433nothing is perfect34,05034try anything once33,37035mother knows best26,84836every little helps23,67237never waste time22,24438fair is fair18,12539slow but sure14,40440consider the source14,20141justice is blind11,60442money is power10,18643time works wonders10,07944time changes everything9,51245like attracts like8,32046familiarity breeds contempt8,16647war is hell7,43948easy does it6,07149gentlemen prefer blondes5,27350courtesy costs nothing3,890
## Bibliography

<ul>
<li id="abello2012">Abello, J., Broadwell, P. and Tangherlini, T. R. (2012a) “Computational folkloristics,”  _Communications of the ACM_ , 55(7), pp. 60–70. doi:<a href="https://doi.org/10.1145/2209249.2209267">10.1145/2209249.2209267</a>.
</li>
<li id="abrams1994">Abrams, R. D. and Babcock, B. A. (1994) “The literary use of proverbs,” in Mieder, W. (ed.) _Wise words: Essays on the Proverb_ . New York: Garland (Garland reference library of the humanities, vol. 1638), pp. 415–437.
</li>
<li id="albig1931">Albig, W. (1931) “Proverbs and social control,”  _Sociology and Social Research_ , (15), pp. 527–535.
</li>
<li id="alshaabi2020">Alshaabi, T. _et al._ (2020) “Storywrangler: A massive exploratorium for sociolinguistic, cultural, socioeconomic, and political timelines using Twitter,”  _arXiv:2007.12988 [physics]_ . Available at:<a href="http://arxiv.org/abs/2007.12988">http://arxiv.org/abs/2007.12988</a>(Accessed: 7 December 2020).
</li>
<li id="alter2018">Alter, C. (2018) “The Young and the Relentless,”  _TIME_ . Available at:<a href="https://time.com/magazine/us/5210502/april-2nd-2018-vol-191-no-12-u-s/">https://time.com/magazine/us/5210502/april-2nd-2018-vol-191-no-12-u-s/</a>.
</li>
<li id="andersson2013">Andersson, D. (2013) “Understanding figurative proverbs: A model based on conceptual blending,”  _Folklore_ , 124(1), pp. 28–44. doi:<a href="https://doi.org/10.1080/0015587X.2012.734442">10.1080/0015587X.2012.734442</a>.
</li>
<li id="bain1939">Bain, R. (1939) “Verbal stereotypes and social control,”  _Sociology and Social Research_ , (23), pp. 431–446.
</li>
<li id="balasubrahmanyan1996">Balasubrahmanyan, V. K. and Naranan, S. (1996) “Quantitative linguistics and complex system studies,”  _Journal of Quantitative Linguistics_ , 3(3), pp. 177–228. doi:<a href="https://doi.org/10.1080/09296179608599629">10.1080/09296179608599629</a>.
</li>
<li id="bnc2001"> “British National Corpus,” (2001). Available at:<a href="http://www.natcorp.ox.ac.uk">http://www.natcorp.ox.ac.uk</a>.
</li>
<li id="cancho2001">Cancho, R. F. i. and Solé, R. V. (2001) “Two regimes in the frequency of words and the origins of complex lexicons: Zipf’s law revisited,”  _Journal of Quantitative Linguistics_ , 8(3), pp. 165–173.
</li>
<li id="cancho2003">Cancho, R. F. i. and Sole, R. V. (2003) “Least effort and the origins of scaling in human language,”  _Proceedings of the National Academy of Sciences_ , 100(3), pp. 788–791. doi:<a href="https://doi.org/10.1073/pnas.0335980100">10.1073/pnas.0335980100</a>.
</li>
<li id="cermak2014">Čermák, F. (2014) _Proverbs: their lexical and semantic features_ . Burlington, Vermont: The University of Vermont (Supplement series of Proverbium Yearbook of International Proverb Scholarship, volume 36).
</li>
<li id="clancy1990">Clancy, T. (1990). _Clear and present danger_ . Berkley mass-market edition. ed. Berkley Books, New York.
</li>
<li id="clauset2009">Clauset, A., Shalizi, C. R. and Newman, M. E. J. (2009) “Power-law distributions in empirical data,”  _SIAM Review_ , 51(4), pp. 661–703. doi:<a href="https://doi.org/10.1137/070710111">10.1137/070710111</a>.
</li>
<li id="corominasmurtra2010">Corominas-Murtra, B. and Solé, R. V. (2010) “Universality of Zipf’s law,”  _Physical Review E_ , 82(1), p. 011102. doi:<a href="https://doi.org/10.1103/PhysRevE.82.011102">10.1103/PhysRevE.82.011102</a>.
</li>
<li id="corral2015">Corral, A., Boleda, G. and Ferrer-i-Cancho, R. (2015) “Zipf’s law for word frequencies: Word forms versus lemmas in long texts,”  _PLOS ONE_ , 10(7), p. e0129031. doi:<a href="https://doi.org/10.1371/journal.pone.0129031">10.1371/journal.pone.0129031</a>.
</li>
<li id="cram1994">Cram, D. (1994) “The linguistic status of the Proverb,” in Mieder, W. (ed.) _Wise Words: Essays on the Proverb_ . New York: Garland (Garland reference library of the humanities), pp. 73–97.
</li>
<li id="creasy2008">Creasy, M. (2008) “'To vary the timehonoured adage': Ulysses and the Proverb,”  _English_ , 57(217), pp. 65–81. doi:<a href="https://doi.org/10.1093/english/efn008">10.1093/english/efn008</a>.
</li>
<li id="dodds2017">Dodds, P. S. et al. (2017) “Simon’s fundamental rich-get-richer model entails a dominant first-mover advantage,”  _Physical Review E_ , 95(5), p. 052301. doi:<a href="https://doi.org/10.1103/PhysRevE.95.052301">10.1103/PhysRevE.95.052301</a>.
</li>
<li id="dodds2021">Dodds PS, Minot JR, Arnold MV, Alshaabi T, Adams JL, Reagan AJ, et al. (2021) “Computational timeline reconstruction of the stories surrounding Trump: Story turbulence, narrative control, and collective chronopathy,” PLoS ONE 16(12): e0260592.<a href="https://doi.org/10.1371/journal.pone.0260592">https://doi.org/10.1371/journal.pone.0260592</a>
</li>
<li id="doyle2012">Doyle, C. C., Mieder, W. and Shapiro, F. R. (2012) _The Dictionary of Modern Proverbs_ . New Haven: Yale University Press.
</li>
<li id="dundes1965">Dundes, A. (1965) “The study of folklore in literature and culture: Identification and interpretation,”  _The Journal of American Folklore_ , 78(308), p. 136. doi:<a href="https://doi.org/10.2307/538280">10.2307/538280</a>.
</li>
<li id="fazly2009">Fazly, A., Cook, P. and Stevenson, S. (2009) “Unsupervised Type and Token Identification of Idiomatic Expressions,”  _Computational Linguistics_ , 35(1), pp. 61–103. doi:<a href="https://doi.org/10.1162/coli.08-010-R1-07-048">10.1162/coli.08-010-R1-07-048</a>.
</li>
<li id="georgia1991">Georgia, S. C. of (1991) “Cunningham v. State 1991.” 
</li>
<li id="glaberson1992">Glaberson, W. (1992) “Assault case renews debate on rape shield law,”  _The New York Times_ .
</li>
<li id="haas2008">Haas, H. A. (2008) “Proverb familiarity in the United States: Cross-regional comparisons of the paremiological minimum,”  _Journal of American Folklore_ , 121(481), pp. 319–347. doi:<a href="https://doi.org/10.2307/20487611">10.2307/20487611</a>.
</li>
<li id="haas2022">Haas, H. A. (2022) “The Proverbs of a Pandemic: The Early Months of the COVID-19 Pandemic Viewed through the Lens of Google Trends,”   _Journal of American Folklore_ , 135 (535), pp. 26–48. Doi:<a href="https://doi.org/10.5406/15351882.135.535.02">https://doi.org/10.5406/15351882.135.535.02</a>
</li>
<li id="hanley1992">[Hanley, R. (1992) “Jury chosen in Glen Ridge assault trial,”  _The New York Times_ .
</li>
<li id="henry1996">Henry, J. (1996) “How the money was spent in previous environmental Bond Acts,”  _The New York Times_ .
</li>
<li id="hunter2007">Hunter, J. D. (2007) “Matplotlib: A 2D graphics environment,”  _Computing in Science & Engineering_ , 9(3), pp. 90–95. doi:<a href="https://doi.org/10.1109/MCSE.2007.55">10.1109/MCSE.2007.55</a>.
</li>
<li id="koplenig2018">Koplenig, A. (2018) “Using the parameters of the Zipf–Mandelbrot law to measure diachronic lexical, syntactical and stylistic changes — a large-scale corpus analysis,”  _Corpus Linguistics and Linguistic Theory_ , 14(1), pp. 1–34. doi:<a href="https://doi.org/10.1515/cllt-2014-0049">10.1515/cllt-2014-0049</a>.
</li>
<li id="lakoff1985">Lakoff, G. and Johnson, M. (1985) _Metaphors We Live By_ . Chicago, Ill.: Univ. of Chicago Press.
</li>
<li id="lau1996">Lau, K. J. (1996) “'It’s About Time': The ten proverbs most frequently used newspapers and their relation to American values,”  _Proverbium_ , 13, pp. 135–59.
</li>
<li id="leskovec2009">Leskovec, J., Backstrom, L. and Kleinberg, J. (2009) “Meme-tracking and the dynamics of the news cycle,” in _Proceedings of the 15th ACM SIGKDD international conference on Knowledge discovery and data mining - KDD ’09_ . Paris, France: ACM Press, p. 497. doi:<a href="https://doi.org/10.1145/1557019.1557077">10.1145/1557019.1557077</a>.
</li>
<li id="lieber1994">Lieber, M. D. (1994) “Analogic ambiguity: A paradox of proverb usage,” in Mieder, W. (ed.) _Wise Words: Essays on the Proverb_ . New York: Garland (Garland reference library of the humanities, vol. 1638), pp. 99–126.
</li>
<li id="loveisblind2020"> “Love Is Blind” (2020). Netflix.
</li>
<li id="mandelbrot1953">Mandelbrot, B. (1953) “An informational theory of the statistical structure of languages,” in Jackson, W. (ed.) _Communication Theory_ . Academic Press, Princeton, pp. 486–502.
</li>
<li id="marchforourlives2018"> “March for Our Lives Highlights: Students Protesting Guns Say 'Enough Is Enough'” (2018) _The New York Times_ .
</li>
<li id="martinezmekler2009">Martínez-Mekler, G. _et al._ (2009) “Universality of rank-ordering distributions in the arts and sciences,”  _PLoS ONE_ . Edited by M. Costa, 4(3), p. e4791. doi:<a href="https://doi.org/10.1371/journal.pone.0004791">10.1371/journal.pone.0004791</a>.
</li>
<li id="mechling2004">Mechling, J. (2004) ““Cheaters Never Prosper” and other lies adults tell kids: Proverbs and the culture wars over character,” in Lau, K. J., Tokofsky, P., and Winick, S. D. (eds) _What goes around comes around: the circulation of proverbs in contemporary life: Essays in Honor of Wolfgang Mieder_ . Logan: Utah State University Press, pp. 107–126.
</li>
<li id="michel2011">Michel, J.-B. _et al._ (2011) “Quantitative analysis of culture using millions of digitized books,”  _Science_ , 331(6014), pp. 176–182. doi:<a href="https://doi.org/10.1126/science.1199644">10.1126/science.1199644</a>.
</li>
<li id="mieder2004">Mieder, W. (2004) _Proverbs: a handbook_ . Westport, Conn: Greenwood Press (Greenwood folklore handbooks).
</li>
<li id="mieder2005">Mieder, W. (2005) _Proverbs are the best policy: Folk wisdom and American politics_ . Logan, Utah: Utah State University Press.
</li>
<li id="mieder2008">Mieder, W. (2008) _'Proverbs speak louder than words': Folk wisdom in art, culture, folklore, history, literature and mass media_ . New York: P. Lang.
</li>
<li id="mieder2012">Mieder, W. (2012) _Proverbs are never out of season: Popular wisdom in the modern age_ . New York: Peter Lang (International folkloristics, v. 7).
</li>
<li id="mieder2019">Mieder, W. (2019) _“Right makes Might”: Proverbs and the American worldview_ . Bloomington, Indiana: Indiana University Press.
</li>
<li id="mieder1992">Mieder, W., Kingsbury, S. A. and Harder, K. B. (eds) (1992) _A Dictionary of American Proverbs_ . New York: Oxford University Press.
</li>
<li id="moon1998">Moon, R. (1998) _Fixed expressions and idioms in English: A corpus-based approach_ . Oxford : New York: Clarendon Press ; Oxford University Press (Oxford studies in lexicography and lexicology).
</li>
<li id="norrick1985">Norrick, N. R. (1985) _How Proverbs Mean: Semantic Studies in English Proverbs_ . Berlin, New York: DE GRUYTER MOUTON. doi:<a href="https://doi.org/10.1515/9783110881974">10.1515/9783110881974</a>.
</li>
<li id="obelkevich1994">Obelkevich, J. (1994) “Proverbs and social history,” in Mieder, W. (ed.) _Wise Words: Essays on the Proverb_ . New York: Garland (Garland reference library of the humanities, vol. 1638), pp. 211–252.
</li>
<li id="ozbal2016a">Özbal, G. _et al._ (2016) “Learning to identify metaphors from a corpus of proverbs,” in _Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing_ . Austin, Texas: Association for Computational Linguistics, pp. 2060–2065. doi:<a href="https://doi.org/10.18653/v1/D16-1220">10.18653/v1/D16-1220</a>.
</li>
<li id="ozbal2016b">Özbal, G., Strapparava, C. and Sinem Tekiroglu, S. (2016) “PROMETHEUS: A corpus of proverbs annotated with metaphors,”  _LREC, Proceedings of the Tenth International Conference on Language Resources and Evaluation_ (LREC’16), pp. 3787–3793.
</li>
<li id="pechenick2015a">Pechenick, Eitan Adam, Danforth, C. M. and Dodds, P. S. (2015) “Characterizing the Google Books corpus: Strong limits to inferences of socio-cultural and linguistic evolution,”  _PLOS ONE_ . Edited by A. Barrat, 10(10), p. e0137041. doi:<a href="https://doi.org/10.1371/journal.pone.0137041">10.1371/journal.pone.0137041</a>.
</li>
<li id="pechenick2015b">Pechenick, Eitan A., Danforth, C. M. and Dodds, P. S. (2015) “Is language evolution grinding to a halt? The scaling of lexical turbulence in English fiction suggests it is not.” 
</li>
<li id="permiakov1989">Permiakov, G. L. (1989) “On the question of a Russian paremiological minimum.,”  _Proverbium_ , 6, pp. 91–102.
</li>
<li id="reagan2016">Reagan, A. J. _et al._ (2016) “The emotional arcs of stories are dominated by six basic shapes,”  _EPJ Data Science_ , 5(1), p. 31. doi:<a href="https://doi.org/10.1140/epjds/s13688-016-0093-1">10.1140/epjds/s13688-016-0093-1</a>.
</li>
<li id="robinson2020">Robinson, D. (2020) _Gutenbergr_ . Available at:<a href="https://cran.r-project.org/web/packages/gutenbergr/index.html">https://cran.r-project.org/web/packages/gutenbergr/index.html</a>.
</li>
<li id="sag2002">Sag, I. A. _et al._ (2002) “Multiword expressions: A pain in the neck for NLP,” in Goos, G. et al. (eds) _Computational Linguistics and Intelligent Text Processing_ . Berlin, Heidelberg: Springer Berlin Heidelberg, pp. 1–15. doi:<a href="https://doi.org/10.1007/3-540-45715-1_1">10.1007/3-540-45715-1_1</a>.
</li>
<li id="sandhaus2008">Sandhaus, E. (2008) “The New York Times Annotated Corpus,”  _Linguistic Data Consortium_ . doi:<a href="https://doi.org/10.35111/77BA-9X74">10.35111/77BA-9X74</a>.
</li>
<li id="semones2020">Semones, E. (2020) “'Enough is enough': Thousands descend on D.C. for largest George Floyd protest yet,”  _POLITICO_ .
</li>
<li id="shutova2010">Shutova, E. (2010) “Models of metaphor in NLP,” in _Proceedings of the 48th Annual Meeting of the Association for Computational Linguistics_ . Uppsala, Sweden: Association for Computational Linguistics, pp. 688–697. Available at:<a href="https://www.aclweb.org/anthology/P10-1071">https://www.aclweb.org/anthology/P10-1071</a>.
</li>
<li id="simon1960">Simon, H. A. (1960) “Some further notes on a class of skew distribution functions,”  _Information and Control_ , 3(1), pp. 80–88. doi:<a href="https://doi.org/10.1016/S0019-9958(60)90302-8">10.1016/S0019-9958(60)90302-8</a>.
</li>
<li id="steyer2015">Steyer, K. (2015) “Proverbs from a corpus linguistic point of view,” in Hrisztova-Gotthardt, H. and Aleksa Varga, M. (eds) _Introduction to Paremiology: A Comprehensive Guide to Proverb Studies_ . Warsaw, Poland: DE GRUYTER OPEN, pp. 206–228. doi:<a href="https://doi.org/10.2478/9783110410167">10.2478/9783110410167</a>.
</li>
<li id="swuste2010">Swuste, P., Gulijk, C. van and Zwaard, W. (2010) “Safety metaphors and theories, a review of the occupational safety literature of the US, UK and The Netherlands, till the first part of the 20th century,”  _Safety Science_ , 48(8), pp. 1000–1018. doi:<a href="https://doi.org/10.1016/j.ssci.2010.01.020">10.1016/j.ssci.2010.01.020</a>.
</li>
<li id="tangherlini2016">Tangherlini, T. R. (2016) “Big folklore: A special issue on computational folkloristics,”  _The Journal of American Folklore_ , 129(511), p. 5. doi:<a href="https://doi.org/10.5406/jamerfolk.129.511.0005">10.5406/jamerfolk.129.511.0005</a>.
</li>
<li id="pandas2020">The pandas development team (2020) _pandas-dev/pandas: Pandas_ . Zenodo. doi:<a href="https://doi.org/10.5281/zenodo.3509134">10.5281/zenodo.3509134</a>.
</li>
<li id="tweedle2012">Tweedle, V. and Smith, R. J. (2012) “A mathematical model of Bieber Fever: The most infectious disease of our time?,” in.
</li>
<li id="underwood2018">Underwood, T., Bamman, D. and Lee, S. (2018) “The transformation of gender in English-language fiction,” p. 25.
</li>
<li id="voteyes1996"> “Vote Yes on the Bond Act,” (1996) _The New York Times_ .
</li>
<li id="whiting2014">Whiting, B. J. (2014) _Modern Proverbs and Proverbial Sayings_ . Available at:<a href="https://0-doi-org.pugwash.lib.warwick.ac.uk/10.4159/harvard.9780674864153">https://0-doi-org.pugwash.lib.warwick.ac.uk/10.4159/harvard.9780674864153</a>.
</li>
<li id="williams2015a">Williams, J. R. _et al._ (2015a) “Text mixing shapes the anatomy of rank-frequency distributions,”  _Physical Review E_ , 91(5), p. 052811. doi:<a href="https://doi.org/10.1103/PhysRevE.91.052811">10.1103/PhysRevE.91.052811</a>.
</li>
<li id="williams2015b">Williams, J. R. et al. (2015b) “Zipf’s law holds for phrases, not words,”  _Scientific Reports_ , 5(1), p. 12209. doi:<a href="https://doi.org/10.1038/srep12209">10.1038/srep12209</a>.
</li>
<li id="zemeckis1994">Zemeckis, R. (1994) _Forrest Gump_ . Paramount Pictures.
</li>
<li id="zipf2012">Zipf, G. K. (2012) _Human behavior and the principle of least effort: An introduction to human ecology._ Mansfield Centre, Conn: Martino Publishing [u.a.].
</li>

</ul>
