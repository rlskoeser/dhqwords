---
type: article
dhqtype: article
title: "The Right Distance: The Researcher’s Key Role between Literary Criticism and Data Visualization in the Atlante Calvino Project"
date: 
article_id: "000784"
volume: 019
issue: 2
authors:
- Virginia Giustetto
- Margherita Parigini
translationType: original
categories:
- data visualization
tags:
- Italo Calvino
- Literary Criticism
abstract: |
   Starting from the multidisciplinary project Atlante Calvino. Literature and Visualization (https://atlantecalvino.unige.ch/?lang=en), which combines literary criticism and data visualization, the paper reflects on the challenges in fusing the diverse methodologies applied by literary scholars (Unité d’italien, University of Geneva) and a team of designers (DensityDesign Lab, Polytechnic University of Milan). The paper describes the process that led from a research hypothesis of literary criticism, designed for Italo Calvino’s fictional work, to the creation of a series of visualizations: in particular, we will focus on the type of text analysis conducted for data collection. Questioning the most common distant reading approach, the Atlante Calvino project adopted a different kind of distance from the text, closer to the practices of scalable reading. The paper aims to reason about the acquisitions and limitations that characterize this method, assigning a new role to the researcher in the context of Digital Humanities.
teaser: "In the Altante Calvino project researchers are pushed to renew their role in the interplay between computational techniques and literary criticism expertise. Altante Calvino project places literary critic at the right distance: far enough from the text to see something new through the visual trends, but still close enough to return to it."
order: 5
draft: true
---
  
# 
  
  

## 1. Introduction
  
Distant reading is one of the boldest ventures that has animated the landscape of literary criticism studies in recent decades. This methodology, inaugurated by Franco Moretti (2000) [^1]  and later applied to various problems in literary criticism, has sparked an intense and controversial debate over time [^anderson2008]; [^herrmann2017]; [^weitin2017]; [^da2019]; [^dobson2021]. Even Moretti himself has raised concerns, acknowledging that this practice often confirms results already acquired through traditional methodologies [^moretti2022]. However, when we consider its merits, the most important one may be that it pushes us to handle literary texts in an entirely new way [^2]  : we are dealing with a type of criticism that seeks  “a  _defamiliarization_ , where the shift in perspective disrupts automatisms, scrapes away the patina of the obvious, and does not mechanically recognize phenomena but forces us to see them as if for the first time”   [^decristofaro_ercolino2021]. [^3]   
  
The distant reading approach can be summarized in this way: through a series of computational techniques, a repeated analysis is conducted on a very high number of texts; this analysis leads to a set of information that, in order to be studied, is represented through visualizations. This description is obviously hasty and superficial, but it allows us to identify the two innovative aspects of this methodology: instead of the text being read by the critic, it is read by the machine; the critic, as a result, will no longer read the text, but visualizations. [^4]  Our discourse, developed from the project  _Atlante Calvino_ , focuses on the visual aspect of the issue and at the same time intends to depart from the automatic dimension of reading. 
  
The project  _Atlante Calvino. Literature and Visualization_ , funded by the SNSF at the University of Geneva (Switzerland), took place from 2017 to 2021. Directed by Francesca Serra, it aimed to investigate a series of critical issues related to Italo Calvino’s narrative work through data visualization techniques. There were two main motivations behind Serra’s decision to conceive the project: first, after having extensively worked on Calvino, to whom she had dedicated two monographs [^serra1996]; [^serra2006] and several papers, she noted the risk of fossilizing the image critics had of the author. Calvino, one of Italy’s most important intellectuals of the 20th century, had been accompanied over the years by an increasing bibliography dedicated to him, further expanded by the recent anniversary of his birth. [^5]  However, many of these essays are often characterized by a sense of  _déjà vu:_  a reverberation effect that presents established interpretations and ideas without a real drive to question what is already known. Therefore, adopting a Digital Humanities approach to explore the work of such a well-studied author can be effective in viewing it from a new perspective and renewing the paths of interpretation. 
  
The second reason is that the  _Atlante Calvino_  project is an experimental field to develop a different practice of literary criticism combined with data visualization. On the one hand, we tried to prove that visual representations allow some literary issues to be addressed and resolved more effectively than through the traditional medium of critical writing itself. The other goal of the project was to enhance the qualitative aspects of the research as much as possible. It is well-known that literary studies, after encountering Digital Humanities, have mostly focused on numerical approaches, prioritizing quantitative aspects over interpretive ones. [^6]  With  _Atlante Calvino_ , we sought to find a boundary space where both components are in constant dialogue but where “counting” is not necessarily the unique strategy. [^7]  The project aimed not only to trace new paths for interpreting Calvino’s work but also to transform data visualization from a simple tool into a crucial node in the critical process, attempting to achieve the type of synergy increasingly desired in the current landscape of criticism [^hinrichs_etal2019]; [^drucker2020]; [^windhager_etal2019]. This is done while avoiding the use of  “visual design […] as a cosmetic retouch of important and complicated issues in an attempt to make them look simpler than they are”   [^lupi2017]. 
  
Both motivations introduce fundamental methodological differences compared to the type of research usually conducted with a distant reading approach. First, the project is dedicated to a single author and his narrative work, drastically reducing the scale of the analysis. Even more significant is the way the relationship between computational tools and the researcher is calibrated: in our case, the data collection is not automatically operated by a machine, but it is manually conducted by the scholar, text by text. 
  
To weave literary criticism with data visualization, two research teams participated in the project: a literary team from the University of Geneva, and the DensityDesign Lab from the Polytechnic University of Milan. [^8]  After an intense three-year collaboration, an online platform was created ([https://atlantecalvino.unige.ch/](https://atlantecalvino.unige.ch/)), which houses all the visualizations produced. However, the visualizations were not the only result achieved. As previously mentioned, these graphic artifacts were designed as glimpses into Calvino’s work, becoming cornerstones in strictly literary research that resulted in two doctoral theses. [^9]  The process behind both outcomes is the real subject of this article. 
  
This essay intends to focus on the type of text analysis conducted, with particular regard to the data collection during the intermediate phase, which led from the literary research question to the visualization. 
  
  
  

## 2. Objects
  
The literary corpus of Italo Calvino’s work [^10]  seemed to fit particularly well with our research for three reasons. The first is extratextual and concerns the author. As mentioned, Calvino is one of the most well-known and translated 20th-century Italian writers whose influence has long transcended national boundaries, as has the critical interest in his work. [^11]  The second reason relates to the work itself: Italo Calvino is an extremely “varied and mutable” [^barenghi2007]  [^12]  writer who, over his roughly forty years of activity, explored and experimented extensively in terms of form as well as content. [^13]  This heterogeneity, which sometimes leads one to feel as if dealing with not just one but many different authors, significantly influenced our choice. Lastly, a practical reason: the corpus of his works is broad but not unmanageable, homogeneous in terms of publication (Calvino published almost exclusively with the same publisher during his lifetime), [^14]  and well-defined. These characteristics made it particularly suitable for our research. 
  
So, how many and what texts are we dealing with? If we choose to count each text as a unit (1 novel = 1 unit, 1 collection of  _n_  short stories =  _n_  units, 1 short story published in a magazine = 1 unit), we are talking about exactly 218 texts of varying lengths, with an average of 17,881 characters per unit, where the shortest ever makes 986 characters and the longest 458,335 characters. [^15]   
  
As with many 20th-century authors, it is not always possible to define the exact type of work being examined. There are certainly novels and collections of short stories, but also cases where such terminology does not fully satisfy classification needs, such as long stories or short novels- terms that have been used interchangeably by critics for works published between the 1950s and 1960s. The difficulty of categorizing a text arose when, during the earliest phase of the project, we created the metadata of the corpus ( _title_ ,  _type_ ,  _length_ ,  _year_ ,  _place of first publication_ , etc.) (Figure 1). From this, after assigning each text an identifier ( _id_ ), we developed a series of guide visualizations of the work. [^16]  Circumscribing and visually representing the boundaries of the corpus proved to be extremely important-not only to clarify which works to include in the textual analyses we were planning but also to gradually familiarize ourselves with the visual language upon which we would base our work. 
{{< figure src="resources/images/Figura%201.svg" caption="Database with the metadata of Calvino’s narrative corpus." alt=""  >}}

    
  
Defining the corpus was the starting point of our research, and the endpoint is the  _Atlante Calvino_  platform, which hosts a series of interactive visualizations organized into three different thematic “itineraries”:  _Doubt_ , considered one of the driving forces behind Calvino’s writing;  _Space_ , which allows for the exploration of the work through mapping all its narrative settings; and  _Form_ , which addresses the fundamental issue of plot. The research questions underpinning all subsequent investigations revolve around these three thematic cores, becoming increasingly sophisticated. The three itineraries are autonomous but deeply connected on a conceptual level (Figure 2). Each of them is composed of three “stages” corresponding to three visualizations: the first offers a concrete and tangible representation of the phenomenon (e.g., the settings of the work); the second seeks to highlight the underlying question (e.g., how do settings change over time?); the third investigates the abstract issue from which the phenomenon originates (e.g., the relationship with realism). [^17]   
{{< figure src="resources/images/Figura%202.svg" caption="Structure of the platform." alt=""  >}}

    
  
Each visualization in the three itineraries presents the same interface. To illustrate the various possible interactions with the visualization, as well as the sections where the different information is located, we will use the second stage of the Space itinerary as an example, which we will return to later. 
{{< figure src="resources/images/Figura%203.svg" caption="The general structure of a visualization. Example taken from the second stage of the Space itinerary, entitled _Transforming_ ." alt=""  >}}

    
  
At the center of Figure 3 appears the visualization, which can be interacted with through a series of simple operations: zooming in, selecting a specific element (which often reveals superficially hidden information, such as text labels), and using filters (e.g., chronological, title, etc.) that reduce the scope of action and highlight certain areas of interest. Textual sections located on the right-hand side of the window aid the correct reading of the visualization: the  _Explanation_  provides concise answers to the questions “What is it?” and “How does it work?” while also suggesting some possible “Reading tips”. The  _Key_  fulfills its traditional role of explaining the different symbols present in the visualization. 
  
In addition to the three itineraries, the platform includes some informative sections ( _Team_ ,  _Project_ ,  _User guide_ ,  _Capta_ ,  _Publications_ ) and the  _Compass_  section (see note 14). 
  
  
  

## 3. Process
  
  

## 3.1 The Space Itinerary as a Case Study
  
We would now like to focus on the process, namely the type of text analysis that allowed us to move from an initial research hypothesis to its realization in a visualization. To illustrate all the steps of this phase as exhaustively as possible, we have selected a case study highlighting a specific stage of the  _Atlante Calvino_ , which is part of the  _Space_  itinerary. 
  
Space, primarily dealing with settings, as we will see, is a central theme in Calvino’s work, whose strong visual inclination is reflected in his considerable attention to  “space, topology, and […] more generally to the surface of the world”   [^belpoliti2006]. Therefore, the starting point was investigating the ways, variations, and effects of this dimension on his work using Digital Humanities practices. Among other things, we believed that through the analysis of settings that form the backdrop of each work and their transformation over time, we could better understand certain nodes of Calvino’s complex relationship with realism. We also wanted to build on some insights from the dialogue between literary studies and geography, which began in the early 1990s [^tally2013]; [^peraldo2016] and has pointed to promising critical directions in the last two decades, which seemed to adapt particularly well to a digital approach. Specifically, there were two important references from which we started to frame the discourse: the literary maps worked on by Franco Moretti in his  _Atlante del romanzo europeo. 1800-1900_ , and the digital project  _A Literary Atlas of Europe: Towards a Geography of Fiction_ , led by Barbara Piatti at the Zurich Institute of Cartography from 2006 to 2013. 
  
These are two very different works, created about fifteen years apart. Moretti’s research, completed at the end of the 1990s, is analog and not yet influenced by the concept of distant reading, either methodologically or instrumentally. However, the core thesis he advanced is crucial for our research: the idea that  “geography is [...] an active, concrete force that leaves its traces on texts, plots, and systems of expectations”   [^moretti1997]. [^18]   Piatti’s cartographic model is more concerned with data classification, stemming from the question:  “How adequately can fictional settings be mapped by means of newly designed tailor-made symbology?”   [^19]  Despite the differences in approach and the approximately fifteen years separating the two studies, our research engages fruitfully with both. Our decision to begin investigating the spatial phenomenon of Calvino’s work by systematically analyzing all the settings [^20]  stems from these two studies. 
  
  
  

## 3.2 The Phases of the Process
  
The process we followed had two main phases: the initial hypothesis and the structuring and collection of data, as illustrated in the diagram (Figure 4). 
{{< figure src="resources/images/Figura%204.svg" caption="Illustration of the process." alt=""  >}}

    
  
Before describing these phases in detail, focusing on the unique aspects that characterized our work, it’s important to clarify: in the context of Digital Humanities, once the research question has been defined and initial critical hypotheses have been made, regardless of the method adopted, the analysis will begin with the selection of a certain number of words (or, depending on the technique, some parts of it, like subwords), which will be used as data through a process of translation. This happens because in a text,  “the only immediately accessible component is the words composing the ‘surface level’ of the discourse”   [^ciotti2023], [^21]  and although this observation might seem obvious, it establishes a constraint with which researchers must immediately come to terms. [^22]  For instance, if the analysis involves a stylometric technique, it is easy to see how a specific word might be used as a measurable value. But if the subject being measured is not a frequency but rather a more abstract concept, such as spatiality or doubt, the operations become more complex. On which words should the analysis be based? 
  
Let’s proceed in order: after deciding that our focus would be on the settings in text, [^23]  it was important first to define clearly and consistently the concept of setting and then, in a second phase, to identify the categories from which to build the data structure. 
  
The definition of setting was particularly aided by the one proposed by Barbara Piatti’s team:  “setting is the location where the action takes place – characters are present”   [^reuschelhurni2011]. [^24]  Here are three examples from three different Calvino’s texts published in 1947, 1957, and 1983: 
  
    
>   
> "Camminava per il sentiero della  **vigna** , a mani in tasca, senz’alzare troppi i tacchi" [^calvino1991]  
> "Eravamo nella […] nostra  **villa**  d’ **Ombrosa** , le finestre inquadravano i folti rami del grande elce del parco" (ivi, p. 549) 
> "Il signor Palomar vorrebbe capire perché le iguane lo attirano; a  **Parigi**  va di tanto 
> in tanto a visitare il  **rettilario**  del  **Jardin des Plantes** " [^calvino1992]  [^25]   
  
  
Although we cannot dwell in detail here on the hermeneutic nuances of this seemingly simple task, we will highlight some unique characteristics that became evident right from the start: 
  
  
  a. In some cases, the locations were geolocatable (e.g., the  _Jardin des Plantes_  in  _Paris_ ), but in many other cases, they were unspecified locations (e.g., a  _vineyard_ ) that could not be geolocated on a map.  b. Among the specific locations, some were existing places (e.g.,  _Paris_ ), while others were entirely fictional (e.g.,  _Ombrosa_ ).  c. In some cases, hierarchical relationships between two places could be identified (e.g., the  _villa_  at  _Ombrosa_ ; the  _reptile house_  at the  _Jardin des Plantes_  in  _Paris_ ), while in other cases, no such relationships existed.  

  
  
Considering these multiple possibilities and the logical consequences that would follow (for instance, the fact that cartographic language might not be suitable for fully representing all locations) was essential in defining the data structure. After consulting with experts from different fields, the data structure took the following form (Figure 5): 
{{< figure src="resources/images/Figura%205.svg" caption="Data structure." alt=""  >}}

    
  
For each word collected, we recorded the name ( _occurrence_ ), any hierarchical relationships with other places mentioned ( _affiliation_ ), the position of the word in the text ( _starts_at_ ,  _ends_at_ ), whether it was a terrestrial location [^26]  ( _terrestrial_ ), whether it was geolocatable ( _geolocation_ ) [^27]  , and whether it was fictional ( _invented_ ). By cross-referencing these last three characteristics, it was possible to categorize the place ( _place category_ ) [^28]  —a feature we immediately imagined would be central to the visual representation of our map. Finally, all the locations in a single text could be assigned a recurring theme (e.g., travel, war), if present, and any particular details could be marked in a note. 
  
The data collection phase was crucial in determining the final form of the visualization. Before starting, it was natural to discuss whether to partially or fully automate the data collection process. Several concerns quickly arose. Some were related to the specific nature of the data, others to contractual constraints, [^29]  and still others to the available tools. The latter, in fact, mostly operate in English, resulting in imprecise or even ineffective outcomes when dealing with Italian texts. However, it was the nature of the data itself that presented the most significant issues. Some software can automatically recognize geographical references in a text, even in Italian, but this is not enough. A tool like GeoDict, [^30]  for instance, can identify geographical references but cannot distinguish between spatial elements within a text (and, consequently, what is a setting and what is not). Moreover, software based on named entity recognition would not have been able to detect unspecified settings that are not geolocatable (e.g., a  _vineyard_  or a  _house_ ) or automatically recognize a location that the author deliberately disguised with a coded name (e.g., the city of “ _***_ ” in the story  _La speculazione edilizia_ ), even though its real-world reference would have been easily deducible by the reader. These considerations highlighted how unsuitable automated data collection would have been for the type of analysis we were conducting. 
  
On the other hand, a fully manual data collection process, while feasible given the size of the corpus, seemed overly time-consuming. Ultimately, a middle-ground solution was found: a non-automated approach supported by a custom-built tool for textual mark-up, Explorer, which sped up the data collection process. [^31]  This solution, dependent on the interpretive choices made by the researcher, offered greater freedom in modeling the data, which, to paraphrase [^lupi2017], introduced new ways of thinking and allowed us to better address complex issues through tailored solutions. 
  
  
  

## 3.3 Returnin to the Text
  
The data collection phase was essentially a translation operation, where the words of a text were used as computational elements, or data. [^32]  It is worth noting what Valeria Burgio  [^burgio2021] has said about the term  _data_ :  “Data does not exist in nature. The name is misleading because no one ‘gives’ data; rather, someone takes it, collects it-not because it grows on trees. Data is the result of an extraction from a reservoir of indistinct possibilities.”  Our data, or as Johanna Drucker would say, our  _capta_   [^drucker2011], are fundamentally  “cultural artifacts contaminated by their historical and material contingencies”   [^burgio2021]. [^33]   
  
The settings in the three examples mentioned earlier were classified as follows: 
{{< figure src="resources/images/Figura%206.svg" caption="Three examples from the location dataset." alt=""  >}}

    
  
Let’s focus on the last example, the  _reptile house_  at the  _Jardin des Plantes_  in  _Paris_ . Figure 7 depicts the visual translation of the data collected: 
{{< figure src="resources/images/Figura%207.svg" caption="Example of a setting visualization from the _Transforming_ stage." alt=""  >}}

    
  
If we assume that  “how a dataset is collected and the information included -and omitted- directly determines the course of its life”   [^lupi2017], there are at least two considerations to be made. First, the fact that this and other visualizations produced for the  _Atlante Calvino_  always represent a subjective critical viewpoint, attributable to the person who directed the analysis with their choices. Secondly, in the data collection phase -and subsequently within the visualization- the original literary text seems to disappear. Some elements remain (e.g.,  _place names_ ), whose characteristics (e.g.,  _place category_ ) and internal relationships are highlighted, but the ability to grasp the text’s overall meaning, appreciating its nuances and intended ambiguities, is inevitably lost. Quite simply, the ability to read it is lost. [^34]   
  
This happens, as Martin Mueller aptly pointed out, because the kind of operation being carried out closely resembles the zoom tool we use when navigating Google Earth:  “you can zoom in and out of things and discover that different properties of phenomena are revealed by looking at them from different distances”   [^mueller2012]. Martin Mueller’s idea, which led to the concept of scalable reading [^35]   [^english_underwood2016]; [^herrmann2017]; [^fickersclavert2021], fits particularly well with our research, as the question underpinning his work is the same that initiated the  _Atlante Calvino_ :  “how can literary scholars analyze texts, text segments or text corpora from different points of view, i.e., with quantitative and qualitative methods alike?”   [^krautter2023]. 
{{< figure src="resources/images/Figura%208.svg" caption="The flow of the analysis." alt=""  >}}

    
  
For example, the visualization of settings [^36]  allows one to visualize the entire literary geography of the writer in one go through a process of reduction (zoom out), which relates only the locations of the corpus, isolated from the rest of the text. On the other hand, by zooming in or selecting specific results, it is possible to delve deeper into the nature of these data, suggesting correspondences and potential critical directions, and prompting a return to the text to verify what has been discovered, either confirming or challenging already established critical hypotheses. The visualization, as Jérôme David affirms, is only  “a ‘moment’ in the reasoning process”   [^decristofaro_ercolino2021]. [^37]  ; it invites the viewer to return to the literary object through a movement of text-visualization-text, which is not confined to a single direction or a single instance (Figure 8). Although the text seems absent from the visualization, it remains a constant reference point to which we continually return during the different phases of the process. Moreover, the interactive nature of all the visualizations of the  _Atlante Calvino_ , which offer overall views but also suggest focused views on specific sections, inevitably leads to scalable reading, distancing itself significantly in terms of methodology from an exclusively distant approach. 
  
Let’s examine one of the previously cited textual examples: the case of Paris. The French city appears as a setting not only in the story  _L’ordine degli squamati_  (1983, part of the collection  _Palomar_ ) but also in various other texts by the author. After analyzing the specific case of the 1983 story, it might be interesting to simultaneously identify all instances of Paris in Calvino’s work (Figure 9). 
{{< figure src="resources/images/Figura%209.svg" caption="All instances of Paris in Calvino’s work within the _Transforming_ stage." alt=""  >}}

    
  
The overall analysis of this setting, [^38]  which appears 12 times between 1954 and 1983, raises a series of intriguing questions. Here are a few examples: Why does the presence of this setting increase starting from the 1970s? Is there a connection between the biographical places of the author -who lived permanently in Paris since 1967- and the literary settings? Do the selected texts tend to emphasize a realistic dimension or an invented one? How many and what kinds of places are contained within Paris? How is the city described? Do the characters in these stories move around the city, or do they remain essentially motionless? In many cases, to answer these questions, it is necessary to return to individual texts, or even specific paragraphs, while in others, the overall view itself guides the responses. 
  
  
  
  

## 4. Critical assessments
  
To consider the overall project, it is certainly helpful to attempt an evaluation of a research endeavor with such a marked experimental character. 
  
A strong stance that influenced the project was the decision to avoid a series of established digital methods for textual analysis. In the  _Atlante Calvino_ , there is no trace of practices like topic modeling or, more generally, of other techniques related to NLP. More than a rejection of these approaches, this choice was driven by the desire to create a genuine synergy between the practices of literary criticism and those of data visualization. And the first major step in this direction was the control over the data. 
  
In each of the visualizations of the  _Atlante Calvino_ , the data is not selected by a machine but by a person: a scholar who examined the text, hypothesized a data collection structure compatible with their research question, and then patiently read and sampled the entire selected corpus, identifying page by page the words, phrases, and paragraphs relevant to the critical problem they wanted to investigate. Such an operation brings several limitations: 
  (a) The first is certainly practical. Manually generating a dataset takes a long time, nullifying one of the main advantages typically associated with Digital Humanities: the ability to conduct research on extremely large corpora in a short time through automation.  (b) Secondly, manual data collection can be seen as a disadvantage in terms of the reliability of the critical result: one of the peculiarities of most Digital Humanities studies is that they emphasize not only the conceptual but also the “technical” verifiability of the various stages of the research, thus guaranteeing the reproducibility of the method and -implicitly- the objectivity of the outcome. [^39]   

  
  
However, both of these limitations offer positive outcomes. First, the slowdown caused by this careful data selection contributes to ensuring its quality. While a strong hermeneutic stance is not common practice in the Digital Humanities, shaping the dataset entirely based on the researcher’s skills opens the door to a new -and perhaps more mindful- way of using digital tools. Jérôme David argued that one of the most stimulating aspects of the Digital Humanities, as synthesized by de Cristofaro and Ercolino, is the effort to articulate as rigorously as possible the links in the chain of hermeneutic reasoning:  “the fertility of this effort lies [indeed] in the ability to raise new problems  _upstream of any attempt at empirical verification through algorithms_  […], thus contributing to enriching the conceptual repertoire of literary studies”   [^decristofaro_ercolino2021]. [^40]  Based on this interpretation, the Atlante Calvino creates an experimental ground where researchers are pushed to renew their role in the interplay between computational techniques and literary criticism expertise. [^41]  The researchers involved did not entrust the machine with the task of analyzing the text but analyzed the text themselves, focusing on the elements needed to create a visualization. By setting up data collection structures designed to answer a specific research question, it became possible to identify new ways of viewing Calvino’s literary work. [^42]  Even the aura of objectivity often associated with results obtained through computational techniques -particularly during the initial phase of the Digital Humanities- is now being questioned within a broader discourse ([^burgio2021]; [^bode2023]) which tends to problematize the positivist approach, partly now outdated [^dastongalison2007]; [^vidalineresini2015]. [^43]  There is sometimes a sense that, rather than fully exploiting the potential of new technologies, the researcher wants to avoid their own role, delegating it to the machine. Or, at the very least, they entrust the machine with a greater responsibility than it might be fair to give. 
  
Moreover, manual data collection is a way of searching for things in the text that might otherwise go unnoticed. As ohanna DruckerJ has said, data is always acquired through a conscious selection and is never provided neutrally. This is even more true when dealing with the work of an author so studied that he risks being overshadowed by his critical reception. The  _Atlante Calvino_  aimed to set aside value judgments expressed on specific volumes or limited areas of the work, analyzing it as a whole. The result is an in-depth knowledge of the author’s oeuvre, challenging the adage Moretti postulated when he coined the term  _distant reading_ :  “Reading ‘more’ is always a good thing but not the solution”   [^moretti2000]. In our case, it was the only solution. A solution that allowed us to minimize the amount of critical information that influences the reading of the text and determines its position in the literary canon. 
  
  
  

## 5. Conclusion
  
Moretti provocatively reversed the traditional formula of  _close reading_ . If we were to describe this critical practice as a movement, we could imagine a person leaning closer to examine an object. Not because that object is not clearly visible, but because we are convinced that beyond appearances, something hidden lies waiting to be brought to light. In his article, Moretti inverted the direction of this movement: no longer approaching the object but stepping back until it disappears from view. What kind of knowledge could we access if we positioned ourselves so far from the text that we could no longer see it?  “Distance, let me repeat, is a  _condition of knowledge_ : it allows you to focus on units that are much smaller or much larger than the text: devices, themes, tropes-or genres and systems”   [^moretti2000]. 
  
With the  _Atlante Calvino_ , we moved closer to the text, making it both the starting point and the destination of the analysis. The visualization is not an outcome in itself but a transitional phase, a critical tool to be handled to discover something new, after which we return to text. [^44]  Thus, a series of variable views follow one another: first, the entire corpus is analyzed microscopically ( _text analysis_  >  _database_ ), then the focus shifts to a macroscopic scale thanks to a “graphic” version of the critical problem ( _database_  >  _visualization_ ); from here, we return to the text, following the visual forms that we consider significant and capable of answering the questions we originally posed ( _visualization_  >  _enhanced analysis_ ). 
  
Perhaps what we have attempted to do is find a formula that places us at the  _right distance_ : far enough from the text to see something new through the visual trends [^morettisobchuk2020], but still close enough to return to it. 
  
  
  

## Acknowledgements
  
We would first like to emphasize the shared authorship of the article: both of us equally contributed to its conception, writing, and editing; only the figures are elaborated by Margherita Parigini. 
  
We would like to thank Francesca Serra, who conceived and directed the  _Atlante Calvino_  project, and our colleague Valeria Cavalloro, who edited the itinerary of  _Form_ . 
  
 We also thank the team at DensityDesign Lab: the founder Paolo Ciuccarelli, the scientific director Michele Mauri, the researchers Ángeles Briones, Tommaso Elli, and Beatrice Gobbo. 
  
The value of collaboration underpinned the project at every stage, contributing decisively to the final outcome of the research. This experience confirms the spirit of cooperation and constructive exchange that distinguishes the Digital Humanities.  
  
  
[^1]: In his article  _A Genealogy of Distant Reading_ , [^underwood2017] argues that Moretti did not actually  “invent the idea of macroscopic literary inquiry. [...] Quantitative interpretation of literature is a story that stretches back through book history, sociology, and linguistics to a range of nineteenth-century experiments.” 
[^2]: This statement is especially true when we look at the study group in Digital Humanities, which does not aim to computationally reproduce already tried-and-true practices, such as the philological edition of text.
[^3]: Our translation from Italian.
[^4]: Distant reading involved to replace the text with an image. These visuals were rather rudimentary-graphs that combined structuralism’s love for numerical frequencies with the potential opened by new technologies [^ciotti2023]; [^giusjacke2022]. A key part of this experiment was thus the “loss” of the text, depriving the literary critic of their usual material. But more importantly, it challenged them to radically change their way of thinking. 
[^5]: Among the various initiatives, we point out the creation of a new series of studies at Carocci Editore to precisely revive the study of the author’s work, created in collaboration with the Laboratorio Calvino research center ([https://www.laboratoriocalvino.org/](https://www.laboratoriocalvino.org/)).
[^6]: Usually, these practices have been used for database creation, concordance lists or analysis of linguistic recurrences [^mitkov2003]; or as an aid in setting up critical editions, manuscript collation and other digital philology work [^pierazzo2015].
[^7]: We highlight the paper of [^correll2019] that reflects on how the practice of “counting” risks distorting the object of research and causing a general flattening of the possibilities for collaboration between “humanists” and “designers.”
[^8]: The various people who collaborated in creating the platform, as well as their different roles, are mentioned in the  _Team_  section ([https://atlantecalvino.unige.ch/equipe?lang=en](https://atlantecalvino.unige.ch/equipe?lang=en)).
[^9]: The two researches concern the itinerary of  _Doubt_ , edited by Margherita Parigini, and  _Space_ , edited by Virginia Giustetto, respectively. Both works are being published by Carocci Editore within the series  “Laboratorio Calvino”   [^parigini2024]; (Giustetto soon to be published in 2025).
[^10]: The corpus of texts examined for the  _Atlante Calvino_  is exclusively narrative; therefore, all texts of a purely non-fiction nature, which, although they make up a significant part of his oeuvre, were voluntarily excluded, as was the important work of rewriting  _Fiabe italiane_ , which engaged the author for two years. The reference edition of all of the author’s texts is the one set up for the Mondadori “Meridiani” edition ([^calvino1991]; [^calvino1992]; [^calvino1994]) the publishing house that today holds the rights to the entire work, of which he has kindly allowed us to use in digital format for the creation of the databases necessary for the visual elaborations.
[^11]: [^rubini2023] reconstructed the international circulation of the author’s works from 1955, the year of the first foreign publication, to 2020, supporting the hypothesis that Calvino is the 20th-century Italian intellectual who has had the most significant impact on a global scale. 
[^12]: Our translation from Italian.
[^13]: This variety manifests itself in terms of genre (in his work, it is possible to identify a neorealist phase, a fantastic phase, a “scientific” phase, a combinatory phase, to name just a few) and in terms of type of publication (ranging from short stories to novels, including an intermediate form that was particularly dear to him), profoundly influencing the style he adopted. This, after all, is an aspect of which Calvino himself was aware, to the point of provocatively declaring, in one of his last literary disguises, that he was “an author who changes greatly from book to book” [^calvino1992] (our translation from Italian).
[^14]: Between 1947 and 1983 Calvino published twenty-five books with the Turin publisher Einaudi, selling about four million volumes and also taking care of the choice of covers, images and flaps [^serra2006]; [^baranelli2007].
[^15]: This dimension empirically confirms the author’s predilection for the short form, on which critics agree theoretically but do not often focus attention.
[^16]: The guide visualizations have flowed into the  _Atlante Calvino_  section titled  _Compass_  ([https://atlantecalvino.unige.ch/compass?lang=en](https://atlantecalvino.unige.ch/compass?lang=en)), always at hand, which highlights, from distinct perspectives, some data on the compositional history of Calvino’s work, useful for finding information on the editorial history of the texts and the author’s mental library. The first visualization, titled  _Time and Works_ , is a concise map that follows the development of Calvino’s four-decade-long literary career, showing the most important turning points in his publishing history. The second one, titled  _Flows of the Stories_ , reconstructs the publishing history of over two hundred short stories through a visualization, highlighting his cooperation with periodicals and newspapers. The third one, titled  _Archipelago of Names_ , is the only one that considers non-fiction works. It gathers together and organizes, in a single view, the nearly two thousand names quoted across the great number of essays and articles published during Calvino’s lifetime.
[^17]: As highlighted in Figure 2, the first stage of all three itineraries - the concrete and tangible representation of the three phenomena - is grafted onto the same starting point, mentioned earlier: the visual reproduction of the narrative corpus, the starting point of the three different itineraries. It is a kind of territory, not surprisingly entitled  _Exploring the corpus_ , which sets the rules of the game and its boundaries (see [https://atlantecalvino.unige.ch/archipelago?lang=en](https://atlantecalvino.unige.ch/archipelago?lang=en)).
[^18]: Our translation from Italian.
[^19]: The quote can be found in the section  _Motivation_  on the website  _Literary Atlas of Europe_  ([https://www.literaturatlas.eu/en/project/project-frame/motivation/index.html](https://www.literaturatlas.eu/en/project/project-frame/motivation/index.html)).
[^20]: In Figure 2 we refer specifically to the view entitled  _Locations_  ([https://atlantecalvino.unige.ch/space/phase1?lang=en](https://atlantecalvino.unige.ch/space/phase1?lang=en)).
[^21]: Our translation from Italian.
[^22]: E.g., a word in literature can contain within itself a component of intentional ambiguity that is often lost in its transformation into data. The attribution of precise characteristics, the need to carry out binary choices, makes it very difficult to keep alive the nuances of meaning that literature feeds on.
[^23]: We refer here to the categorization proposed by Piatti, who identifies five different spatial elements in a literary text:  _Setting, Projected space, Zone of action, Marker, Route_   [^reuschelhurni2011].
[^24]: Thus, all places mentioned as memories of the past or future destinations are excluded, as well as so-called geographic markers, meaningless places mentioned with other functions in the text (e.g., a bar in New York called  _Paris_ ).
[^25]: Our translation from Italian:  “He was walking along the vineyard path with his hands in his pockets, barely lifting his heels” ;  “We were in […] our villa at Ombrosa, the windows framed the thick branches of the large oak in the park” ;  “ Mr. Palomar  wanted to understand why iguanas fascinated him; in Paris, he occasionally visited the reptile house at the Jardin des Plantes.” 
[^26]: This attribution might seem obvious, but several of Italo Calvino’s works are set in cosmic space, hence the need to distinguish between terrestrial and not terrestrial places.
[^27]: For this specific map, it was sufficient to indicate only the “geolocatable” nature of each location (binary value: yes/no). Nevertheless, in order to create a second and more specific visualization limited to geolocatable locations only (titled  _Cartography of the terrestrial locations_ , accessible here: [https://atlantecalvino.unige.ch/space/phase2/focus?lang=en](https://atlantecalvino.unige.ch/space/phase2/focus?lang=en)), we also included the parameter of the coordinates within the dataset.
[^28]: There are five categories of setting places:  _Unspecified cosmic_ ,  _Specific cosmic_ ,  _Specific Terrestrial_ ,  _Unspecified Terrestrial_ ,  _Invented Terrestrial_ . Within the visualization each of these place categories is indicated with a distinct color ([https://atlantecalvino.unige.ch/space/phase2?lang=en](https://atlantecalvino.unige.ch/space/phase2?lang=en)).
[^29]:  In order not to break confidentiality agreements made with the Mondadori publishing house, which holds the copyright on the author’s work, we could not upload the digitized material to external servers, a condition required by most freely accessible tools.
[^30]: See [https://www.math2market.com/](https://www.math2market.com/). On the subject of how easy it is to make mistakes when working on localities (entities that seem to be easily extracted automatically from a large body of texts), we point to Jeremy Rosen’s (2011) counter-analysis to Matthew Wilkens’ (2011) article.
[^31]:  _Explorer_ , created by the DensityDesign Lab ([https://densitydesign.github.io/atlante-calvino/explorer/](https://densitydesign.github.io/atlante-calvino/explorer/)), allows the upload of a text in .txt format and a data structure in .tsv format. Both can be easily produced and provided by researchers and thus fully customizable. The tool is made in the form of a web application, but being completely client-side it does not expose the texts to unauthorized dissemination. For more information see the  _Data Collections Tools_  section of  _Capta_  ([https://atlantecalvino.unige.ch/capta?lang=en](https://atlantecalvino.unige.ch/capta?lang=en)).
[^32]: The timing of the research, closely tied to the progress of the doctoral program, combined with legal injunctions on the confidentiality of the texts, prompted the researchers to forego calculating an “annotator agreement”, renouncing to precisely measure the reliability of the data collection structure. This waiver was partly mitigated by the fact that they relied on an already broken-in classification system as a result of Barbara Piatti’s research group.
[^33]: Our translation from Italian for both quotations from [^burgio2021]
[^34]: Also keep in mind that, as a result of the contract with the publisher Mondadori, portions of text longer than a few lines could not be reproduced on the platform.
[^35]: Some scholars propose to talk about literary modelling, instead of  _scalable reading_    “since it does not suggest a practice limited to reading texts and stresses more the need to make the assumptions explicit about the nature of reading (literary) texts”   [^pianzola_etal2020].
[^36]: The transition from dataset to visualization, guided by the question “What do we want to see?” also requires a whole series of choices that decisively condition the subsequent stages of interpretation, but this topic is not addressed here. For a description of how designers and literary researchers collaborated within the  _Atlante Calvino_  project see [^elli2023]. To extend the discussion, see also: [^manchia2020]; [^benito_santos_sánchez2020]; [^dignaziobhargava2016].
[^37]: Our translation from Italian.
[^38]: In this type of research, as in many others carried out within the  _Atlante Calvino_ , concordance analysis, to quote a word very dear to Martin Mueller, is central.
[^39]: To better understand how “the idea of replication into the humanities” has taken hold: [^piper2020]; [^ries_etal2024]. To reconstruct the debate on the “rhetoric of objectivity and truth surrounding such measures” [^bode2012]; [^fabbrilatour1981].
[^40]: Our translation from Italian. David’s argument refers to the process commonly known as “operationalization” [^moretti2013].
[^41]: Reflections on the relationship between traditional methods of analysis and computational techniques in recent years are increasingly moving in this direction, as the works of [^eve2019] and [^ketzan2021]show. The first of the two, published when  _Atlante Calvino_  was underway, challenges the established opposition between distant and close reading, calling for a synergy similar to what we also tried to achieve with our project, although the methods adopted are very different.
[^42]: This aspect is also reflected in the visual solutions adopted, specifically designed for each of the stages that are part of the three routes of the  _Atlante_ .
[^43]: Even statistical values, which carry an aura of objectivity, are the result of a long research process:  “mean, standard deviation, probability, equivalence class, correlation, regression, sample, [...] the user of statistical data receives compact concepts, encapsulated in concise and economical formulations, whereas these tools are the product of a historical gestation traversed by hesitations, re-translations, conflicts of interpretation”   [^desrosières2010]. Our translation from French.
[^44]: As [^rosen2011] advocated,  “close and distant can be ways of looking that reinforce one another. Perpetuating the false dichotomy between them forecloses a whole range of differently-scaled modes of analysis—from elucidation of the manner in which publishers market the symbolic capital of canonical works, to scrutiny of the ways a given text diverges from a set of generic conventions—that subsist between close reading and data mining.”   
[^anderson2008]: Anderson, C. (2008)  “The End of Theory: The Data Deluge Makes the Scientific Method Obsolete.”  WIRED. 23 June 2008. Available at: [https://www.wired.com/2008/06/pb-theory/](https://www.wired.com/2008/06/pb-theory/).   
[^baranelli2007]: Baranelli, L. (2007)  _Bibliografia di Italo Calvino_ . Pisa: Scuola Normale Superiore di Pisa.   
[^barenghi2007]: Barenghi, M. (2007)  _Italo Calvino, le linee e i margini_ . Bologna: Il Mulino.   
[^belpoliti2006]: Belpoliti, M. (2006)  _L’occhio di Calvino_ . Torino: Einaudi.   
[^benito_santos_sánchez2020]: Benito-Santos, A. and R.T. Sánchez (2020)  “A data-driven introduction to authors, readings, and techniques in visualization for the digital humanities” ,  _IEE Computer Graphics and Applications_ , 40(3), pp. 45-57.   
[^bode2012]: Bode, K. (2012)  _Reading by numbers: Recalibrating the literary field_ . London-New York: Anthem Press.   
[^bode2023]: Bode, K. (2023)  “Doing (computational) literary studies” ,  _New Literary History_ , 53(3), pp. 531-58. Available at: [https://muse.jhu.edu/article/898320](https://muse.jhu.edu/article/898320).   
[^burgio2021]: Burgio, V. (2021)  _Rumore visivo. Semiotica e critica dell’infografica. _ Sesto San Giovanni: Mimesis Edizioni.  
[^calvino1991]: Calvino, I. (1991)  _Romanzi e racconti_ . Vol. 1. C. Milanini, M. Barenghi, and B. Falcetto (eds.). Milano: Mondadori.  
[^calvino1992]: Calvino, I. (1992)  _Romanzi e racconti_ . Vol. 2. C. Milanini, M. Barenghi, and B. Falcetto (eds.). Milano: Mondadori.  
[^calvino1994]: Calvino, I. (1994)  _Romanzi e racconti_ . Vol. 3. C. Milanini, M. Barenghi, and B. Falcetto (eds.). Milano: Mondadori.  
[^ciotti2023]: Ciotti, F. (2023)  _Digital Humanities. Metodi, strumenti, saperi_ . Roma: Carocci.  
[^correll2019]: Correll, M. (2019)  “Counting, collaborating, and coexisting: Visualization and the digital humanities” ,  _Medium_ . Available at: [https://mcorrell.medium.com/counting-collaborating-and-coexisting-visualization-and-the-digital-humanities-1bf157400d8](https://mcorrell.medium.com/counting-collaborating-and-coexisting-visualization-and-the-digital-humanities-1bf157400d8).  
[^da2019]: Da, N.Z. (2019)  “The computational case against computational literary studies” ,  _Critical Inquiry_ , 45(3), pp. 601-639. Available at [https://doi.org/10.1086/702594](https://doi.org/10.1086/702594).   
[^decristofaro_ercolino2021]: de Cristofaro, F. and S. Ercolino (2021)  _Critica sperimentale. Franco Moretti e la letteratura_ . Roma: Carocci.  
[^dastongalison2007]: Daston, L. and P. Galison (2007)  _Objectivity_ . New York: Zone Book.  
[^dignaziobhargava2016]: D'Ignazio, C. and R. Bhargava (2016)  “DataBasic : Design Principles, Tools and Activities for Data Literacy Learners” ,  _The Journal of Community Informatics_ , 12(3), pp. 83-107. Available at: [https://www.media.mit.edu/publications/databasic-design-principles-tools-and-activities-for-data-literacy-learners/](https://www.media.mit.edu/publications/databasic-design-principles-tools-and-activities-for-data-literacy-learners/).  
[^desrosières2010]: Desrosières, A. (2010)  _La politique des grands nombres. Histoire de la raison statistique_ . Paris: La Découverte. Available at: [https://doi.org/10.3917/dec.desro.2010.01](https://doi.org/10.3917/dec.desro.2010.01).  
[^drucker2011]: Drucker, J. (2011)  “Humanities approaches to graphical display” ,  _DHQ_ , 5(1). Available at: [https://www.digitalhumanities.org/dhq/vol/5/1/000091/000091.html](/dhqwords/vol/5/1/000091/).  
[^drucker2020]: Drucker, J. (2020)  _Visualization and interpretation: Humanistic approaches to display_ . Cambridge: MIT Press.  
[^dobson2021]: Dobson, J. (2021)  “Interpretable outputs: Criteria for machine learning in the humanities” ,  _DHQ_ , 15(2). Available at: [https://www.digitalhumanities.org/dhq/vol/15/2/000555/000555.html](/dhqwords/vol/15/2/000555/).  
[^english_underwood2016]: English, J.F. and T. Underwood (2016)  “Shifting scales: Between literature and social science” ,  _Modern Language Quarterly_ , 77(3), pp. 277-295. Available at: [https://doi.org/10.1215/00267929-3570612](https://doi.org/10.1215/00267929-3570612).  
[^elli2023]: Elli, R. (2023)  “Supporting literary criticism with data visualization: Four design guidelines for facilitating interdisciplinary collaborations” ,  _Convergências_ , 16(32), pp. 152-63. 30 November. Available at: [https://doi.org/10.53681/c1514225187514391s.32.215](https://doi.org/10.53681/c1514225187514391s.32.215).  
[^eve2019]: Eve, P.M. (2019)  _Close reading with computers_ . Stanford: Stanford University Press.  
[^fabbrilatour1981]: Fabbri, P. and B. Latour (1981)  “La rhétorique de la science. Pouvoir et devoir dans un article de science exacte” ,  _Actes de la recherche en sciences sociales_ , 16 (1), pp. 87-114. Available at: [https://doi.org/10.31468/cjsdwr.448](https://doi.org/10.31468/cjsdwr.448).  
[^fickersclavert2021]: Fickers, A. and F. Clavert (2021)  “On pyramids, prisms, and scalable reading” ,  _Journal of Digital History_ , 1(1). Available at: [https://doi.org/10.1515/JDH-2021-1008?locatt=label:JDHFULL](https://doi.org/10.1515/JDH-2021-1008?locatt=label:JDHFULL).  
[^ketzan2021]: Ketzan, E. (2021)  _Thomas Pynchon and the digital humanities. Computational approaches to style_ . New York: Bloomsbury.  
[^krautter2023]: Krautter, B. (2023)  “The Scales of (Computational) Literary studies: Martin Mueller’s concept of scalable reading in theory and practice” ,  _Zoomland. Exploring Scale in Digital History and Humanities_ . F. Armaselu and A. Fickers (eds). Berlin–Boston: De Gruyter Oldenbourg, pp. 261-86. Available at: [https://doi.org/10.1515/9783111317779-011](https://doi.org/10.1515/9783111317779-011).  
[^giusjacke2022]: Gious, E. and J. Jacke (2022)  “Are computational literary studies structuralist?” ,  _Journal of Cultural Analytics_ , 7(4). Available at: [https://doi.org/10.22148/001c.46662](https://doi.org/10.22148/001c.46662).  
[^herrmann2017]: Herrmann, J.B. (2017)  “In a test bed with Kafka. Introducing a mixed-method approach to digital stylistics” ,  _DHQ_ , 11(4). Available at: [https://www.digitalhumanities.org/dhq/vol/11/4/000341/000341.html](/dhqwords/vol/11/4/000341/).  
[^hinrichs_etal2019]: Hinrichs, U. S. Forlini, and B. Moynihan (2019)  “In defense of sandcastles: Research thinking through visualization in digital humanities” ,  _Digital Scholarship in the Humanities_ , 34(1), pp. i80-i99. December. Available at: [https://doi.org/10.1093/llc/fqy051](https://doi.org/10.1093/llc/fqy051).  
[^lupi2017]: Lupi, G. (2017)  “Data humanism: The revolutionary future of data visualization” ,  _PrintMag_ . 30 January. Available at [https://www.printmag.com/article/data-humanism-future-of-data-visualization/](https://www.printmag.com/article/data-humanism-future-of-data-visualization/).  
[^manchia2020]: Manchia, V. (2020)  _Il discorso dei dati. Note semiotiche sulla visualizzazione delle informazioni_ . Milano: FrancoAngeli.  
[^mitkov2003]: Mitkov, R. (ed.) (2003)  _The oxford handbook of computational linguistics_ . Oxford: Oxford University Press.   
[^moretti1997]: Moretti, F. (1997)  _Atlante del romanzo europeo. 1800-1900_ . Torino: Einaudi.  
[^moretti2000]: Moretti, F. (2000)  “Conjectures on world literature” ,  _”, New Left Review_ , 1.  
[^moretti2013]: Moretti, F. (2013)  _Distant Reading_ . London-New York: Verso.  
[^morettisobchuk2020]: Moretti, F. and O. Sobchuk (2020)  “Vedere e non vedere. Sulla visualizzazione dei dati nelle discipline umanistiche” ,  _Ácoma_ , 18, pp. 125-51.  
[^moretti2022]: Moretti, F. (2022)  _Falso movimento. La svolta quantitativa nello studio della letteratura_ . Milano: nottetempo.  
[^mueller2012]: Mueller, M. (2012)  _Scalable reading_ . Available at: [https://sites.northwestern.edu/scalablereading/scalable-reading/](https://sites.northwestern.edu/scalablereading/scalable-reading/).  
[^parigini2024]: Parigini, M. (2024)  _Calvino nella nebbia. Dubitare, esitare, cancellare_ . Roma: Carocci.  
[^peraldo2016]: Peraldo, E. (2016)  _Literature and geography. The writing of space throughout history_ . Tyne: Cambridge Scholars Publishing.  
[^pianzola_etal2020]: Pianzola, F., S. Rebora, and G. Lauer (2020)  “Wattpad as a resource for literary studies. Quantitative and qualitative examples of the importance of digital social reading and readers’ comments in the margins” ,  _PLoS ONE_ , 15(1). Available at [https://doi.org/10.1371/journal.pone.0226708](https://doi.org/10.1371/journal.pone.0226708).  
[^piatti2008]: Piatti, B. (2008)  _Die Geographie der Literatur. Schauplätze, Handlungsräume, Raumphantasien_ . Göttingen: Wallstein.  
[^pierazzo2015]: Pierazzo, E. (2015)  _Digital scholarly editing: Theories, models and methods_ . Farham: Ashgate. [https://hal.archives-ouvertes.fr/hal-01182162/document](https://hal.archives-ouvertes.fr/hal-01182162/document).  
[^piper2020]: Piper, A. (2020)  “Do we know what we are doing?” ,  _Journal of Cultural Analytics_ , 5(1). Available at: [https://doi.org/10.22148/001c.11826](https://doi.org/10.22148/001c.11826).  
[^reuschelhurni2011]: Reuschel, A. and L. Hurni (2011)  “Mapping literature: Visualization of spatial uncertainty in fiction” ,  _The Cartographic Journal_ , 48(4), pp. 293-308.  
[^ries_etal2024]: Reis, T, K. van Dalen-Oskam, and F. Offert (2024)  “Reproducibility and explainability in digital humanities” ,  _Int J Digit Humanities_ . Available at: [https://doi.org/10.1007/s42803-023-00083-w](https://doi.org/10.1007/s42803-023-00083-w).  
[^rosen2011]: Rosen, J. (2011)  “Combining close and distant, or, the unity of genre analysis: A response to Matthew Wilkens’s  _Contemporary fiction by the numbers_ ” ,  _Post45_ . 3 December. Available at: [https://post45.org/2011/12/combining-close-and-distant-or-the-utility-of-genre-analysis-a-response-to-matthew-wilkenss-contemporary-fiction-by-the-numbers/](https://post45.org/2011/12/combining-close-and-distant-or-the-utility-of-genre-analysis-a-response-to-matthew-wilkenss-contemporary-fiction-by-the-numbers/).  
[^rubini2023]: Rubini, F. (2023)  _Italo Calvino nel mondo. Opere, lingue, paesi (1955-2020)_ . Roma: Carocci.  
[^serra1996]: Serra, F. (1996)  _Calvino e il pulviscolo del signor Palomar_ . Firenze: Le lettere.  
[^serra2006]: Serra, F. (2006)  _Calvino_ . Roma: Salerno.  
[^tally2013]: Tally, R.T. (2013)  _Spatiality_ . London: Routledge.  
[^vidalineresini2015]: Vidali, P. and F. Neresini (2015)  _Il valore dell’incertezza_ . Milano: Mimesis.  
[^underwood2017]: Underwood, T. (2017)  “A Genealogy of Distant Reading” ,  _DHQ_ , 11(2). Available at: [https://www.digitalhumanities.org/dhq/vol/11/2/000317/000317.html](/dhqwords/vol/11/2/000317/).  
[^weitin2017]: Weitin, T. (2017)  “Scalable reading” ,  _Zeitschrift für Literaturwissenschaft und Linguistik_ , 47(1), pp. 1-6.  
[^wilkens2011]: Wilkins, M. (2011)  “Contemporary fiction by the numbers” ,  _Post45_ . 11 March. Available at: [https://post45.org/2011/03/contemporary-fiction-by-the-numbers/](https://post45.org/2011/03/contemporary-fiction-by-the-numbers/).  
[^windhager_etal2019]: Winghager, F. et al (2019)  “Visualization of cultural heritage collection data: State of the art and future challenges” ,  _IEEE Transactions on Visualization and Computer Graphics_ , 25(6), 1 June, pp. 2311-2330. Available at: [https://ieeexplore.ieee.org/document/8352050](https://ieeexplore.ieee.org/document/8352050).  