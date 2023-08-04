---
type: article
dhqtype: article
title: "Vivas to those who have failed: Walt Whitman Electric and the (Digital) Humanities"
date: 2020-12-20
article_id: "000503"
volume: 014
issue: 4
authors:
- Nicole Gray
translationType: original
abstract: |
   Digital methods in the humanities have helped to create the potential for resurrecting an experimental, recuperative critical mode that approaches literature in terms of its transformability. This essay draws on Walt Whitman’s poems and his material practices to model this mode by interweaving the transformative logics of poetry and code. This can help to illuminate the structural mechanics of each, as well as their mutual dependence on figurative language. These resonances speak to the diverse human voices, practices, and forms of creativity that define digital humanities work today no less than the poetry and print of past centuries.
teaser: "This articles examines a Walt Whitman manuscript through the lens of code."
order: 17
---

> He sees eternity less like a play with a prologue and denouement . . . . he sees eternity in men and women . . . he does not see men and women as dreams or dots.
[Walt Whitman, preface to _Leaves of Grass_ (1855)](#whitman1855)


## Introduction

The field that has emerged as the digital humanities started with dreams and dots: pixelated digits and, beyond them, the prospect of methods and archives that could encompass almost an infinite number of texts. As it has grown it has developed a reputation as one of the few comparatively well-funded, expanding fields in an increasingly de-funded, precariously or under-employed academic humanities.[^1] It has also been criticized for a lack of ethnic and gender diversity and an unwillingness to think across cultures or to reckon with the theoretical insights of the humanities more generally.[^2] 

As a result, in part, of these criticisms, the moment for work at the intersection of digital methods and the humanities has never been more exciting. Creators of forums like #TransformDH, #DHpoco, and #GlobalOutlookDH have worked to transform the digital humanities by opening up space for a more diverse set of practitioners and voices. Projects like the Colored Conventions Project and the Mukurtu CMS have built tools organized around artifacts and knowledge practices associated with African American and Indigenous communities. Scholars and programmers worldwide are engaging questions of access, training, and opportunity.

With these developments have also come a set of theoretical provocations, challenges to return to the difficult work of thinking about digital media and its relationship to human beings.[^3]  “[T]he black digital humanities promotes a system of change,” Kim Gallon has written: “it is a mechanism for deregulating the tendency of technological tools, when employed in the digital humanities, to deemphasize questions about humanity itself” <a class="footnote-ref" href="#gallon2016"> [gallon2016] </a>. This transformative mode of thinking, the call to interrogate basic concepts and assumptions, shares some ground with an earlier moment in digital humanities. In the early 2000s, the SpecLab at the University of Virginia, led by Johanna Drucker and Jerome McGann, conducted a series of textual experiments with that era’s digital tools. These experiments in text and technology were informed by a methodological approach called “deformance” , a creative and playful mode of reading.[^4] One goal of this speculative, theoretical work was an ongoing effort to reimagine key literary terms liketextandwork.

As digital methods that quantify and specify have come to play a prominent role in the digital humanities, perhaps it is worth exploring a complementary return to such ludic and experimental modes.[^5] In the context of the transformation of the digital humanities by scholars of race and gender, however, we may need to reconceptualize the practice and the nomenclature ofdeformanceto one of transformability.[^6] The malleability of form, for those who study connections between the body and identity, is a politically charged matter oriented toward the future as well as the present. Transformability shifts the focus from a product or process that has happened in the past, or is happening in the present, to the crucial role of imagination in turning to what is possible in the future. Transformability involves not only the many forms the text _has_ taken — the realm of book history — or the many forms the text _does_ take — the realm of textual editing — but also the many forms the text _could_ take, the vast scope of its potential iterations within historical fields of embodied practice.

Using Walt Whitman as a case study, this essay explores the ways that the dreams of an American poet have been and could be expressed in dots, presenting an opportunity and a provocation to apply the formal logic of machines to poems, and vice versa. Miriam Posner has written that a useful challenge for the digital humanities, now that many of its methods have become established, might involve rethinking some of the most basic structures and binaries enacted by data. The current political and cultural moment points to the importance of testing the logics that have made machines so functional and so central to human existence in the twenty-first century. Inseparable from such logics are complicated questions, long fundamental to poetry, about kinship, race or ethnicity, age, and gender — differences among human beings that affect the uses to which machines are put and the ways in which they have shaped and been shaped by historical narratives.

Whitman is a useful case study in part because his knowledge about and investment in the technologies of print so thoroughly inform both his composition practices and his poetry. Transformation, and to some extent failure, also define his engagement of race over the course of his lifetime. Recent critical assessments have shown the ways Whitman grappled with trying to develop a national poetry at a moment when the nation’s internal contradictions were tearing it apart. The opposition to slavery and the forms of identification with enslaved people visible in his early poems largely gave way, after the U.S. Civil War, to a much more lukewarm position on the rights of freed slaves and other Americans of African descent.[^7] 

In the poem eventually titled “Song of Myself,” Whitman calls on his readers to “Unscrew the locks from the doors! / Unscrew the doors themselves from their jambs!” <a class="footnote-ref" href="#whitman1855"> [whitman1855] </a>. If this were a hermeneutic challenge, one might propose questions tailored to our technological and philosophical moment: what would a model of criticism look like that combines a deconstruction of performative authorship, the thought-experiment of a (failed) mechanism, and a detailed attention to the material characteristics of an artifact? What lies between the sociology of the door-closer and the sociology of the text?[^8] How do we map the crossroads of reparative reading and algorithmic criticism?[^9] This essay draws on structures of computational processing to reimagine and ultimately transform a manuscript draft of lines that have been at the heart of critics’ discussions of Whitman’s poetic treatment of race. Combining the ludic with the Luciferic, it engages a struggle with embodiment in a text from the past in order to frame that text’s transformation and re-embodiment in a troubled present.

In the first section of the essay, I discuss practices of text encoding and electronic transformation in widespread use by editors of humanities texts, arguing that such practices resonate linguistically and structurally with Whitman’s own poetic and material practices. The second section of the essay situates Whitman’s poem “The Sleepers” as a model for a critical approach that taps into a dialectic of dreams and failure that has been influential in the imagination and the politics of the United States. Casting thedreamspaceWhitman creates in “The Sleepers” as an analogue of namespaces in computer and information science, I suggest that it functions as a transformative, experimental environment in which dreams, failure, contingency, and intentionality combine to produce radical insights and forms of identification. To exhibit that potential, I transform a manuscript draft fragment of “The Sleepers” into a basic script written in the programming language Python. Such transformations have much to offer the critical imagination, drawing our attention to new textual dimensions and to the points at which poetic dreams fail to become functional dots or durable reparative interventions.




## This electric self:Machine Logics and the Transformability of Text

One of the notable revisions Whitman made to his poem “Bardic Symbols,” first published in the _Atlantic Monthly_ in 1860, between that initial publication and its final version ( “As I Ebb’d With the Ocean of Life” ) in later editions of _Leaves of Grass_ , was to substitute the wordelectricfor the wordeternal.Setting the stage for poetic reflection, Whitman wrote in the 1860 version:
> I, musing, late in the autumn day, gazing off southward,Alone, held by the eternal self of me that threatens to get the betterof me and stifle me
<a class="footnote-ref" href="#whitman1860"> [whitman1860] </a>This self was still eternal in 1867, but by the 1881 edition of _Leaves_ , published just two years after Thomas Edison filed a U.S. patent for an electric lamp with a carbon filament, Whitman had revised both lines:
> I musing late in the autumn day, gazing off southward,Held by this electric self out of the pride of which I utter poems
<a class="footnote-ref" href="#whitman1881"> [whitman1881] </a>Now electric rather than eternal, the poet’s self has also along the way become a prideful source of utterance rather than a stifling force. In becoming electric, the self is no longer alone, no longer occupied in wrestling with itself, but now turned outward and uttering poems.[^10] 

The distance from the electric to the electronic self is a matter of a century, a couple of commonplace characters, and some successful inventions. Success, a word with roots in genealogical as well as temporal succession, can be considered to drive much of the work of description and transformation that is today fundamental to electronic editing and data manipulation in computational environments. The markup language XML, with the specific vocabulary created by the Text Encoding Initiative (TEI), has come to dominate the practice of digital editorial work on humanities texts.[^11] As is the case with computer programming and markup languages more generally, the functionality of XML and its related languages depends on logic.

The wordlogicis derived from the Greekλόγος, which has often been translated asword.Logic can refer to a formal system of reasoning depending on symbolic and mathematical procedures to establish claims, or, in a more loosely defined sense, to a set of rules or structures by which argumentation, reasoning, or understanding can be enacted within a given context (logic, _n_ .). Butλόγοςis a complicated concept that extends further, encompassing speech or utterance, teaching, collecting, discourse, mind, principle, law, act, reckoning, cause, form, and pattern, as well as rational (or spiritual, or divine) order, or even revelation — all with just a hint of temporality, drawing on the idea oforiginalororiginary.[^12] I will use logic throughout this essay to refer both to the structure of language, utterance, or argument and to this more complex sense, a spiritualized form of expression, the _making material_ of structure or order in the world, divine or otherwise.

The logic of XML depends on breaking data into machine-readable, processable parts, enforcing the description or the creation of boundaries. These boundaries ideally correspond to clearly defined units or categories, and they enable the construction of hierarchies and relationships. In the case of TEI these categories relate to inscribed materials like manuscripts or books. TEI also often encodes other categories that have been developed over years of academic production, like categories of genre, which underwrite the coherence of the discipline of literary criticism even as they are frequently challenged in individual studies. The logics that combine in the encoding practices and syntax of TEI are thus several, including logics of inscriptive technologies like the book and the manuscript, logics of categorical differences in style observed and enacted by literary criticism, and logics of information and meta-information that developed in library and computational contexts.

The textual crux represented by the wordeternalin Whitman’s “Bardic Symbols,” for example, could be expressed in TEI. In a single file that described multiple versions of the poem, the tags `<app>` (for critical apparatus entry) and `<rdg>` (for reading), with the attribute `@wit` (to point to a textual witness), could be used to mark two versions of the line: 
```xml
<app> <rdg wit="#lg1860"> <l>Alone, held by the eternal self of me that threatens <lb/>to get the better of me, and stifle me,</l> </rdg> <rdg wit="#lg1881"> <l>Held by this electric self out of the pride of which I utter poems,</l> </rdg> </app>
```
 Marking the text in this way reproduces several logics: the structural logic of the text (marking the line as a line with `<l>` ); the logic of the critical apparatus that describes textual revision or versions of the text over time ( `<app>` and `<rdg>` ); and the logic of the printed page, which consists of both inked characters and white space ( `<lb/>` or line break).

A transformation of the text could proceed at the level of any of these logics, or all of them together. One could produce all the different versions of the line, one after the other, so they would display sequentially in a Web browser; or compare them as text strings and generate a visualization of the differences; or show the line in the context of other lines from the poem; or create a toggle allowing users to view or eliminate the line breaks, functionally reformatting the text. Data marked in XML can be transformed into Hypertext Markup Language (HTML), which in turn can be combined with display instructions to render readable, manipulable text in Web browsers. As display technologies and standards develop, XML remains useful, in theory, because the basic assumption is that it can be transformed into any number of other languages or data formats.

For Whitman, as the change frometernaltoelectricwould suggest, the line from “Bardic Symbols” was transformable when he wrote it and remained so even after it was printed. He orchestrated several transformations of both wording and appearance between 1860 and the final printing of the line in his lifetime in the 1891-2 _Leaves of Grass_ . To mark the line with TEI does not alter its ontological status, but it does produce new options for transformability in a digital environment. We might say that digital transformation is simply an extension of the imagination of transformability that, for Whitman, was a basic condition of textual production.

The syntax of transformation provides a surprisingly poetic point of continuity. The transformation of XML, like the original markup, is an interpretive act, introducing display and navigation elements that structure the reader’s experience of a text. A primary language of transformation in such cases is Extensible Stylesheet Language Transformations (XSLT), one of three recommendations that make up the broader language family XSL.[^13] XSL depends on kinship as its metaphor for expressing locations, finding nodes in a document tree hierarchy based on paths articulated as a matter of succession. In the case of XML Path Language (XPath), the expression language used by XSLT, succession is a means of expressing relationships between elements or nodes.[^14] The road from XML to HTML is navigated with siblings, parents, children, ancestors, and descendants. In order to select all of the `<rdg>` nodes to render a particular reading in a TEI file with an XPath that locates them in their relation to their parent `<app>` elements, for instance, you might use the notation: `<xsl:apply-templates select="child::rdg"/>` . In plain (more or less) English, you could say that you are instructing the stylesheet to apply a series of transformations to any reading ( `<rdg>` ) that is a child of the current node.

The logics and syntax of modern markup and transformation languages used for editing depend on a set of technical metaphors, terms for describing relationships that, in the case of XSL and many other languages, draw from family and nature — the stuff of poetry. And Whitman thought in machine logic, too, although his machine was the printing press. The kinds of material transformations that Whitman’s texts underwent in the nineteenth century bear some resemblance to the file transformations and structural logics of the electronic age. Whitman’s poetic transformations often involved cutting and pasting.[^15] Modularity was key, and Whitman, a former printer, often composed with the structure of the printed text in mind. When he received proofs of a set of notes about Elias Hicks that would form part of his 1888 volume _November Boughs_ , for instance, Whitman noted to the printer that he wanted the section to begin on an odd-numbered page:

{{< figure src="images/figure01.png" caption="Page proof of “Notes (such as they are) founded on Elias Hicks.” Walt Whitman Papers in the Charles E. Feinberg Collection. Library of Congress, Washington, D.C." alt=""  >}}


This move made logical sense for situating the Hicks essay as a new section of the prose in the volume — but it also reflected Whitman’s practice of repurposing sections and binding them into later book issues.[^16] He habitually arranged for the printing of poems and other materials independently on slips of paper, using them as the basis for proofing, sending them out for publication, circulating them among friends and acquaintances, and in some cases adding them into books. In ways that anticipated the concerns of twenty-first-century information scientists, Whitman designed his chunks of poetry and prose to be materially interoperable. If they were arranged such that they could be printed on separate sheets or gatherings, they could be assembled into other books or bound and distributed independently.[^17] 

Like XML-marked data today, Whitman’s modular text could be used for a number of (multimedia) futures. Both books and languages like XML depend on structured relations, definitions, hierarchies, and dependencies. And yet the imagination that selects and designs particular transformations is, as tools and books develop, an increasingly crucial component of digital processing. Whitman’s imagination of text and its possible transformations was shaped by the technologies of his time. We face a similar effect today, as critical and creative imaginations are challenged by machines that enable new forms of transformation, as humanities texts and machine languages combine in novel and interesting ways, and as practitioners are increasingly conversant in the logics of both. Conceived as a language whose use-value and sustainability were grounded in the possibility of transformation, XML is in certain ways an investment in the future of both technology and imagination.




## In the ruin, the sediment:Poetic Dreams and Electric Failures

In Whitman’s early, much-revised and much-discussed poem “The Sleepers,” the dreaming poet begins out of sorts: “I wander all night in my vision, / ... / Wandering and confused . . . . lost to myself . . . . ill-assorted . . . . contradictory” <a class="footnote-ref" href="#whitman1855"> [whitman1855] </a>.[^18] And yet the poet is capable, in this dream vision, of acts of acrobatic transcendence and identification. In “The Sleepers,” Whitman first included and then edited out arguably his most striking identification across racial boundaries, lines in which the poet speaks as an enslaved person.[^19] 

Whitman had explored dreams as a space for transcending boundaries as early as his pre- _Leaves of Grass_ fiction, and he may have been tapping into a genre of dream visions in literature. The unsettled mental state of the dreamer at the start of the dream in Whitman’s “The Sleepers” and in his fiction is like that of other dream-vision narrators. The space of the dream for Whitman is liminal, in the sense that it seems to exist somewhere between pure presence and pure transcendence. In it the world of possibility is expanded, sometimes alarmingly.[^20] Critics have argued that the redemptive vision at the close of “The Sleepers,” in which the poet describes the sleepershand-in-handin a restorative sleep through which the illnesses and inequities of the world are healed, is a classicdream visionculmination of wandering in greater understanding and a sympathetic poetic enlightenment.[^21] 

Another way to think about Whitman’s dreamspace — one quite out of time — would be to think of it as a kind of poetic namespace. In computer and information science, namespaces denote distinctions among objects (entities) or vocabularies, establishing boundaries around a specific collection of symbolic terms and related definitions. The use of namespaces allows for combinatory worlds in which the same word, element or object might mean something different in a specified context, or have a different relationship to other words, elements, or objects. Namespaces are often expressed using prefixes. One might, for instance, distinguish between the dreamspaceI(ds:I) of “The Sleepers” and the waking space poeticI(ws:I) of the other poems in the first edition of _Leaves of Grass_ . Let us say `<ds:I>` experiences discomfort, but possesses an ability to see and identify with the population of sleepers that extends beyond even as it informs the ability of `<ws:I>` .

The premise of namespaces and elements is the ability to declare entities like `<ds:I>` and distinguish them from other entities both within a namespace and outside of it. The striking thing about Whitman’s dreamspace in “The Sleepers,” however, is the very impossibility of that activity. In dreamspace, the night is a spatial as well as a temporal setting: of the sleepers, the poet writes, “The night pervades them and enfolds them” <a class="footnote-ref" href="#whitman1855"> [whitman1855] </a>. The poet, too, both penetrates and enfolds the sleepers he describes. The poem begins with description: the poet, “Pausing and gazing and bending and stopping,” simply looks at the sleepers. Next, he comes closer — “I pass my hands soothingly to and fro a few inches from them” — but still the restless sleepers sleep fitfully<a class="footnote-ref" href="#whitman1855"> [whitman1855] </a>. He then joins them, sleeping and dreaming with them — “I sleep close with the other sleepers, each in turn; / I dream in my dream all the dreams of the other dreamers” <a class="footnote-ref" href="#whitman1855"> [whitman1855] </a>. Finally, his dreaming produces a deeper identification: “And I become the other dreamers.” In this state the poet pervades the dreamers like the night, taking on their identities — “I am the actor and the actress” — and acting in their stead. The poet of dreamspace transcends the boundaries between himself and the people he describes. The descriptive work of dividing the sleepers into individuals becomes the work of drawing them together through the consciousness and the transformative dream-vision of the poet. As the poem concludes, the sleepers rest “hand in hand,” unified and beautiful in sleep, and the poet passes from night into day<a class="footnote-ref" href="#whitman1855"> [whitman1855] </a>.

 “Elements merge in the night,” Whitman writes in “The Sleepers.”  “The antipodes, and every one between this and them in the dark, / I swear they are averaged now . . . . one is no better than the other, / The night and sleep have likened them and restored them” <a class="footnote-ref" href="#whitman1855"> [whitman1855] </a>. If the work of descriptive markup or the creation of distinct entities as part of XML namespace vocabularies involves breaking things down into parts, dreamspace might serve as an impetus to imagine ways of bringing them back together — or to recognize the artificiality of their separation. Like night in “The Sleepers,” dreamspace enables the existence, or the imagination of the existence, of two simultaneous possibilities: a difference and a cosmic averaging. Dreamspace brooks mathematical experimentation, perhaps because its elements and entities are defined contingently, in relation to deep, incomprehensible forces — not the natural forces of physics and institutional agency that guide the elements and entities of waking life, but something more inward-looking and subjective. In Whitman’s dreamspace, imaginative forays begin to mediate difference, bridging the gap between entities, even those posed as binary opposites. Transformability has both conceptual and material dimensions for Whitman, informing his dreams of poetic identification as well as his practices of revision and bookmaking.

If the digital humanities represents a field in which the logics of programming and machines are called upon to revise the patterns of humanistic and philosophical inquiry, where multiple namespaces may coexist and serve co-articulated purposes, perhaps dreamspace can be cast as a foil to the functional side of programming, an invocation of the vocabulary of experimentation, of margins, of imagination, and of failure. In an essay on the methodological potentials of repair, Steven Jackson casts breakdown as a starting point in thinking about new media. Noting the role of shipbreaking in Bangladesh, where the raw materials of old ships are recycled into usable products, Jackson situates failure as one stage in a longer story, one in which breakdown and decay form constitutive components of existence in the twenty-first century, and in which imagination and reconfiguration are key to building sustainable practice<a class="footnote-ref" href="#jackson2014"> [jackson2014] </a>.

In science and technology worlds, failure (in moderation) has long held a special status. As journalists and media scholars have pointed out, the vision of failure as a preliminary step in success continues to be lionized in thefail fast, fail oftenmantra associated with Silicon Valley, however well the mantra corresponds to actual conditions of employment and production.[^22] Stories of failure in a rapidly developing media world have an analogue in the newspapers and periodicals of the nineteenth-century. Frank Luther Mott’s histories of early American newspapers and magazines showcase the way such productions went under with sometimes bewildering regularity. Newspapers were not the only industry full of folds, of course — Scott Sandage, tracing the ubiquitous failures of merchants in the nineteenth-century U.S., notes that “in addition to those who went broke or bankrupt, thousands of businessmen teetered on the brink for years” <a class="footnote-ref" href="#sandage2005"> [sandage2005] </a>. Failure, according to Sandage, is the substory of the idea that came to be known as the American Dream. Constituting a central part of stories and experiences of life in the U.S., but never quite fitting into the vision the republic had of itself, failure lingered uncomfortably at the boundaries of success and identity for the American nineteenth century.

In the economic sense that would be associated with failure in the nineteenth-century United States, Whitman’s first edition of _Leaves of Grass_ , self-published in 1855, was undeniably a failure. An unusual book in both size and manufacture, the first edition of _Leaves_ lacked a formal publisher and was set in type between other non-literary jobs at Andrew Rome’s Brooklyn printing shop. Whitman’s friend Horace Traubel reported in _With Walt Whitman in Camden_ that “W[hitman] spoke about the first edition of the Leaves: “It is tragic — the fate of those books. None of them were sold — practically none — perhaps one or two, perhaps not even that many. We had only one object — to get rid of the books — to get them out someway even if they had to be given away” ” <a class="footnote-ref" href="#traubel1906"> [traubel1906] </a>.[^23] 

Today, copies of Whitman’s first edition of _Leaves of Grass_ are listed for sale at prices that range from $50,000 to $270,000.[^24] The books that once failed to sell are now the most expensive and sought-after of the editions of _Leaves of Grass_ . Failure has a place in the narrative of literary production, which like that of technology often centers on dreams, succession, and innovation. For Whitman, the arc of the future and its changing literary preferences fueled the popularity of his work over a century and a half of massive historical and technological changes. In the wake of a transformation in the value readers found in the poems that comprised his _Leaves of Grass_ , the first edition has re-emerged as a site of interest. Its rarity, combined with critical and popular consensus about the value of Whitman’s poems, has helped to make it one of the most expensive books of American literature on the market today. In the same economic sense that once rendered it a failure, one might say that the 1855 _Leaves of Grass_ has become a resounding success.

Discussions of the digital humanities, too, are threaded throughout with tales of failure. Failures in the collection of essays titled _A New Companion to Digital Humanities_ , updated in 2016, include the failures of collaboration<a class="footnote-ref" href="#edmond2016"> [edmond2016] </a>, of fabrication<a class="footnote-ref" href="#sayers2016"> [sayers2016] </a>, of interdisciplinarity<a class="footnote-ref" href="#mccarty2016"> [mccarty2016] </a>, of technology/hardware, of the imaginers of design fictions to account for humanities concerns about ethics and culture<a class="footnote-ref" href="#jorgensen2016"> [jorgensen2016] </a>, of data to interoperate, of the search string to correspond exactly with the search meaning, and so on. Happily, in none of these cases is failure conceived as a reason not to attempt. Indeed, the failure often produces different insights and, in some cases, visions with more comprehensive impact.

Whitman splintered his poetry and prose into pieces, but like the shipbreakers he also brought it back together again in diverse and imaginative ways. One of his friends, Harrison S. Morris, recollected a story about the poet:
> He said an idea would strike him which, after mature thought, he would consider fit to be the “special theme” of a “piece.” This he would revolve in his mind in all its phases, and finally adopt, setting it down crudely on a bit of paper, — the back of an envelope or any scrap, — which he would place in an envelope. Then he would lie in wait for any other material which might bear upon or lean toward that idea, and, as it came into his mind, he would put it on paper and place it in the same envelope. After he had quite exhausted the supply of suggestions, or had a sufficient number to interpret the idea withal, he would interweave them in a “piece,” as he called it. I asked him about the arrangement or succession of the slips, and he said, “They always fall properly into place.” 
[(Qtd. in Kennedy [1896], 24)](#kennedy1896)Did Whitman ever think about failure, as he scratched out lines, cut and pasted, shuffled scraps in envelopes, relying on, in place of the muse, the seemingly mutual co-determinative pull of randomness and data? Do we think of failure as we gather, create, and transform data, trying not to let the questions determine the answers, trying not to let the machine be too much a reflection of our own biases and preconceptions? Is there any creative or analytical work that is not haunted by failure?

As he walks the shore, the poet of Whitman’s “Bardic Symbols” ponders the deposits of the waves, “In the ruin, the sediment, that stands for all the water and all the land of the globe.” The detritus or sediment cast onto the shore is not random (being at least in part the product of known and ordered industries or natural phenomena like shipbuilding, trade, and weather). Neither is it fully recognizable. The poet laments his inability to understand the meaning of the debris — “Oh, I think I have not understood anything, — not a single object, — and that no man ever can!” The signs or bardic symbols represent a momentary configuration, but also a cosmic and historical culmination. Recognition in this poem occurs when the poet stops trying to read, to find a pre-determined meaning, and embraces the transformative work of metaphor.

Struck shortly into “Bardic Symbols” by an “old thought of likenesses,” the poet begins to think about poetry as he observes the detritus. “Bardic Symbols” becomes a poem about printing and inscription as much as it is about a poet observing the sea. “I wish I could impress others,” the speaker begins, using language drawn from the technology of inscription of his time — the printed impression, the pressure of metal type on the page exerted by the printing press. Later, in an ecstasy of recognition, he exclaims “I, too, leave little wrecks upon you, you fish-shaped island!” and concludes by looking up from the page to the reader:
> We, capricious, brought hither, we know not whence, spread out before you, —you, up there, walking or sitting,Whoever you are, — we, too, lie in drifts at your feet.
Capricious, brought hither, through space and time, the drifts take the shape of the inked characters on the page or — now — the pixels or dots on the screen. The “semiotic ecology” of poetry encompasses the cast-off detritus of the ocean as well as of print, and all the forms future likenesses take<a class="footnote-ref" href="#drucker2013"> [drucker2013] </a>. Whitman’s drift, a complicated co-articulation of randomness and intentionality, offers a proleptic vision of digital textuality.[^25] 




## Seized by the spirit that trails in the lines underfoot:Re-scripting Race

Guided by transformability and repair, we might break Whitman’s “Sleepers” back down into draft segments and imagine them further, beyond the familiar ground of TEI and namespaces, into Python, one of today’s most powerful and widely used programming languages.[^26] Like Emily Dickinson’s description of reading poems backward, seized by Samuels and McGann as a provocation for deformance, transforming or translating poetry into a programming script defamiliarizes elements of both, opening the door — or unscrewing it entirely — inviting insights at the intersection of digital and poetic logics.[^27] With particular force, this operation helps to demonstrate the ways in which what Ivy Wilson has described as “the presence of African Americans — suspended between the material and the apparitional, as it were — within the poetic space of [Whitman’s] verse and other writings” could be made to speak back to both the containment of Black U.S. citizens and deterministic, abstract narratives of technological development<a class="footnote-ref" href="#wilson2014a"> [wilson2014a] </a>.

The culminating dramatic moment in the poem that would be titled “The Sleepers,” more dramatic in the form of one of several manuscript drafts, has a striking conditional:
> I am a hell-name and a Curse:TheBlack Lucifer was not dead;Or if he was, I am his sorrowful, terrible heir


{{< figure src="images/figure02.png" caption="Manuscript draft of lines eventually used in “The Sleepers.” Papers of Walt Whitman, 1838-1987. Clifton Waller Barrett Library of American Literature, Albert and Shirley Small Special Collections Library, University of Virginia." alt=""  >}}


From the narrative present of the poem, the speaker looks back to a past time: “Black Lucifer _was_ not dead.” As Ed Folsom has written, the possible sources for Whitman’s Lucifer are many, from the Biblical Isaiah’s reference to “a fallen king of Babylon,...a reference that led to the mistaken notion that Lucifer was the fallen angel from heaven, Satan,” to an ignitable match, to a nineteenth-century _Webster’s Dictionary_ description of Lucifer as “the planet Venus, when appearing as the morning star” <a class="footnote-ref" href="#folsom2001"> [folsom2001] </a><a class="footnote-ref" href="#folsom2000"> [folsom2000] </a>. Folsom notes that in one early notebook, “Whitman lists gods, including Lucifer, who are defined as made up of all that opposes hinders, obstructs, revolts ” <a class="footnote-ref" href="#folsom2000"> [folsom2000] </a>. Lucifer was not dead, the poet-historian, poet-interpreter, asserts — only to undercut the assertion. _Or if he was..._ Neatly bifurcating historical or spiritual time with a possibility, the poet-historian-slave follows one conditional path and moves confidently into the present: “I am his sorrowful, terrible heir.” 

Folsom situates this manuscript as one of several draft versions in which the speaker ceases to speak for the enslaved person and instead speaks _as_ the enslaved person, in a culminating act of identification. The deleted line in this draft shows the speaker beginning with a declaration of identity that is at once naming and invective: “a hell-name and a Curse.” [^28] The fracture or bifurcation of historical/spiritual time introduces the capacity for the speaker to transform, fully, into the divine. As (possible) heir of Black Lucifer, the speaker becomes “the God of Revolt — deathless sorrowful vast.” The draft moves then into the future: “I will either destroy them him or they he shall release me.” 

The published versions of the lines that appeared in the 1855 edition of _Leaves of Grass_ incorporate several revisions, among them the first word of theLuciferline:
> Now Lucifer was not dead . . . . or if he was I am his sorrowful terrible heir;I have been wronged . . . . I am oppressed . . . . I hate him that oppresses me,I will either destroy him, or he shall release me.
<a class="footnote-ref" href="#whitman1855"> [whitman1855] </a>Whitman’s substitution ofNowforBlackis one example of his removal of explicit references to race that appeared in the manuscripts.[^29] Functioning as a transitional word,Nowemphasizes the temporal disjunction of this passage, moving to a new section of dreamspace in this poem about sleepers. But it also opens the door to another apparitional development: the historical moment and the institution of slavery have provoked an emergence that resurrects the God of Revolt, as undead (deathless) or in the form of succession.

The revision between manuscript draft and published poem situates the lines within the larger temporal frame of the poem, which flits, dreamlike, among past, present, and future. Other words already in the draft describe the complicated conditions of both genealogical and temporal succession. The operators in the lines of this manuscript — OR, IF — form the axes of legibility for many programming languages. If these lines were a script written in Python, they might look like: 
```python
def us_slavery(year): year = int(year) if 1619 <= year <= 1863: self = 'enslaved' else: self = 'free' return self def heir(I): I = 'his sorrowful, terrible heir' return I def lucifer(state): I = 'self' if state == 'no': lucifer = 'Black_Lucifer' return lucifer else: I = heir(I) return I def sleepers(): I = 'hell-name' self = 'Curse' year = int(input('What year is it? ')) self = us_slavery(year) if 1849 <= year < 1881: state = input('Was Black Lucifer dead? ') I = lucifer(state) if I != 'Black_Lucifer': print('I am',I) I = ['the God of Revolt','deathless','sorrowful','vast'] for i in I: print('I am',i) else: if not self: print('REVOLT') elif year >=1881: print('A show of the summer softness\na contact of something unseen\nan amour of the light and air') elif 1776 <=year < 1849: print('We hold these truths to be self-evident\nthat all men are created equal') else: print('Replica of the Great Hole of history') sleepers()
```
 [^30] 

Segments of the “Sleepers” manuscript can be produced by the Python script, which enacts executable parts of the poem. Depending on the date a user enters, the execution of the script might generate parts of the draft lines of the manuscript version, or it might generate other lines completely. The parameters are time, history, and the state of existence of Black Lucifer. In this transformation, succession returns to somewhere just short of its biological roots: Lucifer’s conditional successor is a function and a refraction of American slavery. As a “hell-name and a Curse,” Lucifer or his heir is handed down across borders of time and space, iterations of manuscript and print, evolutions of communicative machinery, to emerge briefly and dramatically in a peculiar, failed, breakthrough book of American poetry — or on your computer screen.

The kinship of languages is framed as relations of history (origin, reproduction), but recast as a matter of space, execution, and transformation within the specific, limited temporality of the script, or of dreamspace, or of the boundaries of the logics declared in our interpretations. The program points to the significance and the operability of the conditional. The poem points to the significance and the inoperability of the past tense. For the loop, something is or is not.Wasis not operable or definable within the space of the loop. It could be argued that it is enacted by the space outside the loop, and the variables are handed down. But what must come outside the loop to begin to approximate the meaning? The entire history of U.S. slavery and oppression, condensed into a series of expressions? Would they be definitions, or descriptions, or conditionals?

That computers can draw critical attention to patterns that sometimes go overlooked by the human eye has formed the appeal behind many digital methods. One of the most powerful characteristics of computational analysis tools like text mining classification algorithms is that they can be trained or tweaked by programmers based on specific data or results sets. Can the attention of researchers also be trained to look more closely at the kinds of words that machines would find actionable or significant?[^31] What would it mean to experiment with training as a mutual process, a kind of projection by a human into a computational mode of processing? In a world of posthumanist criticism, the insights of macroanalysis may be used to conduct even closer readings — to see the value in Whitman’stheand hisoras well as hisleavesand hisgrass.Such attention may, as Matthew Wilkins has noted, “suggest that there’s a low-level linguistic basis for the category distinctions we’ve long been inclined to draw.” It might also help us to produce new readings of well-traveled passages.

Book historians and bibliographers have demonstrated that the formal and linguistic interference of the editor is a crucial component of the afterlife of the work, and therefore its continued life in time. “Acts of translation and editing are especially useful forms of critical reflection,” McGann writes, “because they so clearly invade and change their subjects in material ways” <a class="footnote-ref" href="#mcgann2016"> [mcgann2016] </a>. The heart of the way text is increasingly imagined today — the product of our data-vision — is itstransformability. This transformability is a matter of succession, but not always of success. Whitman, an early exponent of modularity or transformability as a fundamental characteristic of textual production, serves as an instructive precursor. His transformational approach is visible in the scraps he shuffled in envelopes, the many editions of _Leaves of Grass_ , and his re-making of books more generally.

Programming, perhaps for everyone, but particularly for those of us not formally trained in the art, becomes a study in errors. In writing the sleepers.py script, I encountered a series of errors: 
```python
TypeError: us_slavery() missing 2 required positional arguments: 'self' and 'year' NameError: name 'slave' is not defined NameError: name 'I' is not defined Traceback (most recent call last): File "sleepers.py", line 21, in sleepers lucifer = Black_Lucifer NameError: name 'Black_Lucifer' is not defined Traceback (most recent call last): File "sleepers.py", line 40, in sleepers lucifer = lucifer(input("Was Black Lucifer dead? ")) UnboundLocalError: local variable 'lucifer' referenced before assignment
```
 The errors — TypeErrors, NameErrors, UnboundLocalErrors — that I produced in the making of sleepers.py mostly had to do with variables, either undefined or not included as part of the execution of a function that required them. In the case of a finished, working script, of course — or a script developed by an experienced, trained programmer — one may be less likely to encounter errors. Nor is it necessarily clear after the fact, unless a log or versioning system is associated with the development and made accessible as a complement to the resource, that they existed. Such data often fades into an invisible history of development, or it vanishes by virtue of being overwhelmed by an avalanche of incremental changes, commits, updates, migrations, transformations, deletions, and additions.[^32] In this case, perhaps as a conceit, one might argue that the errors formed a layer of the transformation, the undefinedness of the variable part of its poetic interpretation. The missing definitions represent segments of American history as it is performed in Whitman’s poems: the specific identity of the reader, the ambiguity of the designations ofslaveandI.Somewhere between the failures of the programmer and the untranslatability of the poem fragment lurks the impossible largeness of poetry, its ambiguities and its historical roots, the unexecutable complicating presence of the undefined and the undefinable.

Before the publication of the 1881 edition of _Leaves of Grass_ , Whitman returned to pages from an earlier edition to revise “The Sleepers” for republication. On those pages, Whitman created a textual event, a deletion of the “Lucifer” passage:

{{< figure src="images/figure03.png" caption="A page from “The Sleepers,” with Whitman’s edits. Walt Whitman Papers in the Charles E. Feinberg Collection. Library of Congress." alt=""  >}}


Editing these and other lines out of his dreamspace, Whitman produced a final version of the poem tuned to a different historical present and different priorities on the part of the poet.[^33] For Whitman, it would seem, the moment for the conjunction of experimental dreamspace with historical possibility had passed. If all you looked at was the 1891,authorizededition of _Leaves of Grass_ , you would never know the self of “Bardic Symbols,” now titled “As I Ebb’d With the Ocean of Life,” had once been eternal — or that Lucifer had ever been there at all.

Luckily, Whitman’s was not the final word on the matter. Transformation is one path to the other side of determinism — a methodology that resurrects fragments, writes dysfunctional scripts, and attends to errors, absences and deletions. Media have always had to do with light and darkness, shadow and space, figures, icons, and projections. They can affect the visibility of history, passion, identification or difference. Perhaps media technologies become most apparent when the binaries break down in the act of translation, transformation, or remediation: in error, or, sometimes, in deletion. Moments at which multiple possibilities exist, suspended in space, can look suspiciously like moments of failure to the backwards glance of history: _Or if he was_ . From this vantage point we watch Whitman on the verge, pencil in hand, weighing the path of erasure. The penciled bars of his hashmark deletion bought “The Sleepers” into a newNow,a post-war moment in which the promise of Lucifer’s heir — “I will either destroy him, or he shall release me” — may have echoed uncomfortably even for many former abolitionists, by then inclined toward reconciliation. The voice of the former slave and his descendants would continue to be locked away and suppressed from full political participation up to and beyond the emergence of Jim Crow in a series of criminal acts of silencing, violence, and oppression whose ongoing existence and implications are abundantly visible in our own time. But in that first conditional instant, thatNowin which the God of revolt was summoned, is alsosuccess, if only in the form of the recognition that one is part of a succession, sorrowful or otherwise.




## Conclusion:I, too, Paumanok

A 2007 _PMLA_ special topic forum about the digital editorial project _The Walt Whitman Archive_ exposed fundamental disagreements about the use of metaphors as substitutions for precise descriptions of digital tools.[^34] Demystifying the tools, however, does not rid us of metaphors, nor of the responsibility of navigating the complicated interplay of imagination, history, language, functionality, exclusion, and desire that defines the use and development of any technology. The transformative work of metaphor continues to inform the way technology functions, as well as the ways literary scholars can put it to work. Using imagination to cast seemingly competing logics against one another, to put pressure on the resonances between the words and the workings of poetic and machine language of the past and present, is one tool among many for training the attention to linger on a particular moment in a poem or other creative work and tease out some of its existing or potential implications.

Creative transformations applied to materials made digitally available by projects like the _Whitman Archive_ can act as provocations to think and act and edit differently. In some cases, this may be a way to explore how underrepresented populations and perspectives are addressed (or erased) in historical documents. Recognition that race, gender, and other forms of diversity have shaped the historical record is finally beginning to affect textual and technological theory in ways that are slowly filtering back into editorial approaches, the digitization of literary and historical documents, and the work of thinking about the multiple versions of those documents in relation to the many different people whose histories they often imperfectly represent.

 “If an electronic scholarly project can’t fail and doesn’t produce new ignorance,” John Unsworth wrote in a 1997 essay, “then it isn’t worth a damn.” The costs of failure or confessing ignorance, in the face of today’s confident, practiced users of digital tools and a historically bad tenure-track academic job market in the humanities, seem unusually high. Contingent, part-time, or adjunct positions can feel an awful lot like failure, without any guarantee of transformation, productive or otherwise. The current funding situation for the humanities and, increasingly, for education more broadly, is easily tied to the worst human motives — greed, racism, nativism, fear — and the darkest political prospects. Redefining the goals and parameters of success and failure for any project may be particularly necessary at such a time. Somewhere in theorizations like Sedgwick’s, or in Jackson’s repair, may be a glimmer of light, in the form of a call for the work of maintaining projects to become visible, for a broader notion ofsuccessto make that phenomenon visible in more places, for transformations of fields and texts to create the space for new voices and insights, and for the role of creation to be recognized in forms of labor other than authorship or innovation.

Is it time for the digital humanities to fail? As the humanities increasingly engages computation as a practice fundamental to the production of scholarship, or as the field called the digital humanities continues to splinter into method-specific approaches, we might resolutely cultivate one of its most exciting vectors: the emergence of a recuperative, radically experimental critical mode. In this mode, the imagination that fuels transformability is key, and failure holds a place of crucial importance. As Whitman’sselfbecame electrified over the course of the nineteenth-century manifestations of “Bardic Symbols,” so might we find in the digital detritus of our own day an electrifying vision of the future, a set of new critical possibilities to build out of the ships and the shipwrecks of history, as well as the transformable lines of poetry and prose to which they give rise.




## Acknowledgements

My thanks to Brett Barney, Matt Cohen, Mike Cohen, Ken Price, and Steve Ramsay for their thoughtful comments on drafts of this essay. Thanks also to the anonymous reviewers for their helpful suggestions.


[^1]: On this phenomenon as perception and as evolving actuality, see[Kirschenbaum (2010)](#kirschenbaum2010)and[(2012)](#kirschenbaum2012)
[^2]: This criticism has prompted a series of conversations about postcolonial, feminist, and queer digital humanities, as well as meditations on the possible complicity of digital methods with neoliberal agendas. See[#transformDH](#transformdh)and[#DHpoco](#dhpoco)for examples of the former; for the latter, see[Allington et al. (2016)](#allington2016)and[Greenspan’s (2019)](#greenspan2019)response.
[^3]: Bailey writes that “The move from margin to center offers the opportunity to engage new sets of theoretical questions that expose implicit assumptions about what and who counts in digital humanities as well as exposes structural limitations that are the inevitable result of an unexamined identity politics of whiteness, masculinity, and ablebodiness.” <a class="footnote-ref" href="#bailey2011"> [bailey2011] </a>
[^4]: Websites for SpecLab and the Applied Research in Patacriticism group are now defunct, though legacy versions are accessible through the Internet Archive’s Wayback Machine. See Samuels and McGann’s development of the term “deformance” in relation to critical interpretation, editing, and translation, and elaborations by McGann ( _Radiant Textuality_ ) and Drucker ( _SpecLab_ ). Later work by scholars and artists like Nick Montfort, Mez Breeze, and Alan Sondheim offers other examples of the creativity that has emerged at the intersection of art and algorithms. For further discussion of codework, the integration of programming syntax and creative expression, see[Raley (2002)](#raley2002).
[^5]: QueerOS is a notable recent example of this kind of imaginative work (see[Barnett et al. [2016]](#barnett2016)). Play was proposed as a methodology for #DHpoco, as well; see Koh and Risam.
[^6]: The “emphasis was placed on de- rather than transformance,” McGann writes, “in order to show that the object of critical reflection is not ultimately directed to the sign as such but to the rhetorical scene and its functional (social) operators, not least of all the person(s) engaged in the acts of deformance we commonly locate in a file headed Interpretation ” <a class="footnote-ref" href="#mcgann2001"> [mcgann2001] </a>.
[^7]: See[Klammer (2006)](#klammer2006);[Folsom (2000)](#folsom2000)and[Folsom (2014)](#folsom2014); and[Mancuso (1997)](#mancuso1997).
[^8]: See[Latour (1988)](#latour1988)and[McKenzie (1999)](#mckenzie1999), respectively.
[^9]: Ramsay’s algorithmic criticism is an effort to “locate a hermeneutics at the boundary between mechanism and theory” that explores transformation as key to the generation of humanities “data” <a class="footnote-ref" href="#ramsay2011"> [ramsay2011] </a>. Sedgwick’s reparative reading continues to offer a provocative possibility of thinking beyond (even computer) binaries, in part because it suggests that the fact that boundaries may structure our world in fundamental ways need not determine the kinds of actions or thoughts that must be taken in relation to or as a function of that knowledge<a class="footnote-ref" href="#sedgwick2003"> [sedgwick2003] </a>
[^10]: The first substantive revision to the second line appeared in the 1867 edition of _Leaves of Grass_ : “Alone, held by this eternal self of me, out of the pride of which I have utter’d my poems” <a class="footnote-ref" href="#whitman1867"> [whitman1867] </a>. See[Gilmore (2009)](#gilmore2009)for a discussion of the electrical and technological developments that underpinned the transformation of the poem titled “Poem of the Body” in 1856 to “I Sing the Body Electric” in 1867 and later editions.
[^11]: The use of XML has been questioned, and in several cases alternatives proposed (see e.g.[Schloen and Schloen [2014]](#schloen2014)), but as inline or embedded markup it remains a common approach to encoding data and a standard for digital scholarly editing.
[^12]: See[Liddell-Scott-Jones](#liddell). Biblical commentary has explored the meaning ofλόγοςin the context of John 1:1 ( “In the beginning was the Word...” ). See, e.g.,[Jeffrey and Morris (1992)](#jeffrey1992)and[Vincent (1889)](#vincent1889).
[^13]: These include XSL-FO, XSLT, and XPath<a class="footnote-ref" href="#xslw3c"> [xslw3c] </a>.
[^14]: This language of succession was inherited from earlier markup and stylesheet languages: the development of XSL syntax was influenced by SGML and its stylesheet language DSSSL, which in turn had been based on earlier programming and query languages. On the history and development of XSL, see[Kay (2008), 26-40,](#kay2008)and[“Transformation.”](#w3c)For a general discussion of lineal trees (and other metaphors) in relation to algorithms and computational data structures, and within a longer history of graph theory, see[Knuth (1973), 305-406](#knuth1973).
[^15]: For further discussion of Whitman’s collaging as fundamental to his poetry composition, see[Miller (2010)](#miller2010).
[^16]: In an entry in _With Walt Whitman in Camden_ dated July 31, 1888, Horace Traubel noted as much: “W. has an idea of putting the Hicks-Fox matter eventually into a special pamphlet. Made many changes of the make-up in order to get the Hicks started on an odd page. This is one of his memorandums to the printer: “begin making up Elias Hicks on page 119 I will supply something for page 118” ” <a class="footnote-ref" href="#traubel1906"> [traubel1906] </a>. For another example of sheets that Whitman published independently and had bound into other volumes, see the entry for _Passage to India_ (1871) in[Winship (1991), 36](#winship1991).
[^17]: See[Winship (1991)](#winship1991),[Myerson (1993)](#myerson1993),[Stallybrass (2019)](#stallybrass2019), and[Grossman (2019)](#grossman2019)for inventories and descriptions of Whitman’s publications and printed slips. This comparison is not meant to gloss over Tara McPherson’s important points about the racial and political implications of the “lenticular” logic of modularity and interoperability in the development of modern computing<a class="footnote-ref" href="#mcpherson2012"> [mcpherson2012] </a>.
[^18]: The poem is untitled (or assigned the recurring title “Leaves of Grass” ) in the 1855 edition. It appeared in the 1856 _Leaves of Grass_ as “Night Poem” and in the 1860-1 and 1867 editions as “Sleep-Chasings.” It was first titled “The Sleepers” in 1871.
[^19]: For a discussion of this poem and related manuscript drafts, see[Folsom (2001)](#folsom2001).
[^20]: A murder is juxtaposed to dream and sleeping scenes in Whitman’s temperance novel “Franklin Evans.” 
[^21]: See, for instance,[French (1990)](#french1990).
[^22]: See, for instance,[Surowiecki (2014)](#surowiecki2014),[Draper (2017)](#draper2017), and[Newman (2017)](#newman2017). See also[Liu (2004a)](#liu2004a).
[^23]: Whitman probably exaggerated here, as often in his discussions with Traubel.
[^24]: Estimates are based on prices and sales figures for copies listed on AbeBooks.com and sold at rare book auctions between 2018 and 2020.
[^25]: On Whitman’s concept of drift and its relation to the distribution and circulation of his writing, see[Cohen (2017)](#cohen2017).
[^26]: GitHub’s 2019 “Octoverse Report” ranked Python as the second most-used language in Git repositories, based on number of unique contributors<a class="footnote-ref" href="#zhou2019"> [zhou2019] </a>. Python, like other programming languages and software platforms, has recently begun to reckon with its metaphors. See[Oberhaus (2018)](#oberhaus2018)on the use and removal of the termsmasterandslave.These terms have long been used (and recently, in some cases, deprecated) in other engineering and computational contexts, including as references to central and backup servers, primary and secondary drives, and primary and replica databases. For further discussion, see[Eglash (2007)](#eglash2007)and[Landau (2020)](#landau2010).
[^27]: Samuels and McGann quote Dickinson’s note, from “an undated fragment on a leaf of stationery:”  “Did you ever read one of her Poems backward, because the plunge from the front overturned you? I sometimes (often have, many times) have–a Something overtakes the Mind–” <a class="footnote-ref" href="#samuels1999"> [samuels1999] </a>.
[^28]: Whitman works through this line in other drafts. For a complete list of transcriptions of the known drafts of these lines, see[Gray (ed.; 2020)](#gray2020)line 1775[https://whitmanarchive.org/published/LG/1855/variorum/main.html#l1775](https://whitmanarchive.org/published/LG/1855/variorum/main.html#l1775).
[^29]: See[Folsom (2014)](#folsom2014);[Price (2004), 17-18](#price2004); and[Sandler (2014), 71-74](#sandler2014).
[^30]: For the line `elif year>=1881:` , if the user enters a year later than or equal to 1881, she returns another line from the version of “The Sleepers” published in the 1881 edition of _Leaves of Grass_ , since the “Lucifer” lines are no longer present. For the line `elif 1776 <=year <1849:` , if the user enters a year after the date of U.S. independence (1776) and prior to the approximate earliest probable date of the manuscript (1849), she returns a line from the Declaration of Independence. On the final print command, see[Parks (1995), 159](#parks1995).
[^31]: For text mining purposes, as Jockers and Underwood point out, “we know from years of authorship-attribution research that the most effective features for distinguishing one author’s style from another’s are high-frequency features such as the words the, of, him, her, and and, as well as common marks of punctuation” <a class="footnote-ref" href="#jockers2016"> [jockers2016] </a>.
[^32]: On the role of this kind of invisibility in the capitalistic exploitation of creativity, see[Liu (2004b)](#liu2004b).
[^33]: For a discussion of this deletion and other omissions as related to Whitman’s increasing concern about the role of Blacks in the Reconstruction and post-Reconstruction U.S., see[Folsom (2000), 52-77](#folsom2000). See also[Klammer (2006)](#klammer2006). Whitman deleted other sections from the poem, as well: see, for instance, the two sections beginning “O hot-cheek’d and blushing! O foolish hectic!” 
[^34]: See[Folsom (2007)](#folsom2007);[McGann (2007)](#mcgann2007); and[Hayles (2007)](#hayles2007).## Bibliography

<ul>
<li id="allington2016">Allington, Daniel, Sarah Brouillette, and David Golumbia. “Neoliberal Tools (and Archives): A Political History of Digital Humanities.”  _Los Angeles Review of Books_ (May 1, 2016).<a href="https://lareviewofbooks.org/article/neoliberal-tools-archives-political-history-digital-humanities/">https://lareviewofbooks.org/article/neoliberal-tools-archives-political-history-digital-humanities/</a>Accessed 13 September 2020.
</li>
<li id="bailey2011">Bailey, Moya Z. “All the Digital Humanists Are White, All the Nerds Are Men, but Some of Us Are Brave.”  _Journal of Digital Humanities_ 1.1 (2011).
</li>
<li id="barnett2016">Barnett, Fiona, Zach Blas, Micha Cárdenas, Jacob Gaboury, Jessica Marie Johnson, and Margaret Rhee. “QueerOS: A User’s Manual.” Klein and Gold, 2016.<a href="dhdebates.gc.cuny.edu/debates/text/56">dhdebates.gc.cuny.edu/debates/text/56</a>. Accessed 20 July 2018.
</li>
<li id="cohen2017">Cohen, Matt. _Whitman’s Drift: Imagining Literary Distribution_ . Iowa City: University of Iowa Press, 2017.
</li>
<li id="ccp"> _Colored Conventions Project_ . University of Delaware. coloredconventions.org. Accessed 1 August 2018.
</li>
<li id="dhpoco">dhpoco.org. Curated by Adeline Koh and Roopika Risam. Accessed 10 July 2018.
</li>
<li id="draper2017">Draper, Nora. “Fail Fast: The Value of Studying Unsuccessful Technology Companies.”  _Media Industries_ , 4.1 (2017).
</li>
<li id="drucker2013">Drucker, Johanna. “From A to Screen: The Migration of Letters.”  _Comparative Textual Media_ , ed. N. Katherine Hayles and Jessica Pressman. Minneapolis: University of Minnesota Press, 2013.
</li>
<li id="drucker2009">Drucker, Johanna. _SpecLab: Digital Aesthetics and Projects in Speculative Computing_ . Chicago: University of Chicago Press, 2009.
</li>
<li id="edmond2016">Edmond, Jennifer. “Collaboration and Infrastructure.” Schreibman et al., 54-65.
</li>
<li id="eglash2007">Eglash, Ron. “Broken Metaphor: The Master-Slave Analogy in Technical Literature.”  _Technology and Culture_ 48.2 (April 2007).
</li>
<li id="xslw3c"> “The Extensible Stylesheet Language Family (XSL).” W3C.<a href="http://www.w3.org/Style/XSL/">www.w3.org/Style/XSL/</a>. Accessed 20 September 2020.
</li>
<li id="folsom2007">Folsom, Ed. “Database as Genre: The Epic Transformation of Archives.”  _PMLA_ 122.5 (October 2007): 1571-9.
</li>
<li id="folsom2014">Folsom, Ed. “Erasing Race: The Lost Black Presence in Whitman’s Manuscripts.” Wilson, ed., 3-31.
</li>
<li id="folsom2000">Folsom, Ed. “Lucifer and Ethiopia: Whitman, Race, and Poetics before the Civil War and After.”  _A Historical Guide to Walt Whitman_ , ed. David S. Reynolds. New York: Oxford University Press, 2000. 45-96.
</li>
<li id="folsom2001">Folsom, Ed. “Walt Whitman’s “The Sleepers.” ”  _The Classroom Electric: Dickinson, Whitman, and American Culture_ . 2001.<a href="http://bailiwick.lib.uiowa.edu/whitman/sleepers/">http://bailiwick.lib.uiowa.edu/whitman/sleepers/</a>. Accessed 18 April 2018.
</li>
<li id="french1990">French, R. W. “Whitman’s Dream Vision: A Reading of “The Sleepers.” ”  _Walt Whitman Quarterly Review_ 8.1 (Summer 1990): 1-15.
</li>
<li id="gallon2016">Gallon, Kim. “Making a Case for the Black Digital Humanities.” Klein and Gold, 2016.<a href="dhdebates.gc.cuny.edu/debates/text/55">dhdebates.gc.cuny.edu/debates/text/55</a>. Accessed 10 July 2018.
</li>
<li id="gilmore2009">Gilmore, Paul. _Aesthetic Materialism: Electricity and American Romanticism_ . Stanford: Stanford University Press, 2009.
</li>
<li id="gray2020">Gray, Nicole, ed. _Leaves of Grass (1855) Variorum_ . The Walt Whitman Archive, 2020.<a href="https://whitmanarchive.org/published/LG/1855/variorum/index.html">https://whitmanarchive.org/published/LG/1855/variorum/index.html</a>. Accessed 27 September 2020.
</li>
<li id="greenspan2019">Greenspan, Brian. “The Scandal of Digital Humanities.” Klein and Gold, 2019.<a href="https://dhdebates.gc.cuny.edu">https://dhdebates.gc.cuny.edu</a>. Accessed 12 September 2020.
</li>
<li id="grossman2019">Grossman, Jay. “Manuprint.”  _Walt Whitman Quarterly Review_ , 37.1 (Summer/Fall 2019): 46–65.
</li>
<li id="hayles2007">Hayles, N. Katherine. “Narrative and Database: Natural Symbionts.”  _PMLA_ 122.5 (October 2007): 1603-8.
</li>
<li id="jackson2014">Jackson, Steven J. “Rethinking Repair.”  _Media Technologies: Essays on Communication, Materiality and Society_ , ed. Tarleton Gillespie, Pablo J. Boczkowski, and Kirsten A. Foot. Cambridge: MIT Press, 2014.
</li>
<li id="jeffrey1992">Jeffrey, David Lyle and Leon Morris. “Logos.”  _A Dictionary of Biblical Tradition in English Literature_ , ed. David L. Jeffrey. Grand Rapids, MI: William B. Eerdmans, 1992. 459-61.
</li>
<li id="jockers2013">Jockers, Matthew L. _Macroanalysis: Digital Methods and Literary History_ . Champaign, IL: University of Illinois Press, 2013.
</li>
<li id="jockers2016">Jockers, Matthew L. and Ted Underwood. “Text-Mining the Humanities.” Schreibman et al., 291-306.
</li>
<li id="jorgensen2016">Jørgensen, Finn Arne. “The Internet of Things.” Schreibman et al., 42-53.
</li>
<li id="kay2008">Kay, Michael. _XSLT 2.0 and XPath 2.0: Programmer’s Reference_ . 4th ed. Indianapolis, IN: Wiley Publishing, Inc., 2008.
</li>
<li id="kennedy1896">Kennedy, William Sloane. _Reminiscences of Walt Whitman_ . London: Alexander Gardner, 1896.
</li>
<li id="klammer2006">Klammer, Martin. “Slavery and Race.”  _A Companion to Walt Whitman_ , ed. Donald D. Kummings. Malden, MA: Blackwell, 2006. 101-121.
</li>
<li id="klein2012">Klein, Lauren F., and Matthew K. Gold, eds. _Debates in the Digital Humanities_ . Minneapolis: University of Minnesota Press, 2012, 2016, and 2019.<a href="https://dhdebates.gc.cuny.edu/">https://dhdebates.gc.cuny.edu/</a>.
</li>
<li id="kirschenbaum2012">Kirschenbaum, Matthew. “Digital Humanities As/Is a Tactical Term.” Klein and Gold, 2012.<a href="dhdebates.gc.cuny.edu/debates/text/48">dhdebates.gc.cuny.edu/debates/text/48</a>. Accessed 20 July 2018.
</li>
<li id="kirschenbaum2010">Kirschenbaum, Matthew. “What Is Digital Humanities and What’s It Doing in English Departments?”  _ADE Bulletin_ 150 (2010): 55-61.
</li>
<li id="knuth1973">Knuth, Donald E. _The Art of Computer Programming_ . Vol. 1. 2nd edition. Reading, MA: Addison-Wesley Publishing Company, 1973.
</li>
<li id="koh2013">Koh, Adeline and Roopika Risam. “The Origins of #DHpoco and the Art of Play.”  _Postcolonial Digital Humanities_ (20 March 2013). Dhpoco.org.
</li>
<li id="landau2010">Landau, Elizabeth. “Tech Confronts Its Use of the Labels Master and Slave. ”  _Wired_ , 6 July 2020.<a href="https://www.wired.com/story/tech-confronts-use-labels-master-slave/">https://www.wired.com/story/tech-confronts-use-labels-master-slave/</a>. Accessed 27 September 2020.
</li>
<li id="latour1988">Latour, Bruno [as Jim Johnson]. “Mixing Humans and Nonhumans Together: The Sociology of a Door-Closer.”  _Social Problems_ 35.3 (June 1988): 298-210.
</li>
<li id="liu2004a">Liu, Alan. _The Laws of Cool: Knowledge Work and the Culture of Information_ . Chicago: University of Chicago Press, 2004.
</li>
<li id="liu2004b">Liu, Alan. “Transcendental Data: Toward a Cultural History and Aesthetics of the New Encoded Discourse.”  _Critical Inquiry_ 31 (2004): 49-84.
</li>
<li id="oed"> “logic, _n_ .”  _OED Online_ . Oxford University Press.<a href="www.oed.com/view/Entry/109788">www.oed.com/view/Entry/109788</a>. Accessed 19 April 2018.
</li>
<li id="liddell"> “λόγος.”  _The Online Liddell-Scott-Jones Greek-English Lexicon_ .<a href="http://stephanus.tlg.uci.edu/lsj/#eid=65855">http://stephanus.tlg.uci.edu/lsj/#eid=65855</a>. Accessed 19 April 2018.
</li>
<li id="mancuso1997">Mancuso, Luke. _The Strange Sad War Revolving: Walt Whitman, Reconstruction, and the Emergence of Black Citizenship, 1865-1876_ . Columbia, SC: Camden House, 1997.
</li>
<li id="mccarty2016">McCarty, Willard. “Becoming Interdisciplinary.” Schreibman et al., 67-83.
</li>
<li id="mcgann2007">McGann, Jerome. “Database, Interface, and Archival Fever.”  _PMLA_ 122.5 (October 2007): 1588-92.
</li>
<li id="mcgann2016">McGann, Jerome. “Marking Texts of Many Dimensions.” Schreibman et al., 358-76.
</li>
<li id="mcgann2001">McGann, Jerome. _Radiant Textuality: Literature After the World Wide Web_ . New York: Palgrave, 2001.
</li>
<li id="mckenzie1999">McKenzie, D. F. _Bibliography and the Sociology of Texts._ Cambridge: Cambridge University Press, 1999.
</li>
<li id="mcpherson2012">McPherson, Tara. “Why Are the Digital Humanities So White? or Thinking the Histories of Race and Computation.” Klein and Gold, 2012.<a href="dhdebates.gc.cuny.edu/debates/text/29">dhdebates.gc.cuny.edu/debates/text/29</a>. Accessed 20 July 2018.
</li>
<li id="miller2010">Miller, Matt. _Collage of Myself: Walt Whitman and the Making of Leaves of Grass_ . Lincoln, NE: University of Nebraska Press, 2010.
</li>
<li id="mott1939">Mott, Frank Luther. _A History of American Magazines_ . 4 vols. Cambridge: Belknap Press of Harvard University Press, 1939-57.
</li>
<li id="mott1941">Mott, Frank Luther. _American Journalism: A History of Newspapers in the United States through 250 Years, 1690 to 1940_ . New York: Macmillan Company, 1941.
</li>
<li id="mukurtu">Mukurtu Archive.<a href="http://www.mukurtuarchive.org/">www.mukurtuarchive.org</a>. Accessed 1 August 2018.
</li>
<li id="myerson1993">Myerson, Joel. _Walt Whitman: A Descriptive Bibliography_ . Pittsburgh, PA: University of Pittsburgh Press, 1993.
</li>
<li id="newman2017">Newman, Daniel. “Secret to Digital Transformation Success: Fail Fast to Innovate Faster.”  _Forbes_ . 16 May 2017.<a href="http://www.forbes.com/">www.forbes.com</a>. Accessed April 18, 2018.
</li>
<li id="oberhaus2018">Oberhaus, Daniel. “ Master/Slave Terminology Was Removed from Python Programming Language.”  _Vice_ . 13 September 2018.<a href="http://www.vice.com/">www.vice.com</a>. Accessed September 30, 2018.
</li>
<li id="parks1995">Parks, Suzan-Lori. _The America Play and Other Works_ . New York: Theatre Communications Group, Inc., 1995.
</li>
<li id="posner2016">Posner, Miriam. “What’s Next: The Radical, Unrealized Potential of Digital Humanities.” Klein and Gold, 2016.<a href="dhdebates.gc.cuny.edu/debates/text/54">dhdebates.gc.cuny.edu/debates/text/54</a>. Accessed 20 April 2018.
</li>
<li id="price2004">Price, Kenneth M. _To Walt Whitman, America_ . Chapel Hill, NC: University of North Carolina Press, 2004.
</li>
<li id="raley2002">Raley, Rita. “Interferences: [Net.Writing] and the Practice of Codework.”  _Electronic Book Review_ (2002).<a href="http://electronicbookreview.com/essay/interferences-net-writing-and-the-practice-of-codework/">http://electronicbookreview.com/essay/interferences-net-writing-and-the-practice-of-codework/</a>. Accessed 31 July 2018.
</li>
<li id="ramsay2011">Ramsay, Stephen. _Reading Machines: Toward an Algorithmic Criticism_ . Urbana: University of Illinois Press, 2011.
</li>
<li id="samuels1999">Samuels, Lisa and Jerome McGann. “Deformance and Interpretation.”  _New Literary History_ 30.1 (Winter 1999): 25-56.
</li>
<li id="sandage2005">Sandage, Scott A. _Born Losers: A History of Failure in America_ . Cambridge, MA: Harvard University Press, 2005.
</li>
<li id="sandler2014">Sandler, Matt. “Kindred Darkness: Whitman in New Orleans.” Wilson, ed., 54-81.
</li>
<li id="sayers2016">Sayers, Jentery, Devon Elliott, Kari Kraus, Bethany Nowviskie, and William J. Turkel. “Between Bits and Atoms: Physical Computing and Desktop Fabrication in the Humanities.” Schreibman et al., 1-21.
</li>
<li id="schloen2014">Schloen, David and Sandra Schloen. “Beyond Gutenberg: Transcending the Document Paradigm in Digital Humanities.”  _Digital Humanities Quarterly_ 8.4 (2014).
</li>
<li id="schreibman2016">Schreibman, Susan, Ray Siemens, and John Unsworth, eds. _A New Companion to Digital Humanities_ . Chichester: John Wiley & Sons, 2016.
</li>
<li id="sedgwick2003">Sedgwick, Eve Kosofsky. “Paranoid Reading and Reparative Reading, Or, You’re So Paranoid, You Probably Think this Essay is About You.”  _Touching Feeling: Affect, Pedagogy, Performativity._ Durham: Duke University Press, 2003. 123-152.
</li>
<li id="stallybrass2019">Stallybrass, Peter. “Walt Whitman's Slips: Manufacturing Manuscript.”  _Walt Whitman Quarterly Review_ , 37.1 (Summer/Fall 2019): 66–106.
</li>
<li id="stephenson1999">Stephenson, Neal. _In the Beginning was the Command Line_ . New York: Avon, 1999.
</li>
<li id="surowiecki2014">Surowiecki, James. “Epic Fails of the Startup World.”  _The New Yorker_ (19 May 2014).<a href="https://www.newyorker.com/magazine/2014/05/19/epic-fails-of-the-startup-world">https://www.newyorker.com/magazine/2014/05/19/epic-fails-of-the-startup-world</a>. Accessed 31 July 2018.
</li>
<li id="traubel1906">Traubel, Horace. _With Walt Whitman in Camden_ . 9 vols. 1906-1996.
</li>
<li id="w3c"> “Transformation.” W3C Standards (XML Technology).<a href="https://www.w3.org/standards/xml/transformation">https://www.w3.org/standards/xml/transformation</a>. Accessed 8 August 2018.
</li>
<li id="transformdh">#transformDH: This is the Digital Humanities. <a href="http://transformdh.tumblr.com/">http://transformdh.tumblr.com/</a>, transformDH.org. Accessed 20 July 2018.
</li>
<li id="unsworth1997">Unsworth, John. “Documenting the Reinvention of Text: The Importance of Failure.”  _The Journal of Electronic Publishing_ 3.2 (December 1997). www.press.umich.edu/jep/03-02/unsworth.html. Accessed 22 August 2018.
</li>
<li id="vincent1889">Vincent, Marvin R. _Word Studies in the New Testament_ . Vol. 2. New York: Charles Scribner’s Sons, 1889.
</li>
<li id="wwarchives"> _The Walt Whitman Archive_ .<a href="http://www.whitmanarchive.org/">www.whitmanarchive.org</a>. Accessed 27 September 2020.
</li>
<li id="whitman1860">Whitman, Walt. “Bardic Symbols.”  _Atlantic Monthly_ 5 (April 1860): 445-47.
</li>
<li id="whitman1842">Whitman, Walt. “Franklin Evans; or, the Inebriate. A Tale of the Times.” _The New World_ (November 1842): [1]-31.
</li>
<li id="whitman1855">Whitman, Walt. _Leaves of Grass_ . Brooklyn, NY, 1855.
</li>
<li id="whitman1860-1">Whitman, Walt. _Leaves of Grass_ . Boston: Thayer and Eldridge, 1860-1.
</li>
<li id="whitman1867">Whitman, Walt. _Leaves of Grass_ . New York: W. E. Chapin & Co., Printers, 1867.
</li>
<li id="whitman1871">Whitman, Walt. _Leaves of Grass_ . Washington, DC, 1871.
</li>
<li id="whitman1881">Whitman, Walt. _Leaves of Grass_ . Boston: James R. Osgood and Company, 1881-2.
</li>
<li id="whitman1891">Whitman, Walt. _Leaves of Grass_ . Philadelphia: David McKay, 1891-2.
</li>
<li id="whitman1888">Whitman, Walt. _November Boughs_ . Philadelphia: David McKay, 1888.
</li>
<li id="wilkins2013">Wilkins, Matthew. “An Impossible Number of Books: Matthew L. Jockers’s Macroanalysis. ”  _Los Angeles Review of Books_ . 16 August 2013.<a href="https://lareviewofbooks.org/">https://lareviewofbooks.org</a>. Accessed 18 April 2018.
</li>
<li id="wilson2014a">Wilson, Ivy G. “Looking with a Queer Smile: Walt Whitman’s Gaze and Black America.” Wilson, ed., vii-xix.
</li>
<li id="wilson2014b">Wilson, Ivay G., ed. _Whitman Noir: Black America and the Good Gray Poet_ . Iowa City: University of Iowa Press, 2014.
</li>
<li id="winship1991">Winship, Michael. “Walt Whitman.”  _Bibliography of American Literature_ , compiled by Jacob Blanck. Vol. 9. New Haven: Yale University Press, 1991. 28-103.
</li>
<li id="zhou2019">Zhou, Cathy. _The State of the Octoverse 2019._ The GitHub Blog, 6 November 2019.<a href="https://github.blog/2019-11-06-the-state-of-the-octoverse-2019/">https://github.blog/2019-11-06-the-state-of-the-octoverse-2019/</a>. Accessed 27 September 2020.
</li>

</ul>
