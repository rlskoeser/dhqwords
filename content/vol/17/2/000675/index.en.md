---
type: article
dhqtype: article
title: "SEDES: Metrical Position in Greek Hexameter"
date: 2023-05-31
article_id: "000675"
volume: 017
issue: 2
authors:
- Stephen A. Sansom
- David Fifield
translationType: original
abstract: |
   This article outlines the processes of SEDES, a program that automatically identifies, quantifies, and visualizes the metrical position of lemmata in ancient Greek hexameter poetry; and gives examples of its application to investigate the effects of metrical position on poetic features such as formularity, expectancy, and intertextuality.
teaser: "Introduction to SEDES, a program that automatically identifies, quantifies, and visualizes the metrical position of lemmata in ancient Greek hexameter poetry."
order: 4
draft: true
---



## Introduction

Metrical position has long interested scholars of Greek hexameter poetry. In his _Encheiridion dia Metrôn_ ( “Handbook on Meter” ), Hephaestion of Alexandria (2nd c. CE) referred to positions within meter asχώραι( “places; positions,” cf. _LSJ_ s.v.χώρα 3) and used the term to describe places in the line that contain various types of metrical “feet” (πόδες, cf.<a class="footnote-ref" href="#lsj"> [lsj] </a>s.v.πούς 4), such as the dactyl (‒ ⏑ ⏑) and spondee (‒ ‒), as well as the “final” (τῆς τελευταίας, 7.1) position that may contain syllabic diversity, such as catalexis.[^1] Aristides Quintilianus (circa 4th c. CE) likewise usedχώραto describe metrical position in his _Peri Musikês_ ( “On Music” ), including the “first places” (ταῖς πρώταις χώραις, 1.24.27) of feet in the line (cf.<a class="footnote-ref" href="#vanophuijsen1987"> [vanophuijsen1987] </a><a class="footnote-ref" href="#winnington1963"> [winnington1963] </a>). But it was not until the early 20th century that scholars interested in the statistical analysis of meter systematized notation for all possible positions of linguistic phenomena in the hexameter line; of these efforts,<a class="footnote-ref" href="#oneill1942"> [oneill1942] </a>has gained the most currency.[^2] Later,<a class="footnote-ref" href="#giangrande1959"> [giangrande1959] </a>and others Latinized theterminus technicusfromχώραto _ sedes _ ( “seat; place” ), and now the term is ubiquitous in philological studies of metrical position.

With this greater precision, scholars have examined various forms of repetition in hexameter according to their metrical position. These studies largely focus on articulating metrical tendencies, such as colometric patterns<a class="footnote-ref" href="#porter1951"> [porter1951] </a>,<a class="footnote-ref" href="#barnes1986"> [barnes1986] </a>and the primacy of _ caesurae _ (τομαί) at certain _ sedes _ <a class="footnote-ref" href="#frankel1926"> [frankel1926] </a>,<a class="footnote-ref" href="#beekes1972"> [beekes1972] </a>.[^3] In particular,<a class="footnote-ref" href="#oneill1942"> [oneill1942] </a>discovered what he called the “localization” of “word-types,” that is, the “concentration of occurrences (of specific metrical shapes) in but a few of the possible positions” (114). Following O’Neill,<a class="footnote-ref" href="#porter1951"> [porter1951] </a>argued that such tendencies established “patterns of expectancy” or norms in the mind of poet and audience, and philologists have begun to explore the potential intertextual, stylistic, cognitive, and literary effects of these patterns, for example, in<a class="footnote-ref" href="#giangrande1967"> [giangrande1967] </a>,<a class="footnote-ref" href="#white1986"> [white1986] </a>,<a class="footnote-ref" href="#hagel1994"> [hagel1994] </a>,<a class="footnote-ref" href="#kahane1994"> [kahane1994] </a>,<a class="footnote-ref" href="#martin2000"> [martin2000] </a>,<a class="footnote-ref" href="#forstall2012"> [forstall2012] </a>,<a class="footnote-ref" href="#schein2015"> [schein2015] </a>, and<a class="footnote-ref" href="#forstall2019"> [forstall2019] </a>.[^4] 

These studies have provided useful data and promising applications, but their potential has been somewhat constrained by limitations in scope, objects of analysis, and at times computational media. O’Neill treated only a relatively small number of lines, though his survey has been expanded and the data verified by<a class="footnote-ref" href="#porter1951"> [porter1951] </a>,<a class="footnote-ref" href="#mcdonough1966"> [mcdonough1966] </a>,<a class="footnote-ref" href="#hagel2004"> [hagel2004] </a>, and<a class="footnote-ref" href="#forstall2012"> [forstall2012] </a>. A lack of aggregate statistics on repeated words bysedeshas restricted intertextual readings to the examination of infrequent words,hapax, ordis legomena, for example in<a class="footnote-ref" href="#mclennan1977"> [mclennan1977] </a>.[^5] Even inquiries into anomalous behavior such as breaks in Hermann’s Bridge (that is, avoidance of word end between the biceps [two short elements] of the fourth foot<a class="footnote-ref" href="#martin2000"> [martin2000] </a>,<a class="footnote-ref" href="#schein2015"> [schein2015] </a>) have been confined to a few authors or passages, due to a lack of available data. Existing digital tools for identifying repetitions in hexameter poetry — for example, the Thesaurus Linguae Graecae<a class="footnote-ref" href="#tlg"> [tlg] </a>or Perseus Project under PhiloLogic<a class="footnote-ref" href="#philologic"> [philologic] </a>, for searching corpora by word list, lemma, or text string; the<a class="footnote-ref" href="#chicagohomer"> [chicagohomer] </a>, for repeated phrases; and<a class="footnote-ref" href="#tesserae"> [tesserae] </a>, for intertexts byn‑gram matching<a class="footnote-ref" href="#forstall2015"> [forstall2015] </a>— do not take into account metrical position. Future work on metrical position in Greek hexameter needs new methods and access to data in order to identify repetitive phenomena in meter more accurately and completely.[^6] With such information, scholars can then better discern their linguistic causes and potential poetic effects.

In this article, we introduce SEDES, a software system for identifying, quantifying, and visualizing metrical position in ancient Greek hexameter poetry. Like intertextualist studies of metrical position, SEDES at present focuses on the repetition of words — more specifically, of lemmata. Our present purpose is to describe the design of the SEDES system and demonstrate a sample of its utility.[^7] Engineering the system required bringing together existing resources in the processing of Greek poetry, as well as the creation of new processes, measurements, tests, and visualizations, all of which aid researchers of Greek literature and otherwise in the processing of poetic texts for computer and literary analysis and, more generally, provide a method that benefits the quantitative analysis of repetitive language in meter. In what follows, we show how SEDES generates these data, before giving examples of its application to Greek hexameter poetics, in particular the fields of oral formularity and intertextuality.




## Processing Pipeline

The core function of SEDES is to assign a numeric value — an expectancy score — to every word in a work of verse. The expectancy of a word is a quantification, in a sense we will define later, of how frequently that word’s lemma appears at a givensedesin a corpus of works. After computing expectancy scores, SEDES provides ways of visualizing and interacting with them. The SEDES system is composed of a pipeline of programs, each of which performs a portion of the processing task. See Figure 1.

{{< figure src="images/figure01.png" caption="The SEDES processing pipeline comprises three programs: tei2csv, expectancy, and tei2html. Visualizing a text requires analyzing not only it, but all other texts of the corpus." alt="Schematic diagram of information flow through the programs of SEDES"  >}}


The input to the pipeline is a set of XML documents marked up according to the TEI Guidelines<a class="footnote-ref" href="#tei"> [tei] </a>. The selection of documents defines thecorpusrelative to which expectancy scores are computed. In developing SEDES, we have used 12 TEI texts from the Perseus Project<a class="footnote-ref" href="#perseus"> [perseus] </a>, totaling about 73,000 lines, with a minimum length of 479 lines and a maximum of 21,356. See Table 1 for a listing of texts, which span more than a millennium and comprise a variety of styles. We often define the corpus as all 12 works, but the system makes it possible to work with only a subset, in order to include or exclude certain authors or eras, for example.
Works in the full SEDES corpus.WorkDate (circa c.)LinesWords[Iliad](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0133),[Homer](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0133)8th BCE15,683111,865[Odyssey](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0135),[Homer](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0135)8th BCE12,10787,185[Homeric Hymns](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0137)7th–6th BCE2,34216,022[Theogony](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0129),[Hesiod](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0129)8th BCE1,0427,040[Works and Days](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0131),[Hesiod](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0131)8th BCE8315,856[Shield of Heracles](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0127),[Hesiod](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0127)6th BCE4793,298[Argonautica](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0227),[Apollonius Rhodius](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0227)4th BCE5,83438,841[Hymns](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:2008.01.0481)[, Callimachus](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:2008.01.0481)3rd BCE9416,480[Phaenomena](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:2008.01.0483),[Aratus Solensis](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:2008.01.0483)3rd BCE1,1557,752[Idylls](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0228),[Theocritus](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0228)3rd BCE2,52718,071[Fall of Troy](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:2008.01.0490)[, Quintus Smyrnaeus](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:2008.01.0490)4th CE8,80160,098[Dionysiaca](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:2008.01.0485),[Nonnus of Panopolis](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:2008.01.0485)5th CE21,356126,870Total73,098489,378
Though similar techniques could be applied to other forms of verse, SEDES is specially adapted to hexameter. In hexameter, vowels are distinguished by length. A line consists of six feet, which each may be either a long syllable followed by another long syllable (a spondee, denoted– –), or a long syllable followed by two short syllables (a dactyl,– ⏑ ⏑). The metrical shape of a word — its pattern of long and short syllables — limits the places (sedes) in a line it may appear. (Though there is some flexibility: a word may, subject to certain rules, sometimes be reinterpreted to have a different metrical shape than it would otherwise have, in order to fit the meter.) Even given the range of permissibleslotsfor each word, most words tend to appear at somesedesmore often than others. It is this non-uniform distribution of word placements that SEDES is designed to analyze.

The first program in the SEDES pipeline, tei2csv, assigns a lemma and asedesto every word in the corpus. (We consider multiple instances of the same word separately — the same word in different lines may appear at differentsedes, for example.) Later parts of the pipeline will operate, not on the original words of the text directly, but on the “lemma– sedes pairs” to which they are mapped by tei2csv. Concretely, tei2csv does the following three steps of segmentation, lemmatization, and scansion for every document in the corpus:

1. Break the document into lines and words.2. Look up a lemma for each word.3. Scan every line metrically, thereby finding asedesfor each word.


The output of tei2csv is a collection of CSV files, one for each TEI file in the corpus. The CSV files map every instance of every word in the corpus to the lemma andsedesof that instance, what we call a lemma–sedespair. The next program in the pipeline, called expectancy, takes these CSV files as input and does the statistics necessary to compute expectancy scores:

4. Compute an expectancy score for every unique lemma–sedespair.


The output of the expectancy program is another CSV file that maps every observed combination of lemma andsedesto a numeric expectancy score. The final program in the pipeline, tei2html, takes as input the expectancy CSV file and the TEI of any single work — which may or may not be part of the corpus that was used to define expectancy — and produces an output visualization of the work:

5. Produce an HTML file that depicts differences in expectancy across words.


We will describe the above steps in detail in the subsections that follow. But first, we will walk through an example of applying the SEDES processing pipeline to book 1, line 1 of the _Odyssey_ <a class="footnote-ref" href="#perseusodyssey"> [perseusodyssey] </a>from start to finish.

In the source TEI file, the line looks like this:[^8] 
 
```xml
<l>a)/ndra moi e)/nnepe, mou=sa, polu/tropon, o(\s ma/la polla\</l>
```
 
The <l> and </l> XML tags delimit a line. The text between the tags is Beta Code<a class="footnote-ref" href="#tlgbetacode"> [tlgbetacode] </a>, a method of representing written ancient Greek using ASCII characters:a represents the letter alpha;),/,\, and =are various diacritics; and so on. The tei2csv program isolates the line from the XML markup and decodes the Beta Code to yield a line of verse represented in Unicode:
 
```
ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ
```
 
( “Tell me, Muse, about the versatile man, who very many…” ) The program then scans the line metrically, marking each syllable as long (notated–) or short (notated⏑). A long syllable counts for 1 position and a short syllable counts for 0.5. The scansion of the example line is:
 
```
ἄν δρα μοι ἔν νε πε, μοῦ σα, πο λύ τρο πον, ὃς μά λα πο λλὰ – ⏑ ⏑ – ⏑ ⏑ – ⏑ ⏑ – ⏑ ⏑ – ⏑ ⏑ – – 1 2 2.5 3 4 4.5 5 6 6.5 7 8 8.5 9 10 10.5 11 12
```
 
Thesedesof a word is thesedesof its first syllable. In this example,ἄνδραis atsedes 1,μοιis atsedes 2.5, and so on. Separately from scansion, every word in the line is mapped to its lemma. Here, the wordἄνδραmaps to the lemmaἀνήρ,μοιmaps toἐγώ, and so on for the rest of the words. The output of this process is a lemma and asedesfor each word: a lemma–sedespair. The calculation ofsedesand the finding of a lemma are independent operations: it is the syllables of the original words of the line, not their derived lemmata, that determinesedes.

The tei2csv program emits a CSV file with one row per input word, representing the word’s lemma,sedes, and other metadata.
workbook_nline_nword_nwordlemmasedesmetrical_shapescannednum_scansionsline_textOd.,1,1,1,ἄνδρα,ἀνήρ,1,–⏑,auto,1"ἄνδρα μοι..."Od.,1,1,2,μοι,ἐγώ,2.5,⏑,auto,1"ἄνδρα μοι..."Od.,1,1,3,ἔννεπε,ἐνέπω,3,–⏑⏑,auto,1"ἄνδρα μοι..."Od.,1,1,4,μοῦσα,μοῦσα,5,–⏑,auto,1"ἄνδρα μοι..."Od.,1,1,5,πολύτροπον,πολύτροπος,6.5,⏑–⏑⏑,auto,1"ἄνδρα μοι..."Od.,1,1,6,ὃς,ὅς,9,–,auto,1"ἄνδρα μοι..."Od.,1,1,7,μάλα,μάλα,10,⏑⏑,auto,1"ἄνδρα μοι..."Od.,1,1,8,πολλὰ,πολύς,11,––,auto,1"ἄνδρα μοι..."
Expectancy is a function of lemma andsedesjointly: it measures, for each lemma, how that lemma is distributed over the possiblesedes, in the context of the overall corpus. Having run tei2csv on the _Odyssey_ , we run it again on the other works of the corpus to obtain the necessary context, in the form of a collection of CSV files that give a lemma and asedesfor every word. The expectancy program takes all these files as input, analyzes the statistical distribution ofsedesfor each lemma, and outputs another CSV file that maps lemma–sedespairs to their expectancy scores, using mathematical formulas we will define below. An excerpt of the output of the expectancy program is shown below. The x column counts the number of occurrences of a lemma–sedespair throughout the corpus, and z shows the expectancy of that pair. From this sample output, we see that the expectancy of the lemmaἀνήρ(man) atsedes 1 is +1.11, that ofἐγώ(I) atsedes 2 is −0.13, and so on.
lemmasedesxz[...]ἀνήρ1452+1.1089031679816ἀνήρ235−1.60788923391802ἀνήρ2.5100−1.18440840388571[...]ἐγώ2430−0.132108322471802ἐγώ, , ,2.51027+1.79559085302027ἐγώ3457−0.0449259477008033[...]ἐνέπω38−1.32295427519852[...]
Finally, the tei2html program takes as input the TEI file of the _Odyssey_ along with the expectancy CSV file. tei2html renders a human-readable HTML representation of the text, optionally highlighting each word according to its expectancy. One visualization style is shown below, with words shaded according to their expectancy: low expectancy is dark and high expectancy is light. Other styles will be explored in the section on visualization.

ἄνδραμοιἔννεπε,μοῦσα,πολύτροπον,ὃςμάλαπολλὰ

The programs that constitute SEDES are written in Python 3. Running SEDES from start to finish on every work in our corpus (12 TEI files, 73,000 lines, and 490,000 words) on a 2019 MacBook Pro takes about one minute. About 45% of the time is spent on segmentation, lemmatization, and scansion; 9% on expectancy computation; and 46% on generating visualization output.




## Segmentation into Lines and Words

Scansion is an operation on individual lines, and lemmatization is an operation on individual words. SEDES begins by breaking a TEI document into lines, and its lines into words.

Segmentation into lines is fairly straightforward. Lines are delimited by either the l element, which encloses lines; or the lb element, which separates them:[^9] 

#  _Iliad_ 1.351–56<a class="footnote-ref" href="#tlgbetacode"> [tlgbetacode] </a><a class="footnote-ref" href="#perseusiliad"> [perseusiliad] </a>
 
```xml
<l>mh=ter e)pei/ m' e)/teke/s ge minunqa/dio/n per e)o/nta,</l> <l>timh/n pe/r moi o)/fellen *)olu/mpios e)gguali/cai</l> <l>*zeu\s u(yibreme/ths: nu=n d' ou)de/ me tutqo\n e)/tisen:</l> <l n="355">h)= ga/r m' *)atrei/+dhs eu)ru\ krei/wn *)agame/mnwn</l> <l>h)ti/mhsen: e(lw\n ga\r e)/xei ge/ras au)to\s a)pou/ras.</l>
```
 
#  _Theogony_ 979–83<a class="footnote-ref" href="#perseustheogony"> [perseustheogony] </a>
 
```xml
<lb/><milestone ed="P" unit="para" />kou/rh d' *)wkeanou=, *xrusa/ori karteroqu/mw| <lb rend="displayNum" n="980" />mixqei=s' e)n filo/thti poluxru/sou *)afrodi/ths, <lb />*kalliro/h te/ke pai=da brotw=n ka/rtiston a(pa/ntwn, <lb />*ghruone/a, to\n ktei=ne bi/h *(hraklhei/h <lb />bow=n e(/nek' ei)lipo/dwn a)mfirru/tw| ei)n *)eruqei/h|.
```
 
Having isolated a line, we decode its text contents from Beta Code to Unicode. We extract words from the line by splitting on sequences of non-letter, non-diacritic characters. For this purpose, the apostrophe character (’), used to mark elision in words likeἀλλ’, is considered to be a letter character. Some TEI documents use apostrophes to mark quotations, which complicates word extraction by giving the character a second meaning as punctuation. When we discovered uses like this, we amended it in the source document using quotation markup.




## Lemmatization

SEDES needs a way of defining which words count asthe samefor the purpose of computing distributions oversedes. Our instrument for deciding which words are considered equivalent is the lemma.[^10] In lexicography, a lemma is the dictionary headword with which all its morphological variants are associated. Ancient Greek is a highly inflected language, one in which words take on many forms according to their grammatical function. The lemma unifies the many related forms of a word and bundles them under one label. For example, the genitive singular wordἀοιδῆςand the dative pluralἀοιδαῖςboth have the same lemma,ἀοιδή(song); the two words therefore fall into the same bucket for the purpose of computing statistics. (Note, however, that lemma assignment does not affect the scansion procedure that will be described in the next section; scansion uses the words of the original text, pre-lemmatization.) As a semantic matter, lemma corresponds to lexeme, an item of meaning removed from a language’s inflectional rules; we may think of a lemma as a representative of a lexeme, standing for a group of related words.[^11] 

Mapping a word to its lemma is not trivial<a class="footnote-ref" href="#heslin2019"> [heslin2019] </a>. But strictly speaking, we do not care about a word’s lemma per se. All we care about is when two words have the same lemma. In mathematical terms, equality of lemmata is an equivalence relation that partitions the universe of words into equivalence classes: all words that have the same lemma are in the same class, and no two words in the same class have different lemmata.[^12] As long as a lemmatization algorithm is consistent, it may as well output abstract tokens likex1234as literal Greek words.[^13] This is to say that the consequence of a word being lemmatized incorrectly is that the word ends up in a different class than it should: it is missing from itstrueclass and is instead grouped with some other class of words (or a class by itself). Whether such an error makes a meaningful difference in the statistics depends on how many times the word occurs, and the sizes of the other lemma classes. In SEDES, we use the backoff Greek lemmatizer[^14] of the Classical Language Toolkit<a class="footnote-ref" href="#cltk"> [cltk] </a>. The backoff lemmatizer employs a chain of sub-lemmatizers (which are various forms of dictionary lookup and regular expression transformations<a class="footnote-ref" href="#burns2018"> [burns2018] </a>,<a class="footnote-ref" href="#burns2020"> [burns2020] </a>), trying each in turn until one returns a result. If no lemma is found by any of these techniques, the last-resort fallback is to use the word itself as the lemma. The fallback occurs for about 2% of words in the corpus (7% of unique words). A random sample of 100 lines suggests a 98.6% accuracy rate: we identified 10 misattributed lemmata among the 721 words in _Iliad_  13.563–662.

We augment the CLTK lemmatizer with a preprocessing step that attempts variations on accent marks: if the initial lemmatization fails, the lemmatizer applies one of a small set of accent transformations, namely, changing a grave accent to an acute accent, or removing an acute accent.[^15] The pre-transformation step makes a few thousand words lemmatizable that would not be otherwise. We further have the lemmatizer first consult a hardcoded list of our own, manually determined lemmata, which we use this list for words that are common in our corpus but for which automatic lemmatization fails.




## Scansion

The computation of expectancy requires a word’s lemma andsedes. In the previous step we found the lemma; now we tackle thesedes.Sedesis a byproduct of scansion, which, in the context of Greek hexameter, means determining the metrical value (long or short) of every syllable in a line.[^16] Once a scansion is settled, thesedesof a word is determined by the metrical values of the words preceding it in the line. For automatic scansion, we use the Python hexameter module<a class="footnote-ref" href="#ranker2012"> [ranker2012] </a>. Here we will briefly describe how the algorithm works.

The first step is to isolate syllables by looking for vowels and diphthongs. Each lexical syllable is assigned a preliminary metrical value according to language rules that are specific to Greek. An example of these rules is that, unless modified by other rules, the vowelsεandοare short,ηandωare long, and other vowels are (for now) undetermined. At this point in the analysis, a syllable may be classified as definitely long, definitely short, or one of a few other values that govern how the syllable may be resolved into long or short in the next step.

Resolution of preliminary metrical values into final metrical values is accomplished using a finite automaton. A finite automaton is a computational state machine that represents (or recognizes) a restricted set of inputs — in our case, the set of properly formed lines of Greek hexameter. The automaton matches lines of hexameter the same way that a regular expression matches a subset of strings. The automaton encodes various rules of the poetic form: for example, that a line contains six feet total; that the first half of a foot must be a long syllable; and that the second half of every foot but the last may be either one long syllable or two short syllables. Each transition in the automaton is marked with both the preliminary metrical values that permit the transition to be taken, and the final metrical value the syllable is to be assigned, when that transition is taken. In general, there is more than one way of fitting a line into the schema of hexameter. For example, one might change a short syllable to a long early in the line, making compensating adjustments to following syllables in order to maintain the same total length. This fact is reflected in the automaton by there being multiple paths from start to finish when there are multiple feasible scansions. Not all scansions are equally good, however. The automaton’s output is biased towards parsimony by weights attached to state transitions, which penalize metrical value assignments that require uncommon metrical rules. The associated final metrical values of the path with lowest weight becomes the scansion of the line.

Occasionally, the automatic scansion algorithm yields either no paths through the automaton, or two or more paths of equal weight. We scanned these problematic lines by hand and added them to a list of scansion overrides, which take precedence over automatic scansions. There are 1,526 entries in the list of overrides, about 2.1% of the lines in the corpus. Manually scanning lines whose automatic scansion is undefined or ambiguous requires human expertise in the form of meter being analyzed. The CSV output of tei2csv records the source of the scansion in the scanned column — either manual or auto. The num_scansions column counts the number of equally weighted automatic scansions found, usually 1.

Once every syllable in a line has been assigned its metrical value, it is straightforward to determine thesedesof each word. Start at the beginning of the line andsedes 1. Advance thesedesby 1 for a long syllable, and by 0.5 for a short syllable. Thesedesof a word is thesedesof its first syllable. Thesedesof words in a line are not all necessarily distinct. For example, in _Iliad_ 1.241<a class="footnote-ref" href="#perseusiliad"> [perseusiliad] </a>,σύμπαντας· τότε δ’ οὔ τι δυνήσεαι ἀχνύμενός περ, the two adjacent wordsδ’andοὔsharesedes 5, because they are pronounced as one word.

To evaluate the accuracy of the automatic scansion algorithm, we randomly sampled 1,200 lines from the entire corpus and manually checked their automatic scansion. 1,195 lines (99.6%) were scanned correctly.




## Expectancy Computation

We now come to the central question: how expected is each word, given its lemma and thesedesat which it appears? Following<a class="footnote-ref" href="#porter1951"> [porter1951] </a>, we call the measure of expectednessexpectancy.Expectancy is not a property of lemma only or ofsedesonly, but of both considered jointly. For each lemma–sedespair, we ask: given the distribution of this lemma in the corpus, is thissedesusual or unusual?

Our metric of expectancy is thez‑score, which measures distance from the mean of a distribution in units of the standard deviation<a class="footnote-ref" href="#hoover2013"> [hoover2013] </a>,<a class="footnote-ref" href="#allen1988"> [allen1988] </a>. The formula for thez‑score of an observed valuexis z = (x - μ)/σ whereμis the mean of a population andσis its standard deviation. A z‑score of +1.5, for example, describes a value that is 1.5 standard deviations greater than the mean. Values greater than the mean have positive scores, and values less than the mean have negative scores. We count how many times a certain lemma appears at a certainsedes, and thez‑score expresses whether that count is greater or less than would be expected, given the counts at that and othersedes.

In our definition of expectancy, different lemmata do not interact.[^17] The expectancy of a lemma at a particularsedesdepends only on the distribution of that lemma. For example, in our corpus, the lemmaβοῦς(cow) appears 448 times, whileχέλυς(tortoise) appears only 8 times. It is moreexpected,then, in some sense, for any given word to beβοῦςthan to beχέλυς. But we are not interested in comparingβοῦςversusχέλυς; rather we weighβοῦςagainst other instances of βοῦς, and χέλυς against other instances of χέλυς.

To establish corpus-wide distributions of lemmata andsedes, we repeat the three previous steps — segmentation, lemmatization, and scansion — for every work in the corpus, using the tei2csv program to create a collection of work-specific CSV files with a lemma andsedesfor every word. Then a separate program, called expectancy, takes as input the whole collection, computes the expectancy of every unique lemma–sedespair across the entire corpus, and writes a table of computed expectancy values to another CSV file. This table will be used in the next step to produce a visualization for a single work.

The expectancy program begins by counting the number of occurrences of each unique lemma–sedespair. Then, for each lemma, it examines the lemma’s distribution over the possiblesedes. Before applying thez‑score formula to the table ofsedescounts, we weight each count by itself. For instance, the weighted mean of the distribution of counts [1, 2, 2, 15] is not (1 + 2 + 2 + 15) / 4 = 5, but rather (1×1 + 2×2 + 2×2 + 15×15) / (1 + 2 + 2 + 15) = 11.7. This is because the counts represent 20 total words, not 4; since the majority of words appear at asedeshaving a count of 15, a representative count should be closer to 15 than it is to 1 or 2. We similarly weight the standard deviation calculation. To be precise, we use the following formulas for the weighted mean and standard deviation of a vector ofsedesfrequency counts [c _1_ , …, c _n_ ]:

$$\begin{align*} \mu &= \frac{\sum_{i=1}^n c_i \times c_i}{\sum_{i=1}^n c_i} \\ \sigma &= \sqrt{\frac{\sum_{i=1}^n c_i \times (c_i - \mu)^2}{\sum_{i=1}^n c_i}}. \end{align*}$$

The output of the expectancy program is a CSV file that maps lemma–sedespairs to their respectivez‑scores.

Thez‑score formula is not defined for distributions whose standard deviation is zero. Such a situation arises when the frequency counts for a lemma are exactly equal in everysedeswhere it appears. Examples areἑκηβόλος(far-shooter), which occurs 42 times but always insedes 6.5, andΚίλλα(the astyonymKilla), which occurs 4 times total, twice each insedes 1 and 11). Important special cases of this general phenomenon are words that appear only once or twice in the corpus, such as the _hapax legomenon_ ἑλώρια( _Iliad_  1.4, lemmaἑλώριον). Expectancy is also undefined for lemmata that never appear in the corpus — those whose table of frequency counts is everywhere zero. This last situation may occur only when when the work under consideration is not part of the corpus that defines expectancy: if it had been, all its lemmata would necessarily have a nonzero count in at least onesedes. For the purposes of visualization, we treat undefinedz‑scores as if they were zero; i.e., neither more nor less frequent than expected. Figure 2 shows the distribution ofz‑scores for every word in the entirety of our corpus.

{{< figure src="images/figure02.png" caption="Histogram ofz‑scores for all words across our entire corpus. This chart excludes about 33,000 words with undefinedz‑scores. Over 95% ofz‑scores lie in the interval [−1.75, +1.75], though the tail of negative values extends as far as −11.5." alt="Histogram ofz-scores."  >}}


Even disregarding lemmata, it is not the case that allsedesare equally likely to be the site of the start of a word. A simple demonstration of this fact is that every line of hexameter contains a word atsedes 1 (the first word), but whether there is a word atsedes 2 depends on the how long the first word is. Figure 3 shows the distribution oversedesfor the works in our corpus. One might reasonably suggest applying a correction to the expectancy formulas to adjust for an assumeda prioridistribution oversedes. We have chosen not to do so, reasoning that a word’s appearing at an uncommonsedesis itself a sign of unexpectedness.

{{< figure src="images/figure03.png" caption="Distribution ofsedescross the full corpus. Not allsedesare equally likely." alt="Bar chart of sedes frequencies."  >}}


Further exploration and justification of the utility ofz‑scores as a measure of expectancy appears below in the section “Interpretation of z ‑scores.” We now show how expectancy scores feed into the final step of the pipeline, namely visualizing numeric expectancy data.




## Visualization

The data files emitted by the previous steps lend themselves to various forms of analysis. Our specific goal is to produce a readable visualization of the source text, with every word highlighted according to its expectancy.[^18] Such a visualization enables a human reader to quickly visually peruse and identify words whose expectancy is much different than expected, aided by the context of the surrounding text. Words thus identified may be worthy of further investigation.

The processing pipeline terminates in the tei2html program, which takes as input a TEI text and the table of lemma–sedesexpectancy scores output by the expectancy program, and produces a visualization that uses HTML, CSS, and JavaScript. Like tei2csv, tei2html isolates words from its TEI input and assigns each one a lemma andsedes. It looks up the expectancy scores of the lemma–sedespairs, and emits an HTML document where every word is annotated with its expectancy and other metadata.

The HTML document provides an interactive selection of visualization styles. A simple and effective way to depict expectancy is to shade the color of words on a scale from dark to light.[^19] In this style, words with higher expectancy fade into the background, and those with lower expectancy are visually emphasized (Figure 4).

{{< figure src="images/figure04.png" caption="Words shaded according toz‑score, dark to light." alt="\"Shade text\" visualization."  >}}


A variation of this style is a diverging color gradient, which, rather than emphasizing the difference between negative and positive, emphasizes distance from the mean. In this style,z‑scores close to zero are visually diminished, while those that are large positive or large negative are highlighted in saturated and contrasting colors. Here, negativez‑scores are red and positivez‑scores are blue (Figure 5).

{{< figure src="images/figure05.png" caption="Words shaded on a diverging scale, red to gray to blue." alt="\"Shade text, diverging\" visualization."  >}}


Words vary in their length and visual density; of two words shaded identically, the longer word may be visually more prominent, simply because up more space. In an attempt to mitigate this potential bias, we have provided alternative styles that attach filled circles of uniform size to words, where the circles are shaded rather than the text (Figure 6). Here, as well, the gradient may be sequential or diverging.

{{< figure src="images/figure06.png" caption="Shaded circles of uniform size are an alternative to text shading." alt="\"Shade bubbles, diverging\" visualization."  >}}


The visualization has analign tosedesgridoption that vertically aligns words according to theirsedes(Figure 7).[^20] This option may be combined with any visualization style.

{{< figure src="images/figure07.png" caption="Align tosedesgridforces words in the samesedesinto vertical alignment." alt="Text aligned to sedes grid."  >}}


The HTML output provides a panel for selecting visualization options and displaying additional information (Figure 8). Clicking on a word shows its metrical shape, lemma,sedes, and expectancy, as well as the distribution of the lemma oversedesand the resultingz‑scores.

{{< figure src="images/figure08.png" caption="The interactive panel that controls visualization and shows information about selected words, here showing thesedesandz‑score distribution of the lemmaζεύς, found in _Iliad_  1.5." alt="Interface showing data provided for a single word"  >}}





## Interpretation ofz‑scores

The essential aspect we hope to capture with SEDES is how expected, in some human sense, a lemma is at a particular metrical position. There are many possible ways to quantify expectancy (e.g., frequency charts à la<a class="footnote-ref" href="#oneill1942"> [oneill1942] </a>); the one we have chosen is thez‑score. Thez‑score is an adaptive measure that does not assume a specific prior distribution of counts oversedes. Because thez‑score is normalized to the standard deviation of a distribution, it provides a common basis of comparison for all lemmata, whether frequent or rare. Let us take two examples to explore the meaning of thez‑score and how it is affected by the underlyingsedesdistribution. The two lemmata we will look at both occur over 50 times, but with markedly different distributions.

First, consider the lemmaμορφή(shape; beauty). It overwhelmingly appears atsedes 11, and only rarely occurs at four othersedes.Sedes 11 is assigned az‑score of +0.33, whose nearness to zero indicates that it is expected, or unmarked, at thissedes.[^21] In contrast, the rarely occurringsedesare assigned large negativez‑scores, less than −3.00, which indicate a low degree of expectancy.
Sedesdistribution and expectancy ofμορφή.Sedesxz‑score18−3.0122−3.1545−3.0861−3.1811150+0.33
Next, consider the lemmaδένδρεον(tree). Its distribution is less skewed. It occurs with roughly equal frequency atsedes 3, 7, and 9; still more often atsedes 1, but not overwhelmingly so. This lemma is more likely to appear atsedes 1 than at any other singlesedes— butsedes 1 accounts for fewer than half of total instances. In this distribution, a count of 11 is closer totypicalthan a count of 19. The evenly distributedsedesaccordingly get negativez‑scores that are relatively close to zero. Thesedeswith a larger count gets a positivez‑score, farther from zero.
Sedesdistribution and expectancy ofδένδρεον.Sedesxz‑score119+1.30310−1.02712−0.51911−0.76
The extremez‑scores — those that are most negative and most positive — naturally stand out as being worthy of attention. The most negative scores are the rare outliers, thesedesat which a lemma appears much less frequently than usual. The first example above illustrates such a situation. A large negative score is a hint (though not a guarantee) that something unexpected is happening compositionally: perhaps a common word is used in an uncommon way, or as part of an uncommon poetic structure. In the other direction, the most positivez‑scores show where a lemma appears _more_ frequently than usual. Note an apparent contradiction: in order for a lemma to be more than expected at a certainsedes, it must appear there a large number of times — does that not make the lemma actually expected at thatsedes? But there is no contradiction, really: large positivez‑scores arise only with counts that are larger than the mean, but which are outweighed by the sum of smaller counts at othersedes. The second example above is such a case. In contrast to the rare outliers signified by large negativez‑scores, large positivez‑scores represent occurrences that occur frequently yet are still unusual in the larger context of the lemma. The diverging color scale visualization options bring out both phenomena.

It is important not to confusez‑scores with pure frequency counts. A lowz‑score does not mean that a lemma itself is uncommon. Just the opposite: it means that _a particular sedes_ is an uncommon one for the given lemma. Intuitively, a lemma’s appearance at onesedescan only count as unusual if there are sufficiently many instances of the lemma at othersedesto establish whatusualis. Large negativez‑scores are only possible with frequently occurring lemmata. To reach az‑score as low as −2, there must be at least 5 total instances of a lemma; for −5 there must be at least 26; and for −10 there must be at least 101. (Compare to the empirical distribution ofz‑scores in Figure 2.)

It may happen that the demands of poetic form affect word placement and therefore the distribution ofsedes. For instance, some lines in a poem may be more or less formulaic than others, and therefore be more or less constrained in their composition. Suppose that in a special subset of lines (invocations, say), a certain lemma falls at asedesat which it does not commonly appear in other, non-invocation lines. The relatively low frequency of the lemma at its place in an invocation is, then, partially a reflection of the relative rarity of invocation lines. In the subset of lines that are invocations, the lemma may in fact be perfectly expected at asedesthat is unusual in the wider context of the poem. It is possible to imagine specializations ofsedesexpectancy that take into account additional factors, such as the functional or literary purpose of the lines in which words appear. Doing so, however, requires presupposing criteria by which a work is to be subdivided. Our present purpose is different: to usesedesas a tool to _discover_ where the placement of words has been affected, whether by formula or by any other cause.




## SEDES in Action: Formula and Intertext

We have engineered SEDES to be useful for diverse types of analysis and, by making the code available as free software, to be adaptable to the interests of future researchers of metrical position in Greek hexameter, by itself or in tandem with other digital humanities tools. Most readily, it is designed to compute and visualize the frequency of lemmata. Users can explore the corpus with the visualization (either online or by downloading the program), look for dark shading among the sea of gray, and click for statistics on the lemma. Or, after downloading the program, they can create the CSV file of underlying data and organize it in a spreadsheet according to their own interests, for example by ordering rows by lemma andz‑scores. Once the user finds a word in an unexpected position, they then can interpret its literary significance (see, e.g.,<a class="footnote-ref" href="#sansom2021"> [sansom2021] </a>). As a sample of its functionality in relation to established ways of interpreting Greek hexameter, in what follows we briefly gesture towards the integration ofsedesanalysis with two prominent interpretative modes: formularity and intertextuality.

SEDES adds granular, novel information to our understanding of formulaic regularity. In oral-poetic theory and Homeric philology, the formula serves as one of the most basic and useful units of composition, though the quality and nature of the formula in epic diction is highly contested.[^22] As defined by<a class="footnote-ref" href="#parry1930"> [parry1930] </a>, a formula is “a group of words which is regularly employed under the same metrical conditions to express a given essential idea” (<a class="footnote-ref" href="#parry1971"> [parry1971] </a>; cf.<a class="footnote-ref" href="#parry1928"> [parry1928] </a> “une expression qui est régulièrement employée, dans les mêmes conditions métriques, pour exprimer une certaine idée essentielle” ). Despite its focus on single and not groups of words, SEDES helps to identify unexpected behavior in constituent words of the group, behavior that should inform our conception of formulaic regularity. Take the phraseπατρίδα γαῖαν,(to one’s) fatherland.Using a collated lemma search in the<a class="footnote-ref" href="#tlg"> [tlg] </a>or a phrase search in the<a class="footnote-ref" href="#chicagohomer"> [chicagohomer] </a>, we find that the phraseπατρίδα γαῖανoccurs 21 times in the _Iliad_ , with 19 instances positioned at line end (after thebucolic diaeresisatsedes 9–12).[^23] Iliad 15.499 is typical:

> οἴχωνταισὺννηυσὶφίληνἐςπατρίδαγαῖαν
> ( _Iliad_ 15.499,πατρίςz= +0.51 atsedes 9, 19 instances at line end)

There is variance in the preceding elements: most often the phrase is introduced with the prepositionφίλην ἐς(to the beloved (fatherland)), though three instances at line end lack precedingφίλην ἐς( _Iliad_  7.335, 13.645, and 15.706). Although the phraseπατρίδα γαῖανis highly regular and predictable in other respects, two exceptional instances in the _Iliad_ shift its metrical position away from line end:

> ἐμβαδὸνἵξεσθαιἣνπατρίδαγαῖανἕκαστος
> ( _Iliad_ 15.505,πατρίςz= −1.81 atsedes 7, Ajax to Achaians)

> σὴνἐςπατρίδαγαῖαν,ἐπείμεπρῶτονἔασας
> ( _Iliad_ 24.557,πατρίςz= −2.37 atsedes 3, Priam to Achilles)

In the two exceptions, by collating the paired lemmata search or phrase search with the SEDES visualization, we see that there is also a change in the expectancy of the phrase’s constituent parts,πατρίςand γαῖα.Sedes 9 is a natural place for the lemmaπατρίς, whether or not part of a formula. While γαῖα remains relatively expected in each position, insedes 3 and 7πατρίςis placed unexpectedly (Figure 9).

{{< figure src="images/figure09.png" caption="Table of lemma πατρίς (οf one’s fathers) bysedesin the Archaic subset of the corpus, with expectancy. The total number of instances of the lemma is Σx= 133." alt="Table showingx,x/Σx, andzvalues"  >}}


When comparing the instances of the phrase at _Iliad_ 15.505 and 24.557 with the 19 others at line end, there is a difference in formularity. If you were to ask which instances of the formulaπατρίδα γαῖανare mostformulaic,it seems reasonable to claim that the 19 instances of the phrase at line end are moreformulaicthan the two that occur elsewhere, due to their regularity in that position of the line. This in itself suggests that not all instances of even a single formula are equally expected in a given metrical position. But we could have seen this shift of phrase even without SEDES, using, for example, the repeated phrase tool of the Chicago Homer or a proximity search for the two lemmata in the _Thesaurus Linguae Graecae_ . What SEDES allows us to see for the first time is that the placement of the phrase atsedes 3 and 7 not only deviates from normal metrical placement for the _phrase_ , it places the _word_ πατρίς, in particular, in a less expected place. In other words, while the phrase isformulaicin all instances, it is less so in _Iliad_  15.505 and 24.557, where it is out of place and where its constituent words, especiallyπατρίς, stray from their typical positions.

This new information about the differing metrical behavior of constituents of formulae has at least three effects. First, it nuances the notion of theflexibilityof formulaic language<a class="footnote-ref" href="#hainsworth1968"> [hainsworth1968] </a>. SEDES shows that words within a phrase may behave in different ways _qua_ words, even if they remain contiguous within the phrase and the phrase is not otherwiseexpandedorcontracted.Future work on epic formularity can adapt and incorporate SEDES to fit different models of concepts central to the idea of the formula. If scholars of epic language who are committed to the empirical investigation of formularity are to define the quality and nature of this fundamental component of epic composition, thesedesexpectancy of constituent elements of formulae — individual words — should factor into notions associated with formularity, such as typicality, regularity, expectation, economy, and flexibility.

Second, unexpected constituents of a formula may interact with other literary features of a text. Scholars have shown how the meaning of individual elements of formulae, such as an epithet, can become more or less salient at different moments in the text<a class="footnote-ref" href="#elmer2015"> [elmer2015] </a>,<a class="footnote-ref" href="#visser1988"> [visser1988] </a>,<a class="footnote-ref" href="#bakker1991"> [bakker1991] </a>. _Sedes_ expectancy may also do something similar when one or more elements of a formula occurs in an unexpected position. Of the two instances above, the more statistically marked instance ofπατρίδαis at _Iliad_  24.557, in which it occurs at asedes(3) that is more than two standard deviations away from the mean (z= −2.37). In the context of book 24, the unexpected placement ofπατρίς(of one’s father[land]) concords with the book’s emphatically paternal semantics, several of which align with thesedesofπατρίδα. The final book of the _Iliad_ features a clandestine visit by Priam, the king of Troy, to Achilles’ tent through divine aid. Priam appears suddenly at Achilles’ camp and kisses Achilles’ hands (24.477–9), astounding Achilles and his companions (θάμβος…θάμβησεν…θάμβησανIliad 24.482–4), and utters his first words of petition:remember your father(μνῆσαι πατρὸς σοῖο _Iliad_ 24.486). As<a class="footnote-ref" href="#edwards1991"> [edwards1991] </a>states, “Priam’s first words are a culmination of (the _Iliad_ ’s) theme (of father–son relationships).” In this sudden, incipient statement,πατρόςoccupiessedes 3, a less expected position for the lemmaπατήρ(z= −1.24) and the same unexpectedsedesasπατρίδα (γαῖα)later. It is notable that of the twenty instances of words with the rootπατρ-in _Iliad_  24, only thisπατρὸς, the errantπατρίδα (γαῖαν)of 24.557, and one final instance (24.592) occur insedes 3. The last time that Achilles addresses Patroklos, whose name etymologizes asglory ( _kleos_ ) of the father ( _patr-_ ),the name of his dead companion occurs insedes 3 (μή μοι Πάτροκλε σκυδμαινέμεν, Iliad 24.592) for the only time in the vocative case — a case particularly marked for Patroklos, as the narrator famously speaks it in apostrophe eight times<a class="footnote-ref" href="#allenhornblower2020"> [allenhornblower2020] </a>. Moreover, as a phrasal search in<a class="footnote-ref" href="#chicagohomer"> [chicagohomer] </a>shows, the lines immediately surrounding the shiftedπατρίδα γαῖαare suffused with paternal referentiality, including an interformulaic reference to the fatherly petitions of Chrysês in book 1 (δέξαι ἄποινα _Iliad_  24.555 ≈δέχθαι ἄποινα1.23) and the often parental formula,ζώειν καὶ ὁρᾶν φάος ἠελίοιο, spoken by Thetis about Achilles twice (18.61, 442; cf. 24.562) and by the Trojan leader Anchises after pleading for hisflourishing progeny(θαλερὸν γόνον) in the _Homeric Hymn to Aphrodite_ (104–5).[^24] Sedesexpectancy draws our attention to potential cross-effects of the unexpectedly placedπατρίς, related words in the samesedes, and paternal thematics in the passage.

Third, the fact that otherwiseformulaicphrases, lines, or passages may contain words that are unexpectedly placed can reveal craft where before the reader may have assumed strict regularity. We see this especially at work in passages that are repeated verbatim in two or more places. Take, for example, Ajax’s speech to the Achaians in _Iliad_  15.560–64, three lines of which are repeated from book 5 (15.562–64 = 5.530–32). We may visualizesedesexpectancy and repeated phrases together using SEDES and notation from the<a class="footnote-ref" href="#chicagohomer"> [chicagohomer] </a>( _Iliad_  15.560–64):

> Ἀργείουςδ’ὄτρυνε[1[2[3μέγας[4Τελαμώνιος3]Αἴας·2]4]
> [5[6[7ὦ1][8[9φίλοι7]ἀνέρες9]ἔστε,8]καὶ6]αἰδῶθέσθ’ἐνὶθυμῷ,5][10ἀλλήλουςτ’αἰδεῖσθε[11κατὰ[12κρατερὰςὑσμίνας.11]12]αἰδομένωνδ’ἀνδρῶνπλέονεςσόοιἠὲπέφανται·φευγόντωνδ’οὔτ’ἂρκλέοςὄρνυταιοὔτέτιςἀλκή10].

> Great Telamonian Ajax roused the Argives:Oh friends, be men, and put shame in your heart, and consider one another throughout the fierce struggles. When men are considerate more of them end up safe but when they flee there is neither glory nor any warcraft.

It is immediately apparent that within the passage’s formulae there is variation in the expectancy of individual words. Some phrases contain words that are especially expected in their givensedes, such as the pronoun and epithets (phrases 1–4) on line 560. We see greater disparity beginning on line 561, where, although they occur elsewhere in repeated phrases, words such asἀνέρες(men) andαἰδῶ(shame) are less expected. Perhaps what is most interesting is that the lines (passage 10) repeated verbatim from book 5 contain several unexpected placements of words atsedes 4 (αἰδεῖσθε, ἀνδρῶν,andοὔτ᾽). Here,sedesexpectancy joins other remarkable stylistic features, such as the pragmatic focus on the participlesαἰδομένωνandφευγόντωνwhich begin both their lines and sentences opposed rhetorically in antithesis (fighting vs. fleeing). Rhetoric affects word order which, with SEDES, we can now see shifts words from their more typical positions and can result instackingof unexpectedly placed words along particularsedes. SEDES also reveals that formulaic analysis with frequency data is insufficient in articulating the regular or erratic composition of constituent features of this otherwise repetitious material of epic diction, as is especially apparent in longer passages repeated verbatim.

There are likely more ways thatsedesexpectancy can alter our understanding of epic formularity, the identification and study of which will occupy future research with SEDES. For example, it is clear from the brief look atsedesexpectancy and formulae above, in particular the regularity ofπατρίδα γαῖαat line end, that formulae too havesedesexpectations of their own. Adaptation of SEDES code and methodology could assist in articulating these expectations quantitatively, a function that could then better identify moments when even formulae subvert expectation.

SEDES allows scholars to better locate and qualify intertextual relationships between different passages based on thesedesexpectation of lemmata. While the utility ofsedesexpectancy to intertextuality is argued more extensively in<a class="footnote-ref" href="#sansom2021"> [sansom2021] </a>, below is a synopsis of the significance ofsedesexpectancy to words that appear in the same or differentsedesin two texts (Figure 10).

{{< figure src="images/figure10.png" caption="Matrix ofsedesintertextuality by expectancy." alt="Matrix with expectancy ofsedesof one word between the same or different texts."  >}}


Passages that feature the same lemma in the samesedeshave different interpretations given the expectancy of the lemma. If a word is expected in a particular position, such asπατρίδαinsedes 9 (z = +0.51 in the Archaic corpus, cf. above), its appearance there in two or more passages should not in and of itself suggest intentional reference or allusion. Rather, it is likely to be the result of typical compositional practice for hexameter poetry, what<a class="footnote-ref" href="#conte1986"> [conte1986] </a>callsmodello-codice(generic model). But if a word occurs in the same unexpectedsedesin both passages, it is more likely to be a direct reference, what<a class="footnote-ref" href="#conte1986"> [conte1986] </a>callsmodello-esemplare(individual model). An example of this can be found in the highly unexpected placement of the lemmaσελήνη(moon), which occurs only twice atsedes 6.5 (x = 2, Σx = 157,z = −8.80 in the whole corpus): in the Shield of Achilles passage in both _Iliad_  18.484 and Quintus of Smyrna’s _Fall of Troy_  5.8. SEDES provides readers of Greek hexameter the quantitative information necessary for better distinguishing between generic and individual types of intertextuality when regarding the shared metrical position of words.

In the past, scholars would often disregard the possibility of an intertextual relationship if a word occured in differentsedes.Sedesexpectancy, however, provides a way to identify new intertexts even in cases when there is a difference insedes. When a word occurs in differentsedesthat are both relatively unexpected, in both instances the unexpectedsedesreflects a break in the pattern of expectancy and thus merits further attention. For example, the name of the goddessἈφροδίτηoccurs atsedes 6 in _Iliad_  9.389 (οὐδ’ εἰ χρυσείῃ Ἀφροδίτῃ κάλλος ἐρίζοι) and atsedes 2 in _Od_ . 20.73 (εὖτ’ Ἀφροδίτη δῖα προσέστιχε μακρὸν Ὄλυμπον), both of which havez‑scores of −10.0 in the whole corpus, which are among the lowest of any lemma–sedespair; the other 99% of the timeἈφροδίτηoccurs exclusively atsedes 10 (x = 200, Σx = 202,z = +0.10).[^25] Despite their differentsedes, both instances thwart expectations. This fact should cause the researcher to investigate the two further, at which point other collective features emerge: shared language such as theworks of Athena(ἔργα δ᾽ Ἀθηναίη) in adjacent lines ( _Iliad_  9.390, _Od_ . 20.72) or their presence in character speech by notoriously versatile speakers, Achilles and Penelope; cf. <a class="footnote-ref" href="#martin1989"> [martin1989] </a>. Conversely, in cases in which the expectancy of the word is high in bothsedes, or mixed high and low, there is perhaps less reason to suppose intertextuality bysedesis a helpful mode of interpretation. Such statistical data combining word and meter could inform future quantitative intertextuality such as that of<a class="footnote-ref" href="#tesserae"> [tesserae] </a>and as described in<a class="footnote-ref" href="#forstall2019"> [forstall2019] </a>. By focusing interpretive efforts on statistically marked instances of words, SEDES gives readers of hexameter an additional tool with which to investigate repetitive phenomena in Greek epic such as formulae and intertexts.




## Conclusion

SEDES reached its current state through a long process of evolution and iterative development. It originated as a tool to investigate sonic patterns in poetry, by identifying lines with similar tonal patterns, counting lettern-grams, and quantifying alliteration. It later became specialized for the purpose of finding the metrical positions of all occurrences of forms of a lemma, which enabled analysis of the kind we have described in this article, albeit of only one lemma at a time. At that point, we were using texts sourced from the Thesaurus Linguae Graecae<a class="footnote-ref" href="#tlg"> [tlg] </a>and Diogenes<a class="footnote-ref" href="#diogenes"> [diogenes] </a>as a tool for lemma lookup. A concrete vision began to take shape of what we wanted to accomplish with SEDES: to compute metrical positions and other statistical information about every word in a large corpus, in an automated fashion. The difficulty of automating Diogenes lookups, and a general preference for freely available data sources, caused us to switch our source of texts from the Thesaurus Linguae Graecae to Perseus, and to begin developing programs around the direct processing of source TEI files. Automating all the steps of the processing pipeline made it feasible to start producing visualizations of an entire work at a time.

The decision to switch to Perseus texts was an important one, enabling us to take control over the entire processing pipeline. Moreover, open-access texts facilitate reproducibility of statistical results, and lower the barriers to participation by people who are not specialists in classical studies. Regardless of the source of texts, a project of this nature requires paying substantial attention to textual and data-format issues.

SEDES was developed in the context of a set of texts we wished to analyze and does not automatically generalize to other Greek hexameter texts. Analyzing texts outside the set we have considered will likely require manual tweaking of the processing programs, as well as adding to the tables of manual lemmatizations and scansions for words and lines that resist automatic processing. When we expanded the corpus from six to twelve texts, to incorporate Hellenistic and Imperial Greek works, we had to make adjustments to the TEI parser to account for previously unseen markup variations.[^26] A beneficial side effect of this work has been the discovery and correction of various errors in the source texts.

SEDES provides groundwork for future corpus-level analysis of Greek hexametrical poetry, including by combining textual features (lemma,sedes, and metrical shape) in different ways and by expanding to additional features. More generally, it provides a framework for the analysis of metrical position in metrical language, by which the researcher assembles a corpus, analytical pipeline, and visualization of basic statistics for further development of the program, model, concept, and interpretation and appreciation of the text. Due to the limited size of the Greek hexameter corpus, the method results more from the slow work of philology using basic statistics than from the capacious abilities of machine learning. In some respects, this methodology reflects the disciplinary background of the authors. Yet the benefits of such an interest in poetic language within a limited corpus have focused our attention on a particular approach to lemmatized word frequencies correlated with metrical position. This attention to metrical position, a long-standing interest in classical philology, demonstrates a new route for future studies that seek strong correlations between linguistic phenomena and other formal features of Greek poetry.




## Availability

SEDES source code and documentation are available at[https://github.com/sasansom/sedes](https://github.com/sasansom/sedes). The project home page, with sample visualization outputs, is[https://sasansom.github.io/sedes/](https://sasansom.github.io/sedes/).




## Acknowledgments

We express gratitude to Patrick Burns, author of CLTK’s Greek lemmatization; Kyle P. Johnson of CLTK; Hope Ranker, author of the hexameter scansion module; Lisa Cerrato of the Perseus project; David Mimno; Rachel Greenstadt; Annie Lamar; Simeon Ehrlich; Stanford’s Center for Spatial and Textual Analysis (CESTA); and the _Digital Humanities Quarterly_ reviewers.


[^1]: <a class="footnote-ref" href="#vanophuijsen1987"> [vanophuijsen1987] </a>: “in Hephaestion ( χώραι ) are places for feet;”  “it seems most correct to say that a metron as it is actually found, a specimen, contains feet, while a metron as a species contains a definite number of places for feet…” (17). For Hephaestion’s _ oeuvre _ , see Suda η 659<a class="footnote-ref" href="#heath2001"> [heath2001] </a>,<a class="footnote-ref" href="#westphal1866"> [westphal1866] </a>.
[^2]: For competing notations, see<a class="footnote-ref" href="#janse2003"> [janse2003] </a>, cf.<a class="footnote-ref" href="#bozzone2014"> [bozzone2014] </a>.
[^3]:  _ Caesura _ ( “cutting” ), as in a pause or word break in a verse, withτομήas the Greek equivalent (cf. _LSJ_ s.v.τομήIV.2).
[^4]: For localization of word-types in iambic trimeter, see<a class="footnote-ref" href="#dik1998"> [dik1998] </a>and<a class="footnote-ref" href="#schein1979"> [schein1979] </a>.
[^5]: Cf.<a class="footnote-ref" href="#sansom2021"> [sansom2021] </a>.
[^6]: Other digital analyses of metrical Greek language focus more exclusively on natural language processing, such as the Classical Language Tool Kit<a class="footnote-ref" href="#cltk"> [cltk] </a>; or grammatico-semantic corpus linguistics, such as The Ancient Greek and Latin Dependency Treebank<a class="footnote-ref" href="#agdt"> [agdt] </a>, the Homeric Dependency Lexicon<a class="footnote-ref" href="#hodel"> [hodel] </a>(cf.<a class="footnote-ref" href="#zanchi2021"> [zanchi2021] </a>), and Ancient Greek WordNet<a class="footnote-ref" href="#agwn"> [agwn] </a>.
[^7]: For additional theorization and application of SEDES to close reading and intertextuality, see<a class="footnote-ref" href="#sansom2021"> [sansom2021] </a>.
[^8]: The Perseus project is undergoing a transition to[Perseus version 5.0](https://scaife.perseus.org/about/), in which, among other changes, TEI texts contain Unicode, rather than Beta Code. At this point, SEDES sources texts from[Perseus 4.0](https://www.perseus.tufts.edu/hopper/)(Perseus Hopper), which require a preliminary step to decode Beta Code.
[^9]: [TEI element l (verse line)](https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-l.html),[TEI element lb (line beginning)](https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-lb.html).
[^10]: For recent work on lemmata in digital philology, see<a class="footnote-ref" href="#forstall2015"> [forstall2015] </a>,<a class="footnote-ref" href="#heslin2019"> [heslin2019] </a>,<a class="footnote-ref" href="#passarotti2020"> [passarotti2020] </a>.
[^11]: Although particular inflections of a lemma may vary in metrical shape and thus only be able to occupy particularsedes(cf.<a class="footnote-ref" href="#oneill1942"> [oneill1942] </a>), we primarily seek to identify potential patterns of expectancy generated by the repetition of a lemma’s various inflections in thesedesthey happen to occupy. To accomplish this empirical study, we need only quantify the frequency of lemmata andsedesat which they do, in fact, occur; cf.<a class="footnote-ref" href="#sansom2021"> [sansom2021] </a>.
[^12]: The idea of grouping words according to a definable equivalence relation immediately suggests generalizations of SEDES beyond lemmata. Other definitions of equivalence could be coarser (more words per class) or finer (fewer words per class). Our focus on lemma in this article is due to lemma being a ready means of uniting the many inflected forms of words in Ancient Greek, as well as its being a relatable concept in itself.
[^13]: That is, for the purpose of statistics. For the purpose of interpretation, it is nice to have the actual lemma at hand.
[^14]: [Source code for cltk.lemmatize.grc](https://legacy.cltk.org/en/latest/greek.html#lemmatization-backoff-method).
[^15]: [#29 Add a transform-ultima fallback step to the lemmatizer](https://github.com/sasansom/sedes/issues/29).
[^16]: <a class="footnote-ref" href="#schumann2021"> [schumann2021] </a>give a summary of approaches to automatic scansion. For ancient syllabification and scansion, see, for example, Hephaestion _Encheiridion_ (On Meter) 1.1–10<a class="footnote-ref" href="#westphal1866"> [westphal1866] </a>,<a class="footnote-ref" href="#vanophuijsen1987"> [vanophuijsen1987] </a>.
[^17]: Just as a lemma aggregates the various inflections of a word and allows for analysis of their metrical distribution, future work could aggregate words into coarser or finer classes. For example, one potentially useful coarser classification is word root. The separate lemmataἀοιδή/ᾠδή(song),ἀοιδός/ᾠδός(singer), andἀείδω/ἀοιδιάω(to sing) all share the same root related to the possibly Indo-European _*h2ueid_ (sing,cf.<a class="footnote-ref" href="#beekes2010"> [beekes2010] </a>); this root may also generate patterns of expectation based on metrical position that could be assessed bysedesanalysis.
[^18]: For theory of visualization, see<a class="footnote-ref" href="#braun2018"> [braun2018] </a>; for other attempts by philologists to visualize repetition in Greek hexameter, see<a class="footnote-ref" href="#martin1989"> [martin1989] </a>,<a class="footnote-ref" href="#chicagohomer"> [chicagohomer] </a>, and<a class="footnote-ref" href="#pavese2003"> [pavese2003] </a>.
[^19]: The steepness of the shading gradient around zero is a configurable parameter. We have tuned the default value to provide good discrimination in the interval [−2, +2], where mostz‑scores are (Figure 2).
[^20]: The alignment of inflected words to the beginning of their first syllable reflects their membership in lemmata with less regard to the quantity of its morphological ending and, as a result, better represents the program’s quantification of lemmata and interest in their patterns of expectancy.
[^21]: For markedness in this sense, cf.<a class="footnote-ref" href="#schein2015"> [schein2015] </a>.
[^22]: For a helpful review of predominant definitions of formula in context of oral poetics and quantitative intertextuality, see<a class="footnote-ref" href="#forstall2019"> [forstall2019] </a>. For the (structural) formula and metrical position, see<a class="footnote-ref" href="#russo1963"> [russo1963] </a>, with the response by<a class="footnote-ref" href="#packard1976"> [packard1976] </a>, and for attention to metrical position and formulapassim,<a class="footnote-ref" href="#tate2010"> [tate2010] </a>.
[^23]:  _Iliad_ 2.140, 158, 174, 454, 4.180, 5.687, 7.335, 460, 9.27, 47, 414, 11.14, 13.645, 15.499, 505 (sedes 7–10), 706, 16.832, 18.101, 23.145, 23.150, 24.557 (sedes 3–6); note also the variants,in the fatherland(ἐν πατρίδι γαίῃ) at _Iliad_ 3.244, 8.359, and 22.404, andfrom one’s fatherland(γαίης ἄπο πατρίδος) at _Iliad_ 13.696 and 15.335.
[^24]: For the idea of interformularity, see<a class="footnote-ref" href="#bakker2013"> [bakker2013] </a>.
[^25]: This information was discovered by using SEDES to create a CSV file of the metrical and frequency statistics of words in the Archaic Greek epic corpus, and then organizing the spreadsheet byz‑score (lowest to highest).
[^26]: [#9: Update TEI parser to handle Hellenistic and Imperial texts](https://github.com/sasansom/sedes/issues/9).## Bibliography

<ul>
<li id="agdt">Celano, Giuseppe G. A., Crane, Gregory, and Almas, Bridget. (2006–2021) “The Ancient Greek and Latin Dependency Treebank” . Available at:<a href="https://perseusdl.github.io/treebank_data/">https://perseusdl.github.io/treebank_data/</a>
</li>
<li id="agwn">Short, William Michael, Forte, Alexander, Tauber, James, Luraghi, Silvia, and Zanchi, Chiara. “Ancient Greek WordNet” . Available at:<a href="https://greekwordnet.chs.harvard.edu">https://greekwordnet.chs.harvard.edu</a>
</li>
<li id="allen1988">Allen, Robert F. (1988) “The Stylo-Statistical Method of Literary Analysis” , _Computers and the Humanities_ 22, pp. 1–10.
</li>
<li id="allenhornblower2020">Allen-Hornblower, Emily. (2020) “Revisiting the Apostrophes to Patroclus in _Iliad_ 16” . _Donum natalicium_ . Available at:<a href="https://chs.harvard.edu/allen-hornblower-revisiting-the-apostrophes-to-patroclus-in-iliad-16/">https://chs.harvard.edu/allen-hornblower-revisiting-the-apostrophes-to-patroclus-in-iliad-16/</a>
</li>
<li id="bakker2013">Bakker, Egbert. (2013) _The Meaning of Meat and the Structure of the Odyssey_ . Cambridge: Cambridge University Press.
</li>
<li id="bakker1991">Bakker, Egbert and Fabbricotti, F. (1991)Peripheral and Nuclear Semantics in Homeric Diction: The Case of Dative Expression forSpear, _Mnemosyne_ 44, pp. 63–84.
</li>
<li id="barnes1986">Barnes, Harry R. (1986) “The colometric structure of Homeric hexameter” , _Greek, Roman and Byzantine Studies_ 27, pp. 125–150.
</li>
<li id="beekes1972">Beekes, R. S. P. (1972)On the Structure of the Greek Hexameter. _Glotta_ 50, pp. 1–10.
</li>
<li id="beekes2010">Beekes, R. S. P. (2010) _Etymological Dictionary of Greek. Volume One_ . Leiden: Brill.
</li>
<li id="bozzone2014">Bozzone, C. (2014) _Constructions: A New Approach to Formularity, Discourse, and Syntax in Homer_ , Diss. University of California in Los Angeles.
</li>
<li id="braun2018">Braun, Steven. (2018) “Critically engaging with data visualization through an information literacy framework” , _Digital Humanities Quarterly_ 12(4). Available at:<a href="http://www.digitalhumanities.org/dhq/vol/12/4/000402/000402.html">http://www.digitalhumanities.org/dhq/vol/12/4/000402/000402.html</a>
</li>
<li id="burns2018">Burns, Patrick J. (2018) _Backoff Lemmatization as a Philological Method_ , In _Digital Humanities_ . Available at:<a href="https://dh2018.adho.org/en/backoff-lemmatization-as-a-philological-method/">https://dh2018.adho.org/en/backoff-lemmatization-as-a-philological-method/</a>
</li>
<li id="burns2020">Burns, Patrick J. (2020) “Ensemble lemmatization with the Classical Language Toolkit” , _SSL_ 58(1), pp. 157–76. Available at:<a href="https://www.studiesaggilinguistici.it/ssl/article/view/273">https://www.studiesaggilinguistici.it/ssl/article/view/273</a>
</li>
<li id="chicagohomer">Chicago Homer, Eds. Ahuvia Kahane and Martin Mueller. Available at:<a href="http://homer.library.northwestern.edu">http://homer.library.northwestern.edu</a>
</li>
<li id="cltk">Johnson, Kyle P.; Burns, Patrick, Stewart, John, Cook, Todd, Besnier, Clément, and Mattingly, William J. B. (2014–2021) “CLTK: The Classical Language Toolkit” . Available at:<a href="https://github.com/cltk/cltk">https://github.com/cltk/cltk</a>
</li>
<li id="conte1986">Conte, Gian Biagio. (1986) _The Rhetoric of Imitation: Genre and Poetic Memory in Virgil and Other Latin Poets_ , Ithaca: Cornell University Press.
</li>
<li id="dik1998">Dik, Helma. (1998) “Words into Verse: The Localization of Some Metrical Word-Types in the Iambic Trimeter of Sophocles” , _Illinois Classical Studies_ 23, pp. 47–84.
</li>
<li id="diogenes">Heslin, Peter. _Diogenes Desktop_ . Available at:<a href="https://d.iogen.es/d/">https://d.iogen.es/d/</a>
</li>
<li id="edwards1991">Edwards, Mark W. (1991) _The Iliad: A Commentary. Volume V: books 17–20_ , Cambridge: Cambridge University Press.
</li>
<li id="elmer2015">Elmer, David. (2015) “The Narrow Road and the Ethics of Language Use in the _Iliad_ and the _Odyssey_ ” , _Ramus_ 44, pp. 155–83.
</li>
<li id="forstall2012">Forstall, Christopher and Scheirer, Walter J. (2012) “Revealing hidden patterns in the meter of Homer’s _Iliad_ ” , In _Proceedings of the Chicago Colloquium on Digital Humanities and Computer Science_ .
</li>
<li id="forstall2019">Forstall, Christopher and Scheirer, Walter J. (2019) _Quantitative Intertextuality: Analyzing the Markers of Information Reuse_ . Cham, CH: Springer.
</li>
<li id="forstall2015">Forstall, Christopher, Neil Coffee, Thomas Buck, Katherine Roache, and Sarah Jacobson. (2015) “Modeling the scholars: Detecting intertextuality through enhanced word-level n-gram matching” , _Digital Scholarship in the Humanities_ 30(4), pp. 503–15.
</li>
<li id="frankel1926">Fränkel, Hermann. (1926) “Der Kallimachische und der homerische Hexameter” , _Göttinger Nachrichten_ 2, pp. 197–229.
</li>
<li id="giangrande1959">Giangrande, Giuseppe. (1959) _Conjectural Emendations_ , _Rheinisches Museum für Philologie_ 102(4), pp. 365–76.
</li>
<li id="giangrande1967">Giangrande, Giuseppe. (1967) “ Arte Allusiva and Alexandrian Epic Poetry” , _Classical Quarterly_ 17, pp. 85–97.
</li>
<li id="hagel1994">Hagel, Stefan. (1994) _Zu den Konstituenten des griechischen Hexameters_ , _Wiener Studien_ 107/108, pp. 77–108.
</li>
<li id="hagel2004">Hagel, Stefan. (2004) _Tables Beyond O’Neill_ , In Spaltenstein, F. and Bianchi, O. eds. _Autour de la Césure_ , Bern: Peter Lang, pp. 135–215.
</li>
<li id="hainsworth1968">Hainsworth, J. B. (1968) _The Flexibility of the Homeric Formula_ , Oxford: Clarendon Press.
</li>
<li id="hodel">Zanchi, Chiara. (2021) _Homeri Dependency Lexicon_ . Available at:<a href="https://hodel.unipv.it/hodel-res/">https://hodel.unipv.it/hodel-res/</a>
</li>
<li id="heath2001">Heath, Malcolm. (2001) “Hephaestion”  _Suda On Line_ , Translation, 2 March 2001. Available at:<a href="http://www.cs.uky.edu/~raphael/sol/sol-entries/eta/659">http://www.cs.uky.edu/~raphael/sol/sol-entries/eta/659</a>(Accessed 27 December 2021).
</li>
<li id="heslin2019">Heslin, Peter. (2019) “Lemmatizing Latin and Quantifying the Achilleid.” In Coffee, Niel, Chris Forstall, Lavinia Galli Milic, and Damien Nelis eds. _Intertextuality in Flavian Epic Poetry_ , Berlin: De Gruyter, pp. 389–408.
</li>
<li id="hoover2013">Hoover, David L. (2013) “Quantitative Analysis and Literary Studies” . In Siemens, R. and Schreibman, S. eds. _A Companion to Digital Literary Studies_ , Oxford: Blackwell.
</li>
<li id="janse2003">Janse, Mark. (2003) “The Metrical Schemes of the Hexameter” . _Mnemosyne_ 56, pp. 343–48.
</li>
<li id="kahane1994">Kahane, Ahuvia. (1994) _The Interpretation of Order: A Study in the Poetics of Homeric Repetition_ , Oxford: Clarendon Press.
</li>
<li id="lsj">Liddell, Henry George, Scott, Robert, Jones, Henry Stuart, and McKenzie, Roderick. (1996) _A Greek-English Lexicon (9th edition)_ , Oxford: Clarendon Press.
</li>
<li id="martin1989">Martin, Richard P. (1989) _The Language of Heroes: Speech and Performance in the Iliad_ , Ithaca: Cornell University Press.
</li>
<li id="martin2000">Martin, Richard P. (2000) “Synchronic aspects of Homeric performance: the evidence of the Hymn to Apollo” , In A. M. González de Tobia, ed. _Una nueva visión de la cultura griega antigua hacia el fin del milenio_ , La Plata, Argentina: Editorial de la Universidad Nacional de La Plata, pp. 403–32.
</li>
<li id="mcdonough1966">McDonough, Jr., J. T. (1966) _The Structural Metrics of the Iliad_ . Diss. Columbia University.
</li>
<li id="mclennan1977">Mclennan, G. R. (1977) _Callimachus: Hymn to Zeus: Introduction and Commentary._ Rome: Ateneo and Bizzari.
</li>
<li id="oneill1942">O’Neill, Jr., Eugene. 1942. “The Localization of Metrical Word-Types in the Greek Hexameter: Homer, Hesiod, Alexandrians” , _Yale Classical Studies_ 8, pp. 102–76.
</li>
<li id="packard1976">Packard, David W. (1976) “Metrical and grammatical patterns in the Greek hexameter” , In Jones, A. and Churchhouse, R. F., eds, _The Computer in Literary and Linguistic Studies. Proceedings of the Third International Symposium_ , Cardiff: University of Wales Press, pp. 85–91.
</li>
<li id="parry1928">Parry, Milman. (1928) _L’Épithète traditionnelle dans Homère; Essai sur un problème de style homérique_ , Paris: Société d’éditions “Les belles lettres” .
</li>
<li id="parry1930">Parry, Milman. (1930) “Studies in the Epic Technique of Oral Verse-Making. I. Homer and Homeric Style” , _Harvard Studies in Classical Philology_ 41, pp. 73–147.
</li>
<li id="parry1971">Parry, Milman. 1971. _The Making of Homeric Verse: The Collected Papers of Milman Parry_ . Ed. Adam Parry. Oxford: Clarendon Press.
</li>
<li id="pavese2003">Pavese, Carlo Odo and Boschetti, Federico. (2003) _A Complete Formulaic Analysis of the Homeric Poems_ , Amsterdam: Adolf M. Hakkert.
</li>
<li id="passarotti2020">Passarotti, Marco, Mambrini, Francesco, Franzini, Greta, and Massimiliano Cecchini, Flavio. (2020) “Interlinking through lemmas. The lexical collection of the LiLa Knowledge, Base of linguistic resources for Latin” , _Studi e Saggi Linguistici_ 68, pp. 177–212.
</li>
<li id="perseus">Perseus Digital Library Project, Available at:<a href="https://www.perseus.tufts.edu/hopper/">https://www.perseus.tufts.edu/hopper/</a>
</li>
<li id="perseusiliad">Homer. (1920) _Homeri Opera in five volumes_ . Oxford: Oxford University Press. Perseus Digital Library, Available at:<a href="https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0133">https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0133</a>(Accessed 14 April 2021).
</li>
<li id="perseusodyssey">Homer. (1920) _Homeri Opera in five volumes_ . Oxford: Oxford University Press. Perseus Digital Library, Available at:<a href="https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0135">https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0135</a>(Accessed 14 April 2021).
</li>
<li id="perseustheogony">Hesiod. (1914) _The Homeric Hymns and Homerica with English Translation, trans. H. G. Evelyn-White. Theogony_ . Cambridge, MA: Harvard University Press. Available at:<a href="https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0129">https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0129</a>(Accessed 14 April 2021).
</li>
<li id="philologic">Dik, Helma. (2008–2021) “Perseus Project Texts Loaded under PhiloLogic” . Available at:<a href="https://perseus.uchicago.edu">https://perseus.uchicago.edu</a>
</li>
<li id="porter1951">Porter, Howard N. (1951) “The Early Greek Hexameter” . _Yale Classical Studies_ 12, pp. 3–63.
</li>
<li id="ranker2012">Ranker, Hope. (2012) “Libraries and command-line tools for metrical analysis of epic Greek hexameter” , Available at:<a href="https://github.com/epilanthanomai/hexameter">https://github.com/epilanthanomai/hexameter</a>
</li>
<li id="russo1963">Russo, Joseph. (1963) “A Closer Look at Homeric Formulas” , _TAPA_ 94, pp. 235–47.
</li>
<li id="sansom2021">Sansom, Stephen A. (2021) “ _Sedes_ as Style in Greek Hexameter: A Computational Approach” , _TAPA_ 151(2), pp. 439–67.
</li>
<li id="schein1979">Schein, Seth. (1979) _The Iambic Trimeter in Aeschylus and Sophocles: A Study in Metrical Form_ . Leiden: Brill.
</li>
<li id="schein2015">Schein, Seth. (2015) _Homeric Epic and its Reception: Interpretative Essays_ . Oxford: Oxford University Press.
</li>
<li id="schumann2021">Schumann, Anne-Kathrin, Beierle, Christoph, and Blößner, Norbert. (2021) “Using Finite-State Machines to Automatically Scan Classical Greek Hexameter” , Available at:<a href="https://arxiv.org/abs/2101.11437">https://arxiv.org/abs/2101.11437</a>
</li>
<li id="tate2010">Tate, Aaron Phillip. (2010) _Modularity and the Spectrum of Formularity in the Homeric Corpus_ . Diss. Cornell University.
</li>
<li id="tei">Text Encoding Initiative. _P5 Guidelines_ 4.2.1. Available at:<a href="https://tei-c.org/Guidelines/P5/">https://tei-c.org/Guidelines/P5/</a>
</li>
<li id="tesserae">Tesserae, Available at:<a href="https://tesserae.caset.buffalo.edu">https://tesserae.caset.buffalo.edu</a>
</li>
<li id="tlg">Thesaurus Linguae Graecae, Available at:<a href="https://stephanus.tlg.uci.edu/">https://stephanus.tlg.uci.edu/</a>
</li>
<li id="tlgbetacode">Thesaurus Linguae Graecae. _The TLG Beta Code Manual_ . Available at:<a href="https://stephanus.tlg.uci.edu/encoding/BCM.pdf">https://stephanus.tlg.uci.edu/encoding/BCM.pdf</a>
</li>
<li id="vanophuijsen1987">van Ophuijsen, J. M. (1987) _Hephaestion on Metre. A Translation and Commentary_ , Leiden: Brill.
</li>
<li id="visser1988">Visser, E. (1988) “Formulae or Single Words? Towards a New Theory of Homeric Verse-making” , _Würzburger Jahrbücher für die Altertumswissenschaft_ 14: 21–31.
</li>
<li id="westphal1866">Westphal, R. (1866) _Scriptores Metrici Graeci. Vol. 1. Hephaestionis. De Metris Enchiridion et de Poemata Libellus cum Scholiis et Trichae Epitomis, Adjecta Procli Chrestomathia Grammatica_ , Leipzig: Teubner.
</li>
<li id="white1986">White, Heather. (1986) “Greek Epic Language and Callimachus’ Hymn to Delos” , _L’Antiquité Classique_ 55, pp. 316–22.
</li>
<li id="winnington1963">Winnington-Ingram, R. P. (1963) _Aristidis Quintiliani de musica libri tres_ , Leipzig: Teubner.
</li>
<li id="zanchi2021">Zanchi, Chiara. 2021. “The _Homeric Dependency Lexicon_ : What it is and how to use it” , _Journal of Greek Linguistics_ 21, pp. 263–97.
</li>

</ul>
