---
type: article
dhqtype: article
title: "Probing Through Iranian Architectural History Within the Framework of an Ontology Development Process"
date: 2021-10-19
article_id: "000559"
volume: 015
issue: 3
authors:
- Dena Shamsizadeh Hayatdavoodi
- Niloofar Razavi
- Mehrdad Qayyoomi Bidhendi
translationType: original
categories:
- visual art
- machine learning
- interdisciplinarity
- history
- linguistics
tags:
- Ontology
- Knowledge Representation
- Domain Ontology
- Iranian Architectural History
abstract: |
   This paper presents a prototype ontology developed in the field of Iranian architectural history. The paper’s central arguments offer a response to questions regarding how to create an ontology in Iranian architectural history, what consideration must be addressed here, and how to resolve problematic issues in developing an ontology in a field such as Iranian architectural history, which lacks a formalized knowledge. The paper is organized into two parts. It primarily presents a discussion on the specific domain of architectural history and what it encompasses and moves on to examine why it is deemed complicated. After that, the process of creating Iranian architectural history ontology and the methodology applied to match the intended domain is explained. In the second part of the paper, the content of the developed ontology is discussed, which includes various parts of the ontology and what it implies to illustrate how the structure of ontology helps in logically representing the domain in a machine-readable format.
teaser: "Explores questions and problems of how to create an ontology in Iranian architectural history and how to represent the domain in a machine-readable format."
order: 11
---
  
  

## Introduction
  
To a great extent, what is known about architectural history stems from its practice, discussions in its various fields of study, and the accumulation of that information into knowledge. Such information has partly been expressed in an explicit form shared between different parties (from people to software agents). This mode of sharing calls for a mutual understanding of the content in the intended domain to unify the conception of different groups involved in the subject matter. The intended consensus also relies on interaction in a formal realm with a unified language. Therefore, in order to make such interaction possible in the field of architectural history, one needs to identify the domain and express the relevant knowledge in a clear and explicit manner. To do so, it seems viable to apply the tools designed specifically for the purpose. 
  
Over the past few decades, in the field of computer science and artificial intelligence, a branch called ontology has developed, which provides the mentioned clarity in expressing the domain knowledge both by providing an inventory of key concepts and treating the relations between the concepts.
  
With the progress of science and technology, human beings’ ability to create new and advanced tools accelerated to the point of surpassing mundane affairs. Such tools were born to replicate human functions. Richard Sennett offers an interesting categorization of human-made tools, which he places into two groups: the replicant and the robot. A replicant is a tool that mirrors humans by mimicking their actions. However, a robot is an ameliorated human; it is more robust, works faster, and never tires. Still, we make sense of its functions by referring to our own human measures [^sennett2008]. The mentioned functions may range from automatically completing an order, saving things in its memory, finding and retrieving certain items in bulk, or other tasks. Such robot-like tools are established on a somewhat simple basis: mirroring the human mind. Unlike the human mind, computers by character lack the willpower to learn and recall information, and it is up to us to accumulate the knowledge into its memory and decide how information is recounted (described) for machines.
  
In this paper, we aim to acknowledge the necessity of creating an intelligent robot-like system in the field of Iranian architectural history in the form of a semantic network; a system capable of functioning faster and more precise than humans and able to assist in completing certain tasks that are naturally too difficult, impossible, or subject to errors when done manually.
  
In order to provide these functions, it is necessary to familiarize the desired system with the field of inquiry by describing what it encompasses. Henceforth, the system would ground its additional functions based on clearly defined descriptions. In other words, human knowledge needs to be presented to the machine. 
  
All forms of knowledge representation, including ontologies, are both mediums of expression for human beings and ways to communicate with machines in order to tell them about the world [^brewster2004]. Therefore, engaging with sets of information related to the intended field, which needs to be categorized and described explicitly and logically, is a crucial act while developing an ontology. 
  
Accordingly, this research mainly applies ontology to create a clear, explicit, and descriptive model of the semantic system in Iranian architectural history, taking into account various aspects of the field based on information provided by prominent scholars. In other words, here, the effort is focused on developing an ontology in the aforementioned field of knowledge, which is both explicit and readable for the machine, through capturing and representing the relevant entities in this field. What ensues this approach helps organize the views and provides consensus between different agents (people with each other or machines with people) on Iranian architectural history concepts.
  
  
  

## Ontology of Iranian architectural history: terminology
  
This title of  “Ontology of Iranian architectural history”  consists of four terms: ontology,  Iranian architecture, and history, each of which offers multifaceted denotation causing the original term to indicate different meanings. To clarify what this title covers in the course of this paper, an overview of the specialized terminology is explained below. 
  
Ontology: In the terminology of Artificial Intelligence, the term Ontology may refer to both the act of describing intended concepts explicitly and the specific outcome that is constructed and saved in the form of an XML or UML file, which contains data on concepts and their descriptions. That is so that we may have ontology files with different purposes and save them on our computers or share them with others. It should be noted that description in an ontology means providing formal definitions of terms in the domain vocabulary and representing each concept’s information in a relational form. 
  
Concepts in an ontology must be structured in a way that is usually referred to as linked data; that is, data interlinked with other data to make information readable for machines and make queries within large bulks of information possible. Such links represent relationships within an area of study, and the model that contains all those concepts and relationships is what we call an ontology. Although at the heart of each ontology there is hierarchical taxonomy, yet since an ontology allows more complex and non-hierarchal relationships to be defined, it can be used to represent the fluidity of the real world, where things can be related to each other in more complex ways than are represented by a hierarchical tree-like structure. In that sense, an ontology is more like a spider’s web [^blaney2017].
  
Iranian architecture: Iran in this paper refers to the Iranian world, which transcends modern Iran’s current political boundaries. Simultaneously, Iranian architecture covers all architectural works associated with Iran’s territory throughout its history.
  
History: Michael Stanford distinguishes two meanings of the term history. History  “may refer either to the course of events, what actually happened. (history 1), or what is believed and written about those events (history 2). Sometimes they are distinguished as  history-as-event  and  history-as-account. ”   [^stanford1998].
  
  

## Iranian architectural history
  
Based on Stanford’s distinction, Iranian architectural history can imply two meanings, where architectural history may be considered as series of events, actually occurred in the world (Iranian architectural history 1), and architectural history as the act of studying and describing what has occurred in the world (Iranian architectural history 2). Given that in developing ontologies, we are appointed to capture how human beings characterize their concepts, rather than actual events and whether or not they happened in a specific way, we need to be associated with Iranian architectural history 2, as the scholarship of architectural history is classified under it, and involves the study of architectural history-as-event [^qayyoomi2009]. 
  
Therefore, the intended domain comprises a broad spectrum of studies on architectural evidence and different sorts of human architectural activities. In other words, we regard Iranian architectural history as a series of reports that narrate certain historical events related to works of architecture, architects, the act of building. 
  
  
  
  

## process of creating The IArchHist ontology[^1]   
  
Architecture and architectural history are among cultural matters related to human affairs that enfold all the changeability and historicity that such matters enjoy in any given culture, including the Iranian culture. Additionally, unlike western tradition, the historiography of Iranian architecture is not a longstanding practice. Contemporary attempts to write Iranian architectural history have been performed mainly by two groups of individuals: first, European travelers, archeologists, and architects that came to Iran during the 20th century and composed reports of their observations; second, Iranian specialists, such as archeologists, architects, and authors, who were mostly employed in institutions like Society for National Heritage (SNH) and were responsible for documenting historical buildings for the purpose of conservation. Both groups lacked academic training in historiography. In other words, the existing historiography of Iranian architecture has been developed by non-historians in its academic sense. Therefore, Iranian architectural history has yet to become an established academic discipline with formalized terminological and theoretical peripheries. The inconsistent quality of historiography in the sphere of Iranian architectural history has given rise to its close association with architectural works, their chronology, and the vocabulary and methods that were used to examine them throughout history.
  
Developing ontologies is drawn on logical relationships, so in branches of the humanities, such as history, art, and architectural history, which are less concerned with positive knowledge, creating an ontology that requires data derived from reasons and logical observation poses some challenges. On top of that, even in the western scholarly world, architectural history is still highly dominated by the disciplines of art history and history of architecture and is advancing towards a distinct discipline. Accordingly, Iranian architectural history, in its current state, lacks a formalized terminology and is still undergoing its formation process.[^2] 
  
Based on the facts explained about the field of Iranian architectural history, describing the terms through their relationships is also challenging since the terms have not been used uniformly in the context of writings from different scholars or even a single source. In other words, the field’s scholars lack a unified language when referring to concepts. 
  
Since Iranian architectural history has yet to evolve as an academic field, its existing sources involve subjective reports of buildings that are influenced by personal feelings, tastes, or opinions of the narrator. This poses a challenge in machinizing Iranian architectural history knowledge, which requires objective and straightforward data.
  
However, the very challenges provoked by the field’s nature simultaneously make it essential to undertake available tools (like ontologies) to organize its knowledge. In fields such as Iranian architectural history, developing an ontology contributes to identifying the field’s ambiguities and immaturities in a precise manner. Therefore, here, the ontology provides advantages related to overseeing the field in the course of its formation.
  
  

## Premise
  
Usually, the first step for developing an ontology is to consider using the existing models, or the least, an existing taxonomy. Over the past few decades, several representational models have become available in the field of art, architecture, and cultural heritage. These models include database schemata for integrating heritage information, such as CIDOC CRM (CIDOC Conceptual Reference Model) metadata for description of museum objects, such as Object ID, controlled vocabularies of related fields like Getty art & architecture thesaurus (AAT). 
  
Assuming that we were to use concepts represented in AAT, for instance, each concept must be an exact equivalent in Persian and English, in terms of definition, implication, and relations to other concepts; otherwise, the goal to represent the reality of Iranian architectural history identities would not be fulfilled. This level of correspondence simply does not exist. That is because the Persian-speaking societies of art and architecture naturally do not match up with the anglosphere one. Many of the identities discussed here are either only found in Persian-speaking cultures, or even if found elsewhere, do not encompass the exact same thing, mainly due to cultural differences that are often neglected in universal attempts to develop comprehensive formal ontologies. Therefore, in most cases, when observed carefully, concepts (that are embedded in words), albeit close in meaning, are not identical in the Persian and anglosphere worlds. Based on these considerations, the IArchHist ontology was developed as a unilingual ontology in Persian. 
  
The most basic premise held in developing the IArchHist ontology is that it is possible to represent the knowledge of architectural history through its identified concepts. Such concepts must be thoroughly defined in the course of developing the ontology and be clarified to reach the processing level of the machines.
  
Here an issue arises: how to make relatively ambiguous concepts understandable for machines. At this point, the second premise emerges, stating that concepts are understood and defined through their association with other concepts. The human mind identifies each concept’s meaning by placing it in an elaborate network of its related concepts and recognizing how they are linked. The ontology replicates the same process by representing existing relational links between concepts. As a result, each concept is conceptualized within a specific structure, which is processable for machines.
  
  
  

## The scope of the inventory
  
As a discipline, Iranian architectural history involves certain concepts, which are indefinite by nature, are not directly expressed, and therefore, cannot be adequately described. For instance, there is the concept of principle in Iranian historical buildings’ architectural design. Pirnia, a distinguished Iranian architectural historian, proposes five principles of Iranian architecture as follows: human scale, introversion, self-sufficiency, precluding futility, structural soundness, and proportion [^pirnia2004]. Although he further describes these concepts in the course of his studies, because of their propensity to diverse interpretations, it is hard or even impossible to catch a clear and explicit, and more importantly, a consensual definition; hence, the possibility of failure in representing these concepts through IArchHist ontology. Therefore, it is essential to delimit the semantic boundary for the selection of concepts in the relevant field.
  
The fundamental criterion is that each IArchHist ontology entity requires a formal description that is logical and certified, which would explain the concept it represents. Therefore, all those concepts that are describable in logical phrases clearly and explicitly are covered in the IArchHist ontology, while evaluative or rhetoric concepts are avoided.[^3]  Consequently, the project scope covers Iranian architectural historians’ works who referred to both the material evidence (the relics) and the textual evidence of Iranian architecture.
  
The information used to build the IArchHist ontology was collected from contemporary (written or published during the 80s and 90s in Iran) domain-specific works.[^4]  The appointed references consist of Iranian scholars’ works from four main fields of architectural history, historical geography, archeology, and restoration, and include classes of objects, events, processes, states of affairs, attributes of objects, parts of objects, segments of processes. The selected scholars and their compositions are considered references and major sources within Iranian architectural history.
  
  
  

## Methodology
  
[Noy & McGuinness (2001)](#noy2001) proposed an outline for developing ontologies, which involves the following seven steps: 1) Determine the domain and scope of the ontology; 2) Consider reusing existing ontologies; 3) Enumerate essential terms in the ontology; 4) Define the classes and the class hierarchy; 5) Define the properties of classes — slots; 6) Define the facets of the slots; 7) Create instances. In developing the IArchHist, the methodology proposed by Noy & McGuinness is applied by simultaneously performing the suggested steps and including additional measures when necessary. Following this strategy, the methodology in building the IArchHist ontology is mapped out into the following five stages: 
  
  Steps 1 & 2: Determining the purpose and the scope; selecting the key references;[^5]  choosing the appropriate ontology language and software.  Steps 3 & 4: A taxonomy is an orderly classification for a defined domain. It comprises controlled vocabulary terms (generally only preferred terms) organized into a hierarchical structure. Each term in a taxonomy is in one or more parent/child (broader/ narrower) relationships to other terms in the taxonomy [^harpring2010]. In order to create the taxonomy for IArchHist ontology, two steps were necessary: 
  1. Forming the inventory: cataloging key concepts from information provided by references;  2. Categorization: grouping related concepts together, organizing them in a hierarchical order, and defining upper-level classes.  

These steps are explained in detail in section 4.  Steps 5 & 6: In order to describe the internal structure of the domain concepts outlined in the previous step, we must identify and draw semantic relations between concepts, which have been suggested and specified by domain scholars. Each link must connect at least two concepts producing precise, unambiguous text definition for every pair of concepts that can be expressed in short logical phrases.  Step 7: The defined concepts in the previous steps mainly cover general entities indicating each concept’s types and genre. In order to make the IArchHist ontology richer and more detailed, we must assign instances to each general concept. Such instances inherit the relations previously outlined between their prime concepts.  Visualization: As soon as the ontology is built, the challenge of how to use it, how to explore it, and what data to recall arises. Visualization is mainly based on mapping the information to a graphical representation to facilitate data interpretation. It also provides ways to limit the amount of data users receive while keeping them  “aware”  of the full information [^silva2012]. The type of visualization depends on the user’s intention; however, concerning IArchHist ontology, direct 2D graphs was deemed the most acceptable since it is more familiar and direct for users.  

  
  
  
  

## IArchHist ontology
  
  

## The Taxonomy of IArchHist Ontology
  
By implementing the conventional methods of building ontologies in the domain of Iranian architectural history, a representative model of the domain was created, which will be thoroughly described in the next section.
  
The IArchHist ontology is an OWL 2 ontology created in Protégé 5 editor, represents Iranian architectural concepts by taking into account different aspects of the subject material. This ontology was developed in Persian. Capturing the main concepts of the IArchHist ontology required building a large lexicon of terms. Here, each term was significant because it referred to a concept of the domain. Concepts, also called Class or Type, or Universal, are fundamental building blocks of the IArchHist ontology, as any other. Each class represents a set of instances (also known as individuals) that share one or more common properties. These properties are identified according to the information provided by key references. Whether physical or nonphysical, spatial or temporal, each item within the domain has been thoroughly represented in the ontology.
  
For example, the class of masjid-i jāmiʿ (Friday mosque)[^6]  includes all the individuals that have the following properties: 
  Is a type of masjid (mosque)  Is a place for duʿā (prayer)  Is a place for namāz-i Jumʿa (Friday prayer)  Has a part minbar (pulpit)  

 Therefore, individuals such as masjid-i jāmiʿ-i Isfahān (Friday mosque of Isfahān, masjid-i jāmiʿ-i Yazd (Friday mosque of Yazd), masjid-i jāmiʿ-i ‎ Ardistān (Friday mosque of Ardistān) all belong to this class, and all share the mentioned properties.
  
To accurately record classes and their related properties, each phrase of the mentioned texts containing related information was documented in a separate datasheet. These phrases were labeled under entries named by the exact terms utilized in the text in the original language.[^7]  The terms were further employed as IArchHist ontology classes and subclasses. An example is shown below (Table 1).[^8]   
    Example of information about sardar (portal)    Text  Citation      A darāygāh (entrance) contains faḍā (space)s such as pīsh-utāq (anteroom), sardar (portal), dargāh (doorway), hashtī (vestibule), keryās (lobby), dehlīz (entrance hall), dālān (corridor).  [^pirnia2004]      Physical parts of the masjid (mosque), shaped around a ḥayāṭ (courtyard) and a dargāh (doorway), with a sardar (portal), and a pīshṭāq (arched portal) are adequately linked together, creating the architecture of the masjid (mosque).  [^pirnia2004]      Each bāgh (garden) comprised a darāygāh (entrance); a building sometimes called sardar (portal). This building was similar to bīrunī (the public or male quarters of wealthy households) part of traditional khāna (house)s, which was the place for padhīrāyī (receiving guests).  [^pirnia2004]      In sangī (stone) kārvānsarā (caravanserai), sardar (portal)s were made from ājur (brick).  [^pirnia2004]      masjid-i jāmiʿ-i ʿAbbāsī (Abbasi Friday mosque) has a sardar (portal) decorated with kāshī-yi tarāsh (mosaic tile)  [^pirnia2004]      
In Table 1, related information to the term sardar (portal) is shown. A sardar (portal) is the main façade of some buildings in Iranian historical architecture containing various elements used as a complex entrance system. Each cited phrase contains related concepts to Sardar, which can be listed as follows (Table 2):
    Concepts related to sardar (portal)    darāygāh (entrance)  ḥayāṭ (courtyard)      faḍā (space)  pīshṭāq (arched portal)      pīsh-utāq (anteroom)  bāgh (garden)      sardar (portal)  bīrūnī (the public or male quarters of wealthy households)      dargāh (doorway)  khāna (house)      hashtī (vestibule)  sang (stone)      keryās (lobby)  kārvānsarā (caravanserai)      dehlīz (entrance hall)  ājur (brick)      dālān (corridor)  masjid-i jāmiʿ-i ʿAbbāsī (Abbasi friday mosque)      masjid (mosque)  kāshī-yi tarāsh (mosaic tile)      
These terms were imported to Protégé in a class-subclass order, which was developed by employing a middle-out approach of classification.[^9]  The class hierarchy of sardar (portal) is shown in Figure 1.
  
{{< figure src="resources/images/figure01.png" caption="Class hierarchy of sardar (portal)" alt=""  >}}

  
  
  

## Interconnections of IArchHist ontology
  
The main challenge of developing the IArchHist ontology was describing the concepts via their interconnected relations. This process passes beyond a taxonomic description, which only lays out the type of each entity by a hierarchical relation to its upper (broader) class. The ontological model was further enriched by the description of the internal structure of concepts, which was accomplished by determining each concept's properties.
  
According to OWL, properties may appear as data properties or object properties. Data properties include all descriptive and behavioral aspects that relate to the entities under consideration – such as their geometrical, physical, and behavioral features – which are defined by specific values associated with those attributes. Instead, the object properties represent the connections that exist between each entity and the others, within and between the involved knowledge domains [^acierno2017].
  
Since the key references provide information in natural language, to identify the properties of each concept, we need to rewrite the information in logical phrases so that the building units (concepts and relations) of each phrase can be inferred and transferred into protégé. For example, in the case of sardar (portal), the following statements are inferred:
  
  
 * sardar (portal) is one of the architectural elements of a darāygāh (entrance).  
 * Some masjid (mosque)s have a sardar (portal)  
 * Some bāgh (garden)s have a sardar (portal)  
 * Some khāna (house)s have a sardar (portal)  
 * Some sardar (portal)s are made of ājur (brick)  
 * Some sardar (portal)s are decorated with kāshī-yi tarāsh(mosaic tile)  

  
Relations in an ontology can be categorized into two groups: first, the general relations (like hierarchy or whole-part), which are not specific to a particular domain and can be found in any domain of knowledge. Second, are specific relations, which are appointed to a particular domain. For example, Having Material or Being Decorated By are two properties probably only directed to the concepts found in the domain of Iranian architecture history.
  
The above list includes some properties that relate a certain concept to sardar (portal) and specify how it is related to sardar (portal). That is how an entity called sardar (portal) participates in connections to other concepts. One instance is explained below:
  
It has been said that in the masjid-i jāmiʿ-i ʿAbbāsī (Abbasi Friday mosque), the sardar (portal) has been decorated with a type of tile (kāshī) called kāshī-yi tarāsh (mosaic tile). According to this statement, a sardar (portal) (like the one in Abbasi Friday mosque) can be decorated with kāshī-yi tarāsh. Therefore, to make the intended connection, units of the statement can be separated: 
  Concept 1: sardar (portal)  Concept 2: kāshī-yi tarāsh (mosaic tile)  Link (OWL object property): IsDecoratedWith  

 The representative model is shown in Figure 2. 
  
{{< figure src="resources/images/figure02.png" caption="Representative model of the relation between sardar (portal) & kāshī-yi tarāsh (mosaic tile)" alt=""  >}}

  
Here, the property IsDecoratedWith describes a binary relationship between two individuals of sardar and kāshī-yi tarāsh. Now consider all of the individuals that have an IsDecoratedWith relationship to some other individual. We can think of these individuals as belonging to the class of individuals with some IsDecoratedWith relationship. What is noteworthy here is the fact that relationships are also capable of defining a class of individuals. In OWL, we can define such classes by using restrictions [^horridge2011]. Using restrictions signifies how each supposed relationship applies to the instances of each concept. For example: 
  Do all instances of sardar (portal) have this property? (Is this property universal?)  Do specific instances of sardar (portal) have this property? (Is this an existential property?)  

 OWL restrictions fall into three main categories: 
  Quantifier Restrictions  Cardinality Restrictions  hasValue Restrictions  

 In IArchHist ontology, the quantifier restriction is the dominant mode of control and can be further categorized into existential and universal restrictions: 
  
 * An existential restriction describes a class of individuals with at least one (some) relationship along with a specified property to an individual that is a member of a specified class.  
 * Universal restrictions describe the set of individuals that, for a given property, only have relationships with other individuals that are members of a specific class [^horridge2011].   

 In the above example, the property IsDecoratedWith was assigned to the class sardar (portal) along with an existential restriction, which describes the class of individuals that have at least one IsDecoratedWith relationship to an individual that is a member of the class kāshī-yi tarāsh, which means there exists at least one instance of the class sardar (portal) that is decorated with kāshī-yi tarāsh.
  
  
  

## Classes and Sub-classes in IArchHist ontology
  
By following the mentioned strategies, the first draft of IArchHist ontology was developed covering 1924 concepts, interconnected by 103 object properties. The critical component of the ontological model, being the concepts and their semantic relations, provided an overview of the knowledge in the field of Iranian architectural history and an understanding of the branches of concepts in this domain. 
  
According to IArchHist ontology, two upper-classes were defined to capture the concepts of the field: IArchHist concept and IArchHist related concept where the former encompasses the central concept of Iranian architectural history and the latter those such as rituals, beliefs, periods, which act as intermediary concepts of the field. 
  
The class IArchHist concept contains the following subclasses (Figure 3):[^10]   
{{< figure src="resources/images/figure03.png" caption="IArchHist concept" alt=""  >}}

  
  
Relic: this class includes objective concepts, which refer to the remained relics related to architecture. Each architectural relic has been the result of an agent's work (a maker); it was accomplished through specific actions and technologies; and has certain characteristics such as form, measurement, material, and layout. Architectural relics are categorized as follows (Figure 4):
  
{{< figure src="resources/images/figure04.png" caption="Architectural relics" alt=""  >}}

    
Characteristics: this class includes concepts that are somehow assignable to relics. Such concepts are widely used when describing certain architectural relics (Figure 5). The characteristics are either physical (such as measurements) or nonphysical (like functions).
  
{{< figure src="resources/images/figure05.png" caption="Characteristics" alt=""  >}}

  
Agent: This class includes the agents that participate in the development of an architectural relic. Agents are divided into two categories: human agents and non-human agents (Figure 6).

Human agents can be further categorized regarding the state of their interaction with the relics. Some agents have a role in erecting buildings (including the architect, the contractor, the tile worker, the carpenter, etc.). Some help in the maintenance of the relics (guards, lightkeepers, etc.). Some are the user of relics (travelers, pilgrims, etc.), and some have instigated the formation of a relic through the needs or beliefs of the social group they belong to (like Christians, Europeans). Additionally, some agents have affected the formation or continuity of relics, despite their non-human origin (like gods or goddesses).
  
{{< figure src="resources/images/figure06.png" caption="Agent" alt=""  >}}

    
Action: This class includes all the actions involved in the creation or usage of a relic. It is further categorized into interaction and creation (Figure 7).
  
{{< figure src="resources/images/figure07.png" caption="Action" alt=""  >}}

    

  
  
  
  

## Resolving challenges in IArchHist ontology
  
As we mentioned briefly in [sub-section 4.2](#section4-2), The main challenge in the development process of IArchHist ontology was representing relations based on the data derived from sources. It is important to note that in languages such as OWL, we are mainly able to draw binary relations (meaning we can use properties that link only two individuals). However, in reality, the domain of Iranian architectural history contains certain concepts that require in their representation, a type of relationship that links an entity to more than just one other entity or value. These relations are called n-ary relations [^noy2006]. N-ary relations are more complex types of links, and drawing them is usually quite tricky and often requires specific tactics.
  
Consider the following examples: 
> The ceiling of Friday mosque of Fahraj is quite detailed but human-scaled.
 In this case, one might view the relationship as a binary relation between the individual Friday mosque of Fahraj and its ceiling and represent it as shown in Figure 8. However, here we see additional aspects of that relationship, including its ornamental attribute (being detailed) and the spatial quality it creates (being human-scaled) associated with it.
  
In most ontologies, especially in humanities, such instances of a relation cannot be viewed as an instance of a binary relation with additional attributes attached to it. Instead, it is an illustration of the individual Friday mosque of Fahraj and the complex object representing various facts about its constituents.
  
Following the general guidelines posed by [Noy & Rector (2006)](#noy2006), in the IArchHist ontology, we represented such problematic relationships by adding an intermediate class involving all sub-relations associated with the broader relationship (Figure 9).
  
{{< figure src="resources/images/figure08.png" caption="Representing the relationship between the Friday mosque of Fahraj and its ceiling with a binary relation" alt=""  >}}

  
{{< figure src="resources/images/figure09.png" caption="Representing the relationship between the Friday mosque of Fahraj and its ceiling with N-ary relations" alt=""  >}}

  
  
  
  

## Iarchhist outcomes
  
As we have shown in the course of this paper, the nature of some fields, such as architectural history, imposes somewhat theoretical regard to ontologies as knowledge representation tools rather than their typical goals involving the establishment of a shared understanding. The challenges faced when developing IArchHist, which for the most part was related to ambiguity and indefiniteness of concepts, gave rise to a strategy for outlining a methodology for developing the intended ontology, a methodology which, unlike other domains, is more simultaneous rather than a step-by-step procedure.
  
 The development of the IArchHist ontology prompted three outcomes that would significantly benefit scholars and researchers of Iranian architecture history. The first outcome is the data collected while developing the ontology. The lack of structured databases or other forms of organized data collections in the focused field was a problematic research challenge. All of the field's main sources are paper-based books and articles. The process of developing IArchHist ontology, as explained earlier, simultaneously led to collecting data in a structured manner, which included describing and representing various and, in some cases, several relationships between each pair of data.
  
The second outcome is producing relatively precise descriptions and definitions for each concept in the scope of IArchHist ontology. Since drawing the relationships between concepts required uncovering each concept's nature and what it logically encompasses, a descriptive set of literal definitions was created during IArchHist ontology development. For example, when attempting to represent the concept of "mosque" and drawing its relations to the concept of "dome," a series of logical questions were raised: what is the nature of the relationship between mosques and domes? Must all mosques encompass a dome? Should a building necessarily include a dome in order to be called a mosque? If any building possesses a dome, can we then call it a mosque? Attempting to answer these questions and others along the same line resulted in uncovering the relations between the concepts, such as mosque and dome, and ultimately made it possible to acquire a comprehensive and exclusive definition for each concept.
  
The third outcome is that by objectively relating our concepts, we are able to identify new patterns and pose new questions or find new explanations for formerly resolved issues. For instance, the concept of architect is among the sub-classes of agent in IArchHist ontology. Typically, vernacular architects are considered to be responsible for building design. However, in IArchHist ontology, the class architect is related to sub-classes of relic and characteristic through the following properties: 
  
 * Architect designs building  
 * Architect erects vault  
 * Architect renovates building complex  
 * Architect calculates building geometry  

 These properties show that there are cases of Iranian architects that were responsible for more than just building designs. They were individuals with knowledge of building construction, and in some cases, they were asked to propose renovation outlines for building complexes. Instances of all the mentioned roles are included in the IArchHist ontology. 
  
  
  

## Conclusion
  
This paper presents an overview of developing an ontology in the field of Iranian architectural history named IArchHist ontology. The main challenge here was responding to the question of "how knowledge representation with ontologies helps organize data in a field consisting of a plethora of ambiguous and unstructured information scattered in resources. As explained in the course of this paper, an exclusive strategy was established, which was based on the development methodologies of conventional ontologies. The results of this research promote two key ideas: 
  Methodological approach: In addition to resolving the fundamental issues of the particular field, the process of IArchHist development provokes a new practice of understanding and studying knowledge, which takes place while describing ambiguous concepts and uncovering their logical relations. Accomplishing such purposes demands revealing the complex semantic network that draws the explicit or implicit connections between concepts.  Developed product: The outcome of this research is basically a bounded part of Iranian architectural history ontology, which can be visualized and analyzed thoroughly with different techniques and further refined under field experts. That act of operating the different tasks, from describing to classifying and linking data sets at the same time, makes the process of developing IArchHist ontology much more valuable than the physical outcome. In order to reach an agreeable description for each concept, a constant reciprocating strategy was needed to improve the representative model of domain concepts continuously.  


  
In conclusion, this research opens up new possibilities for further investigation into the use of ontology as a tool for organizing concepts in the field of Iranian architectural history by displaying their ambiguities and disorders. Furthermore, the suggested classification system could contribute to thinking more clearly within the focused field of knowledge through clear and unambiguous terms and concepts.
  
  
  

## Acknowledgements
  
This research has been developed within the master thesis Project of  “Ontology of Iranian Architectural History: based on contemporary scholarly publications”  in Shahid Beheshti University (2017) under the supervision of Dr. Niloofar Razavi and consultation of Dr. Mehrdad Qayyoomi Bidhendi. We would like to express our personal gratitude to all those who have helped in carrying out the research.
  
  
[^1]:  To avoid verbosity, from this point forward, we will refer to Iranian architectural history ontology by its shortened form IArchHist ontology.
[^2]: The first academic program for training architectural historians was established in Iran in 2005 (A program called  “Iranian architectural studies”  at the university of Shahid Beheshti, Tehran, Iran). For a detailed discussion on the history of Iranian architectural historiography See reference 6. 
[^3]: The point is clarified with examples in section 4 of the paper.
[^4]: The following works were used: [^afshar1995]  [^ayatollah1980]  [^mostafavi1982]  [^pirnia1992]  [^pirnia1994]  [^pirnia2011]  [^pirnia2004]  [^sotoudeh1992]
[^5]: As mentioned before, due to the lack and inadequacy of structured resources such as metadata standards, thesauruses, and databases in the domain of Iranian architectural history, an inventory of written references was chosen under consideration of a group of domain experts to extract the data necessary for building IArchHist ontology. 
[^6]: As demonstrated before, English equivelants and definitions of the Persian architectural terms do not always encompass all their meaning. Therefore, in this section, discussed terms are presented by transliteratation. However, loosely translated English equivelants of terms are provided to make them understandable for anglophone readers. Note that the original version of the IArchHist ontology is entirely developed in Persian.
[^7]: Importing exact terms used in sources written by prominent scholars would simultaneously portray the vocabulary of research in Iranian architectural history.
[^8]: To better understand the process, in the following examples, texts are translated to English, however IArchHist ontology captures Persian terms.
[^9]: Middle-Out approaches identify central concepts in each area/domain identified; core concepts are identified and then generalized and specialized to complete the ontology [^gandon2002].
[^10]: Figures 3 to 7 are translated screenshots of IArchHist ontology.  
[^acierno2017]: Acierno et al.  “Architectural heritage knowledge modelling: An ontology-based framework for conservation process.”  In  _Journal of Cultural Heritage_ , Volume 24 (March–April 2017), pp 124-133.  
[^afshar1995]: Afshar (Afshār), Iraj.  _Yādgārhā-yi Yazd_  (Monuments of Yazd). Tehran: society for the appreciation of cultural works and dignitaries, 1995 (in Persian).  
[^ayatollah1980]: Ayatollah Zadeh Shirazi (Āyatollahzāda Shīrāzī), Baqer.  “Masjid-i jāmiʿ-i ‎ Ardistān (Friday mosque of Ardistān).”  In  _Athar_ , volume 1, issue 1, 1980 (in Persian).  
[^blaney2017]: Blaney, Jonathan.  “Introduction to the Principles of Linked Open Data.”  In  _The Programming Historian_ . Vol 6 (2017), [https://doi.org/10.46430/phen0068](https://doi.org/10.46430/phen0068).  
[^brewster2004]: Brewster, Christopher et al.  “Knowledge Representation with Ontologies: The Present and Future.”  In  _IEEE Intelligent Systems_ , Volume 19 Issue 1 (January 2004), pp. 72-81.  
[^gandon2002]: Gandon, F.  _Distributed artificial intelligence and knowledge management: Ontologies and multiagent systems for a corporate semantic web_ . Scientific Philosopher Doctorate Thesis in Informatics Defended Thursday the 7th of November 2002, INRIA and University of Nice -Sophia Antipolis, Doctoral School of Sciences and Technologies of Information and Communication, (2002).  
[^harpring2010]: Harpring, Patricia.  _Introduction to Controlled Vocabularies: terminology for art, architecture, and other cultural works_ . Los Angeles: Getty Research Institute, 2010.  
[^horridge2011]: Horridge, Matthew.  “A Practical Guide to Building OWL Ontologies: Using Protégé 4 and CO-ODE Tools.”  Edition 1.3. The University of Manchester: 2011. Available online: [http://owl.cs.manchester.ac.uk/tutorials/protegeowltutorial/resources/ProtegeOWLTutorialP4_v1_3.pdf](http://owl.cs.manchester.ac.uk/tutorials/protegeowltutorial/resources/ProtegeOWLTutorialP4_v1_3.pdf)    
[^mojtahedzadeh2018]: Mojtahedzadeh (Mujtahidzāda), Rouhollah.  “Tārīkh-i tārīkh-i meʿmārī-yi Islāmī (The History of Iranian Architectural Historiography: An Overview)”  in  _Art in Islamic Civilization: Architecture 1_ , Mehrdad Qayyoomi Bidhendi (Qayyūmī Bīdhendī), (ed.), Tehran:‎ SAMT, 2018 (in Persian).  
[^mostafavi1982]: Mostafavi (Mustafavī), Mohammad Taqi.  _Āthār-i tārīkh-i-yi Tehrān_  (Historical Monuments of Tehran: Tehran Society of the National Heritage of Iran, 1982 (in Persian).  
[^noy2006]: Noy, Natalya & Alan Rector.  “Defining N-ary Relations on the Semantic Web.”  2, 12 (2006). Available online: [https://www.w3.org/TR/swbp-n-aryRelations/](https://www.w3.org/TR/swbp-n-aryRelations/)  
[^noy2001]: Noy, Natalya and Deborah McGuinness.  “Ontology Development 101: A Guide to Creating Your First Ontology.”  Stanford Knowledge Systems Laboratory Technical Report KSL-01-05 and Stanford Medical Informatics Technical Report SMI-2001-0880 (March 2001).  
[^qayyoomi2009]: Qayyoomi Bidhendi, Mehrdad.  “Sukhanī dar manābiʿ-i maktūb-i tārīkh-i meʿmārī-yi Īrān va shīva-yi justujū dar ānhā (On the Sources of the History of Iranian Architecture and Its Research Principles),”  in  _Gulistān-i Hunar_ , no. 15, 2009 (in Persian).  
[^pirnia1994]: Pirnia (Pīrniyā), Mohammad Karim.  “Çafd-hā va Ṭāq-hā (Arches and Vaults).”  In  _Athar_ , volume 15, issue 24, 1994 (in Persian).  
[^pirnia1992]: Pirnia (Pīrniyā), Mohammad Karim.  “Gunbad dar meʿmārī-yi Īrān (Dome in Iranian architecture).”  In  _Athar_ , volume 12, issue 20, 1992 (in Persian).  
[^pirnia2011]: Pirnia (Pīrniyā), Mohammad Karim.  _Meʿmārī-yi Īrānī_  (Iranian Architecture), Surūsh-i Dānesh, 2011 (in Persian).  
[^pirnia2004]: Pirnia (Pīrniyā), Mohammad Karim.  _Sabk-shenāsī-yi meʿmārī-yi Īrānī_  (The Stylistics of Iranian Architecture), Surūsh-i Dānesh , 2004 (in Persian).  
[^sotoudeh1992]: Sotoudeh (Sutūda), Manouchehr.  _Jughrāfiyā-yi tārīkh-i-yi Shemīrān_  (Historical Geography of Shemiran), Tehran: Institute for Humanities and Cultural Studies, 1992 (in Persian).  
[^sennett2008]: Sennett, Richard.  _The Craftsman_ . New Haven:  _Yale University Press_ , 2008.  
[^silva2012]: Silva, Isabel et al.  “An integrated approach for evaluating the visualization of intensional and extensional levels of ontologies.”  In  _Proceedings of the 2012 BELIV Workshop: Beyond Time and Errors-Novel Evaluation Methods for Visualization,_  (2012).  
[^stanford1998]: Stanford, Michael.  _An Introduction to the Philosophy of History_ . Malden, Massachusetts: Blackwell publishers, 1998.  
[^uschold1996]: Uschold, Mike, and Michael Grüninger.  “Ontologies: principles, methods, and applications.”  In  _Knowledge Engineering Review_ , Vol 11, No 2. (Februrary 1996), p.93–155.  