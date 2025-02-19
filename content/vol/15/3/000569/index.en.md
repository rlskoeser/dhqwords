---
type: article
dhqtype: article
title: "LdoD Visual - A Visual Reader for Fernando Pessoa’s Book of Disquiet: An In-Out-In Metaphor"
date: 2021-10-15
article_id: "000569"
volume: 015
issue: 3
authors:
- José Raposo
- António Rito Silva
- Manuel Portela
translationType: original
categories:
- data visualization
- digital
- graphic design
- reading
tags:
- reading interface
- reading flow
- visualization
- hypermedia
- LdoD Archive
abstract: |
   There is an increasing use of information visualization techniques in Digital Humanities to support the analysis of literary works. On the other hand, the rise of digital reading on the web as well as the development of dedicated e-book readers has triggered a variety of hardware and software solutions to provide new reading environments and new material engagements with textual forms. In this paper, we propose a new metaphor, In-Out-In metaphor, to support the reading of literary works in a digital medium. Our model integrates information visualization techniques with plain text reading into the reading flow. This approach differs from the well-known dichotomy between close and distant reading because its emphasis is not on supporting the analysis of the texts being read, but on providing a smooth flow between focus and digression, which naturally occurs during a reading experience. We present a solution to read and explore the Book of Disquiet by Fernando Pessoa, an unfinished book composed of a set of modular texts that have been edited in different sequences and which can be read multi-sequentially. The research and design decisions for the visual reader of the Book of Disquiet are meant to provide an appealing, rich and interactive online reading experience through a web-based application, LdoD Visual. The implemented features apply information visualization techniques with an emphasis on exploring the modular nature of the book. Since this is a fragmentary literary work, its reading can be fragmentary as well, but providing a smooth multiple flow reading experience.
teaser: "This article presents a solution to read and explore the Book of Disquiet by Fernando Pessoa, an unfinished book composed of a set of modular texts that have been edited in different sequences and which can be read multi-sequentially."
order: 9
---
  
  

## 1. Introduction
  
The _ Book of Disquiet_  (LdoD, from  _Livro do Desassossego_ , in Portuguese) by Fernando Pessoa is a fragmentary literary work that was left unedited and unpublished by the author. In 1982, forty seven years after Pessoa’s death (1935), its first edition was published [^1] . Since then, three additional critical editions of the book have appeared, showcasing significant disparities of interpretation about how the book should be organized. Between 2012 and 2017, a team led by two co-authors of this article (Manuel Portela and António Rito Silva) created the  _LdoD Archive: A Collaborative Digital Archive of the Book of Disquiet_   [^portela2017a]. The  _LdoD Archive_  can be described as a hypermedia interactive engine that has realized the vision of an endlessly reconfigurable book. It is both a scholarly digital edition and meta-edition that enables users to compare each version of the  _Book of Disquiet_  with all of the versions encoded in the archive, and a virtual editing space designed with game-like principles for enabling different types of users (experts, students, general readers) to make their own editions and collections of the  _Book of Disquiet_ . The stated aim of this evolving archive is to experiment with computational forms of editing, reading, and writing in ways that go beyond the bibliographic imagination [^portela2015][^ritosilva2015][^portela2017b][^portela2019][^portela]. The  _LdoD Visual_  – a web application integrated into the  _LdoD Archive _ – explores the reading flow within this complex digital environment.
  
The modularity of  _The Book of Disquiet_  is, in fact, the contingent result of material and historical features that tend to reinforce each other: on one hand, each text is a self-contained unit that has no necessary narrative continuity with other texts; on the other hand, there is no defined ordering of the entire corpus of circa 600 pieces. Autograph textual units are also in various stages of revision: first draft manuscripts, typescripts with manuscript emendations, clean typescripts, twelve published texts. Pessoa only defined a few textual clusters, and even those suffered changes over time during the two stages of composition (1913-1920; 1928-1934). Given this contingent modular nature of the book, its fragments can be read regardless of any particular order, offering the opportunity for a fragmentary reading of the book, that is, a practice of reading that fosters divergent reading paths that can be built by the actual reader, instead of following a typical sequential reading that is bound to happen in a rigidly defined story sequence.
  
In the  _LdoD Visual_ , we used the particular structure and characteristics of the  _Book of Disquiet_  to explore, and smoothly integrate, two current research trends in Digital Humanities: information visualization techniques applied to texts, including the possibility of moving between close and distant reading scales [^janicke2015], with the design of web interfaces for accessing complex literary archives and the emergence of e-books as a reading medium [^koolen2012]. We propose a new reading metaphor, the In-Out-In metaphor, which integrates information visualization techniques with the plain reading of the text, to support the focus-digress flow that structures the embodied activity of the reader. By  _focus-digress flow_  we mean that during the focus stage the reader is in the story, while the digress stage corresponds to moments of self-consciousness of textual form, structure and navigation, as well as associative thought processes, both of which interrupt immersive reading.
  
We have designed and implemented a web-based application to read the  _LdoD_  whose main objective is to give the reader a sense of choice and an active role while reading and browsing through the book’s multiple textual fragments, in what should be a pleasurable and immersive user experience for both humanities researchers or just interested readers. The entire rationale of the  _LdoD Archive _ has been to offer a multi-layered access to the text, mediated through specific interfaces for each major function. Interfaces should be meaningfully navigated by interactors with very different levels of knowledge of the text – from the novice to the learner to the expert – and with distinct aims in mind, including leisure reading, study and analysis, advanced research, and literary creation [^portela2017b].
  
To achieve this goal at the level of the reading interface, we integrate a set of meta-information about the  _Book of Disquiet_  with information visualization techniques. Information visualization is a broad field that can be applied to a large domain of different areas, providing insight based on input data with different perspectives, summarizing relationships, identifying and comparing patterns, trends, outliers, finding correlations, among other tasks [^manovich2011]. In this project, visualization has been conceived as a humanistic interface for integrating different reading strategies and proving readers with a perception of reading as the traversal of a semiotic space that is both topological and semantic, and which is responsive to the readers’ agency [^drucker2014][^murray2012].
  
In order to integrate the existing meta-information with information visualization techniques we developed a tool, the  _LdoD Visual_ , which supports the exploration and pleasurable reading of the  _Book of Disquiet_ . The implemented solution provides new contributions for the reading and exploration of this work, in particular, and to the concept of reading flow in Digital Humanities, in general. This tool is built on top of the  _Collaborative Digital Archive of the Book of Disquiet_ , as mentioned. So the visual reader should be understood as a second-degree interactive representation – i.e., an additional interface – for providing a rewarding reading experience of a highly complex corpus of 600 texts. Its conception brings together a metaphoric model of the reading process, on one hand, and an algorithmic and graphical modelling of that process, on the other.
  
Besides describing the technical and graphical details of the  _LdoD Visual_  as a reading interface, this article makes three related claims. We argue that our computational model of reading interactions is adequate for representing the multiplicity of reading traversals inherent in the  _Book of Disquiet _ as a modular and open network of textual sequences. We also claim that our model of the reading flow as a recurrent process of immersion-emersion can be equated with the networked digital medium itself, insofar as the continuous focus on strings of text required for immersion can be smoothly integrated with the macrotextual logic of the visualizations facilitating textual overviews, hypertextual connections, and frame jumps. Finally, we argue that the ways for moving into, moving within, and moving out of the text provide a satisfactory balance involving two scales of textual representation that could be useful for other digital humanities projects of highly complex textual corpora. We believe the ergonomic solution embodied in our reading interface explicitly integrates close reading, hyper-reading, and machine reading [^hayles2012], and thus contributes to the design of new reading interfaces.
  
  
  

## 2. Related Work
  
In this section we present some background concepts regarding the  _LdoD Archive_ , Visualization in Digital Humanities, and Classification in Digital Humanities, the three conceptual and technical contexts in which this work was developed.
  
  
  

## 2.1. The LdoD Archive
  
The  _LdoD Archive_  provides every reader with the possibility of reading the  _Book of Disquiet _ according to _  _ four expert editions: the first critical edition, edited by Jacinto do Prado Coelho [^coelho1982], which was published in 1982, as well as three critical versions that have been edited by Teresa Sobral Cunha (1990-91 [2008] [^sobral2008]), Richard Zenith (1998 [2012] [^zenith2012]) and Jerónimo Pizarro (2010) [^pizarro2010]  [^2] [^3] . Each edition is composed of the total number of fragments and their relative order varies from edition to edition. In the LdoD Archive, the user can read each fragment while comparing its respective position across these expert editions, and they can also have access to additional information, which may also vary according to the edition, such as date and heteronym attribution.
  
In the  _LdoD Archive_ , users can also create their own virtual editions of the  _LdoD_  by selecting fragments from each of the 4 expert editions, sorting, annotating and tagging them. This virtual edition creation can be produced in a collaborative manner, in which case several users are involved, and users can play the roles of editors and managers of a virtual edition. The tagging of a fragment, which can apply to the fragment as a whole, or to just a segment of the fragment, is done by means of a set of categories that is associated with the virtual edition. This set of categories is designated as the virtual edition’s taxonomy.
  
Each fragment has different properties, such as its title, text, date and the edition and categories to which it belongs. There are many more features and possibilities that can be explored in the archive, such as additional reading tools, original documents, comparisons between textual transcriptions, fragment search, multiplayer classification games, and the writing of variations based on the existing fragments.
  
  
  

##  2.2. Literary Reading on the Web
  
Whereas hypertext structures in print books are generally subordinated to the sequential flow of textual strings on the page (they gravitate around the text, as table of contents, footnotes, references, etc.), hypertext structures in digital media alter the dynamics between self-contained and associative reading, as they can place any textual string in direct relation to a multiplicity of other texts, thus increasing the ratio of textual interruption. Links among disparate strings of text become much more frequent, and readers follow networks of association in interrupted and labyrinthine traversals. With the emergence of the World Wide Web as a hypermedia environment in the 1990s and early 2000s, the integration of verbal text into multimodal genres of communication continued to transform our media for symbolic production and exchange. More recently, mobile social media and the development of smartphones as multifunctional devices further extended this general transformation of digital literacy. 
  
Even if visionary engineers imagined the future interface of computational devices as a sort of augmented book (as is clear from Alan Kay’s 1972 Dynabook prototype), and even if current electronic tablets somehow attempt to emulate the ergonomics of the portable book, the electronic writing and reading space reconfigures and reforms the set of relations inherited from bibliographic structures. The redesign of information spaces of legacy print forms for the networked screens of programmable media has been a source of continuous reflection and engineering experimentation in many areas – from scholarly editing to commercial publishing to educational tools, particularly since the late 1990s. These transformations have also been studied extensively, from human-computer interaction to studies of literacy to cognitive science [^baron2015][^mangen2016][^mangen2019]. Studies seem to concur on the significance of changes to the ecology of reading practices, and on cognitive differences in terms of orientation and comprehension. Complex hypermedia literary archives, such as  _The William Blake Archive_   [^4]  (under development for almost three decades), have had to adapt to this changing ecology of the web. In those scholarly editing projects combination of search functions, navigation structure and reading interface has undergone several redesigns from highly hierarchical networks of links – typical of the early hypertext remediation of bibliographic structures – to current on-the-fly aggregations based on specific XML-encoding conventions. 
  
Interviewed by Werner Herzog, in  _Lo and Behold: Reveries of the Connected World_  (2016), Ted Nelson recalls a childhood episode when he was with his grandparents in a row boat, and, trailing his hand in the water, he notices the water flowing around his fingers in intricate patterns of connection. This epiphanic moment gives him awareness of the connectedness of everything which he associates to his future vision of hypertext as a powerful open-ended multidirectional changing system of relations among all texts and all media. Non-sequential hyperlinked literature as an evolving network of transclusions challenges reading practices based on linear forms of writing [^nelson1965][^nelson1995][^nelson2003]. Although not as flexible and unconstrained as imagined by Nelson, the current mediascape of reading was radically transformed by hypermedia and algorithmic textual production and analysis. Despite the early apology for the liberating, dynamic and heterarchical potential of hypertext by literary theorists and digital writers [^moulthrop1991][^bolter2001][^landow2006], research into hypertext software had always recognized the disorienting effect of link and node structures as both a design and cognitive problem [^theng1996][^theng1998], to which alternative representational and navigational forms, such as spatial hypertext, have been proposed [^marshall1995][^bernstein2011][^solis2011]. 
  
Almost three decades after the first literary experiments with hypermedia, Stuart Moulthrop and Dene Grigar ([2017](#moulthrop2017)) have asked four hypertext writers (Judy Malloy, John McDaid, Shelley Jackson, and William Bly) to revisit their early work of the late 1980s and 1990s in order to recover the writing, programming, and reading mechanics involved in their exploratory uses of specific machines and programs, including the emerging conventions of the hyperlink as a resource for poetic and narrative expression. Moulthrop and Grigar’s deep reading of the works of those authors engages the multilayered nature of digital textuality, including the ways in which hypertext and algorithmic processes affect our reading expectations of texts as holistic self-limited entities. The elusiveness of the textual whole is inherent in the intricate topologies created not just by hyper-reading as an unbounded and labyrinthine traversal, but also by the factorial virtualization of text as a responsive permutation of language bits.
  
Many of the same cognitive challenges of early digital genres continue to be addressed in the design of dedicated e-book readers and in current attempts to create a satisfactory balance between competing reading modes in digital media. Several analyses have been done on the hardware and software features for reading in electronic environments [^koolen2012] that highlight the differences between linear sequential reading and multicursal interactive reading, which are particularly relevant in the context of academic research or education. This tension between continuity and discontinuity pervades all solutions, in which there is a tradeoff between the smooth flow of reading and the possibility of analysis and inquiry about what is being read. If we think of Digital Humanities as the coming together of digitized artifacts, digitized methods for modelling and analyzing those artifacts, and digitized interfaces for representing those artifacts and those analyses, then the development of reading interfaces remains an important component in the invention of rhetorical conventions and modes of communication in networked programmable media.
  
  
  

## 2.2.1. Reading in the LdoD Archive
  
Prior to this work, the  _LdoD Archive_  provided two reading user interfaces: one that emphasizes [comparison](https://ldod.uc.pt/fragments/fragment/Fr080/inter/Fr080_WIT_ED_CRIT_Z) between editions and another that emphasizes the sequence of [reading](https://ldod.uc.pt/reading/fragment/Fr080/inter/Fr080_WIT_ED_CRIT_Z) (Figures 1 and 2). 
  
{{< figure src="resources/images/1000000000000556000003002653CBA78B05DB64.jpg" caption="Reading interface for comparing editions and transcriptions" alt="Screenshot of reading interface for comparing editions and transcriptions"  >}}

  
In the comparison user interface, it is possible to have a detailed highlighting of the differences between the authorial sources and the editorial transcriptions, and also across the editorial transcriptions themselves. It is also possible to annotate particular texts (or textual passages) with comments and tags when specific texts are used in the creation of a virtual edition.
  
The differences between transcriptions among the different expert editions, and authorial sources, are highlighted by placing the fragments side by side, and using colors to identify which parts differ. This user interface also allows the comparison of meta-information assigned by the expert editors, such as title, date of publication, heteronym attribution, page number, which can differ according to the edition. Additionally, this interface also allows users to compare the transcription with the original document sources, by presenting the documents’ facsimiles and providing a diplomatic transcription, which includes deletions, insertions and substitutions. 
  
On the other hand, and since the  _LdoD Archive_  also supports the definition of virtual editions, it is possible, through the comparison user interface, to compare the differences between the fragments, in terms of the assigned tags and annotations done. It is through the comparison interface that authenticated users can annotate and tag the fragments.
  
{{< figure src="resources/images/1000000000000556000003001D739255977409E3.jpg" caption="Reading interface for following multiple reading sequences." alt="Screenshot of multiple reading sequence interfaces"  >}}

  
Due to the focus of the comparison user interface on the analysis aspects, another user interface was defined, in order to provide a smother reading experience, although still emphasizing the comparison between the different sequences of reading the  _LdoD_ . This interface has a look and feel closer to the printed typography of the period the  _LdoD_  was written, and intends to provide reading sequences according to each one of the four expert editions. Besides, it provides a recommendation interface that suggests the next fragment to read, given the fragment being read and a set of criteria, such as, for instance, text similarity between fragments.
  
We could say that the reading interface for comparing editions is aimed at scholarly engagements with the text, whereas the reading interface for showing divergent reading sequences is meant for general readers. In the latter interface readers have the option of reading vertically within a particular sequence or horizontally across the entire corpus, thus redefining their textual traversal according to the multicursal logic of the medium which, in turn, is critically used to explore the modular structure of the work itself. On the other hand, the aim of the new visual reader is to abstract textual units and their meta-information and present them visually in ways that enhance movements within and across the text. The hypertextual and textual dynamics of the  _LdoD Visual _ embodies an ergonomic and cognitive model of the reading process in the design of the interactions.
  
  
  

## 2.3. Visualization in Digital Humanities
  
Jänicke et al. ([2015](#janicke2015), [2017](#janicke2017)) address visual text analysis in Digital Humanities and categorize each of these techniques as distant reading techniques, which aim to generate an abstract view of textual content, and as close reading techniques, which rely mainly on annotations and the use of different colors and underlining styles to lead to a deep comprehension and thorough interpretation of textual passages. They analyze how close and distant reading techniques can be combined in ways that could bridge these two perspectives so that the user can switch between close and distant reading. This is mainly achieved by side-by-side visualizations of the text being read and its meta-information, which make it possible to switch from a close reading of a particular fragment to some kind of overview associated with specific metadata. On the other hand, it is possible to access a particular text from the distant reading view where the text is represented because it has properties that are analyzed in that distant reading mode [^cheema2016]. This integration between close and distant reading is similar to our goal but our emphasis is on providing a reading experience, while the integration of close and distant reading is concerned with the analysis and understanding of the texts, such that close reading is frequently related with the annotation and generation of meta-information while the user is reading a text.
  
  
  

## 2.3.1. Visualization Techniques for LdoD
  
Given the specific characteristics of the  _LdoD_  we can analyze which visualization technique can be applied in its representation. These techniques belong to different areas and types of tasks, such as reading guidance, user navigation, global view, and exploratory analysis.
  
Reading guidance features consist of giving important information for the user regarding a specific fragment or even a collection or category of fragments, where the focus is on the fragment that is currently being read. User navigation features provide the user with an interface to navigate between different parts of the  _LdoD_ , in which the focus is on the relationship between the fragment being currently read and the remaining fragments of the book. Global view features have the objective of giving the user a summarized presentation or zoomed-out view of content from the  _LdoD_ , thus directing the focus to the edition that is being read. Exploratory analysis features present the user with information that is more focused on exploring relationships in the  _LdoD_  without necessarily converging to the task of reading.
  
Word clouds [^viegas2009][^mohammad2012][^heimerl2014] can be used to provide global views and reading guidance. Word clouds can be associated with the taxonomy categories of a virtual edition. After being presented with a word cloud of the available categories, and clicking on one of them, the user would be redirected to a list of fragments that corresponds to the selected category.
  
Also by exploring the categories associated with the virtual editions, it is possible to provide a global view of the edition, using colors to identify those fragments associated with a particular category. This feature would provide a global view of the fragments tagged with that category and the navigation to another fragment that is associated to the same category. This visualization technique, is, for instance, used in the Diggersdiaries web site [^vilaplana2017].
  
Besides the categories criterion, other criteria are supported by the  _LdoD Archive_ , such as text and heteronym, and they can be used to define a distance value between fragments. In this case, when reading a given fragment, the user could browse through similar fragments according to the selected criteria, and this relation can be visually represented using a network graph to show how close certain fragments are in relation to others. This would provide reading guidance. Alexander and Gleicher ([2016](#alexander2016)) make use of network graphs to visualize text similarity between different work by William Shakespeare.
  
By highlighting some of the fragments’ words according to their relevance in the context of the entire book it is possible to provide a guidance while reading a fragment. The weight of this highlighting could be made resorting to a metric like Term Frequency – Inverse Document Frequency (TF-IDF)[^5] . Text Skimming [^brath2014][^brath2015] is a technique used in knowledge maps and to support reading and it can also be applied in this context.
  
There are some differences between the experience of reading a book on a browser or other portable virtual book readers and the actual physical book. In an attempt to close this gap, it would be interesting to provide the user with a graphical representation that makes the awareness of where the actual reading fragment is placed in the current edition. This type of feature belongs to the global view area.
  
  
  

## 2.4. Text Classification
  
The visualization techniques are built on top of the information to be presented plus some meta-information. In the context of the  _LdoD Archive_ , the information is the fragment transcription and its position in an edition, and the meta-information is the date, heteronym and categories assigned to a fragment. Additionally, some meta-information is generated from the fragment through the TF-IDF associated with it, by considering each fragment as a document and the words in the fragment its set of terms.
  
  
  

## 2.4.1.Distance Measures in the  _LdoD Archive_ 
  
The  _LdoD Archive_  implements a set of measures to calculate the distance between two fragments belonging to the same edition according to four types of meta-information: date, heteronym, categories, and TF-IDF. The distance between two fragments is calculated using the cosine similarity [^singhal2001], according to which a vector is defined for each of the fragments to be compared.[^6] 
  
Associated with the heteronym, a vector of two cells is defined, one for each heteronym, Vicente Guedes and Bernardo Soares, in which the value 1.0 is assigned to the cell of the heteronym if the fragment is assigned by the editors to it. 
  
For the date, a vector is defined with the number of cells equal to 1934-1913+1, which corresponds to the period when the fragments were written. For the cell corresponding to the year when a fragment was written, the value 1.0 is assigned and for the other cells a decay of MAX(0.0, 1.0 - N x 0.1) is applied where N is the distance between the year associated with the cell and the closest cell with value 1.0.
  
For the text, the set of the first 100 TF-IDF terms associated with each one of the fragments that we intend to compare is calculated. Note that this set is between 100, in which the two fragments have the same first TF-IDF 100 terms, and 200, in which all terms are different. Then, for each fragment, a vector whose size equals the number of terms in the set is defined, and to the cell associated with a term the value 1.0 is assigned if the term belongs to the first 100 TF-IDF terms of the fragment, and 0.0 otherwise.
  
To calculate the distance between two fragments using the set of categories assigned to them a vector whose size is equal to the number of categories associated with the virtual edition taxonomy is defined. Then, for each fragment, its respective vector is filled with 1.0 for the cells corresponding to the categories the fragment has, and 0.0 for the other cells.
  
Note that the archive also uses a topic modelling algorithm, through the Mallet software[^7] , which allows the virtual editions to be automatically classified using the set of generated topics.
  
  
  

## 3. The In-Out-In Metaphor
  
Reading a book is a task in which the reader constantly switches between two states of focus. The reader is either completely engaged in the reading task or briefly disengages out of the act for various reasons. These moments of disengagement can be triggered, for example, by recalling what happened in previous chapters, picturing a description of a character or scenario, remembering a similar personal experience in relation to what has been read, linking a new event to what has happened in the past or even trying to make a prediction out of it, among other possibilities. Immersion can also be interrupted by the readers’ self- awareness of form, structure and navigation. The in-moment represents the state of being inside the textual world, absorbed by its signifying chain. The out-moment points to the liminal state of being outside the text, a liminality that is a function of the text itself and the ways in which it draws attention to its materiality or generates mental processes of association and reflection.
  
Part of our solution model revolves around this phenomenon, as it is intended to materialize and direct this constant in and out that happens while emerging out of and submerging into the source text. It is important to highlight that, in comparison to a typical book where we have a rigidly defined story sequence, the  _LdoD_  is a fragmentary literary work. This means that these moments of disengagement can turn into a chance for the user to reposition herself in another part of the book. This nuance leads to a reading path and global mental picture of the world created by the book that can greatly vary from reader to reader, opening up space for providing the user with an immersive experience in which she can have a sense of choice and an active role while reading the  _LdoD_ . If we consider that genre is an emergent property that results from specific arrangements of textual units, readers of the  _Book of Disquiet_  - mediated by this in-out-in visual reader – may even experience the oscillation between fictional autobiography and fragmentary narrative as an effect of their traversals. The emergence of a variable textual whole becomes a function of their reading acts. Self-contained textual units, when traversed as reading text, correspond to the in-movement, but when navigated as visual representations correspond to the out-movement. 
  
  
  

## 4. The LdoD Visual
  
The solution’s interface is composed of a group of different main menus: edition selection, reading, current user activity, new user activity, and reading history menus. Before describing each menu in detail, it is important to explain the concepts that will be used throughout this solution proposal.
  
  
  

## 4.1. Core Concepts
  
An  _information visualization technique_ , among other descriptions in previous sections, is a visual representation or metaphor that can provide insight and different perspectives about almost any type of input data, as we saw above from the multiple examples given in the related work applied to the context of the  _Book of Disquiet_ .
  
 _Semantic criteria_  is the set of attributes that can be encoded in the information visualization techniques in the context of the  _Book of Disquiet_ , namely word frequency, word relevance (TF-IDF), chronological order, heteronyms, fragment categories, and taxonomies. Text similarity is another semantic criterion that can be derived from word frequency and word relevance.
  
A  _user activity_  is an activity that can be selected by the user while reading a fragment from the  _Book of Disquiet_ , consisting of making use of an  _information visualization technique_  to encode different  _semantic criteria_ . An example of a user activity is  “Find similar fragments by text similarity”  to find fragments that are similar to the fragment that is currently being accessed, using a network graph as the information visualization technique that encodes text similarity - the semantic criterion that is chosen by the user while selecting the new user activity. To achieve an intuitive and easy-to-use solution, independently of the user activity's information visualization technique and encoded semantic criteria, the user selects a user activity by clicking on a button with a high-level description of what the user activity was designed to achieve, e.g.  “Find similar fragments by text similarity” . 
  
A  _reading flow_  is a sequence of accesses, done by a single user, such that the user progresses in the sequence of fragments through in-in, in-out-in and  _in-out-out-in_  subflows. An  _in-in_  subflow corresponds to a situation when the user is accessing a fragment and accesses another fragment, for instance, by switching to the previous page. This switch is done according to the  _semantic criteria_  the user chose for accessing the fragment, defined by the current user activity. For instance, if the semantic criteria correspond to the set of fragments of a given category, the reader will access another fragment belonging to the same category. An  _in-out-in_  subflow corresponds to a situation in which the user is accessing a fragment, moves to the current user activity menu (to be described in the next subsections) in which the reader has a complete view of the fragments according to the same semantic criteria used to access the fragment being read. For instance, if we consider the previous example, the complete view may show all fragments that have the same category in the context of all fragments. An  _in-out-out-in_  subflow corresponds to a situation when the reader stops reading, according to the current user activity, and chooses a new user activity in which she continues to read.
  
Overall, the reading flow corresponds to the implementation of the  _in-out_  metaphor, where the level of disruption is minimal in  _in-in_  subflows, and maximal in  _in-out-out-in_  subflows. Note that to reduce the disruption of the reading flow, all changes can be done using shortcuts, pressing a single key, and most menu elements fade-out in the reading interface when the reader does not use the mouse so that the screen only contains the text of the fragment.
  
  
  

## 4.2. User Interface Structure: Menus and Navigation
  
In the context of an edition, the  _LdoD Visual_  has three main types of elements: selection menus, reading view, and global views.
  
  
  

## 4.2.1. User Activity Selection Menu
  
Once a context of an edition and one of its fragments is chosen, the main selection menu allows users to choose between the available user activities, given the context, and access the corresponding global view. The user activities are ordered by semantic criteria: edition order, chronological order, text similarity, categories/taxonomy, and heteronym.
  
{{< figure src="resources/images/10000201000005C60000037B3D7ACA0444175D0B.png" caption="User activities that can be chosen in the context of a specific fragment, for an edition that does not assign heteronyms to the fragments (the last user activity is not available)." alt="Image of the user activities that can be chosen"  >}}

  
As shown in Figure 3, each user activity is represented by a card with a title, a button with the corresponding keyboard shortcut between straight parentheses that will take the user to the activity, and an image that represents the information visualization technique for that user activity, which can also be clicked to access the user activity. 
  
The image and button will be greyed out if the activity is unavailable - for example, if the currently selected edition has no taxonomy, user activities that use this semantic criteria category will not be available, displaying a message explaining why it is not available in the title and its selection button is also unavailable.
  
The same semantic criteria can be used with different information visualization techniques. In Figure 3, we can observe that the top 2nd and bottom 1st cards use different information visualization techniques for chronological order, respectively, custom square map and timeline; the top 3rd, bottom 3rd and 4th cards use the semantic criteria associated with the taxonomies, where top and bottom 3rd use the same information visualization technique, word cloud, the former in the context of the selected edition, and the latter in the context of the selected fragment; while the bottom 4th uses a different visualization technique, network graph.
  
  
  

## 4.2.2. Reading View
  
In this view, the focus is on reading the text of a selected fragment, as represented in Figure 4, where the fragment title and text are presented with a reading progress bar. Since the text will be read on a screen, the used text font is a sans serif font. The fragment title font and text font are the same ones used in one of the  _LdoD Archive_  reading interfaces.
  
{{< figure src="resources/images/100002010000066D000003B75D76B5B68D7432C1.png" caption="Plain reading view of a fragment, in which it is possible to navigate to the next and previous fragments using the keyboard arrow keys and in which there is a progress reading bar at the bottom." alt="Plain reading view of a fragment"  >}}

  
Besides the progress reading bar, the reading view features some elements of established browser book readers (see Figure 5). There are previous/next fragment arrow buttons that retreat/advance through the selected edition fragments depending on the currently selected edition. It also allows users to navigate between fragments according to the user selected category or heteronym, using the yellow arrows. There are some detail features, such as smooth animation between fragment change and smooth page scroll back to the top for the same matter. This smooth page scroll can also be triggered by clicking on its matching button or pressing  “T”  on the keyboard.
  
{{< figure src="resources/images/1000020100000674000003B972242A6D5F16EDF6.png" caption="Reading view of a fragment, in which the menu is visible, the most relevant words are highlighted, and it is possible to navigate to the next/previous fragment in the edition, using the black arrows, and to the next/previous fragment according to the selected user category or heteronym, using the yellow arrows." alt="Menu for the plain reading view"  >}}

  
When the user stays inactive for more than 3 seconds, everything in this menu disappears with the exception of the reading progress bar and the fragment's title and text, as shown in Figure 4. Inactivity is timed when the user is not interacting with any button, progress bar or previous/next fragment arrow buttons. It is then possible to trigger everything to appear again by doing a mouse hover on any of these elements of the menu. When the user scrolls down the page and the top buttons overlap the text, there is also a transparency trigger. These features are activated as an effort to maximize the user focus on reading the text and are another extra step towards achieving our metaphor implementation. 
  
In this menu, there is a user activity "under the hood" in the sense that it resembles a user activity that does not break the reading flow: by clicking on the matching button ( “Highlight the most relevant words” ), left button on top (shortcut [R]), the 4 most relevant words are highlighted in blue, as presented in Figure 5. This number was decided after extensive experimentation and fine tuning, trying to find a balance between actual relevant content highlighting and not highlighting too many words to the point it becomes irrelevant to do so. This option makes use of an information visualization technique - text skimming - to encode a semantic criterion - word relevance (more specifically, TF-IDF) -, even though it is not described as a user activity in the sense that it can be applied independently of what is the current user’s activity.
  
The reader can also see his/her own history of reading by pressing the button on the right in the group of three buttons on top (shortcut [H]), as presented in Figure 6.
  
{{< figure src="resources/images/10000201000005C900000318036756AD90ADF665.png" caption="Reading history view of an edition in which the reader as accessed one fragment (De resto eu não sonho) in the context of a different type of user activity." alt="Image of the reading history view for one fragment"  >}}

  
In this view, the reader is presented with an interactive timeline that displays the fragments that have been read for the currently selected edition. Each history entry is a fragment, displaying its title and a thumbnail that represents the information visualization technique of the user activity through which that fragment was reached. Besides, having a similar interaction to the user activity that makes use of the timeline in the global view, the user can navigate back to a given fragment that was previously read by clicking on its entry.
  
The buttons on top right, Figure 5, allow the user to see the instructions for this menu and select another edition. The two first buttons in the group of three buttons allow the user to access the global view associated with the currently selected user activity (shortcut [A]) and to navigate to the new user activity selection menu (shortcut [N]).
  
  
  

## 4.2.3. Global Views
  
The global views correspond to the  _out_  phase of the metaphor and are a combination of semantic criteria with an information visualization technique. In the following subsections we show how the global views are presented in the  _LdoD Visual_  in the context of the various information visualization techniques.
  
  
  

## 4.2.3.1. Network Graph
  
This information visualization technique consists of a network graph with hidden edges, as shown in Figure 7. Each node is a circle that represents a fragment from the currently selected edition. If the user clicks on a circle, she will be taken back to the  _Reading Menu_  with the corresponding fragment of that circle open to be read.
  
When accessing the view, the central orange circle represents the fragment in whose context the user activity was started, and the purple circle represents the fragment being currently read. This strategy was adopted so that the reading occurring during a user activity is contextualized by the initially read fragment. The blue circles represent the other fragments from the edition, and their relative distance to the central circle expresses the encoded semantic criterion.
  

{{< figure src="resources/images/1000020100000503000002776DF5C2E32C219EC2.png" caption="Global View using a Network Graph for the semantic criteria of text similarity. The closest circle will always be in the same position, be it 5% or 100% similar, to allow a sparser representation, note that, for instance, when considering text similarity, the most similar fragments are less than 20% similar. Color encodes the similarity in percentage. There is a blue color range - a 100% similar fragment will have its corresponding circle colored in light blue, while a 0% similar fragment will have its corresponding circle colored in dark blue." alt="Image of a global view using a network graph"  >}}


  
The user can put the mouse cursor over the circle so that a label is displayed, showcasing the title and the value of similarity in percentage. Besides being able to drag and zoom the network graph using the mouse pointer and mouse wheel, the user can also use the green navigation buttons to drag, re-size, zoom in and out of the network graph. This information visualization technique is used to encode similarity by text and taxonomy, which in the case of Figure 7 is by text.
  
  
  

## 4.2.3.2. Word Cloud
  
Word clouds are used to encode semantic criteria associated with the categories of a certain fragment or taxonomy (group of categories) of the selected edition, as shown in Figure 8. It displays each category using different colors and the font size varies according to the number of fragments that belong to that category.
  
{{< figure src="resources/images/10000201000004FC000002DF3C42AAEF57C28901.png" caption="Global view using a Word Cloud for the categories of the taxonomy of the selected edition." alt="Global view using a Word Cloud"  >}}

  
The Word Cloud, and its semantic criteria, can be applied in two cases: (1) the set of categories of the taxonomy of an edition, which corresponds to the case presented in Figure 8; (2) the categories of the current fragment. In both cases, by selecting one of the categories, the user is redirected to a custom squares map that highlights the fragments of the select category, as described in the next subsection.
  
Heimerl et al. ([2014](#heimerl2014)) developed a system that uses word clouds as its central visualization method for interactive text analysis. Its results showed that even though word clouds are aesthetically pleasing with its words disposed in different angles, users do not find them very functional and easy to use. Thus, results showed that participants preferred sequential layouts, where words are placed horizontally without any kind of inclination or angles for aesthetic purposes. For this reason, we decided to follow the same layout in the  _LdoD Visual_ .
  
  
  

## 4.2.3.3. Custom Squares Map
  
This information visualization technique consists of squares linked by arrows, as shown in Figure 9. It is similar to the network graph if we picture the squares as nodes and the arrows as edges. Likewise, each square represents a fragment from the currently selected edition. This group of squares linked by arrows offers a global view of the currently selected edition, and suggests a certain order derived from the arrows. This order depends on the encoded criterion. Each square's color and highlighting also depends on the encoded criterion. Similarly to network graphs, there is a special color highlighting for each square. The orange square corresponds to the fragment where the user activity was initiated, and the purple square to the fragment currently being read.
  
{{< figure src="resources/images/10000201000004EE000003058A27A095E1AB30D6.png" caption="Global View using a Custom Square Map to show the fragments associated with the category “Quotidiano da Cidade” in the context of the edition fragments." alt="Global view using a Custom Square Map"  >}}

  
This information visualization technique is used to encode the following semantic criteria:
  
  
 *  _Edition order._  Fragment squares are sorted by order of the currently selected edition. If the user places the mouse cursor over a square, it will display a label with the fragment title and its position in the edition, almost as if it were a page number. This global view allows users to explore the order of the fragments in the edition.  
 *  _Chronological order._  Fragment squares are sorted by the date in which they were written. Each square displays a two-digit number that represents the year from that date - for example, a fragment from 1927 will have its corresponding square with the number 27. Fragments without date have their corresponding squares greyed out. If the user places the mouse cursor over a square, a label will be displayed containing the fragment title and its date. This global view allows users to explore the edition ordered by date.  
 *  _Categories/taxonomy._  Fragments are displayed exactly as if the semantic criterion was the edition's order, with the addition of highlighting in yellow the squares of the fragments from the selected category. If the user places the mouse cursor over a square, a label will be displayed with the fragment title and the categories to which it belongs, as shown in Figure 9. As previously described, smaller yellow previous/next fragment arrow buttons will appear under the black previous/next buttons in the reading menu.  
 *  _Heteronym._  It has the same behaviour as the categories/taxonomy semantic criteria, but it highlights in yellow the squares of the fragments that were assigned to a specific heteronym. The yellow arrow buttons are used to move exclusively to the previous/next fragment belonging to the selected heteronym. The global view allows users to explore the fragments assigned to a particular heteronym.  

  
  
  

## 4.2.3.4. Timeline
  
This information visualization technique consists of an interactive timeline, in which the user is presented with the timeline centered on the time window around the currently selected fragment, as shown in Figure 10.
  
{{< figure src="resources/images/10000201000005080000029E86AA3A13A338ED8E.png" caption="Global View using a Timeline to represent the chronological order assigned to the fragments." alt="Global View using a Timeline"  >}}

  
There is only one global view that uses this information visualization technique to encode the chronological order as the semantic criterion, in order to explore the fragments around the date of the current fragment. Each timeline entry represents a fragment from the currently selected edition. Being consistent with the color scheme for other visualizations, an entry will be orange if it represents the fragment that was initially selected in the context of the user activity, and purple if it is the fragment currently being read. The user can navigate to a certain fragment by clicking on its entry.
  
  
  

## 5. Results and Discussion
  
The evaluation of the  _LdoD Visual_  was done by two types of tests: usability tests, which assess the system’s usability, independently of the its particular purpose; and, utility tests, which assess the quality of the system, considering its purpose as a reading tool for the  _Book of Disquiet_ .
  
  
  

## 5.1. Usability Tests
  
To assess how usable, efficient and satisfying the interaction with the  _LdoD Visual_  is, we have performed tests with 11 volunteer users who have no expert knowledge on the  _LdoD Archive_  and on the  _Book of Disquiet_ . The results of this type of test are objective and quantitative.
  
Each usability test consisted of 4 stages:
  
  
 * Introduce the user to the  _LdoD Visual_ 's concepts and briefly demonstrate the system in about 5 minutes;  
 * Let the user explore the system freely for about 5 minutes;  
 * Ask the user to execute 10 tasks;  
 * Ask the user to fill and submit a SUS (system usability scale) questionnaire.  

  
In the third stage, for each task, we counted the number of errors and time taken to complete the task. The tasks assess the usability and intuition of the user activities' interaction with the information visualization techniques in order to explore and navigate through the fragments from the selected editions. For instance, to select any fragment from an edition, select the user activity that makes use of the squares map encoding the edition's order, choose the first fragment, highlight the most relevant words and say out loud what are the most relevant words of the selected fragment, which was, actually, task 9.
  
These tasks were always executed in the same order for each user, exactly from the same menus.
  
{{< figure src="resources/images/10000201000003FF00000122CCE88557A61A9DA0.png" caption="Table 1 - Time to perform each task in seconds and respective number of errors." alt="Table of time needed to perform each task"  >}}

  
Figure 11 presents the results from which we conclude that, on average, every task was completed without exceeding the expected time and with basically no errors, with the exception of the last task, which was more difficult. Task 10 was conceived to confirm if users understood why a user activity was not available for certain fragments and what they should do in order to select other fragments that supported that previously unavailable user activity. This was the most complex task, which explains why it took the most time out of all tasks, even though most users ended up figuring out what they had to do.
  
For the fourth stage, the users filled and submitted a SUS (system usability scale) questionnaire. This is a quick questionnaire that is commonly used to figure out if any aspect was not considered by the tests. This questionnaire involved 10 statements for the user to answer how much he would agree with each one of them in a scale from 1 (completely disagree) to 5 (completely agree):
  
  
 * I think I would like to use the  _LdoD Visual_  regularly.  
 * I think the  _LdoD Visual_  was unnecessarily complex.  
 * I think the  _LdoD Visual_  was easy to use.  
 * I think I would need help from a person with technical knowledge to use the  _LdoD Visual_ .  
 * I think that all of the  _LdoD Visual_  features were well integrated.  
 * I think the  _LdoD Visual_  shows a lot of inconsistency.  
 * I think people will learn how to use the  _LdoD Visual_  easily.  
 * I think the  _LdoD Visual_  was very confusing to use.  
 * I felt confident while using the  _LdoD Visual_   
 * I needed to learn a lot of new things before I could use  _LdoD Visual_ .  

  
The score of the SUS questionnaire is obtained by transforming the 1 to 5 scale in a 0 to 4 scale, and converting the values to be consistent, e.g., the odd-number questions express a positive opinion and even-number questions express a negative opinion. Figure 12 presents the results, where the questions' answer values are as given by the subjects, and the sums, averages and SUS final scores are calculated on the converted values.
  
{{< figure src="resources/images/10000201000002290000013AA327983CA0B35C00.png" caption="Table 2 - SUS (system usability scale) questionnaire results" alt="Table of system usability scale questionnaire results"  >}}

  
Analyzing the SUS score, we can observe that the lowest scoring answer is number 4,  _I think I would need help from a person with technical knowledge to use LdoD Visual_ . This makes sense as the  _LdoD Visual_  is relatively complex to users that have no experience with the  _Book of Disquiet_  and the  _LdoD Archive_ , which is the case of the participants. Regarding the final score, when a system scores a SUS score of 80.3 or more, it is considered to be in the top 10% of scores and the testing users are more likely to recommend it to others. This means that if we are considering a SUS scale, the  _LdoD Visual_  is a system with good usability, having a SUS score of 88.41.
  
Besides these 10 SUS questions, we also added questions in order to know about the users. In terms of the characterization of the usability test participants: 9.1% where younger than 18, 36.4% between 18-24, 45.5% between 25-34, and 9.1% between 45-54; and 9,1% have secondary education, 45.5% have a bachelor degree, and 45.5% a master degree. Most users had already used other software to read books in the past and most users had not read the  _Book of Disquiet_ . It is also possible to observe that most users strongly agreed that they would have a good reading experience using the  _LdoD Visual_ .
  
  
  

## 5.2. Utility Tests
  
The purpose of the utility tests is to obtain information about the utility and quality of the experience while using the system. These tests are important in the sense they allow us to assess subjective and qualitative aspects of the  _LdoD Visual_ , which are difficult to be measured quantitatively.
  
The tests were done with 3 users that have expert knowledge about the  _Book of Disquiet_  and the  _LdoD Archive_ . The user of the first case study is a postdoctoral researcher with a PhD thesis on the  _Book of Disquiet_ . This user has also worked, between 2012 and 2015, with the XML encoding of the fragments for the  _LdoD Archive_ . The user of the second case study is a PhD student from the PhD Program in Materialities of Literature, which is a doctoral program that addresses the material and technological mediations of literary practices. One of its research fields is digital humanities. This user has a BA and an MA in graphic design. The user of the third case study is another PhD student from the same PhD Program, who has a BA in graphic design, and an MA in Semiotics. This user is interested in the aspects of usability of the  _LdoD Archive_  since her PhD project involves creative practices through the situated use of the archive. She is one of  _LdoD Archive_ 's most regular users and has been organizing a plan of activities to teach  _LdoD Archive_ 's users how to use it and fully explore its various functionalities, including the creation of virtual editions.
  
The protocol for this type of testing is more flexible in comparison to the usability tests' protocol. The users were contacted by email, introduced to the  _LdoD Visual_  metaphor, and encouraged to explore the system before we had our actual meeting to do the case study.
  
During the case study the users were encouraged to use the  _LdoD Visual_  while  “thinking out loud” . We asked them several questions regarding the real utility, potential and reading experience that they thought the  _LdoD Visual_  provides. We also asked them about the differences they felt as more important, in comparison to other tools and electronic readers available, as well as comparing the reading experience of the  _LdoD Visual_  to the other reading features available in the  _LdoD Archive_ .
  
Considering the feedback received from these case studies, we can conclude that the reception of the  _LdoD Visual_  is positive, both in terms of concept, execution and utility. The users liked the approach on how to read a book. They thought that it is a good match for the fragmentary nature of the  _Book of Disquiet_ . The attempt to output a visual representation of the editions and fragments brings a new perspective on how to read and explore the  _Book of Disquiet _ and use the  _LdoD Archive_ , highlighting its relevance for the field of digital humanities.
  
The second user also described her experience with user activities in a way that suggested that the  _LdoD Visual_ 's metaphor is successfully implemented. She stated:  “The real reading customization strength comes from the activities around the currently selected fragment. If the reader stops and tries, for example, to continue her reading path with a user activity that is related with reading similar fragments by text to the currently selected fragment, there is already a reflexive question that is specific to the reader and the navigation method centered around the selected fragment becomes the medium for the user to be able to read around an idea that is interesting to her. In  _LdoD Visual_ , the reader is able to navigate through the fragments according to what is desired, having a visual reference of the type of navigation and exploration that is being performed in the  _Book of Disquiet_ .” 
  
The users also suggested that the  _LdoD Visual_  is relatively complex and that there should exist more ways of welcoming non-expert users who are not aware of the problem and structure of the  _Book of Disquiet_  and the the  _LdoD Archive_ , such as "selling the concept" both as a ludic and research tool, and showcasing the different uses and possibilities in videos scattered around the application. The users also acknowledged the potential of the  _LdoD Visual_  concepts such that they could be developed and expanded to explore other alternatives of interaction with the  _Book of Disquiet_ . We could observe that each user spent time with different parts and user activities of the  _LdoD Visual_ . Our analysis on this is that the  _LdoD Visual_  seems to provide different affordances for different users, and that the objective of customizing the exploration and reading experience of the _Book of Disquiet_  was met.
  
We can also conclude that the  _LdoD Visual_  is a tool that mainly scripts two different reading behaviours: the possibility of navigating through the  _Book of Disquiet_  with a focus on the pleasurable assisted user-driven reading experience, geared towards a continuous and immersive flow; and the possibility of navigating with a humanities researcher mindset, finding patterns, correlations and textual data insights, according to a discontinuous and interruptive logic. Both of these reading practices are possible resorting to the same mechanisms and representational strategies, i.e., the user activities' information visualization techniques, even though the first type of reading practice is the main focus of the  _LdoD Visual_ .
  
  
  

## 6. Conclusion
  
The  _Book of Disquiet_  by Fernando Pessoa is an unfinished book that can be read in any order. The modular nature of this fragmentary literary work brings endless possibilities on how it can be traversed.The goal of this work was to design and implement a web-based application to read  _The Book of Disquiet_ , giving the reader an active role while reading and browsing through the book's different fragments, defining user activities that make use of information visualization techniques to encode different semantic criteria.
  
In order to achieve this, we researched on the use of information visualization techniques applied to textual data and literature, and on the concept and tools for e-books and web-based reading. Afterwards, we defined the  _in-out-in_  metaphor that was used as the guiding concept for whether or not a certain architecture or feature choice met the objectives and served the overall purpose of this work.
  
According to this metaphor, we defined the user activity concept, which establishes a perspective on how to read the book. A user activity is a combination of an information visualization technique with a semantic criterion, where the latter is used to classify the fragments and the former to visualize them according to the classification. The solution architecture considers three types of user interfaces: a user interface in which the user activity is selected; a global view in which the fragments are visualized according to the chosen user activity; and a reading view to support the reading and navigation between fragments, according to the chosen semantic criteria.
  
The final system was tested for usability and utility, and it got positive feedback from both non-expert and expert users of the  _Book of Disquiet _ and the  _LdoD Archive_ . The usability tests have shown that it is possible to complete the defined tasks in the expected time and without errors, and the utility tests also confirmed that the proposed metaphor meets the experts’ vision of the book and how to explore its multiple paths of reading.
  
As a web-based application for exploring the process of reading, the  _LdoD Visual_  contains several features that correspond to what the  _LdoD Archive_  describes as  “the simulation principle,”  that is, the ability to provide interactors with a reflexive engagement with the textual environment [^portela2020]. Through a recursive process of going into the text and coming out of the text, readers are able to explore the  _Book of Disquiet_  as a particular kind of reading experience and they are also able to see how their acts of engaging with the text become registered in the visualizations. The implemented visualization techniques thus bring together the modularization of the text and the modularization of the reading of the text.
  
The  _LdoD Visual_  is a tool that has the potential to grow and become an improved version of what it already accomplishes. One major improvement would be the possibility of saving the reading history state to a user account, preferably in the  _LdoD Archive_ . This would be a logical extension since the process of reading a book can take days, weeks or months. Another improvement would be developing a feature to generate new virtual editions according to specific reading paths. This would explore the  _LdoD Archive_  goal of fostering the construction of new virtual editions of the  _Book of Disquiet_ . In its reflexive graphical representation of reading activities, this visual reader contributes to the experimental textual rationale of the  _LdoD Archive_ .
  
We believe the In-Out-In metaphor adopted in this project can also be used as a conceptual design tool for modelling reading processes in digital media. The design of interfaces for complex archives of literary materials based on this model would have twofold benefits: limiting hypertextual disorientation, on one hand, and supporting a meaningful transition between human and machine reading processes, on the other, for both general and expert readers. In this light, the model of the reading flow embodied in the  _LdoD Visual_  could also be seen as a prototype of a specifically digital paratextual apparatus for the smooth and optimal integration of close reading and distant reading modes through multiple visualization techniques. 
  
NOTE: In order to keep track of the project’s evolution, the source code is publicly available in a GitHub repository [https://github.com/socialsoftware/edition](https://github.com/socialsoftware/edition).
  
 **Acknowledgements** 
  
The authors wish to thank the anonymous reviewers of this article for their invaluable comments and suggestions.
  
This work was supported by national funds through FCT, Fundação para a Ciência e a Tecnologia, under projects UIDB/50021/2020 and UIDB/00759/2020.
  
  
[^1]: Pessoa’s c. 28,000 unpublished papers remained in the possession of his family until the late 1970s when they were acquired by the National Library of Portugal. After this, the systematic cataloguing, editing, and publication of his works became possible. Although several books had been in circulation between the 1940s and the 1970s, namely those including the poetry of his major heteronyms (Alberto Caeiro, Álvaro de Campos, and Ricardo Reis), it was only in the 1980s that the critical editing of his manuscripts, typescripts, and published works started. The  _Book of Disquiet_  was published in two volumes in 1982. The Critical Edition of the Works of Fernando Pessoa, launched in 1984 by the Imprensa Nacional-Casa da Moeda (general editor, Ivo Castro), is still in progress. Twenty-two volumes have been published since then.
[^2]: The dates between brackets correspond to the editions used in the archive, while the first date corresponds to the date of the first edition.
[^3]: The  _LdoD Archive_  has transcribed what was the latest version of each critical edition when the encoding started in 2012. Since then slightly updated and revised editions by Cunha, Zenith and Pizarro have been published. The project benefited from the support and collaboration of the editors. The copyright notice in the archive reads:  “All items in the LdoD Archive may be shared in accordance with the Creative Commons  “Attribution-NonCommercial 4.0 International”  license (CC BY-NC 4.0). This license does not extend to the four experts’ editions (Prado Coelho-1982; Sobral Cunha-2008; Zenith-2012; and Pizarro-2010), which can only be used within the LdoD Archive infrastructure. Their redistribution or republication on other terms, in any medium, requires express written consent from the editors or their legal representatives.”   [https://ldod.uc.pt/about/copyright](https://ldod.uc.pt/about/copyright)
[^4]:  The editors of  _The William Blake Archive_    _ have_  redesigned its graphical user interface in December 2016, distinguishing between a Gallery Mode and a Reading Mode. This structure reflects both the pictorial and literary character of Blake’s work and the intermedia nature of digital environments as a remediation of multiple analogue materialities. It also highlights the deep modularization of Blake’s work that resulted from establishing the planographic digital facsimile of the printed page as its universal unit of representation. Because of their hypermedia complexity, digital archives of this type remain a challenge for all types of reader. Cf. [http://www.blakearchive.org/](http://www.blakearchive.org/)
[^5]:    “In information retrieval, tf–idf or TFIDF, short for term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus. It is often used as a weighting factor in searches of information retrieval, text mining, and user modeling. The tf–idf value increases proportionally to the number of times a word appears in the document and is offset by the number of documents in the corpus that contain the word, which helps to adjust for the fact that some words appear more frequently in general.”    _Wikipedia_ , accessed 17 November 2020.[https://en.wikipedia.org/wiki/Tf-idf](https://en.wikipedia.org/wiki/Tf-idf)
[^6]:    “Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space. It is defined to equal the cosine of the angle between them, which is also the same as the inner product of the same vectors normalized to both have length 1. The cosine of 0° is 1, and it is less than 1 for any angle in the interval [0, π] radians. It is thus a judgment of orientation and not magnitude: two vectors with the same orientation have a cosine similarity of 1, two vectors oriented at 90° relative to each other have a similarity of 0, and two vectors diametrically opposed have a similarity of -1, independent of their magnitude. The cosine similarity is particularly used in positive space, where the outcome is neatly bounded in [0,1].” , accessed 17 November 2020. [https://en.wikipedia.org/wiki/Cosine_similarity](https://en.wikipedia.org/wiki/Cosine_similarity)
[^7]:  MALLET is the acronym for  “MAchine Learning for LanguagE Toolkit” , developed at the University of Massachusetts Amherst:  “MALLET is a Java-based package for statistical natural language processing, document classification, clustering, topic modeling, information extraction, and other machine learning applications to text.” [http://mallet.cs.umass.edu](http://mallet.cs.umass.edu) In the  _LdoD Archive_  we have used MALLET’s topic modelling toolkit, which contains implementations of Latent Dirichlet Allocation (LDA), Pachinko Allocation, and Hierarchical LDA. One of our virtual editions of the  _Book of Disquiet_  ( “LdoD Mallet” ) was automatically generated by MALLET’s topic modelling software. Cf. [https://ldod.uc.pt/edition/acronym/LdoD-Mallet](https://ldod.uc.pt/edition/acronym/LdoD-Mallet)  
[^alexander2016]: Alexander, Eric, and Michael Gleicher (2016).  “Task-driven comparison of topic models. IEEE Transactions on Visualization and Computer Graphics.”  22(1), 320–329.  
[^baron2015]: Baron, Naomi (2015).  _Words Onscreen: The Fate of Reading in a Digital World. _ Oxford: Oxford University Press.  
[^bernstein2011]: Bernstein, Mark (2011).  “Can We Talk about Spatial Hypertext?”    _HT '11: Proceedings of the 22nd ACM conference on Hypertext and hypermedia_ , June 2011, 103–112. https://doi.org/10.1145/1995966.1995983  
[^bolter2001]: Bolter, Jay David (2001).  _Writing Space: The Computer, Hypertext, and the History of Writing._  London: Routledge [2nd ed.].  
[^brath2014]: Brath, Richard, and Ebad Banissi (2014).  “Using font attributes in knowledge maps and information retrieval.”    _Proceedings of the First Workshop on Knowledge Maps and Information Retrieval _ (KMIR 2014) _co-located with International Conference on Digital Libraries_  (DL 2014), 23–30.  
[^brath2015]: Brath, Richard, and Ebad Banissi (2015).  “Using text in visualizations for micro/macro readings.”  4th Workshop on Visual Text Analytics. ACM, 2015.  
[^cheema2016]: Cheema, Muhammad Faisal, Stefan Jänicke, Gerik Scheuermann (2016).  “AnnotateVis: Combining Traditional Close Reading with Visual Text Analysis.”  Workshop on Visualization for the Digital Humanities, IEEE VIS 2016, Baltimore, Maryland, USA, October 24th, 2016. URL: http://www.informatik.uni-leipzig.de/~stjaenicke/annotatevis.pdf  
[^coelho1982]: Coelho, Jacinto do Prado, ed. 1982. Fernando Pessoa,  _Livro do Desassossego por Bernardo Soares_ . Collection and transcription by Maria Aliete Galhoz and Teresa Sobral Cunha. Lisboa: Ática, 1982. 2 vols.  
[^drucker2014]: Drucker, Johanna (2014).  _Graphesis: Visual Forms of Knowledge Production_ , Cambridge, MA: Harvard University Press.  
[^eaves2020]: Eaves, Morris, Robert N. Essick, and Joseph Viscomi, eds. (1996-2021).  _The William Blake Archive._  Chapel Hill, NC: University of North Carolina at Chapel Hill.  
[^hayles2012]: Hayles, N. Katherine (2012).  _How We Think: Digital Media and Contemporary Technogenesis._  Chicago: The University of Chicago Press.  
[^heimerl2014]: Heimerl, Florian; Steffen Lohmann; Simon Lange; and Thomas Ertl (2014).  “Word Cloud Explorer: Text Analytics based on Word Clouds.”    _47th Hawaii International Conference on System Sciences_ , Jan 2014, 1833–1842. DOI: 10.1109/HICSS.2014.231  
[^herzog2016]: Herzog, Werner, dir. (2016).  _Lo and Behold: Reveries of the Connected World_ (2016). New York: Magnolia Pictures. Film.  
[^janicke2015]: Jänicke, Stefan, Greta Franzini, Muhammad Faisal Cheema, and Gerik Scheuermann (2015).  “On Close and Distant Reading in Digital Humanities: A Survey and Future Challenges.”    _Proceedings of the Eurographics Conference on Visualization (EuroVis)_  Cagliari, Italy, 25–29 May 2015. http://www.informatik.uni-leipzig.de/~stjaenicke/Survey.pdf  
[^janicke2017]: Jänicke, Stefan, Greta Franzini, Muhammad Faisal Cheema, and Gerik Scheuermann (2017).  “Visual Text Analysis in Digital Humanities.”    _Computer Graphics Forum_ , 36(6), 226-250. https://doi.org/10.1111/cgf.12873.  
[^koolen2012]: Koolen, Coorina, Alex Garnet, and Raymond G. Siemens (2012).  “Electronic Environments for Reading: An Annotated Bibliography of Pertinent Hardware and Software.”    _Scholarly and Research Communication_ , 3(4), 1-62.  
[^landow2006]: Landow, George P. (2006).  _Hypertext 3.0: Critical Theory and New Media in an Era of Globalization. _ Baltimore, MD: The Johns Hopkins University Press.  
[^mangen2019]: Mangen, Anne, Gérard Olivier, and Jean-Luc Velay (2019).  “Comparing comprehension of a long text read in print book and on Kindle: Where in the text and when in the story?”    _Frontiers in psychology: cognitive science_ . 15 February 2019 https://doi.org/10.3389/fpsyg.2019.00038  
[^mangen2016]: Mangen, Anne, and Adriaan van der Weel (2016).  “The evolution of reading in the age of digitisation: an integrative framework for reading research.”    _Literacy_ , 50(3), 116-124. https://onlinelibrary.wiley.com/doi/abs/10.1111/lit.12086  
[^manovich2011]: Manovich, Lev (2011).  “What is visualisation?” ,   _Visual Studies_ , 26(1), 36-49. DOI:10.1080/1472586X.2011.548488  
[^marshall1995]: Marshall, Catherine C., and Frank M. Shipman (1995).  “Spatial hypertext: designing for change.”    _Communications of the ACM_ , 38(8), 88-97. August 1995 https://doi.org/10.1145/208344.208350  
[^mohammad2012]: Mohammad, Saif M. (2012).  “From once upon a time to happily ever after: Tracking emotions in mail and books.”    _Decision Support Systems_ , 53(4), 730-741. DOI: 10.1016/j.dss.2012.05.030  
[^moulthrop1991]: Moulthrop, Stuart (1991).  “You Say You Want a Revolution? Hypertext and the Laws of Media” .  _Postmodern Culture_ , 1.3. DOI: https://doi.org/10.1353/pmc.1991.0019  
[^moulthrop2017]: Moulthrop, Stuart, and Dene Grigar (2017).  _Traversals: The Use of Preservation for Early Electronic Writing_ . Cambridge, MA: The MIT Press.  
[^murray2012]: Murray, Janet H. (2012).  _Inventing the Medium: Principles of Interaction Design as Cultural Practice_ . Cambridge, MA: The MIT Press.  
[^nelson1965]: Nelson, Theodor H. (1965).  “A File Structure for the Complex, the Changing, and the Indeterminate.”    _Association for Computing Machinery: Proceedings of the 20th National Conference_ , 84–100.  
[^nelson1995]: Nelson, Theodor H. (1995).  “The Heart of Connection: Hypermedia Unified by Transclusion. ”  _Communications of the ACM_  38(8), 31–33.  
[^nelson2003]: Nelson, Theodor H. (2003).  “Computer Lib/Dream Machines”  (1974).  _The New Media Reader_ , ed. Noah Wardrip-Fruin and Nick Montfort. Cambridge, MA: MIT Press. 303-338.  
[^pizarro2010]: Pizarro, Jerónimo, ed. 2010. Fernando Pessoa,  _Livro do Desasocego. Edição Crítica das Obras de Fernando Pessoa, Vol. XII (Tomos I e II)_ . Lisboa: Imprensa Nacional-Casa da Moeda.  
[^portela2015]: Portela, Manuel, and António Rito Silva (2015).  “A model for a virtual LdoD.”    _Digital Scholarship in the Humanities_ , 30(3), 354-370. http://dx.doi.org/10.1093/llc/fqu004  
[^portela2017a]: Portela, Manuel, and Rito Silva, António, eds. (2017).   _Arquivo LdoD: Arquivo Digital Colaborativo do Livro do Desassossego_ . Coimbra: Centro de Literatura Portuguesa da Universidade de Coimbra. URL: https://ldod.uc.pt/  
[^portela2017b]: Portela, Manuel (2017).  “The   _Book of Disquiet_   Archive as a Collaborative Textual Environment: From Digital Archive to Digital Simulator.”    _The Writing Platform: Digital Knowledge for Writers_ . Brisbane: Queensland University of Technology. Web. URL: https://thewritingplatform.com/2017/07/book-disquiet-archive-collaborative-textual-environment-digital-archive-digital-simulator/  
[^portela2019]: Portela, Manuel (2019).  “The  _LdoD Archive _ as a creative textual environment and a model of literary performativity.”    _Computational Creativity Meets Digital Literary Studies, Dagstuhl Reports_ , Edited by Tarek Richard Besold, Pablo Gervás, Evelyn Gius, and Sarah Schulz, 9(4), 87–106 [p. 98].  
[^portela2020]: Portela, Manuel, and Cecília Magalhães (2020).  “The Book of Disquiet Digital Archive as a Role-Playing Experiment.”    _Attention à la Marche! Mind The Gap! Thinking Electronic Literature in a Digital Culture._  Eds. Bertrand Gervais and Sophie Marcotte. Montréal: Les Presses de l'Écureuil. 307-325.  
[^portela]: Portela, Manuel.  “From Meta-Editing to Virtual Editing: The   _LdoD Archive_   as a Computer-Assisted Editorial Space.”     _Approaches to Teaching Pessoa's The Book of Disquiet.  _  Eds. Paulo de Medeiros and Jerónimo Pizarro. New York: Modern Language Association. [forthcoming].  
[^ritosilva2015]: Rito Silva, António, and Manuel Portela (2015).  “TEI4LdoD: Textual Encoding and Social Editing in Web 2.0 Environments.”     _Journal of the Text Encoding Initiative_ , 8. URL : http://journals.openedition.org/jtei/1171. DOI : 10.4000/jtei.1171  
[^singhal2001]: Singhal, Amit (2001).  “Modern Information Retrieval: A Brief Overview.”    _Bulletin of the IEEE Computer Society Technical Committee on Data Engineering_  24 (4), 35–43.  
[^sobral2008]: Sobral Cunha, Teresa, ed. 2008. Fernando Pessoa,  _Livro do Desassossego por Vicente Guedes, Bernardo Soares. Lisboa: Relógio d’Água_ . [First ed. 1990-91]  
[^solis2011]: Solís, Carlos, and Nour Ali (2011).  “An Experience Using a Spatial Hypertext Wiki.”    _HT '11: Proceedings of the 22nd ACM conference on Hypertext and hypermedia_ , June 2011, 133-142. DOI: 10.1145/1995966.1995986  
[^theng1996]: Theng, Yin Leng, Matthew Jones, Harold Thimbleby (1996).  “ “Lost in hyperspace” : Psychological problem or bad design?”    _Proceedings 1st Asia-Pacific Conference on HCI_ , 387-396.  
[^theng1998]: Theng, Yin Leng, and Harold Thimbleby (1998).  “Addressing Design and Usability Issues in Hypertext and on the World Wide Web by Re-Examining the  “Lost in Hyperspace”  Problem.”    _Journal of Universal Computer Science_ , 4(11), 839-855.  
[^viegas2009]: Viégas, Fernanda B., Martin Wattenberg, and Jonathan Feinberg (2009).  “Participatory visualization with wordle.”    _IEEE Transactions on Visualization and Computer Graphics_ , 15, 1137–1144. DOI: 10.1109/TVCG.2009.1  
[^vilaplana2017]: Vilaplana, Jaume Nualart, and Mario Pérez-Montoro (2017).  “Diggersdiaries: Using text analysis to support exploration and reading in a large document collection.”    _Eurographics Conference on Visualization (EuroVis), Posters Track (2017)_ , A. Puig Puig and T. Isenberg, Eds. 9-11. DOI: 10.2312/eurp.20171156  
[^zenith2012]: Zenith, Richard, ed. 2012. Fernando Pessoa,  _Livro do Desassossego. Lisboa: Assírio & Alvim_ . [First ed. 1998]  