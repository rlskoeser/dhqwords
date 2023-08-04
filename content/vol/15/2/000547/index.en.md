---
type: article
dhqtype: article
title: "Towards Hermeneutic Visualization in Digital Literary Studies"
date: 2021-06-15
article_id: "000547"
volume: 015
issue: 2
authors:
- Rabea Kleymann
- Jan-Erik Stange
translationType: original
abstract: |
   In this article, we present our reflections on hermeneutic data visualizations for digital literary studies. Hermeneutic approaches in the digital humanities have been rather agnostic about the epistemological premises of hermeneutic theory. These can be summarized as (1) differentiation author/text, (2) hermeneutic circle and (3) dependency text/recipient. In this article, we present the concept of hermeneutic visualization as a means of bridging the gap between classic literary hermeneutics and the emerging practice of digital literary hermeneutics. Since data visualization is based on epistemological premises stemming from the natural or social sciences, it is not well-equipped to meet hermeneutic demands. In this article, we argue that the digital humanities can meet hermeneutic demands through a critical interface and visualization concept. We discuss four postulates that can be used as guidelines and help transform more traditional data visualization into hermeneutic visualization, while respecting the epistemological foundations of hermeneutic theory. We demonstrate the usefulness of the postulates with an interactive prototype Stereoscope designed to support them.In our article, we refer to the discussions and results of the three-year research project Three-Dimensional Dynamic Data Visualisation and Exploration for Digital Humanities Research (3DH) at the University of Hamburg (04/2016–12/2018). The considerations on hermeneutic visualizations presented here are therefore the result of a very productive collaboration. Therefore we cannot claim the presented ideas as our own.
teaser: "This article discusses hermeneutic data visualizations within the field of digital literary studies."
order: 3
---



## 1. Introduction

Data visualization has become a prolific method in digital literary studies to represent the results of a research process. While it is most commonly used to communicate these results to a scholarly audience, there is an increasing number of cases that exhibit an analytical use of the method in order to gain a better understanding of the textual data under investigation (cf.<a class="footnote-ref" href="#jessop2008"> [jessop2008] </a>;<a class="footnote-ref" href="#sinclair2013"> [sinclair2013] </a>). A common definition of data visualization is: “The use of computer-supported, interactive, visual representations of abstract data to amplify cognition” <a class="footnote-ref" href="#card1999"> [card1999] </a>. Although literary text can be transformed into abstract data with the help of statistical or computational methods like natural language processing, this is not the kind of data that literary scholars practicing an hermeneutic approach are concerned with. Here, scholars are dealing with subjective and ambiguous data, usually in the form of text annotations, for which conventional data visualization is not adequate (cf.<a class="footnote-ref" href="#drucker2018"> [drucker2018] </a>). Precisely this discrepancy between conventional data visualizations used and the interpretative data and processes to be visualized is the starting point of our considerations for a more reflective interface and visualization concept for literary analysis and interpretation processes.

As Meister et al. point out: “Most current DH visualizations are thus epistemological one-way avenues toward knowledge, from data via rendering algorithm to visual display” <a class="footnote-ref" href="#meister2017"> [meister2017] </a>. But the process of understanding texts and other cultural artifacts in the humanities is a continuous, dynamic interplay of modeling as well as reasoning operations. These operations repeatedly affect a dynamic data model in form of enrichment and reconfiguration (cf.<a class="footnote-ref" href="#gius2017"> [gius2017] </a>). The hermeneutic approach is a specific form of the process of understanding, which has significance especially for literary and cultural studies. In the humanities, the termhermeneutic(hermeneueinin Greek means “to say, to explain, to translate” <a class="footnote-ref" href="#palmers1969"> [palmers1969] </a>) generally stands “for the practice of exegesis (i. e. interpretation) that leads to understanding, [...] [as well as] for the theory of interpretation as a reflection on the conditions and norms of understanding and linguistic utterance in general” <a class="footnote-ref" href="#mittelstrab2008"> [mittelstrab2008] </a>[^2] . Already developed as a practice in ancient times, hermeneutics took different forms over the 19th century, especially in Schleiermacher’s and Herder’s approach, then around 1900 in Dilthey’s conception and finally in the 20th century in the thinking of Heidegger, Gadamer and the “Konstanzer Schule” . As a result, the following distinction has become established in the humanities. On the one hand, hermeneutic refers to a literary-philological art theory of the interpretation of texts (and other cultural artefacts). We speak ofliterary hermeneutics. On the other hand, hermeneutic is a philosophical discipline with an universalistic claim that is concerned with the conditions of humanistic understanding per se (cf.<a class="footnote-ref" href="#nunning2008"> [nunning2008] </a>;<a class="footnote-ref" href="#stiening2016"> [stiening2016] </a>). In this context, we are talking of _hermeneutic philosophy_ . However, both meanings of the term are strongly interdependent and partly overlap in different theories of the humanities.

In digital humanities research, there has been some discussion on how the digital humanities might live up to expectations and methodological requirements associated with a digitally supported hermeneutic practice (cf.<a class="footnote-ref" href="#zundert2016"> [zundert2016] </a>;<a class="footnote-ref" href="#rockwellandsinclair2016"> [rockwellandsinclair2016] </a>). Often a very broad notion of hermeneutics as a theory of understanding (as opposed to explaining) is applied. We can observe results that have arisen from these discussions in a number of software tools (e.g. _Catma_ , _Voyant_ ). These tools are, for example, replicating traditional scholarly activities that are considered a part of the interpretation process. Unsworth<a class="footnote-ref" href="#unsworth2000"> [unsworth2000] </a>gives a systematic account of “scholarly primitives” , as he calls these activities, some of which are applied by scholars during the interpretative process. Among these are annotation, comparison and representation. As for annotation, this is often the starting point of hermeneutic practice: highlighting parts of a document and writing down comments in the margins are two of the oldest scholarly techniques.

While the integration of these primary activities into digital tools certainly is a step towards hermeneutics in the digital realm (ordigital literary hermeneutics), most of these efforts have been rather agnostic about the epistemological premises of hermeneutic theory. We argue that visualization could serve as the missing link between fundamental hermeneutic premises and digital (literary) hermeneutics. We claim that visualizations not only have to fulfill certain conditions to adequately support literary analysis and interpretation. Rather, we assert that, in referring to the traditional theory of hermeneutics, these qualities can be distinctively described and designed for. We definehermeneutic visualizationas:
> The use of computer-supported, interactive, visual representations of text annotations to manipulate, reconfigure and explore them in order to create visual interpretations that can be used as arguments and allow a critical reflection of the hermeneutic process in light of a research question.
By clarifying the premises and postulates for hermeneutic visualization, we address two research desiderata. First, a systematic elaboration of the implicit premises of hermeneutic text interpretations is still missing. What premises of hermeneutics do we have to consider when we want to use visualizations as tools for the interpretation process? We propose four premises for hermeneutic visualizations. These can be summarized as (1) differentiation author/text, (2) hermeneutic circle and (3) dependency text/recipient.

Second, data visualizations within the DH scholarship are often limited to a representational usage. The current data visualization paradigm in the digital humanities foregrounds operations and transformations of input data at the expense of the human user whose agency as producer and interpreter of visualizations is largely ignored. This has triggered a conceptual and technical reification of visualization that invites its misinterpretation as an objective representation. At worst, visualizations are taken as quasi-objects that appear to exist on the same ontological level as the objects whose properties they claim to faithfully represent. But especially in digital literary studies, we are dealing with data that rather refer to an interpretation process. Polyvalence is a characteristic of this data generated by interpretation. Because of the assumed objective nature of the data, polyvalence is not accounted for in the visual representation of the visual variables, which raises a range of questions: What demands must be made on a critical interface and visualization concept for hermeneutic text interpretations? What do hermeneutic visualizations look like? How do we create them? In order to tackle these questions we propose four postulates for hermeneutic visualizations: _Two Way Screen, Quality, Parallax_ and _Discourse_ [cf.<a class="footnote-ref" href="#meister2017"> [meister2017] </a>;<a class="footnote-ref" href="#drucker2018"> [drucker2018] </a>]. These four postulates serve as guidelines for creating hermeneutic visualizations and embedding them in user interfaces. To get our postulates on a concrete footing, we will demonstrate their usefulness with the help of the interactive visualization prototype “Stereoscope” .

In our paper, we want to raise awareness for the extent to which research in digital humanities always contributes to the “epistemic self-enlightenment” <a class="footnote-ref" href="#albrecht2015"> [albrecht2015] </a>of one’s own discipline. This article aims to show how digital humanities research is based on a thorough and continuous reflection of the epistemological principles at work. Our article represents an attempt to think visualization in terms of literary hermeneutics. Contrary to current narratives of an “end of theory” (cf.<a class="footnote-ref" href="#anderson2008"> [anderson2008] </a>) or a post-theoretical era (cf.<a class="footnote-ref" href="#scheinfeldt2012"> [scheinfeldt2012] </a>) in the DH, we argue for a productive discussion of theories, in our case literary theories. Against this background, we believe that the question of hermeneutic visualizations gains an exemplary status. We are not only interested in demonstrating possibilities of operationalization for the singular case of hermeneutic visualizations. Rather, we believe that our case of hermeneutic visualization can be regarded as a prototypical procedure with respect to the question of methodology in digital humanities research in general. The issue of “hermeneutic visualization” is, we argue, both a demonstration object and a medium of reflection.

Here is the structure of our argument: In section 2, we will begin with a short synopsis of the development of classic hermeneutics and an exposition and explanation of the three epistemological premises. Against this backdrop, we will discuss how visualizations are well-suited to represent these activities, but are also lacking qualities in order to meet the epistemological premises. Section 3 will address these lacking qualities by discussing four postulates. In section 4 we will then demonstrate how these postulates have been addressed in a software prototype. In closing, we reflect on the results and discuss directions for future research.




## 2. From the Hermeneutic Foundation to Digital Hermeneutic Visualizations

This section is initially dedicated elaborating implicit premises in hermeneutic literary theory. These premises are then the lens through which we discuss current hermeneutical approaches in digital humanities, especially with regard to the role of visualizations.



## 2.1 Interpretation, Theory, Method, and Argument in Literary Studies

Among the main activities of researchers working in the field of literary studies one can count the following: interpretation, development and application of literary theory and of methods, argumentation. These core activities form part of the wider literary studies framework and therefore warrant closer inspection. In order to investigate hermeneutic visualizations we think that work on our terminology is required.

Interpretation is considered one of the main activities of literary studies (cf.<a class="footnote-ref" href="#albrecht2015"> [albrecht2015] </a>).[^3] The terminterpretation, a derivation from the Latin word “interpretatio: understand, explain, translate” , is defined as “the methodically induced result of understanding texts in their totality” <a class="footnote-ref" href="#spree2000"> [spree2000] </a>as well as “the formulation of hypotheses about aspects of meaning in literary texts” <a class="footnote-ref" href="#gius2017"> [gius2017] </a>. Following Winko<a class="footnote-ref" href="#winko2003"> [winko2003] </a>the synthesizing interpretation can, on the one hand, presuppose the results of a rather descriptive and analytical text analysis. Analysis and interpretation are thus considered in a procedural relationship. On the other hand, text analysis and interpretation can be determined as synonyms, since both terms are based on the same rules of meaning-making treatment of the text. Despite the idea of a reasoning process that does not require any principles or the claim of some literary scholars “that literary texts are ambiguous or polyvalent by nature” , as Gius & Jacke<a class="footnote-ref" href="#giusjacke2017"> [giusjacke2017] </a>point out, a literary interpretation is based on rules [cf.<a class="footnote-ref" href="#jannidis2003"> [jannidis2003] </a>]. These rules, which are applied in a reasoning process, can be provided by different theoretical approaches (cf.<a class="footnote-ref" href="#spree2000"> [spree2000] </a>).

A _literary theory_ can be defined as an
> explicit, elaborated, logical structured system of categories in order to describe, explore or explain certain issues [of texts]
<a class="footnote-ref" href="#nunning2010"> [nunning2010] </a>. Literary theories provide not only specific epistemological implications regarding, for example, the concept of authorship or the relevance of contexts, but also contain an implicit idea of meaning. During decades of theoretical debates and throughout different turns, the parameters indicating or representing meaning have shifted (cf.<a class="footnote-ref" href="#jannidis2003"> [jannidis2003] </a>). Besides the epistemological implications, this also changed the definition of what actually constitutes a research object as such.[^4] Methods, however, differ from theories. A literary method is a procedure for accomplishing knowledge in a research inquiry. Methods can be characterized as purposeful and rule-based (cf.<a class="footnote-ref" href="#nunning2010"> [nunning2010] </a>;<a class="footnote-ref" href="#winko2003"> [winko2003] </a>). A theory could not only encompass one or a set of several methods, but also demand the application of methods with varying degrees of specification (for example, deductive or dialectical methods compared to the more general operations such as reading or generating hypotheses).

Argumentation is described as the “unfolding of given proofs” by Cicero in De partitione Oratoria (cf.<a class="footnote-ref" href="#radle2000"> [radle2000] </a>). In literary studies, argumentation plays an important role for the process of generating and validating interpretations (cf.<a class="footnote-ref" href="#albrecht2015"> [albrecht2015] </a>). Argumentation can be described as a formal or logical organization of single observations, that serve as arguments “to provide evidence in favor of some point of view” <a class="footnote-ref" href="#groarke2017"> [groarke2017] </a>. Krämer<a class="footnote-ref" href="#kramer2015"> [kramer2015] </a>speaks of “practices of arguing” , that means “patterns of links, in which certain types of text data can be associated with certain ways of attributing meaning.” An argumentation explicates the interpretative process in a textual or visual form by structuring, connecting, and subsuming single observations (cf.<a class="footnote-ref" href="#eemeren2009"> [eemeren2009] </a>). Von Savigny, on the one hand, distinguishes eight types of literary arguments, for example “arguments of understanding” or “poetic arguments” <a class="footnote-ref" href="#savigny1976"> [savigny1976] </a>. Kindt and Schmidt<a class="footnote-ref" href="#kindt1976"> [kindt1976] </a>, on the other hand, mention three attributes for the evaluation of an argumentation: rigor, intersubjectivity, validation. One issue, for example, is the idea of “evidentiary transparency” <a class="footnote-ref" href="#piper2020"> [piper2020] </a>. How can we verify a literary hypothesis? Is it acceptable for a hypothesis to merely resist falsification, or does it need to be positively confirmed via case studies? (cf.<a class="footnote-ref" href="#albrecht2015"> [albrecht2015] </a>).




## 2.2 Foundations of Literary Hermeneutics

The next point to be addressed concerns the foundations of the type of hermeneutics practiced in the field of literary studies. Thus, the first sentence of Szondi’s _Introduction to Literary Hermeneutics_ <a class="footnote-ref" href="#szondi1995"> [szondi1995] </a>reads: “Literary hermeneutics is the study of the interpretation [...] of literary works.” Köppe & Winko<a class="footnote-ref" href="#winko2003"> [winko2003] </a>point out that the hermeneutic approach is a “precursor” theory, which is not practiced anymore. But according to introductions into literary studies, hermeneutic theory is not only still widespread, it is often also mentioned before all other theories (cf.<a class="footnote-ref" href="#jessing2007"> [jessing2007] </a>;<a class="footnote-ref" href="#nunning2010"> [nunning2010] </a>;<a class="footnote-ref" href="#jahraus2002"> [jahraus2002] </a>). While Stiegler notes a kind of “hermeneutics bashing” <a class="footnote-ref" href="#stiegler2015"> [stiegler2015] </a>conducted by other theoretical approaches, hermeneutic theory and its methodological tradition constitute an essential approach to text interpretation.

Essential for hermeneutic theory is the idea of an understanding, which aims to reach a deeper meaning or hidden reason of a text. Consequently, it is assumed that (literary) texts have a meaning, which can be exposed under certain conditions. This meaning does not have an objective, but rather an observer-dependent and contextual status. In that regard, the hermeneutic approach differs widely, for example, from Derrida’s deconstruction (cf.<a class="footnote-ref" href="#derrida1967"> [derrida1967] </a>). In his work _Hermeneutik und Kritik mit besonderer Beziehung auf das Neue Testament_ (1838) Friedrich Schleiermacher (1768–1834) stresses two important epistemological premises of the hermeneutic understanding of meaning. First, Schleiermacher differentiates between the intentions of the author and the expressions in the text. Schleiermacher’s distinction leads to the idea of an autonomous intention of the text, which is not necessarily congruent with the intention of the author. Therefore, the text is regarded as an artificial and aesthetic work of art with a specific meaning (cf.<a class="footnote-ref" href="#selbmann2002"> [selbmann2002] </a>). Second, Schleiermacher argues that a profound understanding of the text corresponds with the holistic dependency of parts and the whole. He proposes the “Grundsatz der Ganzheit” : “[T]he same way that the whole is, of course, understood in reference to the individual, so too, the individual can only be understood in reference to the whole” (cf.<a class="footnote-ref" href="#schleiermacher1838"> [schleiermacher1838] </a>,<a class="footnote-ref" href="#mantzavinos2016"> [mantzavinos2016] </a>).

Moreover, the philologist Friedrich Ast (1778–1841) and later Schleiermacher emphasize the circular procedure of interpretation, i.e., the hermeneutic circle. In literary studies, the hermeneutic circle or spiral is regarded as an instrument for the formulation of a hypothesis connecting a meaningful whole and its elements [cf.<a class="footnote-ref" href="#otoole2018"> [otoole2018] </a>]. In Gadamer’s conception of hermeneutic experience, understanding is also determined as a circular movement that arises precisely through the examination of the text. The circular structure of understanding thereby aims to change the view of the world in a way that reveals something new or revises old experiences and prejudices (cf.<a class="footnote-ref" href="#rese2010"> [rese2010] </a>). The negation of certain experiences through the reading and analysis of a text leads to the transformation of the horizon of understanding (cf.<a class="footnote-ref" href="#gadamer1990"> [gadamer1990] </a>). “Textual understanding” , as Gius & Jacke<a class="footnote-ref" href="#gius2017"> [gius2017] </a>describe it, “is attained in the interplay between (contextual) assumptions about the text on the one hand, and textual data on the other hand […].” Thus, the act of interpretation constitutes a specific practice of a “reading and questioning […], back and forth, shifting the focus of one’s attention and revising interim interpretations and judgements along the way” <a class="footnote-ref" href="#chamber2006"> [chamber2006] </a>.[^5] 

Another premise of the hermeneutic method – besides the differentiation between author and text intention and the holistic premise – is the highly valued co-dependency between the text and the recipient. The co-dependency is linked to the issue of context and subjective or social perceptions and views. According to Gadamer’s _fusion of horizons_ , a recipient, who engages with the text in a productive way, generates partial and subjective knowledge. This generated knowledge in the form of meaning “can neither be deduced theoretically, nor be fully articulated, but rests on a kind of tact or sensitivity that is only exhibited in the form of exemplary judgments and interpretations” <a class="footnote-ref" href="#ramberg2005"> [ramberg2005] </a>. Gius & Jacke<a class="footnote-ref" href="#giusjacke2017"> [giusjacke2017] </a>explain: “Because these reasoning processes are non-deductive, i.e., they are not strictly based on rules of deductive logic, they may result in more than one account of meaning.” 

In summary, we define literary hermeneutics as a specific approach to produce meaning through an iterative, non-deterministic, and subjective procedure. Essential for this approach are three premises, as explicated in the previous paragraphs:
The differentiation between intentions of author and textThe holistic premise (hermeneutic circle)The dependency between text and recipient

The hermeneutic approach is one possibility to tackle the complexity of text comprehension. Further research could investigate visualization in other literary interpretative processes based on Derrida’s idea of deconstruction or Foucauldian parameters of discourse, for example.




## 2.3 Conceptions of Digital Literary Hermeneutics

So far, hermeneutics, as understood in traditional literary studies and based on these three premises, has not played a prominent role in digital humanities. As van Zundert<a class="footnote-ref" href="#zundert2016"> [zundert2016] </a>states:
> The dialogue surrounding hermeneutics seems not to have developed fully yet in digital humanities – references to hermeneutics are scant and often at a concrete level of the practice of text interpretation, such as when Katherine Hayles (2012) uses the phrasehermeneutic close reading. Yet from several paragraphs and sections in the literature the emergence of a debate seems traceable.


Literary scholars participating in this debate on hermeneutics in digital humanities or _digital hermeneutics_ , as it is often called, have different views on how (the use) of digital technology might shape literary hermeneutics and what digital literary hermeneutics should encompass. Generally speaking, the debate is dominated by attempts to digitally replicate interpretative processes known from the analog world. However, a systematic effort to reflect on how the hermeneutic premises might be answered by digital technology is still missing.

Commonly, approaches toward a digital literary hermeneutics, or more generally toward interpretation, share the notion that it involves a process of “reconfiguration, reorganization or restructuring” <a class="footnote-ref" href="#armaselu2017"> [armaselu2017] </a>, or as Samuels & McGann<a class="footnote-ref" href="#samuels1999"> [samuels1999] </a>describe it, “deformance” . Rockwell<a class="footnote-ref" href="#rockwell2003"> [rockwell2003] </a>calls the results of algorithmic analysis of texts “hybrid texts” that operate as “interpretive aids” : “[T]hey are generated by processes of taking information apart and putting it back together into new configurations for the purposes of discovery and reflection.” This reconfiguration can be carried out automatically by an algorithm, as is the case, for example, in concordances, or by manual annotations and comments of text passages by scholars [cf.<a class="footnote-ref" href="#rapp2017"> [rapp2017] </a>;<a class="footnote-ref" href="#jacke2018"> [jacke2018] </a>]. While the former is idiosyncratic to the digital realm, the latter has been practiced in literary hermeneutics for a long time. In terms of possibilities to reconfigure and restructure, however, the digital world grants considerably more freedom than analog annotations. Bradley<a class="footnote-ref" href="#bradley2008"> [bradley2008] </a>describes a research software prototype called _Pliny_ that is guided by scholarly practice of interpretation in the analog world:
> Notetaking, and this kind of juggling of notes to discover previously unrecognised patterns and relationships and to stimulate new ideas is one of the long established methods of scholarship.


 _Pliny_ allows scholars to annotate texts, images and other media by creating digital notes that can be arranged to one’s likings on a plane. Relationships between notes can be conveyed by placing them in spatial proximity or by nesting notes to account for hierarchical relationships. In contrast to analog environments, notes can be reused in different structures and contexts as they are references, not actual objects. References between all the notes can be visualized in a special graph view.

Boot (2009) takes up Bradley’s tripartition of the scholarly process into “Reading and Annotation (Resource)” , “Developing Interpretation” and “Presentation of Interpretation (Article/Argument)” and describes the structure of annotations as “mesotext” that is made out of “mesodata” (individual annotations). _Mesotext_ acts as a connector between the primary text (which it references) and “secondary texts” or “narratives” (the article a scholar is working on), for which it provides arguments. Similar to _Pliny_ , allowing scholars to adjust the _mesotext_ structure, when new insights have been gained, the concept comes close to the traditional analog annotation process.

As a clear differentiation from the scientific method and a way of strengthening the literary hermeneutic approach, some scholars argue for exploration or a “hermeneutic of play” <a class="footnote-ref" href="#rockwell2003"> [rockwell2003] </a>. van Zundert<a class="footnote-ref" href="#zundert2016"> [zundert2016] </a>calls for a usage of data not so much as evidence in the scientific sense, but rather as a resource to “provoke new questions and explorations” that can be utilized in a “playful iterative approach” . Ramsay<a class="footnote-ref" href="#ramsay2007"> [ramsay2007] </a>even speaks of a “Screwmeneutical Imperative” that scholars should follow, an obligation to be playful and try out things.




## 2.4 Towards Hermeneutic Visualizations

In addition to the still pending consideration of hermeneutic premises in digital literary studies, we now take a look at approaches from data visualization. How are visualizations used in digital literary studies so far? Why does an “uncritical” use of data visualizations possibly interfere with an interpretation process? For this purpose, we discuss two ways of incorporating visualization into digital humanities research: humanizing visualizations and visual text analysis.

Firstly, research approaches can be brought together that ask about the critical potential of data visualizations in the humanities. The starting point is often the criticism of the purely instrumental function of visualizations. Visualizations serve, following Card et al.<a class="footnote-ref" href="#card1999"> [card1999] </a>, as “external aids” . Hinrichs et al.<a class="footnote-ref" href="#hinrichs2019"> [hinrichs2019] </a>critically conclude that visualizations have been considered only as tools “to facilitate quantitative and qualitative analysis processes, potentially within any research discipline or practice.” Further the authors explain that “this pragmatic approach risks overlooking the research value of visualization and relegating computer science and design to service-based roles.” Moreover, Correll<a class="footnote-ref" href="#correll2019"> [correll2019] </a>even argues “that visualization is a bad neighbor to the digital humanities: it exacerbates the worst tendencies of DH scholarship and promotes parasitic, technocratic collaborations.” In this context, he pleas not only for new alliances between the humanities and visualization research. Rather, he points out, that “[w]e need to humanize visualization before we visualize the humanities.” Traditionally, visualizations have been developed and used in scientific contexts. Drucker<a class="footnote-ref" href="#drucker2011"> [drucker2011] </a>explains that “realist models of knowledge” have been instrumental in forming these representations and that “we need to take on the challenge of developing graphical expressions rooted in and appropriate to interpretative activity.” 

In order to re-explore new alliances, visualizations are on the one hand reconsidered by means of concepts or function in a humanities context. Seifert et al. speak of visualization as “an effective enabler for exploratory analysis, making it a powerful tool for gaining insight into unexplored data sets.” <a class="footnote-ref" href="#seifert2014"> [seifert2014] </a>Dörk et al.<a class="footnote-ref" href="#dork2013"> [dork2013] </a>go one step further and show a critical approach to information visualization. Disclosure, plurality, contingency, and empowerment are presented as the main characteristics of critical information visualization. In the context of trans-disciplinary research in the digital humanities, Hinrichs et al. advocate for the concept of “sandcastles” , which they describe as “tailored, unique, often stunning yet also transient and unstable interactive visualizations.” <a class="footnote-ref" href="#hinrichs2019"> [hinrichs2019] </a>With this, the authors oppose the reification of data and refer to an iterative process of understanding. In contrast to a conception of visualization as tools, they “elicit critical insights, interpretation, speculation and discussions within and beyond scholarly audiences.” 

While Galey & Ruecker<a class="footnote-ref" href="#galey2010"> [galey2010] </a>do not refer to visualizations in particular (although they use visualizations as case studies), they argue for the use of digital artifacts as arguments:
> The digital humanities must not lose sight of the design of artifacts as a critical act, one that may reflect insights into materials and advance an argument about an artifact’s role in the world. Our purpose here is to follow the implications of a hermeneutical approach to design for digital humanities projects that entail the strategic prototyping of digital artifacts.


However, as Ramsay & Rockwell<a class="footnote-ref" href="#ramsay2012"> [ramsay2012] </a>convincingly point out, Galey & Ruecker’s concept of argument refers rather to the interface of the digital artifact than to the contents of the text which is supposed to be analyzed with the digital tool. Relating to our earlier comment on argumentation in the context of literary studies as a formal or logical organization of single observations that serve as arguments “to provide evidence in favor of some point of view” <a class="footnote-ref" href="#groarke2017"> [groarke2017] </a>, visualizations could serve as another non-linear form of argument that complements textual explications in an argumentation (cf.<a class="footnote-ref" href="#meirelles2019"> [meirelles2019] </a>). In a similar vein, Ramsay & Rockwell also sees visualization tools behaving “like hermeneutical theories” <a class="footnote-ref" href="#ramsay2012"> [ramsay2012] </a>that offer new perspectives on the research object. Kath et al.<a class="footnote-ref" href="#kath2015"> [kath2015] </a>have already brought to attention the need for a second order hermeneutics, termed _New Visual Hermeneutics_ , which can guide the interpretation of such visualizations.

A second research field that plays a role in our demand for hermeneutic visualizations are the approaches from visual text analysis. Although there is a large selection of mainly generic visualization tools scholars can choose from (The TAPoR website[^6] with its large collection gives a good overview), some tools have gained significant popularity for certain use cases and can almost be considered the de facto standard. Stylometry, for example, is usually conducted with the _Stylo_ [^7] package of the statistical language _R_ , _Gephi_ [^8] is very popular for visualizing character networks (cf.<a class="footnote-ref" href="#barbot2019"> [barbot2019] </a>). These visualization tools and techniques offer quite complex user interfaces to control the appearance of a visualization. However, a direct manipulation of the resulting visualization is often not possible and so the process is split into two parts: Manipulation of the interface followed by the generation of a static visualization image as an end result. The image does not contain any information on how the scholar got there and what other possible visual configurations might have been possible by changing the parameters and the data used.

Static visualization images produced by visualization tools are decoupled from the raw text and the modeled text data (produced by the scholar and/or an algorithm), neither allowing a direct manipulation of the data, nor a back-and-forth between data and text.

Other software applications for example _Voyant Tools_ [^9] offer a coexistence of text and data in one user interface, thereby creating the general possibility for hermeneutic process. A constant movement between text and data is a prerequisite formulated by the holistic premise and as a representation of the data the visualization should be tightly linked to the text and allow to view text and visualization side-by-side or at least enable quick changes between these two views. In order to enable that we need to take into account not only the visualization but the user interface surrounding it.[^10] Most of these tools need to be bent to comply with hermeneutic practice. Especially the third premise, the dependency between recipient and text and how it could be represented, has only started to become an object of special attention in the digital humanities (cf.<a class="footnote-ref" href="#drucker2018"> [drucker2018] </a>,<a class="footnote-ref" href="#binder2014"> [binder2014] </a>,<a class="footnote-ref" href="#theron2018"> [theron2018] </a>,<a class="footnote-ref" href="#piotrowski2019"> [piotrowski2019] </a>).

A special use case of visual text analysis is annotation visualization. As Jannidis et al.<a class="footnote-ref" href="#jannidis2017"> [jannidis2017] </a>explain: “The creation of annotation categories, the discovery of corresponding phenomena and the enrichment with appropriate annotations is part of the hermeneutical analysis process.” Meister<a class="footnote-ref" href="#meister2020"> [meister2020] </a>even claims, that we need to understand annotation as “a methodological mediator that can prove the connectivity of digital methods also and especially for traditionally hermeneutically oriented literary scholars.” Baumann et al.<a class="footnote-ref" href="#baumann2020"> [baumann2020] </a>give a differentiated overview of current approaches to annotation visualization. But what we think has not yet been sufficiently considered in visualization approaches is the hermeneutic profit of annotation following Gius & Jacke<a class="footnote-ref" href="#giusjacke2017"> [giusjacke2017] </a>. The authors refer to Piez’s<a class="footnote-ref" href="#piez2010"> [piez2010] </a>conception of a hermeneutic markup:
> Byhermeneutic markupI mean markup that is deliberately interpretive. It is not limited to describing aspects or features of a text that can be formally defined and objectively verified. Instead, it is devoted to recording a scholar’s or analyst’s observations and conjectures in an open-ended way.


According to Gius & Jacke, what constitutes Piez’s approach to hermeneutical markup is that it is precisely the polyvalence and context sensitivity of literary texts that are taken into account. In order for visualizations to meet hermeneutical requirements, they need to be linked to annotations as interpretative endeavors [cf.<a class="footnote-ref" href="#zirker2017"> [zirker2017] </a>,<a class="footnote-ref" href="#nantke2020"> [nantke2020] </a>]. Polyvalence in particular is not only the decisive feature of interpretative data. Rather, the acknowledgement of polyvalence is one of the conceptual requirements that need to be taken into account in the sense of our hermeneutical premises when using visualizations. This is also linked to the distinction of data and capta, as emphasized by Drucker. In other words, in order to serve this purpose of polyvalence, hermeneutic visualizations must value the performative and theoretical aspect of an interpretative endeavor (modelling, theorizing, critique and discourse) higher than the declarative visual output (results, experimental validation, applicability).

We have now discussed approaches of digital hermeneutics and data visualization against the background of our premises. Based on our research approach, the question now arises which requirements visualizations have to fulfill in order to support hermeneutic interpretation processes. For this, we will propose the four postulates that help creating and embedding such visualizations into a user interface.[^11] 





## 3. Hermeneutic Visualization: Four Postulates

As we have seen, one issue of the current approaches to digital hermeneutics is the disregard of the epistemological premises of hermeneutics, i.e., the differentiation between intention of author and text, the holistic idea of the understanding of the whole and its parts (circularity of the interpretation process), as well as the dependency between the text and the recipient (subjective and context-dependent reasoning process). Second, the visualizations used in the DH seem to contradict the hermeneutical premises. We see a distortion of the hermeneutic interpretation process, for example, in the use of visualizations that do not take into account the polyvalence of interpretative data. However, in order for visualizations to be used as the missing link in the process of “becoming hermeneutical” in the digital humanities, we need a concept of visualizations that meets the following four postulates as guidelines: _Two Way Screen, Quality, Parallax and Discourse_ . We understand these postulates as transformers of and mediators between the theoretical hermeneutic model and the concrete visual arrangement.

The postulate of the _Two Way Screen_ refers to the interface, which should not be restricted to rendering, but allow manipulation as well. More precisely, a commitment to the _Two Way Screen_ implies that the screen serves as an interactive and visual environment in which interpretation (ranging from low-level annotation and structuring to high-level theorizing activity) takes place, not only gets displayed [cf.<a class="footnote-ref" href="#drucker2018"> [drucker2018] </a>].

The structure of the interface does not serve as a mere representation space for an interpretative result. Rather, the interface provides incentives to engage and to change bidirectionally between the representation of text data and the modelling of text data. This means that actions taken by changing any graphical feature as an act of interpretation are registered as new data and/or as changes in the data model on the fly. The underlying principle is to get away from the flat screen as a space of display by acknowledging the additional dimension of interpretative activity [cf.<a class="footnote-ref" href="#drucker2016"> [drucker2016] </a>]. The postulate of the _Two Way Screen_ is based on the holistic premise, as it allows a continuous shift between exploring the visualization to learn something about the text (the whole) and applying that new knowledge to change text data (the part), in consequence, creating new representations. Here, as well as in the postulate of _Quality_ , the constructedness of the data becomes apparent and we can grasp it “as capta, taken and constructed” <a class="footnote-ref" href="#drucker2011"> [drucker2011] </a>.

{{< figure src="images/figure01.jpg" caption="Drucker<a class=\"footnote-ref\" href=\"#drucker2016\"> [drucker2016] </a>: Conception of the Two-Way-Screen (draft originated in the 3DH project)" alt="A hand-drawn representation of a 3DH project showing the relationship between data and the display."  >}}


While the postulate of the _Two Way Screen_ formulates the necessity of providing means for changing and constructing interpretative data through the visualization, it does not specify how the data might be visually represented. To this end, the postulate of _Quality_ demands the incorporation of the epistemological qualities of hermeneutic practice into the visualization. Responding to the hermeneutic premise of the dependency between text and recipient, _Quality_ takes into account the subjective and contextual quality of the data by showing the annotated text data as _capta_ . We suggest an extension of the use of Bertin’s visual variables (position, color, tone, size, shape etc.) [cf.<a class="footnote-ref" href="#bertin1983"> [bertin1983] </a>;<a class="footnote-ref" href="#meirelles2019"> [meirelles2019] </a>] to the encoding of _capta_ , allowing literary scholars to express interpretative dimensions like salience or relatedness [cf.<a class="footnote-ref" href="#drucker2018"> [drucker2018] </a>].

The third postulate of _Parallax_ stresses the importance of providing multiple views on the object of hermeneutic inquiry [cf.<a class="footnote-ref" href="#drucker2018"> [drucker2018] </a>]. The termparallax “(Greek παράλλαξις (parallaxis)), meaning alternation ” [cf.[Oxford English Dictionary](https://en.oxforddictionaries.com/definition/parallax)] is a metaphorizedterminus technicusof optics. We understand Parallax as visual multiperspectivity or multiple points of view that reveal the ambiguity of a text. Coles<a class="footnote-ref" href="#mccurdy2016"> [mccurdy2016] </a>stresses the aesthetic importance of the “ambiguity of meaning” in contrast to scientific replicability. Ambiguity, as Berndt<a class="footnote-ref" href="#berndt2009"> [berndt2009] </a>points out, “denotes a fundamental ‘equivocalness’ that engenders uncertainty and doubt .” The visualization in its parallax function, hence, provokes an ambiguity of a maybe “assumed” certainty or evidence. This provocation generated by the visualization relates to the premise of dependency between text and recipient once more and puts the situatedness and partialness of the hermeneutic reasoning process into effect. Moreover, the ambiguity evokes a “questionability whose astonishment gives cause to further research” <a class="footnote-ref" href="#mersch2009"> [mersch2009] </a>. Instead of limiting the points of view, the postulate of _Parallax_ increases the possibility for productive contradiction in the reasoning process.

The last postulate _Discourse_ defines the role of the visualization in the argumentation. Following Latour<a class="footnote-ref" href="#latour1986"> [latour1986] </a>, who claims that “the ways in which we represent our arguments changes the way in which we argue” (cf.<a class="footnote-ref" href="#hinrichs2017"> [hinrichs2017] </a>), we think that a hermeneutic visualization fosters the critical reflection of the hermeneutic process itself. An argumentation comprised of text as well as visualizations as single observations differs from the mere textual form. The connection between visualization, annotations (the object of study) and textual arguments enables a complex, non-linear movement between these entities that does not restrict scholars to one possible reading, but allows a multitude of readings. Furthermore, the direct connection between annotations and visualizations creates a transparency of individual arguments that invites the author as well as the audience to critically reflect the argumentation. In this way, it lives up to the evaluation criteria rigor, intersubjectivity and validation mentioned in 2.1 and leads to an iterative refinement of the argumentation and an oscillation between part and whole, addressing the holistic premise in that way.

The postulates describe four interrelated aspects, under which visualizations can be beneficial for the hermeneutic process in the digital realm and act as hermeneutic visualizations. In the next part, we would like to underpin their validity by presenting their exemplary application in an interface concept and its prototypical implementation.




## 4. The Four Postulates Used as Guidelines for Prototypical Implementation

Referring to Boot’s<a class="footnote-ref" href="#boot2009"> [boot2009] </a>model of _mesotext_ as a particular configuration of annotations ( _mesodata_ ) that relates to the primary text, as well as to the secondary text (an article for example), we incorporated a tripartite user interface in our concept. There is a text area on the left side holding the primary text a scholar is studying, a canvas in the middle that can represent different configurations of annotations of the text with different visualizations and a views area on the right side that allows a scholar to build arguments by saving different views of canvasses with tags and comments assigned to them (Fig. 2). All these parts are connected with each other, so that interacting with one part of the interface, such as a mouse hover over an annotation in the text area, leads to a highlight of that annotation in the canvas area (or highlight of the visually represented annotation, respectively).

Our concept will be illustrated by screenshots of our prototype _Stereoscope_ that implements the most important features of the concept. Stereoscope is a web-based software prototype for visualizing two core processes of literary studies: hermeneutic exploration of textual meaning and construction of arguments about texts. In Stereoscope scholars can represent their manually created digital annotations with multiple visualizations to record and convey qualitative statements.[^12] In this article, we use a German-based text, but Stereoscope can be applied to texts in other languages, too.

{{< figure src="images/figure02.png" caption="User interface of the Stereoscope prototype with “overlays” layout selected" alt="A screenshot of a Stereoscope scatter plot of various colored circles in clusters."  >}}




## Text

The area on the left side shows the primary text a scholar is working on and the parts of the text that have already been annotated. Hovering over annotations produces a pop-up that informs about the categories of the annotations for the respective text passage. Annotations can be saved to a selection by clicking them. A toggle switch at the top of the text area allows scholars to switch between the linear text view and a view of the selected annotations.

The prototype allows to upload a text file together with an annotation file created by the software _CATMA_ . For practical purposes the prototype was developed to work with the CATMA format, however, a compatibility with other formats would be desirable.




## Canvas

The canvas is the larger area in the middle of the interface that serves as a plane for creating configurations expressed through visualizations. Each visualization contains circles of different sizes that represent annotations. We call these circles _glyphs_ . Their size informs the length of individual annotations. While the circles themselves are immutable, the position of glyphs on the canvas can change depending on the visualization layout scholars have selected. Furthermore, different types of relationships between annotations can be expressed with connecting lines between glyphs. Currently, there is only one type of relationship that depicts the degree of textual proximity of text passages in the _overlaps_ layout.

When hovering over a glyph a little pop-up reveals the type of annotation category. The category is also expressed by the color of the circle. Clicking on a glyph causes the text area to scroll to the corresponding annotated text passage. Analogous to the text area, alt-clicking on glyphs allows scholars to collect annotated text passages that can be viewed in the text area in the selected _annotations_ mode (Fig. 3).

{{< figure src="images/figure03.png" caption="Selected annotations mode: Collected annotations shown on the left and corresponding glyphs highlighted on the canvas" alt="Screenshot of a scatter plot with various colored circles depicting glyphs."  >}}


Using the scroll wheel of the mouse or a pinch gesture on the track pad visualizations can be zoomed in and out of and parts of the visualization can be moved into focus.

Above the canvas area different controls allow scholars to change the layout, show and hide panels and labels and export the current view as an image. We call the current state of the visualization on the canvas a “view” .

There are three selectable panels for filtering by annotation category, adding comments to a canvas view, and adjusting settings for individual visualizations. When activated, these overlay the canvas in the bottom half (Fig. 4). Scholars can currently select from three different types of visualizations: grid, scatterplot, and overlaps (network diagram). These visualizations are integrated into the prototype as template files and the list can be extended to incorporate further visualization techniques. Scholars are encouraged to add new visualizations that are suited to their individual research questions and needs.

{{< figure src="images/figure04.png" caption="Panels filter, comment and layout shown with three categories selected in the filter panel (Annotated text not falling under these categories is grayed out in the text area)" alt="A screenshot of a scatter plot with various colored circles."  >}}





## Views

The narrow column on the right side offers space for saving different views of the canvas as small thumbnails. Each view in this area consists of a miniature static image of the selected layout for the view, a title, the name of the layout, tags, and a button to assign tags. If a comment has been written for a particular canvas, it is shown here as well. The currently selected view is marked by an orange border. All manipulations of the canvas, like selected filters or glyphs, adjusted settings or a change in zoom state are saved automatically for each view and are re-established, when scholars click on other canvasses to switch to them.

Clicking the plus sign at the top opens a dialog window for adding a new view. Here, title, layout, and comment can be filled in. All the comments assigned to the views can be searched with a search field at the top. Typing something in there filters the list of views, fading out views that do not contain comments that match the search term. If tags have been assigned to views, clicking on one of them filters the list with the respective tag. In that way, either ad-hoc search strings or tags can be used to create temporary subselections of the list. Individual views can also be exported as images.




## Using the four postulates as guidelines for implementation

In this section, we will elaborate on the concrete development of a prototype using the four postulates. Naturally, this prototypical implementation is exemplary and not exhaustive. There are alternative ways of adhering to the postulates when developing a user interface.

As described in the previous part, understanding annotations as _capta_ rather than data, we accounted for this in the interface of the prototype with the possibility of assigning different attribute values to selected annotations (or glyphs, respectively). This is exemplified with two attributes scholars can add: certainty and importance. Both attributes take values on a scale from 1 to 5. Setting these values changes the appearance of the glyphs and saves the changes in the underlying JSON format (see Fig. 5). The altered JSON file can be downloaded for each individual view (by clicking on the respective icon on the thumbnail image in the views area). This functionality provides an example of the postulate of the _Two Way Screen_ , that could be extended to further functionality, like assigning other attributes or the change of categories, for example. Generally, when thinking about applying our concept to a full-fledged software tool, it would be desirable to integrate full annotation functionality into the system, while allowing the manipulation of annotation metadata via text as well as visualization.

{{< figure src="images/figure05.png" caption="Changing certainty and importance values changes the appearance of the glyphs and writes these changes to the JSON file" alt="A screenshot of a scatterplot showing one annotation."  >}}


When assigning certainty or importance values scholars create a qualitative statement about the epistemic status of annotations, in that way addressing the _Quality_ postulate. Qualitative statements are not restricted to the individual annotation. Adding comments and tags to views offers a way of making qualitative assessments about a particular configuration of annotations or collection of configurations, respectively (Fig. 6).

In the prototype, visualizations are always based on an automatic structuring algorithm, be it the two scales of the scatterplot or the forces operating in the network layout. In addition to it, the interface concept also includes a functionality that allows scholars to define the spatial structures themselves, for example, by positioning glyphs freely on the canvas or allowing to group them by encircling them with lines drawn on the canvas. Interacting with the glyphs on the canvas in such a way could also be a way to offer meta annotations.

{{< figure src="images/figure06.png" caption="Canvas with assigned comment and tags (Tags visible in the views area on the right side)" alt="A screenshot of a visualization showing a network with various colored circles connected by lines."  >}}


In the most basic way, the postulate of _Parallax_ is accomplished by presenting annotations in the context of the surrounding text in a linear fashion side by side with the different non-linear configurations represented by the visualization layouts. Furthermore, with the views area on the right side of the prototype it becomes possible to compare different configurations with each other by switching between them. On another level, the ambiguity mentioned in the postulate is exemplified by the certainty attribute values assigned to glyphs. When looking at a particular visualization on the canvas, the filter and settings panel allow scholars to change the foundation for the representation, for example, by showing only certain categories of annotations in the visualization or to change parameters regarding the visualization layout (Fig. 7).

The views column on the right side of the interface responds to the _Discourse_ postulate. Here, scholars are encouraged to build an argumentation out of visualizations (views) and texts (comments) as single observations.

{{< figure src="images/figure07.png" caption="“Enclosed” lines deselected in the settings panel (bottom right) for the overlaps layout" alt="A screenshot of a visualization of overlaps of various colored circles."  >}}


Tags assigned to views provide a structuring mechanism that can be used to form different argumentations out of the same views, thus presenting different possible readings to compare with each other.

Scholars can jump between views and, by clicking on them, in that manner read the argumentation in a non-linear way. By investigating individual views they can follow the argument down to the specific annotations in the text that constitute the foundation for the argument. This possibility to drill down creates a transparency in the argumentation that allows critical reflections on the rigor, intersubjectivity, and validation of the argumentation. Figure 8 shows the usage of several views for different argumentations (Fig. 8).

{{< figure src="images/figure08.png" caption="A scholar scrolls through views belonging to two different argumentations (three leftmost images). In the right image the tag “Häufungen und Lücken” representing one of the two argumentations has been selected." alt="A screenshot showing varies views of the interface."  >}}






## 5. Conclusions

In this article, we suggested four postulates as guidelines for developing hermeneutic visualizations. The resulting visualizations are designed to promote the connection of digital literary hermeneutics with digital approaches, since they address the epistemological premises of hermeneutics, as we have shown in our exemplary prototypical implementation guided by the postulates.

Looking at the hermeneutic visualizations in the prototype, one might notice that they have an appearance similar to traditional visualizations. This leads us back to the question formulated in the introduction: What do hermeneutic visualizations look like? In other words: Are we able to name distinctive qualities of hermeneutic visualizations?

The answer to this is to be found in the nature of hermeneutic theory expressed by the three premises and operationalized by the four postulates. While certainty and importance are typical examples of partial, contextual, and subjective knowledge and are expressed with the help of visual variables in the prototype, the central holistic premise demands an iterative, circular process of generating meaning and forming arguments that becomes visible in the structure of the user interface, but not primarily in individual visualizations.

Future implementations might put a stronger focus on the premise of the dependency between text and recipient (represented by the _Qualitative_ and _Parallax_ postulate), which might result in more examples of visual variables depicting partial, contextual and subjective knowledge or even completely new visualizations. Newness for its own sake, however, has not been our concern here.

Although the presented prototype has been iteratively developed and reviewed by the researchers within our team based on a real-world hermeneutic scenario (Interpretation of Franz Kafka’s _In der Strafkolonie_ ), we are interested to learn more about other scholars’ experience with the prototype in order to further study the appropriateness of the postulates and the idea of hermeneutic visualization. To this end, the prototype has been launched on a website for other scholars to use.[^13] In addition, the source code has been published on BitBucket[^14] in order to give interested scholars the opportunity to contribute to the development. Being aware that our prototype cannot address all eventualities of hermeneutic activity, we deemed it important to enable scholars to extend the repertoire of hermeneutic visualizations that can be used as arguments. The source code provides a visualization template that can be used to develop other visualizations. Following Hinrichs et al.<a class="footnote-ref" href="#hinrichs2019"> [hinrichs2019] </a>, we encourage scholars to come up with new visualizations and adjust existing hermeneutic practices, in that way building “sandcastles” and experimenting with hermeneutic visualizations. The prototype itself necessarily has to be a generic tool, that is capable of supporting a diverse range of hermeneutic scenarios.

Finally, we hope that our research might inspire other researchers to investigate what premises need to be considered in order for visualization to benefit other interpretative approaches. Since some attributes like ambiguity are not specific to hermeneutics, but common to all theories of interpretation, this research might serve as a starting point for the development of respective approaches in other areas.




## 6. Acknowledgements

The research and the software prototype Stereoscope was developed as part of the 3DH project _Three-Dimensional Dynamic Data Visualisation and Exploration for digital humanities Research_ at the University of Hamburg (04/2016–12/2018).[^15] The project is conducted by Jan Christoph Meister. Associated members are Marian Dörk (University of Applied Sciences Potsdam), Johanna Drucker (University of California), Evelyn Gius (TU Darmstadt), Geoffrey Rockwell (University of Alberta), Florian Windhager (Danube University Krems).

Furthermore, we would like to thank Jan Christoph Meister, Jan Horstmann and Marian Dörk for comments and suggestions on this paper.




## 7. Links


 * Article “Parallax” in _Oxford English Dictionary_ . Available at:[https://en.oxforddictionaries.com/definition/parallax](https://en.oxforddictionaries.com/definition/parallax)
 * [https://voyant-tools.org/](https://voyant-tools.org/)
 * [https://github.com/computationalstylistics/stylo](https://github.com/computationalstylistics/stylo)
 * [https://gephi.org/](https://gephi.org/)
 * [http://tapor.ca](http://tapor.ca)
 * [http://threedh.net/](http://threedh.net/)
 * [http://catma.de/](http://catma.de/)
 * [https://github.com/janerikst/stereoscope](https://github.com/janerikst/stereoscope)



[^2]: Original German text passages quoted or paraphrased above are translated by the authors of this paper.
[^3]: We acknowledge that the chosen terms overlap with terms for example likeheuristic, technique, practice.
[^4]: Krämer<a class="footnote-ref" href="#kramer2015"> [kramer2015] </a>points out that in the practice of text interpretation different theoretical approaches are often mixed up.
[^5]: Problems and critics of the hermeneutic circle cf. Danneberg (1995).
[^6]: [http://tapor.ca](http://tapor.ca)
[^7]: [https://github.com/computationalstylistics/stylo](https://github.com/computationalstylistics/stylo)
[^8]: [https://gephi.org/](https://gephi.org/)
[^9]: [https://voyant-tools.org/](https://voyant-tools.org/)
[^10]: These insufficiencies which many tools have in common do not prevent hermeneutic practice with them entirely. Literary scholars practicing an hermeneutic approach have found workarounds to enable a critical handling of these visualization tools despite their shortcomings.
[^11]: In our understanding hermeneutic visualizations have to be developed with respect to the user interface that is holding these visualizations. To be able to reconfigure, explore and form arguments with hermeneutic visualizations there has to be a user interface surrounding these visualizations that is oriented towards the hermeneutic process as a whole and allows the manipulation of the visualizations as well as the arrangement of them.
[^12]: [http://stereoscope.threedh.net/](http://stereoscope.threedh.net/)
[^13]: [http://threedh.janerikstange.com/](http://threedh.janerikstange.com/)(temporary domain)
[^14]: [https://github.com/janerikst/stereoscope](https://github.com/janerikst/stereoscope)
[^15]: [http://threedh.net/](http://threedh.net/)## Bibliography

<ul>
<li id="albrecht2015">Albrecht, A., Danneberg, L., Krämer, O., Spoerhase, C., (eds.) (2015). _Theorien, Methode und Praktiken des Interpretierens_ . Berlin: de Gruyter.
</li>
<li id="anderson2008">Anderson, C. (2008). “The End of Theory: The Data Deluge Makes the Scientific Method Obsolete” , in _Wired_ , 23/06/2008. Available at:<a href="https://www.wired.com/2008/06/pb-theory/">https://www.wired.com/2008/06/pb-theory/</a>.
</li>
<li id="armaselu2017">Armaselu, F., van den Heuvel, C., (2017). “Metaphors in Digital Hermeneutics: Zooming through Literary, Didactic and Historical Representations of Imaginary and Existing Cities” , in _DHQ: Digital Humanities Quarterly_ , 11(3). Available at:<a href="http://www.digitalhumanities.org/dhq/vol/11/3/000337/000337.html">http://www.digitalhumanities.org/dhq/vol/11/3/000337/000337.html</a>.
</li>
<li id="barbot2019">Barbot L., Fischer, F., Moranville, Y., Pozdniakov I. (2019). “Which DH Tools are actually used in Research?” , in weltliteratur.net, A Black Market for the digital humanities, Available at:<a href="https://weltliteratur.net/dh-tools-used-in-research/">https://weltliteratur.net/dh-tools-used-in-research/</a>.
</li>
<li id="baumann2020">Baumann, M., Koch, S., John, M., Ertl, T. (2020). “Interactive Visualization for Reflected Text Analytics” , in Reiter, N., Pichler, A., Kuhn, J. (eds.) _Reflektierte algorithmische Textanalyse. Interdisziplinäre(s) Arbeiten in der CRETA-Werkstatt_ , Berlin: de Gruyter, pp. 269-296.
</li>
<li id="berndt2009">Berndt, F. (2009). “In the Twilight Zone. Ambiguity and Aesthetics in Baumgarten” , in Berndt, F., Kammer, S. (eds.) _Amphibolie, Ambiguität, Ambivalenz_ . Würzburg: Königshausen & Neumann, pp. 121-137.
</li>
<li id="bertin1983">Bertin, J. (1983). _Semiology of Graphics: Diagrams, Networks, Maps_ . Madison: University of Wisconsin Press.
</li>
<li id="binder2014">Binder, F., Entrup, B., Schiller, I., Lobin, H. (2014). “Uncertain about Uncertainty: Different ways of processing fuzziness in digital humanities data” , in _Conference Abstracts_ , DH2014, pp. 95-98. Available at:<a href="https://d-nb.info/1164023926/34">https://d-nb.info/1164023926/34</a>.
</li>
<li id="boot2009">Boot, P. (2009). _Mesotext: digitised emblems, modelled annotations and humanities scholarship_ . Amsterdam: Amsterdam University Press.
</li>
<li id="bradley2008">Bradley, J. (2008). “Thinking about interpretation: Pliny and scholarship in the humanities” , in _Literary and linguistic computing_ , 23(3), pp. 263-279.
</li>
<li id="card1999">Card, S., Mackinlay, J., Shneiderman, B. (1999). _Readings in information visualization: Using vision to think_ . San Francisco: Kaufmann.
</li>
<li id="chamber2006">Chambers, E., Marshall G. (2006). _Teaching & Learning English Literature_ . Thousand Oaks: SAGE Publications.
</li>
<li id="correll2019">Correll, M. (2019). _Counting, Collaborating, and Coexisting: Visualization and the digital humanities_ . Available at:<a href="https://mcorrell.medium.com/counting-collaborating-and-coexisting-visualization-and-the-digital-humanities-1bf157400d8">https://mcorrell.medium.com/counting-collaborating-and-coexisting-visualization-and-the-digital-humanities-1bf157400d8</a>.
</li>
<li id="danneberg1995">Danneberg, L. (1995). “Die Historiographie des hermeneutischen Zirkels: Fake und fiction eines Behauptungsdiskurses” , in _Zeitschrift für Germanistik_ , 5(3), pp. 611-624.
</li>
<li id="derrida1967">Derrida, J. (1967). _De la grammatologie_ [dt. Grammatologie 1974, 2004]. Paris: Editions de Minuit, Frankfurt: Suhrkamp.
</li>
<li id="dork2013">Dörk, M., Feng P., Collins, C., Sheelagh C. (2013). _Critical InfoVis: Exploring the Politics of Visualization_ , in _alt.chi 2013_ : Extended Abstracts of the SIGCHI Conference on Human Factors in Computing Systems, ACM, pp. 2189-2198.
</li>
<li id="drucker2011">Drucker, J. (2011). “Humanities approaches to graphical display” , in _DHQ: Digital Humanities Quarterly_ , 5(1). Available at:<a href="http://www.digitalhumanities.org/dhq/vol/5/1/000091/000091.html">http://www.digitalhumanities.org/dhq/vol/5/1/000091/000091.html</a>.
</li>
<li id="drucker2016">Drucker, J. (2016). _3DH Visualizations: Three dimensional / digital humanities_ . Available at:<a href="https://pages.gseis.ucla.edu/faculty/drucker/3DH_Gallery/Text_3DH_Gallery.html">https://pages.gseis.ucla.edu/faculty/drucker/3DH_Gallery/Text_3DH_Gallery.html</a>.
</li>
<li id="drucker2018">Drucker, J. (2018). “Non-representational approaches to modeling interpretation in a graphical environment” , in _Digital Scholarship in the Humanities_ , 33(2), pp. 248-263.
</li>
<li id="eemeren2009">Eemeren, F., Grootendorst, R., Snoeck Henkemans, A. F. (1996, 2009). _Fundamentals of argumentation theory : a handbook of historical backgrounds and contemporary developments_ . New York, London: Routledge [Erlbaum].
</li>
<li id="gadamer1990">Gadamer, H.-G. (1960, 1990). _Hermeneutik I. Wahrheit und Methode. Grundzüge einer philosophischen Hermeneutik_ . Tübingen: Mohr.
</li>
<li id="galey2010">Galey, A., Ruecker, S. (2010). “How a prototype argues” , in _Literary and Linguistic Computing_ , 25(4), pp. 405-424.
</li>
<li id="gibson2014">Gibson, J. (2014). _The ecological approach to visual perception_ . London: Psychology Press.
</li>
<li id="giusjacke2017">Gius, E., Jacke, J. (2017). “The hermeneutic profit of annotation: on preventing and fostering disagreement in literary analysis” , in _International Journal of Humanities and Arts Computing_ , 11(2), pp. 233-254.
</li>
<li id="gius2017">Gius, E., Kleymann, R., Meister J.C., Petris M. (2017). “Datenvisualisierung als Aisthesis” , in _Conference Abstracts_ , DHd 2017, pp. 115-120. Available at:<a href="http://doi.org/10.5281/zenodo.4646123">http://doi.org/10.5281/zenodo.4646123</a>.
</li>
<li id="glinka2017">Glinka, K., Pietsch, C., Dörk, M. (2017). “Past Visions and Reconciling Views: Visualizing Time, Texture and Themes in Cultural Collections” , in _DHQ: Digital Humanities Quarterly_ , 11(2). Available at:<a href="http://www.digitalhumanities.org/dhq/vol/11/2/000290/000290.html">http://www.digitalhumanities.org/dhq/vol/11/2/000290/000290.html</a>.
</li>
<li id="groarke2017">Groarke, L. (2017). “Informal Logic” , in Zalta, E. (ed.) _The Stanford Encyclopedia of Philosophy_ . Available at:<a href="https://plato.stanford.edu/archives/spr2017/entries/logic-informal/">https://plato.stanford.edu/archives/spr2017/entries/logic-informal/</a>.
</li>
<li id="hinrichs2017">Hinrichs, U., Forlini, S. (2017). “In defense of sandcastles: research thinking through visualization in DH” , in _Proceedings of the conference on Digital Humanities_ . International Alliance of Digital Humanities Organizations (ADHO). Available at:<a href="https://dh2017.adho.org/abstracts/133/133.pdf">https://dh2017.adho.org/abstracts/133/133.pdf</a>.
</li>
<li id="hinrichs2019">Hinrichs, U., Forlini, S., Moynihan, B. (2019). “In defense of sandcastles: Research thinking through visualization in digital humanities” in _Digital Scholarship in the Humanities_ , 34(1), pp. 180-199. DOI:<a href="https://doi.org/10.1093/llc/fqy051">https://doi.org/10.1093/llc/fqy051</a>.
</li>
<li id="jacke2018">Jacke, J. (2018). “Manuelle Annotation” , in _forTEXT. Literatur digital erforschen_ . Available at:<a href="http://fortext.net/routinen/methoden/manuelle-annotation">http://fortext.net/routinen/methoden/manuelle-annotation</a>.
</li>
<li id="jahraus2002">Jahraus, O., Neuhaus, S. (eds.) (2002). _Kafkas Urteil und die Literaturtheorie. Zehn Modellanalysen_ . Stuttgart: Reclam.
</li>
<li id="jannidis2003">Jannidis, F., Lauer, G., Martínez, M., Winko, S. (eds.) (2003). “Der Bedeutungsbegriff in der Literaturwissenschaft. Eine historische und systematische Skizze” , in _Regeln der Bedeutung. Zur Theorie der Bedeutung literarischer Texte_ . Berlin: de Gruyter, pp. 3-32.
</li>
<li id="jannidis2017">Jannidis, F., Kohle, H., Rehbein, M. (eds.) (2017). _Digital Humanities. Eine Einführung_ , Stuttgart: Metzler.
</li>
<li id="jessop2008">Jessop, M. (2008). “Digital Visualization as a scholarly activity” , in _Literary and Linguistic Computing_ , 23(3), pp. 281-293.
</li>
<li id="jessing2007">Jeßing, B., Köhnen, R. (2007). _Einführung in Die Neuere Deutsche Literaturwissenschaft_ . Stuttgart [u.a.]: Metzler.
</li>
<li id="kath2015">Kath, R., Schaal, G., Dumm, S. (2015). “New Visual Hermeneutics” , in _Zeitschrift für germanistische Linguistik_ , 43(1), pp. 27-51.
</li>
<li id="kindt1976">Kindt, W., Schmidt, S. (1976). _Interpretationsanalysen: Argumentationsstrukturen in Literaturwissenschaftlichen Interpretationen_ . München: Fink.
</li>
<li id="kramer2015">Krämer, O. (2015). “Goethes Wahlverwandtschaften in Interpretationen von der Geistesgeschichte bis zum Poststrukturalismus” , in Albrecht, A., Danneberg, L., Krämer, O., Spoerhase, C., (eds.) (2015) _Theorien, Methode und Praktiken des Interpretierens_ . Berlin: de Gruyter, pp. 159-203.
</li>
<li id="koppe2013">Köppe, T., Winko, S. (2013). _Neuere Literaturtheorien. Eine Einführung_ . Stuttgart: Metzler.
</li>
<li id="latour1986">Latour, B. (1986). “Visualization and Cognition: Drawing Things Together” , in _Knowledge and Society: Studies in the Sociology of Culture Past and Present_ , 6, pp. 1-40.
</li>
<li id="maceachren2012">MacEachren, A. M., Roth, R. E., O'Brien, J., Li, B., Swingley, D., Gahegan, M. (2012). “Visual semiotics & uncertainty visualization: An empirical study” , in _IEEE Transactions on Visualization and Computer Graphics_ , 18(12), pp. 2496-2505.
</li>
<li id="mantzavinos2016">Mantzavinos, C. (2016). “Hermeneutics,”  _The Stanford Encyclopedia of Philosophy_ (Fall 2020 Edition), Edward N. Zalta (ed.).<a href="https://plato.stanford.edu/archives/fall2020/entries/hermeneutics/">https://plato.stanford.edu/archives/fall2020/entries/hermeneutics/</a>.
</li>
<li id="mccurdy2016">McCurdy, N., Lein, J., Coles, K., Meyer, M. (2016). “Poemage: Visualizing the Sonic Topology of a Poem” , in _IEEE Transactions on Visualization and Computer Graphics_ , 22(1), pp. 439–448.<a href="https://doi.org/10.1109/TVCG.2015.2467811">https://doi.org/10.1109/TVCG.2015.2467811</a>.
</li>
<li id="mersch2009">Mersch, D. (2009). “The Chiasmus of Language - Six Theses of Language and Alterity” , in Berndt, F., Kammer, S. (eds.) _Amphibolie, Ambiguität, Ambivalenz_ . Würzburg: Königshausen & Neumann, pp. 107-120.
</li>
<li id="meirelles2019">Meirelles, I. (2019). “Visualizing information” , in Flanders, J., Jannidis, F. (eds.) _The Shape of Data in the Digital Humanities. Modeling Texts and Text-based Resources_ . London, New York: Routhledge, pp. S. 167-177.
</li>
<li id="meister2017">Meister, J.C., Drucker, J., Rockwell, G. (2017). “Modeling Interpretation in 3DH: New dimensions of visualization” in _Proceedings of the conference on Digital Humanities_ . International Alliance of Digital Humanities Organizations (ADHO). Available at:<a href="https://dh2017.adho.org/abstracts/058/058.pdf">https://dh2017.adho.org/abstracts/058/058.pdf</a>.
</li>
<li id="meister2020">Meister. J.C., (2020). “Annotation als Mark-Up avant la lettre” , in Jannidis F., Winko, S., Rapp, A., Meister J.C., Stäcker T. (eds.) _Digitale Literaturwissenschaft_ . DFG-Symposium Villa Vigoni, 2017. Berlin, Boston: de Gruyter (to appear).
</li>
<li id="mittelstrab2008">Mittelstraß, J. (ed.) (2008). _Enzyklopädie Philosophie und Wissenschaftstheorie_ . Vol. 3. Stuttgart: Metzler.
</li>
<li id="nantke2020">Nantke, J., Schlupkothen, F. (eds.) (2020). _Annotations in Scholarly Editions and Research. Functions, Differentiation, Systematization_ , Berlin, Boston: de Gruyter.
</li>
<li id="nunning2008">Nünning, A. (2008). _Metzler Lexikon Literatur- und Kulturtheorie: Ansätze – Personen – Grundbegriffe_ . Stuttgart: Metzler.
</li>
<li id="nunning2010">Nünning, V., Nünning, A. (2010). _Methoden der literatur- und kulturwissenschaftlichen Textanalyse. Ansätze – Grundlagen – Modellanalysen_ . Stuttgart: Metzler.
</li>
<li id="otoole2018">O'Toole, M. (2018). _The Hermeneutic Spiral and Interpretation in Literature and the Visual Arts_ . New York: Routledge.
</li>
<li id="palmers1969">Palmers, R. E. (1969). _Hermeneutics. Interpretation Theory in Schleiermachers, Dilthey, Heidegger, and Gadamer_ . Evanston: Northwestern University Press.
</li>
<li id="piez2010">Piez, W., (2010). _Towards Hermeneutic Markup: An architectural outline_ . Available at:<a href="http://dh2010.cch.kcl.ac.uk/academic-programme/abstracts/papers/pdf/ab-743.pdf">http://dh2010.cch.kcl.ac.uk/academic-programme/abstracts/papers/pdf/ab-743.pdf</a>.
</li>
<li id="piotrowski2019">Piotrowski, M. (2019). “Accepting and Modeling Uncertainty” , in Kuczera, A., Wübbena, T., Kollatz, T. (eds.) _Die Modellierung des Zweifels – Schlüsselideen und -konzepte zur graphbasierten Modellierung von Unsicherheiten_ . Zeitschrift für digitale Geisteswissenschaften. Wolfenbüttel.<a href="https://zfdg.de/sb004_006">DOI: 10.17175/sb004_006a</a>.
</li>
<li id="piper2020">Piper, A. (2020). _Can We Be Wrong? The Problem of Textual Evidence in a Time of Data_ . Cambridge: Cambridge University Press.
</li>
<li id="radle2000">Rädle, F. (2000). “Argumentum” , in Fricke, H. (ed.) _Reallexikon der deutschen Literaturwissenschaft_ . Vol. 1. Berlin: de Gruyter, pp. 130-132.
</li>
<li id="rapp2017">Rapp, A. (2017). “Manuelle und automatische Annotation” , in Jannidis, F., Kohle, H., Rehbein, M. (eds.) _Digital Humanities. Eine Einführung_ . Stuttgart: Metzler, pp. 253-267.
</li>
<li id="ramsay2007">Ramsay, S. (2007). “Algorithmic criticism” , in Siemens, R., Schreibmann, S. (eds.) _A Companion to Digital Literary Studies_ . Oxford: Blackwell. Available at:<a href="http://www.digitalhumanities.org/companion/view?docId=blackwell/9781405148641/9781405148641.xml&chunk.id=ss1-6-7&toc.depth=1&toc.id=ss1-6-7&brand=9781405148641_brand">http://www.digitalhumanities.org/companion/view?docId=blackwell/9781405148641/9781405148641.xml&chunk.id=ss1-6-7&toc.depth=1&toc.id=ss1-6-7&brand=9781405148641_brand</a>.
</li>
<li id="ramsay2012">Ramsay, S., Rockwell, G., (2012). “Developing Things: Notes toward an Epistemology of Building in the Digital Humanities” , in Gold, M. (ed.) _Debates in the Digital Humanities_ . Available at:<a href="http://dhdebates.gc.cuny.edu/debates/text/11">http://dhdebates.gc.cuny.edu/debates/text/11</a>.
</li>
<li id="ramberg2005">Ramberg, B., Gjesdal, K. (2005). “Hermeneutics” , in Zalta, E. (ed.) _The Stanford Encyclopedia of Philosophy_ . Available at:<a href="https://stanford.library.sydney.edu.au/archives/sum2010/entries/hermeneutics/">https://stanford.library.sydney.edu.au/archives/sum2010/entries/hermeneutics/</a>.
</li>
<li id="rese2010">Rese, F. (2010). “Hans-Georg Gadamer” , in Martínez, M., Scheffel, M. (eds.). _Klassiker der modernen Literaturtheorie_ . München: Beck, pp. 168-190.
</li>
<li id="rockwell2003">Rockwell, G. (2003). “What is text analysis, really?” , in _Literary and linguistic computing_ , 18(2), pp. 209-219.
</li>
<li id="rockwellandsinclair2016">Rockwell, G., Sinclair, S. (2016). _Hermeneutica: Computer-assisted interpretation in the humanities_ . Cambridge, Massachusetts, London, England: The MIT Press.
</li>
<li id="samuels1999">Samuels, L., McGann, J. (1999). “Deformance and interpretation” , in _New Literary History_ , 30(1), pp. 25-56.
</li>
<li id="savigny1976">von Savigny, E. (1976). _Argumentation in der Literaturwissenschaft_ . München: Beck.
</li>
<li id="scheinfeldt2012">Scheinfeldt, T. (2012). “Where’s the Beef? Does Digital Humanities Have to Answer Questions?” , in Gold, M. (ed.) _Debates in Digital Humanities_ . Minnesota: University of Minnesota Press. Available at:<a href="http://dhdebates.gc.cuny.edu/debates/text/18">http://dhdebates.gc.cuny.edu/debates/text/18</a>.
</li>
<li id="schleiermacher1838">Schleiermacher, F. (1838). _Hermeneutik und Kritik_ . Deutsches Textarchiv. Available at:<a href="http://www.deutschestextarchiv.de/schleiermacher_hermeneutik_1838/8">http://www.deutschestextarchiv.de/schleiermacher_hermeneutik_1838/8</a>.
</li>
<li id="schwan2019">Schwan, H., Jacke, J., Kleymann, R., Stange, J. E., Dörk, M. (2019). “Narrelations – Visualizing Narrative Levels and their Correlations with Temporal Phenomena” , in _DHQ: Digital Humanities Quarterly_ , 13(3). Available at:<a href="http://www.digitalhumanities.org/dhq/vol/13/3/000414/000414.html">http://www.digitalhumanities.org/dhq/vol/13/3/000414/000414.html</a>.
</li>
<li id="selbmann2002">Selbmann, R. (2002). “Kafka als Hermeneutiker. Das Urteil im Zirkel der Interpretation” , in Jahraus, O., Neuhaus, S. (eds.) _Kafkas Urteil und die Literaturtheorie. Zehn Modellanalysen_ . Stuttgart: Reclam, pp. 36-58.
</li>
<li id="seifert2014">Seifert, C., Sabol, V., Kienreich, W., Lex, E., Granitzer, M. (2014). “Visual analysis and knowledge discovery for text” , in _Large-Scale Data Analytics_ . New York: Springer, pp. 189-218.
</li>
<li id="sinclair2013">Sinclair, S., Ruecker, S., Radzikowska, M. (2013). “Information Visualization for Humanities Scholars” , in Price, K. M., Siemens, R. (eds.). _Literary studies in the digital age: An evolving anthology. New York: Modern Language Association_ . Available at:<a href="https://www.researchgate.net/publication/273450219_Information_Visualization_for_Humanities_Scholars">DOI: 10.1632/lsda.2013.6</a>.
</li>
<li id="spree2000">Spree, A. (2000). “Interpretation” , in Fricke, H. (ed.): _Reallexikon der deutschen Literaturwissenschaft_ . Vol. 2. Berlin, New York: de Gruyter, pp. 168-172.
</li>
<li id="stiegler2015">Stiegler, B. (2015). _Theorien der Literatur- und Kulturwissenschaften_ . Paderborn: Schöningh.
</li>
<li id="stiening2016">Stiening, G. (2016). “Hermeneutik. Über die Grenzen des Verstehens und die Gefahren ihrer Missachtung” , in Jahraus, O. (ed.) _Zugänge zur Literaturtheorie_ . Stuttgart: Reclam, pp. 54-70.
</li>
<li id="szondi1995">Szondi, P. (1995). _Introduction to literary hermeneutics_ . Trans. by Martha Woodmansee. Cambridge: Cambridge University Press.
</li>
<li id="theron2018">Therón, R., Losada, A. G., Benito, A., Santamaría, R. (2018). “Toward supporting decision-making under uncertainty in digital humanities with progressive visualization” , in _Proceedings of the Sixth International Conference on Technological Ecosystems for Enhancing Multiculturality_ , pp. 826-832.
</li>
<li id="unsworth2000">Unsworth, J. (2000). “Scholarly primitives: What methods do humanities researchers have in common, and how might our tools reflect this” , in _Symposium on Humanities Computing: Formal Methods, Experimental Practice_ . King’s College, London, 3.
</li>
<li id="weimar2000">Weimar, K. (2000). “Hermeneutik” , in Fricke, H. (ed.): _Reallexikon der deutschen Literaturwissenschaft_ . Vol. 2. Berlin, New York: de Gruyter, pp. 25-29.
</li>
<li id="winko2003">Winko, S. (2003). “Textanalyse” , in Fricke, H. (ed.): _Reallexikon der deutschen Literaturwissenschaft_ . Vol. 2. Berlin, New York: de Gruyter, pp. 597-601.
</li>
<li id="zirker2017">Zirker, A., Bauer, M. (2017). “Explanatory Annotation in the Context of the Digital Humanities: Introduction” , in _International Journal of Humanities and Arts Computing - A Journal of Digital Humanities_ , 11 (2017), pp. 145-152.
</li>
<li id="zundert2016">van Zundert, J. (2016). “Screwmeneutics and hermenumericals: the computationality of hermeneutics” , in Schreibmann S., Siemens, R., Unsworth J. (eds.) _A New Companion to Digital Humanities_ . Oxford: Wiley Blackwell, pp. 331-347.
</li>

</ul>
