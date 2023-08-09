---
type: article
dhqtype: article
title: "Tracking the Consumption Junction: Temporal Dependencies between Articles and Advertisements in Dutch Newspapers"
date: 2020-06-19
article_id: "000445"
volume: 014
issue: 2
authors:
- Melvin Wevers
- Jianbo Gao
- Kirstoffer L. Nielbo
translationType: 
categories:
- history
- interdisciplinarity
- content analysis
- area studies
- data modeling
abstract: |
   Historians have regularly debated whether advertisements can be used as a viable source to study the past. One of their main concerns centered on the question of agency. Were advertisements a reflection of historical events and societal debates, or were ad makers instrumental in shaping society and the ways people interacted with consumer goods? Using techniques from econometrics (Granger causality test) and complexity science (Adaptive Fractal Analysis), this paper analyzes to what extent advertisements shaped or reflected society. We found evidence that indicates a fundamental difference between the dynamic behavior of word use in articles and advertisements published in a century of Dutch newspapers. Articles exhibit persistent trends. Contrary to this, advertisements have a more irregular behavior characterized by short bursts and fast decay, which, in part, mirrors the dynamic through which advertisers introduced terms into public discourse. On the issue of whether advertisements shaped or reflected society, we found particular product types that seemed to be collectively driven by a Granger causality going from advertisements to articles. Generally, we found support for a complex interaction pattern, analogous to Cowan’s concept of the consumption junction. Finally, we discovered noteworthy patterns in terms of Granger causality and long-range dependencies for specific product groups. All in, this study shows how methods from econometrics and complexity science can be applied to humanities data to improve our understanding of complex cultural-historical phenomena such as the role of advertising in society.
teaser: "Shows how methods from econometrics and complexity science may be applied to humanities data to improve understanding of the role of advertising in society"
order: 13
---
  
  

## Introduction
  
  

## Advertisements as a Lens on the Past
  
Over the course of the twentieth century, branded consumer goods turned into an integral part of society [^cross2000]  [^degrazia2005]. Consequently, researchers turned to consumer goods as an object of research. In addition to writing histories of particular consumer goods, researchers have also conceptualized consumer goods as entry points into broader cultural phenomena. Scholars have, for instance, studied how advertisements represented consumerism, gender identities, and the globalization of food cultures (see [Lears, 1994](#lears1994); [Parkin, 2007](#parkin2007); [Sivulka, 2012](#sivulka2012)). In these studies, advertisements functioned as a lens on the past. Roland Marchand argues that advertisements provide an insight into the ideals and aspirations of past realities. He argues that they show the state of technology, the social functions of products, and that they provide information on the society in which a product was sold. Furthermore, Marchand poses that advertisements contributed to the shaping of a  “community of discourse” . He claims that advertisements infused public discourse with a particular type of language [^marchand1985].
  
At the same time, scholars have debated to what extent adverts actually offer a meaningful depiction of the past. In their effort to sell more products, producers, and ad makers amplified or distorted certain social and cultural aspects to make products more appealing to consumers [^brandt2004]. Erving Goffman points out that ads shaped consumer’s lived experience by prescribed certain conceptions of identity [^goffman1985]. Put differently, ad makers used adverts to shape society by tweaking the desires of consumers [^fox1997]. This form of social engineering was rooted in psychological and sociological theories of the day. Especially the tobacco industry was actively involved in developing new ways of advertising that could entice people to turn to smoking cigarettes [^brandt2004].
  
These theoretical debates raise the question whether we can actually use advertisements to study the past, or are we merely studying a version of the past constructed by ad makers? Theories on the relationship between advertisements and society can be summarized by three positions. The first position contends that advertisements reflected the desires and aspirations of consumers. The second argues that advertisements merely represented the interest of advertisers and the companies that produced the commodities. This approach attributes more agency to the advertisers. The third approach proposes the existence of a more complex consumption junction, in which producers, distributors, consumers, and advertisers collectively negotiated the meaning and success of a consumer product [^cowan1987].
  
This article examines the validity of these three positions in a specific historical context (i.e. twentieth-century Netherlands) and sets out to answer to what extent did advertisements reflect or shape society. We studied this interplay between advertisers and society by analyzing advertisements and articles in newspapers. Newspapers are a well-read rich historical source that contains  “conscious representations of conditions and events”  as well as  “unconscious reflection[s] of the tastes, the interests, the desires, and the spirit of its day”   [^smail2008]. As such, newspapers function as a proxy for public discourse [^marshall1995]  [^schudson1982]. Newspapers contained a large number of advertisements. Even though advertisements were a major source of revenue for newspaper publishers, the editors writing the news were generally separated from the people selecting the advertisements [^rooij1974]  [^schreurs2001]. For this reason, we argue that we can view the articles and advertisements in the same source as separate sources of information. The possible relationships between the two are, therefore, more likely to be reflective of relations existing in the  _real_  world rather than reflective of choices made by editors. The availability of digitized newspapers enables researchers to use computation to explore the archive, locate particular instances of language use, or extract specific linguistic patterns [^wevers2017].
  
This study combines techniques from econometrics and complexity science to examine the dynamics of word use in articles and advertisements. Complexity science has been used successfully in the past to model large-scale dynamics of human language, increasing our understanding of social systems and collective dynamics on the macro-scale [^helbing2015]  [^petersen2012]. We set out to answer the following three questions. First, did advertisements shape or reflect newspaper discourse? Second, did word use in ads differ in dynamics from articles? And finally, were these characteristics more pronounced for particular product groups? Answering these questions will further our understanding of the dynamics underpinning a complex cultural-historical phenomenon, such as advertising.
  
  
  

## Beyond Counting Word Frequencies
  
With the proliferation of large databases that hold temporally-dispersed text content, time series plots of word frequencies have become a valuable source of exploration and validation of cultural trends [^gao2012]  [^michel2011]. Google has popularized this approach through their web-based n-gram viewer based on its digitized book collection.[^1]  The popularity of the Google Ngram viewer has sparked other digital archives to also develop n-gram viewers based on their collection.[^2] 
  
N-gram viewers can help researchers to determine when words appeared and how they evolved. Plots of word frequencies, however, only offer an overview of particular trends in discourse. To gain more insight into the trends in and between advertisements and articles, we applied two techniques from econometrics and complexity science to the (relative) frequencies of words. First, we applied the Granger causality test to determine whether trends in word use in ads followed trends in articles or vice versa. Second, we analyzed the persistence of words using fractal analysis to identify whether ads differed from articles in terms of dynamics related to word use. Put differently, we determined whether advertising discourse was distinct in its behavior from discourse in articles. Also, we set out to identify specific words that  _stuck_  with people? This stickiness can be indicative of social dynamics on a macro-scale. Can we detect behavior of words that transcends individual uses and is more reflective of the existence of memory in communication?
  
Memory in a time series is modeled as the presence of self-similarity, or more precisely persistent correlation, between the values of these features at various time steps. Merely glancing at visualizations produced by n-gram viewers might show sudden peaks or slow decays in word use, which might suggest dynamic processes reflective of memory. In this paper, however, we quantify such behavior and show the extent to which word use exhibits particular memory functions exhibited in cultural expressions. Jan Assman has described cultural memory as  “a collective concept for all knowledge that directs behavior and experience in the interactive framework of a society and one that obtains through generations in repeated societal practice and initiation”   [^assman2011]  [^assman1995]  [^donald2002]. One of these repeated societal practices is language use, which also shapes our collective understanding of a shared culture. According to Assman, cultural memory is formed over large periods of time whereas communicative memory represents memories shaped over shorter time spans (80-100 years). In a way, communicative memory can be viewed as the short-term memory of a society [^assman2008]  [^assman1995]. Can we use time series of word frequencies in newspapers to detect communicative memory?
  
  
  
  

## Methods
  
  

## Data
  
The National Library of the Netherlands (KB) has digitized thousands of Dutch historical newspapers using optical character recognition (OCR) software.[^3]  This software turns scans of physical pages into machine-readable data. Unfortunately, the text extracted from the digital scans is often flawed due to imperfections in the original material or limitations of the recognition software. These material blemishes cause the software to not recognize and transcribe every word correctly, which has resulted in conjoined words, complete gibberish, or words in which certain characters were replaced. The age and quality of the original material are important determinants of the software’s ability to correctly recognize the text; hence, older newspapers contain many more errors than more recent papers. For this reason, we focused on twentieth-century newspapers. Also, the KB does not provide suitable metrics on the quality of the OCR’ed text [^traub2015]. The study, therefore, assumes that OCR errors are uniformly distributed over the period.
  
For analysis, we relied on two subsets of the digitized newspaper data. The first subset consisted of the entire set of advertisements (      n      1      =  18,564,411  ) in the KB’s digitized newspaper archive. The second set held newspaper articles (      n      2      =  11,465,220  ) from two national newspapers:  _De Tijd_  (1890-1974) and  _De Telegraaf_  1893-1989. During digitization, the OCR software separated articles from advertisements and stored the document type in the metadata, allowing us to select these two types of documents. Because advertisements made up a smaller portion of the newspapers, we selected the entire set of advertisements to make it more comparable to the corpus of articles in terms of size. Also, we narrowed our focus to two national newspapers because these are more likely to represent wider public discourse than regional newspapers.
  
We calculated keyword frequencies, more specifically, normalized relative daily term frequency per document for these two subsets. We explicitly looked at 265 words (singular and plural forms collapsed) that denoted consumer products. Based on exploratory data analysis using an n-gram viewer, we selected words that appeared in both advertisements and articles throughout greater periods of time with considerable frequency. Brand names were excluded for two reasons. First, brand names often appeared as part of logos in advertisements, making it more difficult to convert these images to machine-readable text. Second, the techniques used in this paper necessitate the existence of the same words over longer periods of time. More often than not, there existed multiple brand names for the same products, which were also not used over longer periods of time.
  
  
  

## Causal Dependencies
  
Several techniques can be used to compare lagged values of time series   X   with values of a second time series   Y   to model variation in their correlation coefficient as a function of temporal displacement. The most widely used technique is cross-correlation, which is simply used to detect the variation in the correlation between two time series as a function of lag. The Granger causality test goes beyond mere correlation and tests for the existence of causal-like dependencies between temporally disjunctive time series of, for instance, words from two sources [^granger1969]. The test, which originated in econometrics, is based on the assumption that causality is more than temporal disjunction, it involves directionality between time series. The relation tested by the Granger causality test is often characterized as predictive causality and represented as   X       G  r  a  n  g  e  r       c  a  u  s  e       Y   to distinguish it from more direct causality [^sugihara2012]. At its core, Granger causality, which is related to correlation, expresses if values of time series   X   contain information that is uniquely predictive of subsequent values in time series   Y  .
  
For our study, we used the Granger causality test as follows. To identify a  _shaping_  relation, we test if variation in a specific word frequency for newspaper discourse (  Y  ) at time   t   is predicted by variation in the frequency for the same word in advertisement discourse (  X  ) at earlier time steps   t  -  1  …  t  -  k  . We test for   X       G  r  a  n  g  e  r       c  a  u  s  e       Y  , by comparing the performance of the ‘newspaper discourse only’ model:
  
      y      t      =      β      0      +      β      1          y      t  -  1      +  …  +      β      k          y      t  -  k      +  ϵ  
  
with the full  _newspaper and advertisement discourses_  model:
  
      y      t      =      β      0      +      β      1          y      t  -  1      +  …  +      β      k          y      t  -  k      +      α      1          x      t  -  1      +  …  +      α      m          x      t  -  m      +  ϵ  
  
to identify which one does the better job at explaining word frequency (      y      t      ) based on the residuals. The zero-model for the hypothesis is       H      0      :      α      i      =  0   for each   i   of the element   [  1  ,  m  ]   with the alternative hypothesis being       H      1      :      α      i      ≠  0   for at least one   i   of the element   [  1  ,  m  ]  . We applied the test bi-directionally such that a shaping relation finds support if we can confirm that ‘  X       G  r  a  n  g  e  r       c  a  u  s  e       Y  ’, and in the case of a reflecting relationship we can reject ‘  Y       G  r  a  n  g  e  r       c  a  u  s  e       X  ’. Finally, if both ‘  X       G  r  a  n  g  e  r       c  a  u  s  e       Y  ’ and ‘  Y       G  r  a  n  g  e  r       c  a  u  s  e       X  ’ find support, we viewed this as indicative of a more complex relationship between the two time series.
  
  
  

## Long-range Dependencies
  
In addition to the Granger Causality test, we used fractal analysis to identify if words exhibited long-range dependencies.[^4]  Fractal Analysis is a method to assess the complexity of data. In our case, we look at long-range dependencies, which indicate a rate of decay between two points with increasing time intervals that is slower than exponential decay. Analysis of time-dependent change in complex systems — systems composed of many interacting elements — is an important application of Fractal Analysis.
  
Some random processes in complex systems are self-affine, that is, fluctuation patterns at shorter time scales are (statistically) similar to fluctuations at longer time scales. In the case of reading, for instance, fluctuations in reading speed are self-affine across multiple time scales, because both reading fluency and comprehension are affected by elements at short time scales (e.g., words and sentences) and longer times scales (e.g., paragraphs and chapters) [^obrien2014]. Such fractal behavior is also found in a range of processes related to psychology [^chater1999], economy [^marchant2008], sociology [^gao2017], health [^eke2002], language [^gao2012] and music [^voss1975]. We argue, therefore, that fractal analysis has great potential for the study historical trends in cultural expressions [^nielbo2019]. This is particularly the case when we are dealing with big data, consisting of large sets of mostly unknown parameters [^gao2012].
  
We are interested in a particular kind of fractal processes called   1  /      f      2  H  +  1       processes, in which   H   refers to the Hurst exponent. The Hurst exponent quantifies the degree of long-range dependencies in a time series (Figure [1](#figure01)), such that when   0  <  H  <  0.5  , the time series is an anti-persistent process (i.e., a jump up is followed by a jump down, or vice versa, in the incremental process). When   H  =  0.5  , the time series only has short-range dependencies, and when   0.5  <  H  <  1  , the time series is characterized by long-range dependencies (i.e. a jump up is followed by another jump up, or vice versa, in the incremental process). It is possible the   H  >  1   indicates a non-stationary process. In this study, persistence represents whether a word ‘stuck’ with people and it is in that manner analogous to how scholars have viewed communicative memory.
  
{{< figure src="resources/images/figure01.png" caption="Figure 1: Left: Time series that exhibit anti-persistent (top), short-range (middle), and long-range (bottom) dependencies. Anti-persistent time series oscillate rapidly around its average, which is sometimes referred to as mean-reverting or rigid behavior. Short-range dependencies are indicated by the short cycles, while long-range dependencies show repetitive cycles at multiple time scales. Right: Estimation of the Hurst exponent as the slope of the residual fit `F(w)` on the time window `w` for the matching time series in the left column. Anti-persistent time series have a slope <0.5, the slope for short-range dependencies is 0.5, and long-range dependencies >0.5." alt="Left: Time series that exhibit anti-persistent (top), short-range (middle), and long-range (bottom) dependencies. Anti-persistent time series oscillate rapidly around its average, which is sometimes referred to as mean-reverting or rigid behavior. Short-range dependencies are indicated by the short cycles, while long-range dependencies show repetitive cycles at multiple time scales. Right: Estimation of the Hurst exponent as the slope of the residual fit F(w) on the time window w for the matching time series in the left column. Anti-persistent time series have a slope < 0.5, the slope for short-range dependencies is 0.5, and long-range dependencies >0.5."  >}}

  
  

## Adaptive Fractal Analysis
  
Adaptive Fractal Analysis (AFA) is a relatively new technique for determining the Hurst exponent of a time series [^gao2011]  [^riley2012]. AFA improves the popular detrended fluctuation analysis [^peng1994] by identifying a global smoothed trend that can automatically deal with arbitrary, strong nonlinear trends (Gao et al., 2011). The technique is based on a nonlinear adaptive multi-scale decomposition algorithm [^gao2011].
  
After constructing a random walk process from the time series, the initial step of AFA involves partitioning the time series into overlapping segments of length   w  =  2  n  +  1  , in which neighboring segments overlap by   n  +  1   points. In each segment, the time series is fitted with the best polynomial of order   M  , obtained using standard least-squares regression. The fitted polynomials in overlapped regions are then combined to yield a single global smoothed trend. Denoting the fitted polynomials for the   i  -  t  h   and   (  i  +  1  )  -  t  h   segments by       y      i      (      l      1      )   and       y      (  i  +  1  )      (      l      2      )  , respectively, where       l      1      ,      l      2      =  1  ,  ⋯  ,  2  n  +  1  , we define the fitting for the overlapped region as
  
      y      (  c  )      (  l  )  =      w      1          y      (  i  )      (  l  +  n  )  +      w      2          y      (  i  +  1  )      (  l  )  ,            l  =  1,2  ,  ⋯  ,  n  +  1  ,   where       w      1      =  (  1  -      l  -  1      n      )   and       w      2      =      l  -  1      n       can be written as   (  1  -      d      j      /  n  )   for   j  =  1,2  , and where       d      j       denotes the distances between the point and the centers of       y      (  i  )       and       y      (  i  +  1  )      , respectively. Note that the weights decrease linearly with the distance between the point and the center of the segment. Such a weighting is used to ensure symmetry and to effectively eliminate any jumps or discontinuities around the boundaries of neighboring segments. As a result, the global trend is smooth at the non-boundary points and it has the right and left derivatives at the boundary [^riley2012].
  
The global trend can be used to maximally suppress the effect of complex nonlinear trends on the scaling analysis. The parameters of each local fit are determined by maximizing the goodness of fit in each segment. The different polynomials in the overlapped part of each segment are combined such that the global fit will be the smoothest fit of the overall time series. Even if the local fits are linear,   M  =  1  , the global trend signal will still be nonlinear. AFA then can be described accordingly: for an arbitrary window size   w  , we determine, for the random walk process   u  (  i  )  , a global trend   v  (  i  )  ,  i  =  1,2  ,  ⋯  ,  N  , where   N   is the length of the walk. The residual of the fit,   u  (  i  )  -  v  (  i  )  , characterizes fluctuations around the global trend, and its variance yields the Hurst exponent   H   according to the following scaling equation:
  
  F  (  w  )  =  [      1      N        ∑    i  =  1      N        (    u  (  i  )  -  v  (  i  )      )      2          ]      1  /  2      ∼      w      H      .  
  
By computing the global fits, the residual, and the variance between original random walk process and the fitted trend for each window size   w  , we can plot       log      2      F  (  w  )   as a function of       log      2      w  . The presence of fractal scaling amounts to a linear relation in the plot, with the slope of the relation providing an estimate of   H   (see Figure [1](#figure01)).
  
  
  
  

## Design
  
To determine whether advertisements reflected or shaped public discourse, we first applied Granger causality tests to each of the 265 keywords, comparing time series from newspaper and advertisement discourse. We hypothesize the existence of the following three Granger causal-like patterns:
  
  Advertisements shaped newspaper articles as expressed by Granger causality directed exclusively from advertisements to articles;  Advertisements reflected newspaper articles as expressed by Granger causality directed exclusively from articles to advertisements;  A complex, possibly externally-driven, causal pattern as evidenced by cases where Granger causality goes from articles to advertisements  _and_  vice versa.  

  
For the second step of the analysis, we used AFA to model the persistence for each keyword in both types of discourse. This enabled us to identify possible dynamic properties of either advertisements and articles as a whole, and possibly the dynamic properties of particular words. Similar to Granger causal-like patterns, the Hurst exponent has three possible patterns of persistence: anti-persistent processes, short-term correlation processes, and persistent processes. Each keyword’s behavior can thus be described by one of nine possible combinations of causality (Granger causality test) and persistence (AFA). Insights into these dynamic properties alongside the causal patterns can help to increase our understanding of the relationship between advertisements and articles, and by extension, between advertisements and society.
  
  
  

## Data Analysis
  
Statistical tests were conducted with an   α   level of .005 [^benjamin2017]. Pearson’s correlation coefficient   R   was used to measure the non-lagged association strength between the time series. We converted Pearson’s   R   using Fisher’s Z-transformation to normally distributed z-values to permit averaging. Before applying the Granger causality test for comparison of discourses, lag-1 differencing was used to obtain a stationary keyword time series.
  
For the analysis of the Hurst exponent for each keyword time series per discourse, we used a simple linear regression and compared this with the constant model. This allowed us to test differences in long-range dependencies between the two different discourses. The Shapiro-Wilk   W   test confirmed that the distribution of the Hurst exponent did not deviate significantly from normality [^shapiro1965].[^5] 
  
  
  
  

## Results
  
  

## Directionality
  
On average, the variance in correlation for each keyword in all the time series was similar between advertisement and articles. The mean correlation coefficient,       R    ¯    , between advertisements and the articles in the newspapers  _De Tijd_  and  _De Telegraaf_  was       R    ¯    =  .  25   and       R    ¯    =  .  27   respectively. Sixty-two percent (62%) of these correlations were statistically reliable. The within-newspaper correlation, that is, the correlation between  _De Tijd_  and  _De Telegraaf_ , was considerably stronger,       R    ¯    =  .  42  . Seventy-three percent (73%) of these correlations were significant, suggesting that word use over time in articles between these two newspapers was more similar than between the articles and advertisements.
  
{{< figure src="resources/images/figure02.png" caption="Figure 2: Six keyword frequencies plotted at bi-annual intervals for the two newspapers (News 1: _De Tijd_ ; News 2: _De Telegraaf_ ) and the advertisements (Ads). The line is smoothed using a simple moving average filter (window size of five years) and gray bands represent confidence intervals at 95%. Notice how ‘Cinema’ shows a distinct shaping Granger causal pattern, where fluctuations in Ads antecede fluctuations in News. In contrast ‘Potato’ displays a complex Granger causal pattern, where fluctuations in Ads both seem to antecede and succeed News fluctuations. The ‘Potato’ system’s spiky behavior during the Dutch famine (1944-45) indicates that war is part of the external cause." alt="Six keyword frequencies plotted at bi-annual intervals for the two newspapers (News 1: De Tijd; News 2: De Telegraaf) and the advertisements (Ads). The line is smoothed using a simple moving average filter (window size of five years) and gray bands represent confidence intervals at 95%. Notice how Cinema shows a distinct shaping Granger causal pattern, where fluctuations in Ads antecede fluctuations in News. In contrast Potato displays a complex Granger causal pattern, where fluctuations in Ads both seem to antecede and succeed News fluctuations. The Potato system’s spiky behavior during the Dutch famine (1944-45) indicates that war is part of the external cause."  >}}

  
Analysis showed that there was no overarching causal pattern, but rather multiple Granger causal patterns that were keyword-dependent. Twenty percent (20%) of the product terms show evidence of a shaping causality, in which discursive trends in advertising discourse uniquely predict those in articles. For 17% of the product terms, we found the causal pattern in which advertisements reflect articles. Almost half of the product terms (49%) belong to the complex externally-driven category, that is, fluctuations in both advertisements and articles seem to be predicted by extraneous events that perturb the reflecting-shaping dynamic between the time series. Finally, 14% of the terms show no indication of predictive causality.
  
Almost half of the product terms exhibit complex behavior, pointing towards an external source driving changes in discourse in advertisements and newspapers. These could include economic developments or possibly the invention of new products or technologies. In a way, this underpins that the relationship between advertisements and articles was one of negotiation with external developments. Noteworthy keywords in this category were related to produce (apple, cauliflower,  lettuce), energy (stove, cokes, furnace, gasoline) and audiovisual technology (tape recorder, gramophone, radio, television).
  
There are slightly more keywords for which advertisements were shaping articles than ads reflecting articles. In case of shaping, we detected that behavior in word use in advertisements was related to behavior in articles. Words that exhibited this behavior referred quite generally to fashion and clothing (men’s clothing, sweater, fur, wool, flannel, jeans, heels), interior design (living room, dining room, bedroom) and movies (cinema, film). The keywords that exhibited reflecting behavior were more difficult to categorize into particular categories. They ranged from words such as teapot, dictionary, to cheese. Generally, the words with reflecting behavior seemed to be more specific than the words in the shaping category. For instance, the keywords chair cushions and winter coat are specific types of cushions and coats.
  
  
  

## Detection of Persistence in Word Use
  
The Hurst exponent   H   for both articles (      t      1058      =  32.8  ,  p  <  .  00001  ) and advertisements (      t      538      =  38.5  ,  p  <  .  00001  ) was significantly higher when compared to a no-memory baseline (  H  :   M  =  0.5  ,       S  D  =  0.18  ). In terms of persistence, discourse in articles and advertisements was different from processes that only showed short-range correlations. AFA found an average difference (  Δ  H  ) between articles of 0.21. The dynamics related to word use in articles thus differed from advertisements. Word use in articles was more likely to be a persistent process (  H  :   M  =  0.89  ,       S  D  =  0.19  ) than it was in advertisements (  H  :   M  =  1.1  ,       S  D  =  0.17  ). Notice that advertisements display non-stationary dynamics with   H  >  1  . To test whether the difference between ads and articles was significant, we ran linear regression to predict  _H_  as a function of advertisement and articles (advertisement as baseline). Compared to the constant model, a statistically significant regression model was found (      χ      1      2      =  149.1  ,  p  <  .  00001  ) showing that  _H_  was, indeed, reliably lower for articles than for advertisements (articles:   β   = -0.18 ,   S  E      ±  0.01,       F      1,793      =  163.9      p  <  .  00001  ).
  
On the whole, word use in articles more clearly expressed persistent trends, while word use in advertisements tended to be more irregular, displaying bursts of high activity followed by little or no activity. This indicates that articles more closely express behavior that could be interpreted as communicative memory, while ads seem more haphazard and perhaps catalytic to the existence of memory in wider public discourse, as represented through articles.
  
Our findings indicate three distinct types of persistent trends (see [Table 1](#table01)). Persistence in only articles, persistence in advertisements and articles, and a lack of persistence in either source. Words that only exhibited persistence in articles included products related to interior design (living room, couch, lamp, bedroom). This suggests that discourse about these products was part of a shared language but that it was not clearly part of an advertising discourse. Conversely, words that showed persistence in both discourses included those related to cigarettes but not to cigars and tobacco (cigarettes), fashion (fur, jeans), energy (cokes, furnace, gasoline) and produce (apple, cauliflower, lettuce). This suggests that advertising discourse for these products was much more persistent and relied on an established frame of reference. Interestingly, cigarettes and fashion are often presented as typical examples of strongly branded products [^blaszczyk2008]  [^brandt2004]  [^hill2002]  [^white2012]. Advertisements for produce, on the other hand, might exhibit persistent processes due to its highly seasonal and reoccurring nature ([cf. Gao et al., 2012](#gao2012)). Keywords that showed no persistence were related to technology (cinema, tape recorder, gramophone, radio).
    Table 1: Example of keywords grouped on type of persistent trend (persistence in articles only, persis- tence in articles and advertisements, and no persistence    Persistence in articles  Persistence in ads & articles  No persistence      Living room  Cigarettes  Cinema      Dining room  Fur  Film      Bedroom  Wool  Tape recorder      Chair  Flannel  Gramophone      Couch  Jeans  Radio      Cupboard  Heels  Television      Seat  Apple        Lamp  Cauliflower          Lettuce          Cokes          Furnace          gasoline        
  
  
  

## Discussion
  
Using AFA, we found a significant difference in persistent behavior between word use in advertisements and articles. The latter exhibited long-term dependencies whereas advertisements displayed more non-stationary and irregular behavior. In general, advertisements introduced terms, but many of these terms did not persist and their decay was rapid. For articles, on the other hand, keywords that denoted products showed more persistent behavior and were either mentioned recurrently in a self-reinforcing manner or decayed much slower than advertisements. We speculate that this reflects an overarching media dynamic in which ads introduced keywords and articles represented how these products became part of public discourse. However, this dynamic does not hold for all products as evidenced by Table 1, and, at least partially, by keywords that exhibit a reflecting causal pattern.
  
The time series of keywords between the two newspapers were more clearly correlated than the time series between the newspapers and advertisements. This shows that word use in newspapers more closely followed each other than word use between advertisements and newspapers. Along with the found difference in   H   between articles and advertisements, the dissimilarity in correlation adds evidence to the hypothesis that the dynamics of discourse in ads are different from articles. This demonstrates that advertisements are not merely a lens on the past, but more clearly a distorted mirror that is shaped to a certain degree by advertisers and its own dynamics.
  
In terms of directionality, we did not find one dominant pattern. For 20% percent of the keywords, advertisements reflected articles, and for 17% of the keywords, advertisements shaped articles. But for almost half of the keywords, there was a more complex causal relationship, indicative of external forces. This lends support to Cowan’s argument for a complex interaction pattern in which advertisers, distributors, producers, and consumers negotiated the meaning of a product [^cowan1997].
  
  

## Product Groups
  
The causal direction and type of persistence seems to be, to some extent, related to product type. We were not able to identify specific categories of keywords in the reflecting causal category. However, the complex relationship and shaping category offered interesting groupings of words. The groupings made on the basis of the existence of memory and causal directionality leads to the following four points of discussion.
  
First, products with a shaping dynamic  _and_  long-term dependencies in articles might point towards products that are not constantly advertised — expressed by the lack of persistence in ads — but that nevertheless are part of the cultural life of Dutch consumers throughout the twentieth century, such as bikes, pets, interiors, and clothes. The shaping dynamic reveals that ad makers might have pushed the popularity of these products, which can be described as lifestyle products. One could argue that advertisers might have been able to affect the longevity of these products, effectively installing them within a shared community of discourse.
  
Second, one of the most noteworthy behaviors is associated with the cigarette. This product exhibits persistence in advertisements  _and_  in articles, and it shows a shaping causal behavior. This suggests that in advertising discourse and in newspaper discourse, cigarettes were a recurring topic that built upon earlier discourse. Moreover, advertisers seemed to be able to shape newspaper discourse on cigarettes. This finding is in line with scholars that view advertisements for cigarettes as the prime example of social engineering [^brandt2004]. Our study finds that, at least for the Dutch context, cigarette advertisements were a steadily successful form of advertising. The unique behavior of cigarettes was underlined by the fact that related products such as tobacco and cigars behaved dissimilarly. Tobacco and cigars exhibit no persistence and are driven by a complex causal relationship, underscoring different advertising dynamic than found for cigarettes.
  
Third, some products revealed persistence in both advertisements and articles without displaying a uniform causal relationship. These products include produce, energy sources, and computer systems. One interpretation might be that produce was of prolonged importance, indicated by the existence of long-range dependencies, yet its importance was not driven by advertisers but by an external source. In the case of produce, this external source could be seasonal or economic shifts. The other two product groups (energy sources and computer systems) were also quite instrumental in society, albeit not for prolonged periods during the twentieth century. The keywords associated with energy were most dominant in the first half of the century, whereas, the words associated with computers only appeared in the latter quarter of the century. Nonetheless, they both still exhibited persistence in newspaper articles.
  
Finally, keywords associated with technological innovations showed two distinct types of behavior. First, keywords such as cinema, tape recorder and television did not exhibit any persistence, which could have resulted from the constant innovation and disruptions in the field of audiovisual technology. Another explanation could be the use of different keywords to refer to similar technologies. Further research is needed to explore this behavior related to technology. Second, we found a distinction in the causal relationship between types of technology. Cinema and film showed a clear causal relationship between ads and articles. The causal relationship might have resulted from the fact that advertisements played an important role in pushing these innovations to a wider audience. Keywords associated with household technology (radio and television), on the other hand, displayed the complex type of causality. These technological products might be more closely related to particular economic, seasonal, or innovative cycles. Again, further research is needed to untangle these dynamics.
  
  
  
  

## Conclusion
  
Through two data experiments, we have found evidence of a fundamental difference between the dynamic behavior of word use related to consumer products in articles and advertisements published in newspapers. Articles — taken as a proxy for public discourse — exhibit persistent trends that are likely to be reflective of communicative memory. Contrary to this, advertisements have a more irregular behavior characterized by short bursts and fast decay, which, in part, mirrors the dynamic through which advertisers introduced terms into public discourse. On the issue of whether advertisements shaped or reflected society, we found particular product types that seemed to be collectively driven by a causality going from advertisements to articles. Generally, we found support for a complex interaction pattern that Cowan dubbed the  “consumption junction” . Finally, we discovered noteworthy patterns in terms of causality and long-range dependencies for specific product groups.
  
These findings resonate with Marchand’s claim that advertisements contributed to the  “shaping of a  community of discourse,  an integrative common language shared by an otherwise diverse audience” [^marchand1985]. In other words, ads seem to behave as a driver of processes in newspaper articles. Their behavior clearly differs from general discourse, which might stem from the fact that ads are to a large extent driven by ad makers and particular technological innovations.
  
This study shows how methods from fields of econometrics and complexity science can be applied to improve our understanding of complex cultural-historical phenomena. Further research that employs more extensive keyword lists that also includes brand names and cross-cultural comparisons will make it possible to propose a more detailed and general account of the mechanics that underpin the aforementioned consumption junction.
  
  

## Acknowledgements
  
Part of this research was performed while the authors were visiting the Institute for Pure and Applied Mathematics (IPAM), which is supported by the National Science Foundation. The newspaper data was provided by the National Library of the Netherlands (KB).
  
  
  
[^1]: Google Books Ngram Viewer: [https://books.google.com/ngrams](https://books.google.com/ngrams)
[^2]: Examples of ngram viewers: The British Library: [https://www.webarchive.org.uk/ukwa/ngram/](https://www.webarchive.org.uk/ukwa/ngram/), Danish Royal Library: [http://labs.statsbiblioteket.dk/smurf/](http://labs.statsbiblioteket.dk/smurf/), and National Library of the Netherlands [http://kbkranten.politicalmashup.nl](http://kbkranten.politicalmashup.nl)
[^3]: These newspapers can be accessed through Delpher: [https://www.delpher.nl](https://www.delpher.nl)
[^4]: Long-range dependency is also called persistent behavior or long-memory in time series. The terms will be used interchangeably.
[^5]: While some keyword time series did show indications of multifractal structure (i.e. local fluctuations with either small or large variation), this information was discarded from the final analysis for the purpose of simplification.  
[^assman2008]: Assmann, J. (2008),  “Communicative and Cultural Memory” , in Erll, A., Nünning, A. and Young, S.B. (Eds.),  _Cultural Memory Studies: An International and Interdisciplinary Handbook_ , Walter de Gruyter, New York, pp. 109–119.  
[^assman2011]: Assmann, J. (2011),  _Cultural Memory and Early Civilization: Writing, Remembrance, and Political Imagination_ , Cambridge University Press, New York.  
[^assman1995]: Assmann, J. and Czaplicka, J. (1995),  “Collective Memory and Cultural Identity” ,  _New German Critique_ , No. 65, p. 125.  
[^benjamin2017]: Benjamin, D.J., Berger, J.O., Berk, R., Bollen, K.A., Brembs, B., Brown, L., Camerer, C., et al. (2017),  “Redefine statistical significance” ,  _Nature Human Behaviour_ , available at: [https://doi.org/10.1038/s41562-017-0189-z](https://doi.org/10.1038/s41562-017-0189-z).  
[^blaszczyk2008]: Blaszczyk, R.L. (Ed.). (2008),  _Producing Fashion: Commerce, Culture, and Consumers_ , University of Pennsylvania Press, Philadelphia.  
[^brandt2004]: Brandt, A. (2004),  “Engineering Consumer Confidence in the Twentieth Century” , in Zhou, X. and Gilman, S. (Eds.),  _Smoke: A Global History of Smoking_ , Reaktion Books, London.  
[^chater1999]: Chater, N. and Brown, G.D. (1999),  “Scale-invariance as a unifying psychological principle” ,  _Cognition_ , Vol. 69 No. 3, pp. B17–B24.  
[^cowan1987]: Cowan, R.S. (1987),  “The consumption junction: A proposal for research strategies in the sociology of technology” , in Bijker, W., Hughes, T. and Pinch, T. (Eds.),  _The Social Construction of Technological Systems: New Directions in the Sociology and History of Technology_ , MIT Press, Cambridge, pp. 261–80.  
[^cowan1997]: Cowan, R.S. (1997),  “A Proposal for Research Strategies in the Sociology of Technology” , in Bijker, W.E., Hughes, T. and Pinch, T. (Eds.),  _The Social Construction of Technological Systems: Papers of a Workshop Held at the University of Twente, The Netherlands, in July 1984_ , MIT Press, Cambridge, pp. 261–280.  
[^cross2000]: Cross, G. (2000),  _An All-Consuming Century: Why Commercialism Won in Modern America_ , Columbia University Press, New York.  
[^donald2002]: Donald, M. (2002),  _A Mind So Rare: The Evolution of Human Consciousness_ , Norton, New York.  
[^eke2002]: Eke, A., Herman, P., Kocsis, L. and Kozak, L.R. (2002),  “Fractal characterization of complexity in temporal physiological signals” ,  _Physiological Measurement_ , Vol. 23 No. 1, pp. R1–R38.  
[^fox1997]: Fox, S.R. (1997),  _The Mirror Makers: A History of American Advertising and Its Creators_ , University of Illinois Press, Urbana.  
[^gao2017]: Gao, J., Fang, P. and Liu, F. (2017),  “Empirical scaling law connecting persistence and severity of global terrorism” ,  _Physica A: Statistical Mechanics and Its Applications_ , Vol. 482, pp. 74–86.  
[^gao2012]: Gao, J., Hu, J., Mao, X. and Perc, M. (2012),  “Culturomics meets random fractal theory: insights into long-range correlations of social and natural phenomena over the past two centuries” ,  _Journal of The Royal Society Interface_ , Vol. 9 No. 73, pp. 1956–1964.  
[^gao2011]: Gao, J., Hu, J. and Tung, W. (2011),  “Facilitating Joint Chaos and Fractal Analysis of Biosignals through Nonlinear Adaptive Filtering” ,  _PLOS ONE_ , Vol. 6 No. 9, p. e24331.  
[^goffman1985]: Goffman, E. (1985),  _Gender Advertisements_ , Macmillan, London.  
[^granger1969]: Granger, C.W.J. (1969),  “Investigating Causal Relations by Econometric Models and Cross-spectral Methods” ,  _Econometrica_ , Vol. 37 No. 3, pp. 424–438.  
[^degrazia2005]: de Grazia, V. (2005),  _Irresistible Empire: America’s Advance Through Twentieth-Century Europe_ , Kindle Edition., Belknap Press of Harvard University Press, Cambridge.  
[^helbing2015]: Helbing, D., Brockmann, D., Chadefaux, T., Donnay, K., Blanke, U., Woolley-Meza, O., Moussaid, M., et al. (2015),  “Saving human lives: What complexity science and information systems can contribute” ,  _Journal of Statistical Physics_ , Vol. 158 No. 3, pp. 735–781.  
[^hill2002]: Hill, D.D. (2002),  _Advertising to the American Woman, 1900-1999_ , Ohio State University Press, Columbus.  
[^lears1994]: Lears, T.J. (1994),  _Fables of Abundance: A Cultural History of Advertising in America_ , Basic Books, New York.  
[^marchand1985]: Marchand, R. (1985),  _Advertising the American Dream: Making Way for Modernity, 1920-1940_ , University of California Press, Berkeley.  
[^marchant2008]: Marchant, T. (2008),  “Scale invariance and similar invariance conditions for bankruptcy problems” ,  _Social Choice and Welfare_ , Vol. 31 No. 4, pp. 693–707.  
[^marshall1995]: Marshall, M. (1995),  _Contesting Cultural Rhetorics: Public Discourse and Education, 1890-1900_ , University of Michigan Press, Ann Arbor.  
[^michel2011]: Michel, J.-B., Shen, Y.K., Aiden, A.P., Veres, A., Gray, M.K., The Google Books Team, Pickett, J.P., et al. (2011),  “Quantitative Analysis of Culture Using Millions of Digitized Books” ,  _Science_ , Vol. 331 No. 6014, pp. 176–182.  
[^nielbo2019]: Nielbo, K.L., Baunvig, K.F., Liu, B. and Gao, J. (2019),  “A curious case of entropic decay: Persistent complexity in textual cultural heritage” ,  _Digital Scholarship in the Humanities_ , Vol. 34 No. 3, pp. 542–557.  
[^obrien2014]: O’Brien, B.A., Wallot, S., Haussmann, A. and Kloos, H. (2014),  “Using Complexity Metrics to Assess Silent Reading Fluency: A Cross-Sectional Study Comparing Oral and Silent Reading” ,  _Scientific Studies of Reading_ , Vol. 18 No. 4, pp. 235–254.  
[^parkin2007]: Parkin, K. (2007),  _Food Is Love: Advertising and Gender Roles in Modern America_ , University of Pennsylvania Press, Philadelphia.  
[^peng1994]: Peng, C.-K., Buldyrev, S.V., Havlin, S., Simons, M., Stanley, H.E. and Goldberger, A.L. (1994),  “Mosaic organization of DNA nucleotides” ,  _Physical Review_ , Vol. 49 No. 2, p. 1685.  
[^petersen2012]: Petersen, A.M., Tenenbaum, J.N., Havlin, S., Stanley, H.E. and Perc, M. (2012),  “Languages cool as they expand: Allometric scaling and the decreasing need for new words” ,  _Scientific Reports_ , Vol. 2, p. 943.  
[^riley2012]: Riley, M.A., Bonnette, S., Kuznetsov, N., Wallot, S. and Gao, J. (2012),  “A tutorial introduction to adaptive fractal analysis” ,  _Frontiers in Physiology_ , Vol. 3, available at: [https://doi.org/10.3389/fphys.2012.00371](https://doi.org/10.3389/fphys.2012.00371).  
[^rooij1974]: Rooij, M. (1974),  _Kranten: dagbladpers en maatschappij_ , Wetenschappelijke Uitgeverij, Amsterdam.  
[^schreurs2001]: Schreurs, W. (2001),  _Geschiedenis van de Reclame in Nederland_ , Het Spectrum, Utrecht.  
[^schudson1982]: Schudson, M. (1982),  _The Power of News_ , Harvard University Press, Cambridge.  
[^shapiro1965]: Shapiro, S.S. and Wilk, M.B. (1965),  “An Analysis of Variance Test for Normality (Complete Samples)” ,  _Biometrika_ , Vol. 52 No. 3/4, pp. 591–611.  
[^sivulka2012]: Sivulka, J. (2012),  _Soap, Sex, and Cigarettes: A Cultural History of American Advertising_ , 2nd ed., Wadsworth, Boston.  
[^smail2008]: Smail, D.L. (2008),  _On Deep History and the Brain_ , University of California Press, Berkeley.  
[^sugihara2012]: Sugihara, G., May, R., Ye, H., Hsieh, C., Deyle, E., Fogarty, M. and Munch, S. (2012),  “Detecting causality in complex ecosystems” ,  _Science_ , Vol. 338 No. 6106, pp. 496–500.  
[^traub2015]: Traub, M.C., van Ossenbruggen, J. and Hardman, L. (2015),  “Impact analysis of OCR quality on research tasks in digital archives” ,  _International Conference on Theory and Practice of Digital Libraries_ , Springer, pp. 252–263.  
[^voss1975]: Voss, R.F. and Clarke, J. (1975),  “ 1/ f noise  in music and speech” ,  _Nature_ , Vol. 258 No. 5533, pp. 317–318.  
[^wevers2017]: Wevers, M. and Verhoef, J. (2017),  “Coca-Cola: An Icon of the American Way of Life. An Iterative Text Mining Workflow for Analyzing Advertisements in Dutch Twentieth-Century Newspapers” ,  _Digital Humanities Quarterly_ , Vol. 11 No. 4.  
[^white2012]: White, C., Oliffe, J.L. and Bottorff, J.L. (2012),  “From the Physician to the Marlboro Man: Masculinity, Health, and Cigarette Advertising in America, 1946–1964” ,  _Men and Masculinities_ , Vol. 15 No. 5, pp. 526–547.  