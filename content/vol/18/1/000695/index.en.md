---
type: article
dhqtype: article
title: "Building an Interface as an Argument? The Case Study of Untangling the Cordel"
date: 2024-03-14
article_id: "000695"
volume: 018
issue: 1
authors:
- Elina Leblanc
translationType: original
categories:
- #digital_libraries
- #graphic_design
- #users
- #data_visualization
tags:
- digital libraries
- interface design
- usability
- data visualization
abstract: |
   The project Untangling the cordel (2020-2024) aims at studying and promoting a collection of 19th-century Spanish chapbooks via a digital library (DL). This resource is composed of digital scholarly editions of chapbooks and of a catalogue of woodcuts, which decorate the first page of almost all the documents. In this paper, after presenting the project’s editorial workflow, we focus our attention of the way we design the interface of this DL to represent the different facets of chapbooks (document, text and illustrations). For that, we have chosen to follow a method, proposed by Andrews and van Zundert in 2018, that consider an interface as an argument editors made about their data and their digital editions. Through this case study, we demonstrate the feasibility of this approach, where each component of an interface contributes to the scientific discourse a project made about its goals and its perception of digital editing. We also stress the impact of this method on user experience and on a project itself, as another way to see data and their modelling.
teaser: "This paper describes how the Untangling the cordel project created the interface for its digital library, using a method that considers an interface as an argument that editors make about their project and their data"
order: 7
---
  
  

## 
  
  

## Introduction
  
In a recent article, Claire Warwick compares digital interfaces of digital humanities (DH) projects to dust jackets of books or to picture frames, i.e. functional objects that can be easily discarded in the first case, or that we cease to see in the second case, as they fade behind the picture they are framing [^warwick2020]. The same can be said about digital interfaces. They are so present that they become transparent to users. They appear as a decorative and convenient support for data, but are not considered as a topic for research. Yet, interfaces say something about the data they present, and how the project perceives them. They  “dictat[e] not only how a digital resource looks but also how it works, and how information may be accessed and comprehended by users”   [^warwick2020]. For these reasons, Warwick calls to take into consideration interface design during the analysis of a project and to preserve the different versions of an interface. Indeed, interfaces attest of the intentions and the context of creation of a project over time, just as dust jackets contain valuable information about commercial strategies, or readers’ tastes at different time. Therefore, we must  “look at the interface, not simply through it”   [^warwick2020].
  
These considerations echo the ones made by Ruecker and Galey in 2010, or by Andrews and van Zundert in 2018, about interfaces of digital scholarly editions (DSE). In their respective papers, they consider interfaces as an argument a project makes about its edition.
  
>  _User interfaces are […] a language_  through which arguments are made, even when the makers of these interfaces are not conscious of the language they are using. As such,  _they reflect the interpretations of the materials_  they are supposed to represent as well as the culture, the politics, and the motives of their designers. [^andrews_zundert2018]
  
Two important facts appear here. Firstly, each interface communicates with its users through a set of colours, signs, and symbols, that forms a  “semiotic environment”   [^andrews_zundert2018]. Secondly, interfaces are not neutral. Even if they seem transparent and opaque to the users, they are nonetheless a rhetoric discourse about the data. They are also dependent on their context of creation, and of the background of their designers, whether it is cultural, identitary, scientific, or political. They are  “means of communication of scholarly arguments”   [^andrews_zundert2018], that must be considered by their makers. Thus, their study and long-term preservation matter to understand not only the position of a project towards its data and field of research, but also what strategies projects have adopted over time [^warwick2020]. Therefore, an interface is not just a nice-looking box. Its design must be seen as a heuristic process that represents a theoretical model, as well as a central step in the life of a project.
  
In this paper, we propose an application of these considerations about interface design as an argument and a witness of projects’ intentions, with a case study: the digital library (DL)  _Untangling the cordel_   [^1] , dedicated to Spanish peddler literature. After a presentation of the project and its editorial workflow, we will analyse its interface and the scholarly arguments behind our design choices with different examples of pages. Through this case study, in turn, we would like to stress the importance of taking the interfaces into account in the scientific discourse of a project. We also aim to demonstrate the feasibility of this approach, as well as its contribution to user navigation and to the project itself, as another way to see data and their modelling.
  
  
  

## The project Untangling the cordel: corpus and objectives
  
The project  _Untangling the cordel_  (2020-2024) is dedicated to a collection of almost 900 19th-century Spanish chapbooks hold by the University library of Geneva. Spanish chapbooks, also known as  _pliegos de cordel_ , have existed since the beginning of printing, and are still published in some Ibero-American countries such as Brazil. These documents were printed in mass on a low-quality paper and sold in the streets by peddlers, for a modest sum. In verse or prose, they relate fictitious stories and real events, share songs, poems and plays, or copy prayers and other religious writings, amongst other contents [^gomis_botrel2019]. Their format is consistent and almost independent of the type of text they contained: they are made of a few pages and share a common layout, with a text usually displayed on two columns, and one or several woodcuts on the front page [^botrel2001].
  
Chapbooks are complex documents. They are both written and oral, constant in their appearance but heterogeneous in their content, and at the frontier between popular and scholarly literature, between books and archives [^botrel2000]; [^botrel2001]. From a librarian and bibliographical perspective, these documents are difficult to classify and to describe with tools and standards that have primarily been thought for books. These impediments lead to an invisibility of chapbooks in libraries’ catalogues, as they are often stored in boxes [^nieto2015]; [^lambert2015]
  
However, over the last decades, with a renewed interest for this peddler literature and the emergence of digital tools, several projects have been launched to highlight this type of documents. Spanish chapbooks can not only be found among the larger collections of national or academic digital libraries[^2] , but also in portals and libraries dedicated to them[^3] . The study of these projects stresses that even if there is no consensus on the way to describe this type of content, they tend to focus their attention on chapbooks as documents rather than on texts or on illustrations, by offering metadata and services related to their editorial process (printers, sellers, prices, etc.) and their  “material aspects”   [^leblanc2019]. This tendency can be explained by the relative homogeneity of the format of chapbooks, which constitute a publishing genre, whereas texts and illustrations are subject to a great diversity in their topic and their type[^4] .
  
   _Untangling the cordel_  is in line with this movement of digital promotion of Spanish chapbooks. It aims at studying (1)  _documents_  from a bibliographical and sociological point of view, as they witness printers’ works and what people liked, (2)  _texts_  with a literary approach (rewritings, medieval patterns, narration of real or fictional events, etc.), and (3)  _woodcuts_  and their uses within and out of our corpus. To achieve these objectives and by following the model chosen by similar projects, the project has developed a DL. However,  _Untangling the cordel_  stands out by offering services that are mainly focused on texts and illustrations through digital scholarly editions and a catalogue of woodcuts, and by using XML-TEI to sustain the library and its functionalities, instead of relational databases and librarian formats such as UNIMARC or MARC-XML.
  
  
  

## From diplomatic digital editions to a catalogue of woodcuts: description of the workflow
  
As the backbone for our document representation, we have chosen the XML-TEI standard as the core element of our editorial workflow. In a first step, we focused our attention on the textual and  “material aspects”   [^leblanc2019] of chapbooks. We began with their transcription by using different automatic transcription tools[^5] . The results were exported in XML formats[^6]  and transformed in XML-TEI, through a XSLT transformation sheet. The obtained digital editions were then enriched manually. Finally, they were displayed online with the web application  _TEI-Publisher_ , side-by-side with their digitisations stored in the IIIF ( _International Image Interoperability Framework_ ) server of the University of Geneva.
  
These editions are diplomatic. They preserve the original punctuation, words spelling ( _muger_ ,  _mujer_ ), and accentuation ( _José_ ,  _Josè_ ). Printing errors and word additions are encoded as well and signalled on the interface with different colours and positions. While page breaks and line breaks are consistent with the original print, we decided to not consider column breaks as well as the position of stanzas and paragraphs on the page, except for the titles and colophons which are automatically centred. It was not relevant for our purposes to reproduce the layout of the page to that extent. As we mainly focus our attention on texts, we choose to indicate information about columns and other page features in the descriptive metadata of each edition.
  
This editorial workflow centred on text has been the basis for the development of a woodcut catalogue. Indeed, during the automatic transcription of the corpus, automatic transcription tools allowed us not only to detect lines and characters, but also illustrations. We could then know which documents contained illustrations and on which page, as well as the coordinates of their position on an image. This information was centralized in a spreadsheet and enriched with keywords about the elements being represented (women, men, clothing, animals, places, etc.). Finally, as the woodcuts in our corpus can and do appear in different chapbooks, we used the software VISE[^7]  to detect similar items. The results have also been recorded in the spreadsheet.
  
To create our catalogue and display it with  _TEI-Publisher_   [^e-editiones2021], we developed a script that transforms each line of the spreadsheet into an XML-TEI file. As for the digital editions, the image of a woodcut is presented alongside its descriptive metadata (keywords, title and date of the chapbook it comes from, list of similar or quasi-identical woodcuts). To do so, we add the illustration coordinates given by the automatic transcription tools to the IIIF URI of a page. Thus, we merely display the portion of the digitized page that corresponds to a woodcut, without duplicating the images on the IIIF server.
  
This workflow allows us to elaborate three types of services that highlight the different components of a chapbook, i.e. document, text and illustrations:
  
  
 *  _Search _ services: full-text search (with keywords in context), text browsing with filters (publishers, places, dates, type and nature of text), woodcuts browsing by keywords (types of characters, clothes, attitudes, places, etc.).  
 *  _Reading _ services: parallel display of texts and facsimiles, linking between chapbooks and illustrations, comparison of chapbooks.  
 *  _Sharing_  services: export of texts and images, sharing of images (IIIF) and texts (DTS —  _Distributed Text Services_   [^8] ) with other projects.  

  
These services propose several levels of analysis, by taking separately each component of a chapbook or by relating them to each other. They echo the three main axes that structure the research on Spanish chapbooks: (1) a  _librarian axis_ , which consists of cataloguing and examining chapbooks from a critical perspective; (2) a  _literary axis_  pertaining to the analysis of the content of chapbooks and of their intertextuality or intermediality with the interconnections between text and woodcuts; and, (3) a  _bibliographical axis_  interested in chapbooks as an editorial format, i.e. in its production, its selling or its reception [^gomis_botrel2019]. Each axis can be studied with one or several services and is therefore reflected in the interface itself.
  
  
  

## Design of the interface
  
In their demonstration, Andrews and van Zundert distinguish three levels of arguments that an interface might convey. The first level is related to the  _general usability_  of an interface, i.e. if it follows ergonomic criteria and offers a suitable user experience, which indicates a good understanding of its users’ needs from a project [^andrews_zundert2018]. The second level is a  _conceptual level_ , which offers a discourse about DSE itself. For instance, some projects might choose to put texts first and provide reading editions, with few functionalities to explore them. In contrast, other projects might prefer DSEs that look like toolboxes, with numerous services to interact with texts [^andrews_zundert2018]. In both cases, projects will say something about their conception of DSEs as interfaces. Finally, the third one is  _a data level,_  which “pertains to what the edition conveys about its specific text” and the way editors interpret it [^andrews_zundert2018]. These levels have originally been thought for DSEs, but they can be transposed to the context of a DL.
  
It is not always easy to make a distinction between a DSE and a DL. We could say that a DL is dedicated to  “digitized editions”   [^sahle2016] and to the modelling of an object, whereas a DSE is focused on a work and expresses a specific point of view about it [^pierazzo2015]. However, in our context, we decided to consider the project as a DL. Even if we offer DSEs of each chapbook, this is not the only component of our project. Indeed, the catalogue of woodcuts is not a side functionality that complements the editions, but an essential element of our project, which then cannot be seen solely as a DSE. With these different types of data, we could refer to our project as a hub or a portal. Yet, we found these terms less convenient, as they are typically used to name data aggregators. Besides, as our project is based on the content of the University Library of Geneva, it seems more consistent to us to refer to the project as a  _digital_  library.
  
Therefore, if we apply the arguments defined by Andrews and van Zundert to a project such as ours, the second argument would also be related to the type of our DL, and the third one not only to the text, but also to other types of data, such as the woodcuts in our case. In the following examples, we will present the way these different levels of argument occur in our interface, as well as the way they have guided our design choices.
  
  

## The list of chapbooks
  
From a general perspective, we have chosen a minimal design, with a hint of pastel and green colours to give a dynamic and refreshing look to the website[^9]  (Figure 1). The menu bar insists firstly on the scientific aspects of the project, with general information about its objectives, the presentation of the editorial principles followed during the editing of the texts, as well as the project’s bibliography. Thus, from the menu bar, the interface argues for a transparency of the project to reassure its users about the reliability and quality of its data. Indeed, just like with analogue content, users are sensitive to the origin of the data, and to the scholarly rigour with which they have been structured and displayed online. The more a project gives details about its elaboration, the more users will be encouraged to continue their navigation and use of the DL [^warwick_etal2008]; [^warwick2012]. The About tab goes in the same way by providing information about the tools used to prepare the data.
  
{{< figure src="resources/images/figure01.png" caption="Figure 1: List of chapbooks" alt=""  >}}

  
From the Collection tab, users access the list of chapbooks (Figure 1), where they can narrow it down by using facets. These allow them to freely browse the collections of the DL, without resorting to paths that have been predefined by the designers. They also give them an idea of the way the collections have been conceived by their creators, and of the vocabulary used to describe the content [^leblanc2019].
  
Users are usually familiar with the concept of faceted search as they have likely experienced it in other contexts. It allows us to create a familiar environment  “that feels intuitive”   [^nielsen1994]. This is analogous to commercial websites whose lists of products may be narrowed by brands, colours, sizes, prices, etc. But it has also been demonstrated that facets can reproduce the practices of today’s readers in physical libraries. Indeed, when readers look for a specific book in a library, they will often look at the other books on the surrounding shelves. This phenomenon has been called the  “neighbour effect”   [^mckay_etal2014]; [^mckay_etal2015]. It encourages the discovery of unexpected books, also known as serendipity, which can be about subjects other that the ones readers were looking for in the first place. In a DL, filters can play the role of a physical library’s shelves by suggesting users other topics or content that fall within the scope of their interests – for instance, someone interested in  _coplas_  might also be interested in  _trovos_  or  _décimas_   [^10]  – or belong to a different genre [^mckay_etal2014]; [^mckay_etal2015].
  
To complete facets and help users in their discovery and selection of chapbooks, we chose to present each item in the list with preliminary metadata and a thumbnail of its first page (Figure 1). This information is extracted from the XML-TEI files and, for the thumbnails, generated with IIIF. The benefit of producing these data to users before they even click on an item is to distinguish one document from another. Indeed, it is common for chapbooks in our collection to have similar or identical titles. It can be the result of different printings of the same text, or different texts with the same title (Figure 2). Giving the title and the list of content (chapters, poems, songs, acts) is not enough, because different printings of the same text can have different layouts or woodcuts (Figure 3).
  
{{< figure src="resources/images/figure02.jpg" caption="Figure 2: Example of chapbooks with the same title: The first two documents (José María Moreno ed., s.d.) are different printings of the same text. The last one contains a different text, but the title is the same (José María Moreno ed., s.d.)." alt=""  >}}

  
{{< figure src="resources/images/figure03.jpg" caption="Figure 3: Example of chapbooks with the same title and text, but with different layouts and woodcuts (José María Moreno ed., 1859 and s.d.)." alt=""  >}}

  
Therefore, to facilitate search for our users, we choose to also add a thumbnail of the first page and the imprint (Figure 1). Following the usability guidelines defined by [^nielsen2001], with that information, users will not have to multiply clicks to know what is behind a title. They can distinguish, at a glance, different printings of the same text from different texts with the same title.
  
However, the presence of thumbnails is not just a matter of disambiguation of chapbooks or an aesthetic choice. As a metaphor of the  _cordel_ , they reproduce the way Spanish chapbooks were sold and presented to 19th-century readers. Indeed, to be sold, chapbooks were hung with clothespins on strings. The first thing bystanders saw was the first page, whose purpose was to attract them with catchy woodcuts and titles. With the thumbnails, we aim at offering a similar experience to our users without sacrificing the legibility or usability of our interface.
  
Finally, as with facets, thumbnails are also a way to reproduce today’s readers’ practices. Indeed, to choose a document in a physical library, each user has her own strategies and criteria such as the cover, the length and thickness of a document, the themes or the presence of illustrations [^hinze_etal2012]; [^mckay_etal2014]. To recreate a part of these practices and render an idea of the materiality of the documents, we decided to highlight the first page of chapbooks, and to give information about the number of pages and about the content inside.
  
Thus, the design of this interface unites various uses acquired elsewhere, and the context of production and sale of chapbooks. An interface element can be chosen for reasons related to several levels of arguments. For instance, thumbnails can argue that (1) we use images as a powerful way to engage users with our interface [^norman2007]; (2) our DL follows the practices in physical libraries and is aimed at users with a scholarly background, and (3) the appearance of chapbooks is a major component in their production and sale.
  
After several months of use we implemented a new version of this interface, due to technical issues which became apparent at usage (Figure 4). Between the first and the second version of this interface, the conceptual and data arguments remain the same. Indeed, even with this new look, the facets still follow the concepts explained above. However, their usability has been improved toward a more minimalist design and more control over the interface for the users.
  
Previously, facets followed the default behaviour of  _TEI-Publisher_ , which regenerates the list of documents when a facet is selected. Therefore, users were unable to select several facets at once, as the choice of a facet immediately triggered a request. We changed this default behaviour to let users select several keywords in different categories and submit their own request through a new button. This makes this interface more controllable, by allowing to easily do and undo requests [^nielsen1994]. Users also have access to a help documentation that describes the different ways to search within the corpus.
  
Another change was the use of collapsible categories to reduce the facets list so that users can see all of them at once. Finally, we made the navigation bar clearer and more explicit. The corpus, which is at the heart of the project, now appears first. It is followed by a Results tab containing the project’s productions, and the About tab, that now also contains the explanation of the project’s goals and of the editorial process. This new menu bar inscribes the project within an academic orientation and maintains its transparency.
  
{{< figure src="resources/images/Figure4%202.png" caption="Figure 4: The new interface of the list of chapbooks" alt=""  >}}

  
  
  

## The interface of a digital edition
  
When users click on an item in the list, they access a new page that presents the digital edition of the selected chapbook (Figure 5). The interface follows the tradition of digital diplomatic editions, by presenting the text and the facsimile side by side [^sutherland_pierazzo2012]; [^pierazzo2017]. Being unobtrusive, it fades behind the chapbook, which occupies a central place, and encourages its reading. Our goal is to  “minimize the [users] memory”   [^nielsen1994] and to reduce their mental load when they discover a page. If they want detailed information about the chapbook, they can display it with a set of buttons, that target different aspects of this type of content. For instance, the Metadata button provides bibliographical information about the document (dimensions, material, other prints, etc.), while the Content button gives an overview of the different parts that might compose the text (chapters, poems, songs, etc.).
  
{{< figure src="resources/images/Figure5%202.png" caption="Figure 5: Notice of a chapbook ( _Belardo y Lucinda_ , José María Moreno ed., 1858)[^11]" alt=""  >}}

  
For expert users, the interface allows to go beyond the reading of the text. They can download the data in different formats (PDF, ePub, XML-TEI) and reuse them elsewhere[^12] . They can also compare facsimiles using another visualisation tool, called  _Mirador_ . Through the availability of two visualisation tools, the interface gives several levels of reading: a simple reading with the native tool provided by  _TEI-Publisher_ , and an advanced reading with  _Mirador_ , which resembles a virtual workspace. Indeed, with this tool, users can add as many documents as they want in the same space to compare them, or to modify their appearance with image filters (opacity, contrast, etc.). The interface targets different user profiles: from a  **passer-by reader**  who wants to collect information quickly and easily without spending too much time on the interface, to a  **reader-user** , interested in online reading, to an  **expert user** , looking for advanced functionalities and online analyses of text and document [^rasmussen2016]; [^leblanc2019].
  
The offer of these buttons and tools is in line with the usability recommendations for a flexible and personalized interface [^nielsen1994]. It is also a reference to the literary axis of Spanish chapbooks studies, which is interested in  “intertextual relationships between different items”   [^gomis_botrel2019]. Finally, this interface argues for the study of the  “intermediality”  of chapbooks with the  “Illustrations”  button. It lists the woodcuts present in the document and refers users to their respective notices, so they can analyze the relationship between a woodcut and a text, as well as the woodcut itself.
  
  
  

## The notice of a woodcut
  
The notice of a woodcut follows the same structure as that of a DSE, with an image of the woodcut and its metadata side by side (Figure 6). Woodcuts are not often highlighted in other digital projects dedicated to Spanish chapbooks. Most of the time, these projects only state their presence, but without any other information[^13] . Yet, woodcuts play a central role in the characterisation of Spanish chapbooks as an editorial format and the understanding of popular culture. They are present on the first page of almost all documents. At first glance, they offer an anterior and parallel reading of the text, by giving readers some clues about its topics and its type [^botrel2001]; [^botrel2014]. They also manifest the way printers’ shops operated and were organized [^bozalfernandez1979]; [^vivas2010]; [^garcia2018]. Indeed, some woodcuts were used several times not only by a same printer on different chapbooks, but also by different printers across Spain: some stocks of woodcuts might have been bought or inherited by another printers; others might be copies of a preexisting woodcut [^portus2000].
  
{{< figure src="resources/images/Figure6%202.png" caption="Figure 6: Notice of a woodcut (extracted from the chapbook _Pasillo de las Amazonas_ , José María Moreno, 1859)" alt=""  >}}

  
The model of the interface we propose (Figure 6) highlights some of these specificities. First, woodcuts can help dating chapbooks, by observing traces of degradation from one woodcut to another, or by looking at the date of printing of the chapbooks, where there is one. Therefore, for the chapbook from which the woodcut has been extracted, and for the similar woodcuts, we add the date of printing. At first glance, users can make a hypothesis about the period during which a specific woodcut has been used. Then, by comparing the similar items, they might be able to narrow this hypothesis. For that, users can click on the button Compare, that opens a new window with an implementation of the image comparison application VDIFF[^14] . It provides an interface to compare the differences between two images through different visualizations (image superposition, side-by-side view, etc.).
  
The metadata also specify the title of the chapbooks where an illustration can be found. That gives an idea of the type of text, often indicated in the title, and of the subjects with which an illustration is most often used. For instance, in our example (Figure 5), the illustration of this woman is associated with stories about royal families. Considering the type of text, it is mostly used with  _romances_   [^15] , a very popular genre in Spanish chapbooks.
  
The presence of the title of the originator chapbook is also a way to stress the link between text and images. Indeed, as we explained previously, the first thing bystanders saw on chapbooks kiosks was the first page, and with it the illustrations. But the first thing they heard and their first contact with the content were titles, as peddlers were declaiming them in the streets [^catedra2002]; [^castellano2016]. Then, by putting these two pieces of information side by side, the interface stresses the close connection that exists between illustrations and titles, which form a semantic block. It is a valued information to understand chapbooks and the way they were conceived by printers.
  
Finally, users have the possibility to navigate from the notice of a woodcut to the edition of the text, and vice versa. By looking at the whole chapbook, they can study the position of an illustration on the page, as well as the possible other illustrations it is used with to form a scene. If we go back to our example, in our corpus, this lady is always used on the front page with woodcuts representing kings and soldiers. From there, we could navigate from the edition to the notice of these other illustrations (Figure 4)[^16] .
  
Again, the way we organise the information on the page allows several levels of interpretation. Users could analyse the illustration for itself, for example to look at the representation of specific patterns, or to study woodcut techniques in 19th-century Spain. They could also explore the links between different illustrations, the similar ones, and the ones that form a scene on a specific chapbook. Lastly, they could investigate its connections with text – through the titles and the whole text, as DSE and woodcuts are interconnected.
  
  
  
  

## Influence of the tools on the design of an interface
  
The choice of a backbone software is guided by a project’s needs and objectives, but in return, this software might open new design perspectives through the functionalities it offers and the way it works. Undoubtedly, the appearance of our interface and its services have been influenced by the tool we used to develop them, the web application  _TEI-Publisher_ . If we compare our interface with some other  _TEI-Publisher_ -based projects, such as  _Antonomaz_  or  _DiScholEd_  (Figure 7), we can find common design patterns that inscribe these projects in the same community of practices — for instance, the composition of the menu bar, the presence of filters, the position of the facets on the page or the search bar.
  
{{< figure src="resources/images/figure07.jpg" caption="Figure 7: Homepages of the projects _Antonomaz_ and _DiScholEd_" alt=""  >}}

  
Without knowing anything about  _TEI-Publisher_ , a user could easily see that  _Untangling the cordel_  shares something in common with these two projects, just by observing the way the three of them are organized. Some elements are indeed predefined by the software and cannot be overridden without editing the core code of  _TEI-Publisher_ , which would go against its purposes in terms of sustainability [^e-editiones_n.d.]. One could argue that this software leads to an uniformization of the DSEs’ interfaces, but what makes each project unique and specific is the meaning it puts into each of the components of its interface, a meaning that is induced by its objectives and its data. For instance, the interfaces of  _Untangling the cordel_  and  _Antonomaz_  are similar because their data and their objectives are similar: both aim at studying and promoting ephemera, respectively in 19th-century Spain and in 17th-century France. However, the interface of  _DiScholEd_  argues for a hub that contains several DSEs of correspondences. If we go further in the interface of these projects, we observe that, regarding the presentation of the documents, each project has adopted different perspectives. While, as we saw previously,  _Untangling the cordel_  offers reading editions,  _Antonomaz_  chooses to highlight the facsimile. As for  _DiShcolEd_ , it provides a synoptic edition that allows users to see varied information at once (Figure 8).
  
{{< figure src="resources/images/figure08.jpg" caption="Figure 8: Examples of a digital edition of a notice on the project _Antonomaz_ [(https://antonomaz.huma-num.fr/exist/apps/Antonomaz/corpus/Moreau52_GBOOKS.xml)](https://antonomaz.huma-num.fr/exist/apps/Antonomaz/corpus/Moreau52_GBOOKS.xml) and of a letter on the project DiScholEd [(https://discholed.huma-num.fr/exist/apps/discholed/pec/corpus/Lettre0001_15aout1914.xml)](https://discholed.huma-num.fr/exist/apps/discholed/pec/corpus/Lettre0001_15aout1914.xml)" alt=""  >}}

  
These different representations of DSEs are possible because of the way  _TEI-Publisher_  works. Indeed, one of key-concepts of this software is the one of web-components[^17] . They can be considered as blocks, each one corresponding to a functionality. For example, there is a web-component for displaying facsimiles, another for creating a map, and another for adding a simple search bar[^18] . These blocks can be combined with each other to build an interface: even if they share a common look, the way they are laid out on a page is specific to each project. Like TEI,  _TEI-Publisher_  is a modular and flexible tool that allows editors and designers to represent a DSE in different ways. It provides a framework to help them make their own  “rhetorical argumen” t (Andrews and van Zundert 2018, 8) about their data and their conception of a DL and DSEs.
  
Finally, our experience with  _TEI-Publisher_  leads us to consider that it does not only influence the design of our website, but also our data model. Usually, a clear distinction is made between content and its form [^andrews_zundert2018]: when we work with XML, we start by examining the meaning of the data, then think about their visualisation with scripts and stylesheets. However, in this case, some of our editing choices have been determined by the way the tool functions. For instance, the way we display facsimiles does not follow the prescriptions made by the XML-TEI community but simplifies them.
  
No project operates in isolation. It is influenced by the design of other projects, by the expectations of their scientific communities, by the type of digital edition chosen or by the tools used, whether software ( _eXist-DB_ ,  _TEI-Publisher_ ,  _EVT_ ) or libraries ( _Bootstrap_ ). In the last case, the choice of standard technologies argues for the awareness of a project about interoperability and sustainability issues, and about what is advised and acknowledged by its scientific community.
  
  
  

## Conclusions
  
The design of our interface relies on ergonomic and scholarly considerations, that reflects the nature of our corpus and our goals. If we return to the three levels of arguments defined by Andrews and van Zundert, from a usability perspective, the interface of  _Untangling the cordel_  argues for a minimalist design, that leaves space for data and personalisation. Whether it is with the list of chapbooks or their notice, it does not impose a predefined way to interact with data, but let users decide which functionalities or information they want to display.
  
The conceptual level of our interface is related both to the model of a DL and of a DSE. On one hand, the interface argues that our DL follows the model of a physical library. It reuses concepts and practices common to analogue libraries, such as the way users select their books, and can thus be perceived as their extension. On the other hand, it argues that our DSEs are reading editions, favourable to a  “solitary concentration” , by according a central place to text and facsimiles.
  
Finally, regarding the third level and what the DL and DSEs say about our data, the layout of the interface underlines the intertextuality or intermediality of Spanish chapbooks. By offering various levels of analysis, it allows to study components of a chapbook separately (document, text, or woodcuts) or in relation with each other.
  
In conclusion, working with the levels of arguments proposed by Andrews and van Zundert helped us in the creation of our interface by providing us a frame and a better perception of the meaning we put in each component and design choices. We believe that following this method is a way to encourage the study of interfaces and their long-term preservation, thus joining the recommendations made by Claire Warwick in her recent paper.
  
No interface is neutral: deliberately or not, it tells something about a project at a given moment, its values, or its perceptions of a specific subject. When it comes to the development of a digital interface, it is important to keep in mind that designing is not just about the way an interface looks like (the  _dessin_  in French), but also about its intention and meaning (the  _dessein_ ).
  
  
  

## Cited Projects
  
   _Antonomaz_ : [https://antonomaz.huma-num.fr](https://antonomaz.huma-num.fr)  
  
   _Biblioteca Virtual Cordel_ : [http://cordel.edel.univ-poitiers.fr/](http://cordel.edel.univ-poitiers.fr/)  
  
   _Broadside Ballads Online_ : [http://ballads.bodleian.ox.ac.uk/](http://ballads.bodleian.ox.ac.uk/)  
  
CBDRS: [https://www.bidiso.es/CBDRS/](https://www.bidiso.es/CBDRS/)  
  
   _Calaix_ : [http://calaix.gencat.cat/handle/10687/120608](http://calaix.gencat.cat/handle/10687/120608)  
  
   _Coleccion Literatura oral y Tradiciones populares_ : [http://www.bibliotecanacionaldigital.gob.cl/bnd/627/w3-channel.html](http://www.bibliotecanacionaldigital.gob.cl/bnd/627/w3-channel.html)  
  
   _Comedias Sueltas USA_ : [https://comediassueltasusa.org/](https://comediassueltasusa.org/)  
  
   _CUDL – Spanish Chapbooks_ : [https://cudl.lib.cam.ac.uk/collections/spanishchapbooks/1](https://cudl.lib.cam.ac.uk/collections/spanishchapbooks/1)  
  
   _Untangling the cordel  _ : [https://desenrollandoelcordel.unige.ch/](https://desenrollandoelcordel.unige.ch/inicio.html)  
  
   _DiScholEd_ : [https://discholed.huma-num.fr/](https://discholed.huma-num.fr/)  
  
   _EVT – Edition Visualization Technology_ : [http://evt.labcd.unipi.it/](http://evt.labcd.unipi.it/)  
  
   _eScriptorium_ : [https://gitlab.inria.fr/scripta/escriptorium](https://gitlab.inria.fr/scripta/escriptorium)  
  
   _eXist-DB_ : [http://exist-db.org/exist/apps/homepage/index.html](http://exist-db.org/exist/apps/homepage/index.html)  
  
FoNDUE: [https://www.unige.ch/lettres/humanites-numeriques/recherche/projets-de-la-chaire/fondue](https://www.unige.ch/lettres/humanites-numeriques/recherche/projets-de-la-chaire/fondue)  
  
   _Impresos Populares Iberoamericanos_ : [https://www.literaturaspopulares.org/ipm/w/Inicio](https://www.literaturaspopulares.org/ipm/w/Inicio)  
  
   _Lira Popular_ : [https://bibliotecadigital.uchile.cl/discovery/search?vid=56UDC_INST:56UDC_ABELLO](https://bibliotecadigital.uchile.cl/discovery/search?vid=56UDC_INST:56UDC_ABELLO)  
  
   _Literatura de cordel y teatra_ : [http://www.pliegos.culturaspopulares.org/](http://www.pliegos.culturaspopulares.org/)  
  
   _Mapping Pliegos_ : [http://biblioteca.cchs.csic.es/MappingPliegos/](http://biblioteca.cchs.csic.es/MappingPliegos/)  
  
   _TEI-Publisher_ : [http://teipublisher.com/exist/apps/tei-publisher-home/index.html](http://teipublisher.com/exist/apps/tei-publisher-home/index.html)  
  
   _Transkribus_ : [https://transkribus.eu/lite/fr](https://transkribus.eu/lite/fr)  
  
VDIFF: [http://codh.rois.ac.jp/software/vdiffjs/](http://codh.rois.ac.jp/software/vdiffjs/)  
  
VISE: [https://www.robots.ox.ac.uk/~vgg/software/vise/](https://www.robots.ox.ac.uk/~vgg/software/vise/)  
  
  
  
[^1]:  This project is led by the professor Constance Carta (University of Geneva), with the support of the  _Philanthropic Monique de Meuron Family Foundation_ . The digital library is available at [https://desenrollandoelcordel.unige.ch/inicio.html](https://desenrollandoelcordel.unige.ch/inicio.html) &lt;Consulted the 03/05/2023&gt;.
[^2]:  We can name the Cambridge University Digital Library (CUDL), the Digital National Library of Chile with its collection  _Literatura oral y Tradiciones populares_ , the Digital Library of the Chile University with its collection  _Lira popular_ , or the library  _Calaix_  of the Generalitat de Catalunya.
[^3]:  We can think about the  _Catálogo y biblioteca Digital de Relaciones de Sucesos_  (CBDRS), the portal  _Mapping Pliegos_ , and the projects  _Comedias Sueltas USA_ ,  _Literatura de cordel y teatro en España_ ,  _Impresos Populares Iberoamericanos_  (IPI) or  _Biblioteca Virtual Cordel_ .
[^4]:  The projects that offer services dedicated to the content of texts are mainly focused on a specific type of Spanish chapbooks, like the project  _Literatura de cordel y teatro en España_  interested in chapbooks with plays.
[^5]:  At the beginning of the project, we used  _Transkribus_   [^kahle_etal2017], due to its ease of installation and use. However, after one year of the project, an HTR platform called FoNDUE, based on the HTR tool  _eScriptorium_   [^kiessling_etal2019], had been developed at the University of Geneva. We became beta-testers of this new infrastructure, which explains the change of tool during the project.
[^6]:  With  _Transkribus_ , we exported the HTR predictions in PAGE-XML. With FoNDUE, we exported the results in Alto-XML to respect its recommendations and its pipeline.
[^7]:  The VISE software ( _VGG Image Search Engine_ ), maintained and developed by the Department of Engineering Science of the Oxford University, enables the search of images or portions of images in large corpora [^dutta_etal2021].
[^8]:  DTS is an API Specification that aims at facilitating the navigation in text collections, their manipulation, and their citation by relying on Linked Open Data [^almas_etal2021].
[^9]:  Indeed, there could be a gap between what we want to convey or not about our project and data, and what users will see on the interface. For instance, someone could argue that this choice of colours would rather reflect the feminine and young team behind the project.
[^10]:    _Coplas_ ,  _trovos_  and  _décimas_  refer to different metrical forms in Spanish poetry.
[^11]: For the next interfaces, we present the third version of our interface, because there were no major changes. The first version of the website is available at [https://zenodo.org/record/7889635](https://zenodo.org/record/7889635)(Consulted the 03/05/2023).
[^12]:  Providing different formats of our data is, for us, a way to ensure the transparency and reliability of our project, by enabling our users to see our raw data.
[^13]:  To our knowledge, only two projects offer a space dedicated to Spanish chapbook woodcuts:  _Mapping Pliegos_  which uses Pinterest and its imageboards to classify woodcuts by topic, and  _Comedias Sueltas USA_  which is currently developing a catalogue dedicated to ornaments. Regarding English chapbooks, however, the project  _Broadside Ballads Online_  has adopted an approach like ours by proposing an image search engine to detect similar patterns in their corpus of illustrations.
[^14]:  VDIFF is a JavaScript application, developed and maintained by the Center for Open Data in the Humanities (CODH) of the University of Tokyo [^homma2022].
[^15]:  The word  _romance_  has not to be confused with its equivalent in English. In Spain, it  “refers to the meter that has been most popular since medieval times, consisting of octosyllabic lines of verse with assonant rhymes in even lines”   [^gomis_botrel2019]. As numerous Spanish chapbooks used this type of versification, the word  _romance_  has come to define the “printed material” itself ( _ibid._ ).
[^16]:  We are currently devising a way to ease the study of the scenes, which now supposes multiple clicks and a good control of the interface.
[^17]:  Web-components are a W3C standard. They can be seen as blocks that contain the HTML code, the CSS and the Javascript needed by a specific functionality to function.
[^18]:  A list of the  _TEI-Publisher_ ’s web-components can be found through an API: [https://unpkg.com/@teipublisher/pb-components@1.30.3/dist/api.html](https://unpkg.com/@teipublisher/pb-components@1.30.3/dist/api.html) [Accessed 28 march 2023].  
[^almas_etal2021]: Almas, B., Thibault C., Hugh C., Jolivet, V., Liuzzo, P., Romanello, M., Robie, J., and Scott, I. (2021). “ Distributed Text Services (DTS): A Community-Built API to Publish and Consume Text Collections as Linked Data” . [https://hal.archives-ouvertes.fr/hal-03183886.](https://hal.archives-ouvertes.fr/hal-03183886)  
[^andrews_zundert2018]: Andrews, Tara L., and Joris J. van Zundert (2018).  “What Are You Trying to Say? The Interface as an Integral Element of Argument” ’. In  _Scholarly Digital Editions as Interfaces_ , edited by Roman Bleier, Martina Bürgermeister, Helmut W. Klug, Frederike Neuber, and Gerlinde Schneider, 3–33. Norderstedt: BoD – Books on Demand.  
[^botrel2000]: Botrel, Jean-François (2000).  “Littérature et Imprimés de Cordel Dans La Péninsule Ibérique” . In  _Des Conquêtes de Charlemagne Au Brésil. Le Moyen Age Européen Dans La Littérature Populaire Brésilienne. Catalogue de l’exposition_ , edited by R. Lemaire and A. Moreau, 21–29. Poitiers: Médiathèque François Mitterand. https://botrel-jean-francois.com/Cordel_colportage/Lit._cordel.html.  
[^botrel2001]: Botrel, Jean-François (2001).  “El Género de Cordel” . In  _Palabras Para El Pueblo. I. Aproximación General a La Literatura de Cordel_ , edited by Luis Díaz G. Viana, 41–69. Madrid: CSIC. [http://www.cervantesvirtual.com/obra-visor/el-gnero-de-cordel-0/html/0133d94a-82b2-11df-acc7-002185ce6064_7.html#I_0_](http://www.cervantesvirtual.com/obra-visor/el-gnero-de-cordel-0/html/0133d94a-82b2-11df-acc7-002185ce6064_7.html#I_0_).  
[^botrel2006]: Botrel, Jean-François (2006).  “Entre material e inmaterial: el patrimonio de cordel” . In  _La voz y la memoria: palabras y mensajes en la tradición hispánica_ , edited by Fundación Centro Etnográfico Joaquín Díaz., 122–31. Urueña (Valladolid): Fundación Joaquín Díaz.  
[^botrel2014]: Botrel, Jean-François (2014). Literatura de Cordel. In  _Diccionario Español de Términos Literarios Internacionales_ . CSIC.   
[^bozalfernandez1979]: Bozal Fernández, Valeriano (1979).  _La ilustración gráfica del XIX en España._  Comunicación. Madrid: A. Corazón.  
[^castellano2016]: Castellano, Abel Iglesias (2016).  “El Ciego Callejero en la España Moderna: balance y propuestas” .  _LaborHistórico_  2 (1): 74–90. [https://doi.org/10.24206/lh.v2i1.4809](https://doi.org/10.24206/lh.v2i1.4809).  
[^catedra2002]: Cátedra, Pedro M. (2002).  _Invención, Difusión y Recepción de La Literatura Popular Impresa (Siglo XVI)_ . Mérida: Ed. regional de Extremadura.  
[^dutta_etal2021]: Dutta, A., Arandjelović R., and Andrew Z. (2021).  “VGG Image Search Engine” . C++. Oxford University: Visual Geometry Group (VGG). [https://www.robots.ox.ac.uk/~vgg/software/vise/](https://www.robots.ox.ac.uk/~vgg/software/vise/)  
[^e-editiones2021]: e-editiones (2021).  “TEI-Publisher.”   [https://teipublisher.com/index.html](https://teipublisher.com/index.html).  
[^e-editiones_n.d.]:    “Best Practice Recommandations - TEI Publisher’s Documentation” . Accessed 28 March 2023. [https://teipublisher.com/exist/apps/tei-publisher/doc/documentation.xml?odd=docbook.odd&id=customization-best-practice&root=3.39.](https://teipublisher.com/exist/apps/tei-publisher/doc/documentation.xml?odd=docbook.odd&id=customization-best-practice&root=3.39.        )  
[^galey_ruecker2010]: Galey, Alan and Stan Ruecker (2010). ‘How a Prototype Argues’.  _Literary and Linguistics Computing_  25 (4): 405–24. [https://doi.org/10.1093/llc/fqq021](https://doi.org/10.1093/llc/fqq021).  
[^garcia2018]: García, Nuria Aranda (2018).  “Literatura e imagen: las portadas en las historias de cordel decimonónicas” . In  _La escritura y su órbita: nuevos horizontes de la crítica literaria hispánica_ , 261–77. Universidad de León. [https://dialnet.unirioja.es/servlet/articulo?codigo=6665373](https://dialnet.unirioja.es/servlet/articulo?codigo=6665373).  
[^]:   
[^gomis_botrel2019]: Gomis, Juan and Jean-François Botrel (2019).  “ _Literatura De Cordel_  From A Transnational Perspective. New Horizons For An Old Field Of Study” . In  _Crossing Borders, Crossing Cultures_ , edited by Massimo Rospocher, Jeroen Salman, and Hannu Salmi, 127–42. Berlin, Boston: De Gruyter. https://doi.org/10.1515/9783110643541-008.  
[^hinze_etal2012]: Hinze, A., McKay, D., Vanderschantz, N., Timpany, C., and Cunningham, S. (2012).  “Book Selection Behavior in the Physical Library: Implications for Ebook Collections” . In  _Proceedings of the 12th ACM/IEEE-CS Joint Conference on Digital Libraries_ , 305–14. JCDL ’12. New York, NY, USA: ACM. [https://doi.org/10.1145/2232817.2232874](https://doi.org/10.1145/2232817.2232874).  
[^homma2022]: Homma, Jun (2022).  “Vdiff.Js - JavaScript-Based Visual Differencing Tool” . JavaScript. Center for Open Data in the Humanities. [http://codh.rois.ac.jp/software/vdiffjs/](http://codh.rois.ac.jp/software/vdiffjs/).  
[^kahle_etal2017]: Kahle, P., Colutto, S., Hackl, G., and Mühlberger, G. (2017).  “Transkribus - A Service Platform for Transcription, Recognition and Retrieval of Historical Documents” . In  _2017 14th IAPR International Conference on Document Analysis and Recognition (ICDAR)_ , 04:19–24. [https://doi.org/10.1109/ICDAR.2017.307](https://doi.org/10.1109/ICDAR.2017.307).  
[^kiessling_etal2019]: Kiessling, B., Tissot, R., Stokes, P., and Stökl Ben Ezra, D. (2019).  “EScriptorium: An Open Source Platform for Historical Document Analysis” . In  _2019 International Conference on Document Analysis and Recognition Workshops (ICDARW)_ , 2:19–19. [https://doi.org/10.1109/ICDARW.2019.10032](https://doi.org/10.1109/ICDARW.2019.10032).  
[^lambert2015]: Lambert, Julie (2015).  “Pérenniser l’éphémère : paradoxe et défi dans le contexte de la John Johnson Collection” .  “Fabula Colloques. Les éphémères, un patrimoine à construire” , November. [https://www.fabula.org:443/colloques/document2940.php](https://www.fabula.org:443/colloques/document2940.php).  
[^leblanc2019]: Leblanc, Elina (2019).  “Bibliothèques Numériques Enrichies et Participatives : Utilisateurs, Services, Interfaces” . These de doctorat, Université Grenoble Alpes (ComUE). [http://theses.fr/2019GREAL017](http://theses.fr/2019GREAL017).  
[^leblanc2023]:  Leblanc 2023 Leblanc, Elina (2023).  “Modelling of a Heterogeneous Corpus: The Example of Chapbook Literature” . Digital Studies / Le champ numérique 13(1). [https://doi.org/10.16995/dscn.8091](https://doi.org/10.16995/dscn.8091)  
[^mckay_etal2015]: McKay, D., Buchanan, G., and Chang, S. (2015).  “Tyranny of Distance: Understanding Academic Library Browsing by Refining the Neighbour Effect” . In  _Research and Advanced Technology for Digital Libraries. TPDL 2015._  Cham: Springer. [http://dx.doi.org/10.1007/978-3-319-24592-8_21](http://dx.doi.org/10.1007/978-3-319-24592-8_21).  
[^mckay_etal2014]: McKay, D., Smith, W., and Chang, S. (2014).  “Lend Me Some Sugar: Borrowing Rates of Neighbouring Books As Evidence for Browsing” . In  _Proceedings of the 14th ACM/IEEE-CS Joint Conference on Digital Libraries,_  145–54. JCDL ’14. Piscataway, NJ, USA: IEEE Press. [http://dl.acm.org/citation.cfm?id=2740769.2740794](http://dl.acm.org/citation.cfm?id=2740769.2740794).  
[^nielsen1994]: Nielsen, Jakob (1994).  “10 Usability Heuristics for User Interface Design” . Nielsen Norman Group. 1994. [https://www.nngroup.com/articles/ten-usability-heuristics/](https://www.nngroup.com/articles/ten-usability-heuristics/).  
[^nielsen2001]: Nielsen, Jakob (2001).  “” ‘113 Design Guidelines for Homepage Usability (Jakob Nielsen)’. Nielsen Norman Group. 2001. https://www.nngroup.com/articles/113-design-guidelines-homepage-usability/.  
[^nieto2015]: Nieto, Philippe (2015). ‘Cataloguer les éphéméras. Quelques pistes de réflexion’.  _Fabula Colloques. Les éphémères, un patrimoine à construire_ , November. [https://www.fabula.org:443/colloques/document2896.php](https://www.fabula.org:443/colloques/document2896.php).  
[^norman2007]: Norman, Don (2007).  _Emotional Design: Why We Love (or Hate) Everyday Things_ . Hachette UK.  
[^pierazzo2015]: Pierazzo, Elena (2015).  _Digital scholarly editing: theories, models and methods_ . Farnham: Ashgate. [https://hal.archives-ouvertes.fr/hal-01182162/document](https://hal.archives-ouvertes.fr/hal-01182162/document).  
[^pierazzo2017]: Pierazzo, Elena (2017).  “Facsimile and Document-Centric Editing” . In  _Creating a Digital Scholarly Edition with the Text Encoding Initiative_ , edited by Marjorie Burghart. DEMM.  
[^portus2000]: Portús, Javier (2000).  “Imágenes de Cordel” . In  _Palabras Para El Pueblo_ , edited by Luis Díaz G. Viana, 1:403–28. Madrid: CSIC.  
[^rasmussen2016]: Rasmussen, Krista Stinne Greve (2016).  “Reading or Using a Digital Edition? Reader Roles in Scholarly Editions”  in Matthew James Driscoll and Elena Pierazzo (ed.)  _Digital Scholarly Editing: Theories and Practices_ . Cambridge, UK: Open Book Publishers, 119–33. [Google Books.](https://books.google.fr/books?id=qW_jDAAAQBAJ&pg=PT103&lpg=PT103&dq=digital+scholarly+editions+user+studies&source=bl&ots=aJV5Gxw2Lf&sig=WZ9F9rUs0USxyyH_0jd5v2jLcBE&hl=fr&sa=X&ved=0ahUKEwiBw6Cv1PnVAhUGcBoKHUP5DBEQ6AEIXTAG#v=onepage&q&f=false.       )  
[^sahle2016]: Sahle, Patrick (2016).  “What Is a Scholarly Digital Edition?”  in Matthew James Driscoll and Elena Pierazzo (eds.)  _Digital Scholarly Editing: Theories and Practices_ . Cambridge, UK: Open Book Publishers, 19–39. [https://www.openbookpublishers.com/reader/483#page/58/mode/2up](https://www.openbookpublishers.com/reader/483#page/58/mode/2up).  
[^sutherland_pierazzo2012]: Sutherland, Kathryn and Pierazzo, Elena (2012).  “The Author’s Hand: From Page to Screen”  in Willard Mccarty and Marilyn Deegan (eds.)  _Collaborative Research in the Digital Humanities_ , Aldershot: Ashgate, 191-212.  
[^vivas2010]: Vivas, Vicente Pla (2010).  _La ilustración gráfica del siglo XIX: Funciones y disfunciones_ . Universitat de València.  
[^warwick2012]: Warwick, Claire (2012).  “Studying Users in Digital Humanities” . In  _Digital Humanities in Practice_ , by Claire Warwick, Melissa Terras, and Julianne Nyhan. London: Facet Publishing.  
[^warwick2020]: Warwick, Claire (2020).  “Interfaces, Ephemera, and Identity: A Study of the Historical Presentation of Digital Humanities Resources” .  _Digital Scholarship in the Humanities_  35 (4): 944–71. [https://doi.org/10.1093/llc/fqz081](https://doi.org/10.1093/llc/fqz081).  
[^warwick_etal2008]: Warwick, C., Melissa T., Paul H., and Pappa, N. (2008).  “If You Build It Will They Come? The LAIRAH Study: Quantifying the Use of Online Resources in the Arts and Humanities through Statistical Analysis of User Log Data” .  _Literary and Linguistic Computing_  23 (1): 85–102. [https://doi.org/10.1093/llc/fqm045](https://doi.org/10.1093/llc/fqm045).  