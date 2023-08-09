---
type: article
dhqtype: article
title: "ᐊᒐᐦᑭᐯᐦᐃᑲᓇ ᒫᒥᑐᓀᔨᐦᐃᒋᑲᓂᐦᑳᓂᕽ | acahkipehikana mâmitoneyihicikanihkânihk | Programming with Cree# and Ancestral Code: Nehiyawewin Spirit Markings in an Artificial Brain"
date: 2023-07-20
article_id: "000699"
volume: 017
issue: 2
authors:
- Jon Corbett
translationType: original
categories:
- indigenous
- cs
- language studies
- digital
- code studies
- project report
- users
tags:
- storytelling
- Indigenous culture
- Indigenous language
- nehiyawewin
- Ancestral Code
abstract: |
   In this article, I discuss my project Ancestral Code, which consists of an integrated development environment (IDE) and the Nehiyaw (Plains Cree) based programming languages called Cree# (pronounced: Cree-Sharp) and ᐊᒋᒧ (âcimow). These languages developed in response to western perspectives on human-computer relationships, which I challenge and reframe in Nehiyaw/Indigenous contexts.
teaser: "Jon Corbett shares the challenges and solultions he's proposed coding in Nehiyawewin development environments."
order: 10
cluster: "Critical Code Studies"
---
  
  

## Introduction
  
  Nohkompan,[^1]  my paternal grandmother, was Nehiyaw (Cree) and Saulteaux (Chippewa). After her passing and understanding the matriarchal nature of many Cree peoples, I found myself looking at the Nehiyaw culture of her mother,   Nitâpân  ,[^2]  for inspiration for my creative works. In 2014, I attempted to use Nehiyawewin (the Cree language) words as variables using the Unified Canadian Aboriginal Syllabics [^unicode2021]. My early attempts were instantly problematic because the development environments (IDEs) I used would render the syllabics, like ᑖ, as empty boxes ⌧. So I searched for other solutions. However, at that time, the platforms I was most familiar with, such as Processing, openFrameworks, Java, and C#, all shared this same problem. This experience sparked my desire to bring Nehiyawewin, in its syllabic form, into being as a programming language. In this article, I present the physical and abstract challenges of developing my Ancestral Code digital toolkit that allows a programmer to insert code blocks into transcribed Indigenous stories that, once executed, produce a generative visual narrative of the transcribed story. But for you to better understand this desire’s importance, it is customary in my heritage to first introduce myself.
  
I identify as Nehiyaw-Métis and belong to the Métis Nation of Alberta. The Métis in Canada are federally recognized as one of the three Indigenous groups of peoples, the other two being First Nations and Inuit. The Métis have been historically referred to as half-bloods or, more derogatorily, half-breeds. We are a people that came to be from the blending of cultures and traditions of the first European visitors with the numerous Indigenous peoples of the new world. Many of these first visitors were not men seeking to settle; they were merely coming to seek a better living as fur traders. They were nomadic and travelled extensively, with many intending to return to their respective homelands when they retired.
  
Nevertheless, these traders married into First Nation and Inuit tribal communities, often for financially strategic reasons.  My Great-Grandfather five times over was a historically notable English fur trader named John Sayer and was one of these first visitors. These early relationships between European visitors and Indigenous peoples continued through generations, with subsequent mixed-racial generations raised with a blend of European knowledge and their original Indigenous languages and traditions. This concrescence of cultures and languages is how the Métis developed into a unique culture that privileges the cultural teachings of their respective Indigenous heritages without entirely rejecting their European roots.
  
My research as a Métis scholar and digital media artist has since evolved from using computers and programming as  _tools_  to generate my artwork to viewing computers as  _animate creatures_ , digital representations of my Indigenous heritage. Subsequently, I see computer languages as digital extensions of Nehiyaw storywork and ceremonies that reflect the epistemological, ontological, and axiological concerns of my Nehiyaw beliefs and practices. My perspectives on computer programming critique the prevalent use of English in coding languages and the reflection of settler/colonial perspectives in their design. Though I recognize that computer programming languages, like most technologies, are constantly evolving and changing, I maintain that they are also seemingly immutable and typically manifest from a    “historically-essential … colonial impulse” [^ali2014]  . Most notably, the culture(s) from which modern programming languages and practices grow    “[come] with significant cultural baggage” [^heaven2013]  . Through my own visual media art explorations with the popular new-media-art programming development environment  “Processing” , I recognized significant challenges to programming in anything other than English.
  
The detrimental legacy of colonial practices on the lives of Indigenous people is well documented, from forced displacement from traditional homelands to attempted erasure of culture, language, and practices [^gca1857]  [^venne1981]  [^milloy2008]  [^milloy2017]. As citizens of a globally connected techno-culture, we perpetuate this erasure by embracing a technicism that incorporates a blind acceptance of technologies and the cultural systems from which they are derived as necessary to engage with one another in our digital lives. Yet, critical theories of technologies are continually demonstrating that digital technologies are neither    “socially or culturally neutral” [^garneau2018]   nor are they    “determinist, but rather [sites] of social struggle” [^warschauer1998]  . Despite this technicism, navigating the modern technology ecosystem remains vital to Indigenous peoples, who actively utilize these new computing domains for    “survivance” [^vizenor2008]   and (re)establish both individual and community identities from these technological relationships and their ancestral cultures [^ormondparker_etal2013].
  
By viewing computing through a lens of my Indigenous heritage, my perceptions of computer languages and programming have been dramatically altered. My awareness of programming contexts informed by Nehiyaw language and cultural practices has opened new understandings of how programming languages can facilitate a greater sense of personal and digital identity and cultural belonging that go far beyond the purely functional operations of programming. These experiences are at the heart of what has become my Ancestral Code project.
  
  Ancestral Code is a wholistic programming environment built upon my own Indigenous computing design theory. It consists of both hardware, in the form of a specialized keyboard for typing Nehiyawewin syllabics, and software in the forms of a programming IDE and a multi-form programming language. The programming language component of Ancestral Code that is the focus of this article aims explicitly to integrate a    “wholistic” [^absolon2010]   braiding of Nehiyaw language and cultural practices within its design. I use wholistic here instead of holistic because Indigenous learning interconnects all aspects of being that include mind, body, emotion, and spirit and is not merely referring to a whole as a sum of parts. In particular, Ancestral Code is my vision of how Nehiyaw culture and language can be utilized as a primary interface for computer programming and computing design, uniting the values/benefits of Nehiyaw perspectives with western programming practices. To begin this journey, I will first provide a brief background of what I frame as an Indigenous computing design theory, describing the importance of this framework when approaching technology and computing design development with an Indigenous focus. Next, I describe how this design influences a unique perspective that views Code as Story. And then, I delve into the challenges (and related solutions) to my ongoing efforts to bring the Ancestral Code platform for programming in Nehiyawewin to Nehiyaw communities. I hope this platform can open new opportunities for heritage language use in our modern technological context and further foster Indigenous cultural maintenance. Finally, I surmise and summarize how this work can be used or reproduced by other Indigenous cultures with similar cultural perspectives and language construction.
  
  

## Indigenous Wholistic Computing Design Theory
  
Computing system design theories continue to evolve and have been described by or compared to a wide range of systems such as mechanical [^worden_etal2011], biological [^babaoglu_etal2006]  [^benenson2012], and hierarchical [^kleinrock_etal1980]  [^abdelbarr2009], to name just a few. Similarly, the past decade has also seen increased interest in postcolonial computing and colonialism as an influencing or embedded aspect of technological architectures [^irani_etal2009]  [^irani_etal2010]  [^merritt_etal2011]  [^dourish_etal2012]  [^philip_etal2012]  [^abdelnournocera_etal2013]  [^ali2014]. In developing an Indigenous computing theory, I consider common concerns from a general pan-Indigenous perspective, recognizing that research by Indigenous scholars commonly employs cultural practices and knowledge such as ceremony [^wilson2008]  [^cormier_etal2018], wholistic practices [^absolon2010], honouring of oral knowledges [^thomas2005], and community engagement [^madden_etal2013].
  
From these general characteristics I also used Nehiyaw-specific knowledge to help shape my own approach of establishing an Indigenous computing framework. The English term Cree is an anglicized form of the French word cri meaning to shout or cry aloud, and is how early European settlers came to name the Cree/Nehiyaw people. However, I do not refer to myself as Cree-Métis. I am Nehiyaw-Métis. Nehiyaw, in my heritage language, translates as four-bodied or four-spirit people. We see ourselves as a people composed of four bodies: the physical, mental, emotional, and spirit. Therefore, specific to Nehiyaw culture, I use spiritual teachings of the four-bodies framework to inform, describe, and highlight the aspects of computing that are inherently Nehiyaw and reflect Nehiyaw understandings and knowledge development.
  
Furthermore, each of these bodies has numerous cultural teachings that exist as living (oral) histories highlighting the cultural significance of their meanings and relationships between humans and the world. In other words,  _   kinehiyâwiwininaw nehiyawewin  / The Cree Language is our Identity_   [^wolfart_etal1993]. The Cree language, Nehiyawewin, is an intricately woven fabric that unites our life, being, and identity, across generations of knowledge and embodies spiritual and sacred knowledge that spans thousands of years. Because Nehiyaw language is so integral to Nehiyaw life, understanding user-computer relationships in a Nehiyaw context requires redefining philosophical understandings of computer system design using Nehiyaw terms. Therefore, using Nehiyawewin in my theoretical designs serves as a ceremonial healing practice in addition to its functional role of creating computational instructions. I find these considerations crucial to the design of computing technologies for Nehiyaw people as they re-envision the computer as a member of the community and an extension of one’s cultural identity.
  
Therefore, placing culture as the driving force behind the development of an Indigenous Wholistic Computing Design Theory can, and will, often be at odds with western philosophies on computer function and design. For instance, cultural attitudes towards concepts of time, order/sequencing, and efficiency can be radically different from their computational definitions. For example, I wrote a program to digitally-bead portraits of my family. The first version of this program used a basic loop to place pixel-beads on the screen in a sequence of rows, which it did in a left-to-right fashion. From a computational perspective, this loop was simple and efficient. However, the original computational instructions did not reflect my physical action of beading if I were to bead this image by hand. Nor did it capture the cultural significance of the continuous thread that connects each bead. There is a special meaning in the unbroken thread. As a result, I reformatted my code to reflect my Métis beading practice. The new code created alternating rows of digital beadwork that progress from left-to-right, then right-to-left in a continuous unbroken stream. This updated code better represents my physical process instead of code that created patterns that flowed in one direction, from left-to-right, as multiple individual lines instead of a continuous loop. The  _best_  or  _most efficient_  code fractures the image’s construction, resulting in digitally rendered images conforming to the technological tools’ design and language, favouring efficiency over cultural focus.
  
Experiences such as these altered my perspectives on general computing design theories and stimulated my desire to investigate computing design from Indigenous wholistic perspectives. Shifting the source of computing design from one driven by systemic operations to one that is human and cultural requires a certain degree of re-prioritization. I opted to expand existing system design theories by creating an Indigenous Wholistic Computing Design Theory. By identifying and privileging Indigenous and Nehiyaw-specific perspectives within existing computational environments, I aim to reevaluate what aspects of computing design are favoured over others.
  
In more concrete terms, systems design processes are vital because they create a clear overview intended to guide the actual development of a given product, whether it is hardware or software. In an Indigenously informed design process, this overview is still as essential but follows principles that promote [Indigenous] community collaboration and engagement over the tools and technologies that will be used; emphasizes interrelationships between components by establishing connections between Indigenous lived experience and the involved digital artifacts and their behaviours; and is open and flexible, or even unconcerned, with time and timelines in solution development. In such a theoretical framework western principles like Gestalt grouping or Fitt’s Law may not be applicable because the effects of cultural knowledge on a design may alter how components are typically created, or how they behave and interact with one another in comparison to systems focused directly at efficiency concerns like those found in data categorization, code flow, and execution and processing times.
  
  
  

## Indigenous Story as Code
  
What is coding if not a story? At a basic level, a story consists of five essential components: character(s), setting, plot, conflict, and resolution. Scholar Annette Vee, known for her study of composition and rhetoric in computer programming literacy, compares narrative writing with computer programming stating that they    “are not the same thing [but] have a lot in common and can even merge into each other” [^vee2017]. The relationship between story and code is particularly evident in esoteric computer languages such as  “Inform 7”   [^aikin2009] and  “Shakespeare”   [^hasselstrom_etal2001], where code is literally formatted as stories. Moreover, I argue that normal programming languages like C/C++, C#, and Java also share storytelling’s main elements despite their visual structure, notation, syntax, and semantic constructions. In normal programming languages, these story elements exist in more abstract contexts where variables represent the characters, the setting is the programming environment, and the plot is the program’s function as it operates up until its resolution or termination. I first learned how to program in elementary school in 1979 using Applesoft BASIC. My teacher explained BASIC’s syntax using story examples. I was so enthralled with the idea of being able to represent the world around me using computer code that I started writing my journal entries in language arts class as BASIC code. For me, coding is very much a form of storytelling.
  
In creating the Ancestral Code programming languages  “Cree#”  and  “ᐊᒋᒧ”  (âcimow)[^3] , my vision arrived as a genuine dream. In this dream, I was sitting in a community lodge (i.e., tipi), listening to an Elder tell a story. In this story, an image of Wîsahkecâhk, sometimes known as the Trickster Raven in Nehiyaw cultural teachings, was animated on the wall behind him. Wîsahkecâhk was puppeted through the Elder’s words, while a syllabic subtitled transcription of the story ran beneath the imagery. This dream revealed a path for me. It led me to understand that this generative virtual landscape was a relationship between Nehiyawewin and the computer, and though this landscape was digital, it was still a place. And here, in this place, I experienced my Ancestral Code project as each of the four spirits: The physical experience of seeing and being present; the mental experience of processing and parsing the story; the emotional experience of being attached to an Elder and  _feeling_  the story; and the spiritual experience of the dream state itself.
  
Furthermore, in my dream, the syllabic transcription was an instruction-set that manipulated the vision of Wîsahkecâhk, thereby exposing me to the computing code. Thus, though this is a brief origin story of my Ancestral Code project, I have interpreted the role of the four spirits in furthering its creation as a critical component of its development. As a result, I have found new ways of applying Nehiyaw cultural teachings to my computer coding practice.
  
  
  
  

## Challenges and Solutions
  
Though I expected to encounter obstacles in this project, I did not honestly foresee how deep into my coding practice and theory I would be required to go to design the Ancestral Code programming language. In this section, I trace out each of the challenges with working the Nehiyawewin orthography — including its use in the software and hardware, how I incorporated Nehiyaw language structures into the programming language, and how I see culture as being crucial to the programming languages I developed.
  
  

## Orthography
  
The Nehiyawewin orthography, called ᐊᒐᐦᑲᓯᓇᐦᐃᑲᓇ or acahkasinahikana, literally translates into English as spirit markers. Nehiyawewin also has a Standard Roman Orthographic (SRO) writing system in which the language can be written with the standard Latin alphabet to aid English speakers in pronunciation. Though Nehiyawewin learners frequently use SRO, many Nehiyaw first language speakers consider SRO an accommodation or adoption of western processes. They also feel this system voids much of the cultural significance and meaning attached to the spirit markers. Though I prefer to use Nehiyawewin spirit markers, most of the Nehiyawewin in this article is written in SRO form for easier readability by English readers. I have included a [glossary at the end of this article](#glossary) with definitions and a pronunciation guide using the International Phonetic Alphabet (IPA) phonetic notation system.
  
My original desire to use acahkasinahikana exclusively in Ancestral Code was a conscious decision to combat the accommodation of English language constructions and representations. However, in investigating my needs as a programmer, these language-based concerns revealed that support for both SRO and acahkasinahikana are required to support Nehiyawewin language learners that may come from different dialects or communities. For this reason, programming in Ancestral Code can be performed in its Romanized form that I call Cree# (pronounced Cree-sharp) or its syllabic form ᐋᒋᒧᐤ (âcimow). The Ancestral Code IDE allows the programmer to switch between the two styles, where Cree# accommodates a certain level of familiar structure to the C# programming language, separating it from the more story-like narrative structure of ᐋᒋᒧᐤ (âcimow). Switching between these modes provides unique alternatives to experiencing written Nehiyawewin, where representing code in multiple cultural forms can be done without necessarily favouring one over the other. Furthermore, the IDE development aspect revealed a couple, albeit minor, concerns, namely: 
  How to use the Unified Canadian Aboriginal Syllabics block of the Unicode Standard, that is, what font family/typeface to use for coding with syllabics.  How to address coding without, or with minimal, punctuation and numeracy.  


  
  

## Software: acahkasinahikana for coding
  
Using Unicode characters in modern programming environments is possible if the computing system supports the desired character sets. The Unified Canadian Aboriginal Syllabics block of the Unicode Standard occupies 640 code positions from 1400hex to 167Fhex. It includes orthographic glyphs for Blackfoot, Carrier, Cree, Dene, Inuktitut, Ojibwe, and other Canadian Athabascan languages. Unfortunately, the coding environment is often the main obstacle in using Unicode characters, especially as variable names and, more problematically, as keywords or reserved words. Typically, this lack of support is simply because the environment often uses a pre-installed font that does not contain glyph(s) in the desired code points of the font file. By default, the coding environments I am familiar with, such as  _Visual Studio_  and  _Processing_ , use a fixed-width font/typeface such as Consolas, Courier, or Monospace. These fonts are common to Windows OS systems but do not have the Canadian Aboriginal Syllabics block of glyphs. Until recently, changing this font was not easy. Although, as of the writing of this article, the settings or preferences support in some IDEs is open to changing the default font, some still limit the fonts that can be used. There also are limited fonts suitable for programming using the Unicode Canadian Aboriginal Syllabics, and I argue there are currently no suitable fonts. Though it is theoretically possible to use syllabics as variable names in those IDEs, reliance on English programmatic tokens remains. The question then becomes, which font(s) can or should be used for programming with acahkasinahikana?
  
  
  

## Software: acahkasinahikana fonts
  
Though this may sound like a trivial topic from a western perspective, as it truly has little to do with actual coding and more to do with aesthetic preference, my critical reflection on coding practice makes this a necessary point of discussion. Remember that Nehiyaw acahkasinahikana are visual representations and extensions of being. They are called spirit markers for a reason. So, their representation in the computer must be treated with equal consideration.
  
Most programmers would agree that fixed-width or monospaced typefaces are ubiquitous in coding because they align very well in rows and columns and generally provide a greater distinction between similarly shaped characters like 0, o, O, narrow characters like I, l, i, as well as providing more space for syntactical and operational characters (, {, [,!  [^ardley2014]. Combining this respect for the visual aspects of language with the need for a monospaced coding font reveals two challenges. The first challenge is that, to my knowledge, only one monospaced font purposefully includes the Canadian Aboriginal Syllabics blocks, Everson Mono.[^4]  The second challenge is that the physical structure of syllabics makes using non-fixed-width fonts challenging to navigate as code. The visual structure of the major glyphs (i.e., the glyphs representing a consonant and vowel pair) consists of reflected orientations of a single shape (ex. ᒥ ᒣ ᒪ ᒧ). The resulting printed text is fairly consistently sized but is visually similar to coding in all English caps. This is not necessarily a negative, as my original programs written in BASIC were done in all caps. But a more significant point of consideration is how a culture perceives the visual design of its language. For example, in developing typefaces for Canadian syllabics, Canadian typography designer Kevin King worked directly with Indigenous communities to ensure their languages were written in the respective community’s preferred style. He notes that  “to ignore this would result in a text that was neither culturally appropriate for local readers nor able to convey adequately the meaning and atmosphere of the text for that readership” [^king2022]. Adding to these, the limited number of monospaced fonts that support Canadian syllabic glyphs encouraged me to develop a new code-friendly font to address these obstacles. This font ([Figure 1](#figure01)), I tentatively named  “AC Mono,”  was constructed using my wholistic design framework, and my choices in the font design process are consciously aware of Indigenous visual aesthetics. I want to note here that my design of this font was considered from a more pan-Indigenous perspective and not specific to Nehiyaw culture. This is because the Unified Canadian Aboriginal Syllabics is not Nehiyaw specific – it represents glyphs from various North American Indigenous languages. For example, as seen in the syllabic T-series glyphs like tâ (ᑖ) and te (ᑌ), I used thicker lines, an emphasis on fluidity in the curves, and rounded features on the start and end points of the strokes. These organic geometries and gestures are found in numerous Indigenous art traditions in North America, including the ovoid traditions of Coast-Salish artforms, Inuit bone and stone carving, and Métis beadwork.
  
{{< figure src="resources/images/figure01.png" caption="AC Mono Font glyphs for tâ (ᑖ) and te (ᑌ). Image by Jon Corbett." alt="Two glyphs of the AC Mono typeface which fill the space between the ascender line and the baseline."  >}}

  
In the construction of AC Mono, I used the typefaces of Everson Mono and Consolas only as sizing templates, building my resulting font with the stroke weight of Consolas and the mildly rounded stroke end of Everson Mono. Of particular note, syllabics have no differing case structures. Therefore, no glyphs need to accommodate space for descenders that extend below the baseline. The removal of the descender area results in a noticeably reduced distance between the glyph baseline and the edge of the glyph-space in the AC Mono font compared to ASCII/English fonts ([Figure 2](#figure02)), allowing for a more consistent line height, providing better options for vertical spacing between rows when coding.
  
{{< figure src="resources/images/figure02.png" caption="Font design comparison between Everson Mono, Consolas, and AC Mono, the English glyphs selected here are chosen for their visual similarity to the Nehiyawewin syllabics, they are not representative of English pronunciations or linguistic function." alt="A comparison of glyphs in the typefaces Everson Mono, Consolas, and AC Mono."  >}}

  
  
  

## Software: acahkasinahikana punctuation and numeracy
  
  

## 
  
A more significant challenge is how to support specific programming tasks using limited punctuation and, preferably, an alternative numeric symbology. Programming nomenclature and notation have had a unique evolution and, as Arawjo notes, have developed in  “concert and conflict with discretizing infrastructure[s]” [^arawjo2020]. Without getting into a long history lesson on programmatic notation, I have seen how my own programming practice evolved from coding in BASIC, using very little punctuation except the double quote and round brackets, to today, where I predominantly use C# and Java that, use nearly every non-numeric and non-alpha character on the standard keyboard. In today’s programming culture, it is rare to see a programming language not use every symbol and character on the keyboard. Notation marks that currently have meaning and function in many modern programming languages can be problematic when developing solutions for Indigenous orthographies that traditionally do not use these marks.
  
As I mentioned earlier, the only punctuation commonly found in Nehiyawewin text is the full stop syllabic that looks like a lowercase x but is actually U+166E (᙮); and the hyphen - most often used to separate certain morphemes or break up very long sentence-word constructions when reading. My understanding of this lack of punctuation stems from my understanding of Nehiyawewin morpheme structures that provide the necessary context and grammatical positioning in its word construction, making punctuation usage unnecessary, except to indicate the end of thought or discussion [^wolfart1973]  [^okimasis_etal2008].
  
Another point of consideration between western culture and Nehiyaw culture is numeracy. Much of the world uses the ten symbols of the Hindu-Arabic decimal number system to represent numbers. Though Nehiyaw numeracy has become pretty much forgotten in favour of Hindu-Arabic numerals, Nehiyaw culture did develop a way to represent numbers using the syllabic glyphs (Figure 4). Furthermore, from a language perspective, Nehiyaw culture has developed certain relationships to numbers and numeric meanings that are often associated with Nehiyaw ontologies, as exemplified previously in my explanation of the meaning of Nehiyaw as the four-bodied people.
  
  
  

##  Punctuation Symbols: 
  
A simple but effective example of a  _traditional_  programming style that would execute a print-to-screen command might look like this: 
```perl
print("hello world");
```
 In this example, the parentheses mark the start and end of the function contents, and the double quotes mark the entry and exit points of the text to render to the screen.
  
  
  

## 
  
So how would a programmer make this indication if there are no brackets or quotation marks? Another common symbol in modern programming languages is the semi-colon (;) as an instruction separator or terminator. Again, how does a programmer indicate where to terminate an instruction without this mark? These orthographic punctuation devices have become so commonplace in modern programming that it is difficult to envision not having access to them. It is precisely these kinds of practices that I have attempted to overcome in developing Ancestral Code. My intent here is not a need to use minimal punctuation. Instead, it is a resistance to adopting marks and practices that belong to other languages. To that end, one of the first steps I took was to inventory the Nehiyaw syllabary and functional language glyphs. I then established a list of necessary programmatic functions and decided on the syllabic symbols for my programming language.
  
To start this investigation, I started with the most straightforward programming language I know — BASIC. I used a variety of dialects of BASIC for nearly fifteen years, and upon reflection, it was one of the languages that I could use with the least amount of punctuation. BASIC also provides a good starting point for just reading code as if it were a recipe or short story. It also helped me identify the bare necessities I felt Ancestral Code required. In the end, I came to the following general determinations to make language development easier. These initial determinations were primarily based on my Indigenous Computing Design’s resistance to western computing reliance on non-alpha characters:
  
  
 * The Unified Canadian Aboriginal Syllabics block of the Unicode Standard currently contains 640 symbols. However, my dialect of Plains Cree only uses 107 syllabics from a total block of 134 glyphs that  _could_  be used in Nehiyaw speech. So the remaining 533 symbols from the syllabary became potential candidates to fulfill those programmatic roles where western punctuation is usually employed.  
 *   Ancestral Code will be line-driven. In other words, the linefeed/carriage return is the primary instruction terminator. Using the linefeed, makes parsing of instructions easier.   
 * The full stop symbol (᙮) is used to terminate  _and_  exit code (especially within a loop). Being the only punctuation mark, its function and use needed to make sense in the narrative flow of the source code.   
 * Language-based reserved words are used to mark code start and end positions instead of braces or other symbols. For example, in Visual Basic  
```unspecified
IF
```
  and  
```unspecified
END IF
```
  mark the start and endpoints of a conditional code block; similarly, sipiy and  _âniskôsîpiy_  perform the same roles in Ancestral Code.  
 * In Ancestral Code, [Nehiyawewin syllabic-numerals](#numeracy) replace Hindu-Arabic numbers. Hindu-Arabic numerals will be allowed, but only in SRO mode, and a built-in calculator will convert Hindu-Arabic numbers to their appropriate syllabic representations when in syllabic mode.[^5]   

  
With this software side of the orthography resolved, I looked at the next obstacle: how should the user input code?
  
  
  
  

## Hardware: the acahkasinahikana keyboard
  
The history of print cultures has led to privileging western  “stories, voices, and values” [^risam2018], and modern coding cultures and computer language development have naturally adopted. Though Nehiyawewin can be typed on standard keyboard layouts using a Romanized orthography, this seemingly innocuous accommodation is probably the number one contributor to the continued erosion of Indigenous culture and language in the digital age.
  
Initially designed for English typewriters in the mid-to-late 19th century, the International Standards Organization officially adopted the QWERTY keyboard layout in 1971, becoming  “the de facto Standard layout for Communications and computer interface keyboards”  in 1972 [^noyes1983]. Over the last 50 years, the ISO Standard has evolved as our communication technologies have, and ISO 9995-9:2016 now includes definitions for multilingual and multiscript keyboard layouts [^iso2016]. However, these standards still assume that most languages can be represented with a Latin alphabet. The ISO Standard clearly states that it  “is intended to address all characters needed to write all contemporary languages using the Latin script, together with standardized Latin transliterations of some major languages using other scripts” [^iso2016]. This assumption that  “all contemporary languages”  can be written using a Latin character set is the type of colonial coercion that continues to institute western ideologies as dominant.
  
Regarding computing, our experiences are configured and guided by technology design philosophies that do not always include a combined understanding of  “people, technology, society, and business” [^norman_etal2015]. By working with members of my community, my Ancestral Code project has allowed me to explore keyboard designs that can better represent Nehiyawewin and Nehiyaw culture when entering syllabics into the computer. I aimed my design objectives at challenging assumed western standards by investigating the role of the keyboard as an input device, and how such devices can support Nehiyaw cultural pedagogy and improve the relationships between the user, their language (i.e.,  Nehiyawewin), and the computer. Though Nehiyaw syllabics are taught in several ways, one popular method is the arrangement of the Nehiyawewin syllabary into a star design, often referred to as a Cree syllabic star chart ([Figure 3](#figure03)). This design is used often in teaching syllabics and contains several culturally specific teachings. For example, as a student at University nuhelot’ine thaiyots’i nistameyimâkanak Blue Quills, my favourite syllabic origin-stories were about the ᒐ syllabic, described as being symbolic of the pipe used in Nehiyaw ceremony, ᐱ is a medicine lodge (i.e., tipi), and ᑕ can be interpreted as the toe of a moccasin. Whether or not these story sources are the true inspirations for the initial syllabic creations, I recognize the importance the visual imagery of syllabics holds and how they are intricately tied to cultural representations and understandings. Furthermore, due to the reflected and rotational arrangement and orientation of Nehiyaw syllabics, these teachings cannot be represented using the modern four-row keyboards used for typing in western computing.
  
{{< figure src="resources/images/figure03.png" caption="My own Nehiyawewin syllabic star chart." alt="Nehiyawewin syllabic glyphs arranged in rough four-fold symmetry with phonetic guides printed in miniature next to each corresponding symbol."  >}}

  
I feel that a keyboard or input device that uses this Nehiyaw star layout is culturally significant, meaningful to a Nehiyaw user, and therefore appropriate for capturing Nehiyawewin. Through my iterative design process for the Nehiyawewin keyboard, I critically evaluated everything from the keycaps to the printed circuit boards (PCB). During this process, I created five distinct designs to retain cultural associations, allow efficient syllabic entry, and have practical usability for typing everyday documents. I found the star design keyboard was best suited as the primary interface for coding with Nehiyawewin in the Ancestral Code programming environment ([Figure 4](#figure04)). Similarly, testing these designs with Nehiyawewin language-learners, users found typing syllabics with a star keyboard easier than QWERTY layouts because of the grouping of syllabic sounds in each of the four quadrants establishes a mental-map making locating syllabics by sound easier. For example, all the i syllabics are located in the keyboard's top left and top vertical. This relationship between spoken language, computer language, and teachings of the syllabic orthography is meaningful and is one that I feel is better supported by a device derived from Nehiyawewin pedagogy.
  
{{< figure src="resources/images/figure04.png" caption="One of my proposed Nehiyawewin Star Chart Keyboard designs." alt="A radially-symmetrical image of a keyboard with eight rays of keys emanating from a central space key."  >}}

  
  
  
  

## Bringing Nehiyawewin characteristics to a programming language
  
With the formalities of the orthography addressed, I progressed to investigating how to engage with Nehiyawewin programmatically. I initially approached this project with a very naive and western mindset. I considered common modern computing ideas and abstractions that included variables, data types, loops, conditional branching, and linear/sequential instructions (i.e., lines of code), and embarked on a journey to convert their English versions to Nehiyawewin. Thinking that some of these concepts would easily convert from English to Nehiyawewin, I quickly realized that this approach of language substitution in Nehiyawewin would not work. As I discovered on my first day as a Nehiyawewin student, Nehiyawewin technically does not have a word for computer, let alone any of the programming concepts I was hoping to capture. Technological words in English like programming, network, and protocol I found were, for the most part, non-translatable to Nehiyawewin, at least not a way I could use in developing a programming language. Today, finding appropriate Nehiyaw cultural meanings that can map to technological terminology remains the biggest challenge in developing the Ancestral Code project as a fully Nehiyawewin-privileged computing platform. Nevertheless, I took these challenges with language and formulated an approach that involved finding easily translatable concepts (if they existed), and borrowing from Nehiyaw language construction and word forms to create a unique coding paradigm.
  
  

## Translating Nehiyawewin
  
What is a computer? I asked the most knowledgeable person in my Nehiyaw class, the Elder. That conversation went something like this:
    Me  
How do you say computer?
      Elder  
Well, that depends. There really is no word for computer, but some people use masinatakan cikastepayicikanis.
      Me  
What does it mean?
      Elder  
  Masinatakan means to type or write, but actually comes from words that mean using a tool to create or stamp a mark and cikastepayicikanis is the word we use for TV, it comes from a word about shadows so something like making a shadow, or full of shadows, or a box of shadows. You can interpret these words together as making marks in a box of shadows without a pen.
      Me  
Uh-huh… Ayhay.  
    
I note that this was not an isolated occurrence. Well, that depends. There really is no word for [insert word], was a very common response to almost anything western in my classes and applied to most modern technologies like radios, televisions, and cell phones. Depending on whom you asked, there are as many ways to describe these modern contraptions as there are dialects of Nehiyawewin. However, I accept and now use mâmitoneyihcikanihkân  [^6] , suggested by Wayne Jackson, an esteemed Nehiyaw language expert and Nehiyawewin professor at University Blue Quills. As explained to me, this word is understood to mean artificial thought/brain. I choose this definition over masinatakan cikastepayicikanis because I feel it better conveys the essence of what a computer is. I find that masinatakan cikastepayicikanis  [^7]  is more about describing the computer as a physical, non-animate object of utility than the more conceptual or abstract and humanized idea of what a computer is. After all, we as a species have a considerably long history of relating technologies to aspects of being human [^travers1996], and mâmitoneyihcikanihkân suits this tradition.
  
Finding suitable replacements for some of the more programming-specific lingo such as integer, float, string, array, variable, subroutine/function, do/while, for/next, and if/then proved to be highly problematic. These concepts either do not translate easily, can only be translated in a general sense, and/or require a broader context. And, in most cases, they cannot be translated without simplifying their meaning. Additionally, these concepts can only be translated by conversation and engagement with community members, fluent speakers, and Elders with the required experience and knowledge.
  
My solution to this particular challenge was one of metaphoric application rather than translation. I credit Hawai’ian game developer and computer programmer Kari Noe for introducing me to this philosophical change. Noe was a member of a Ōlelo Hawai’ian programming team engaged with translating C# into Hawai’ian [^muzyka2018]. She described the if/then/else statement as an example where the if/then/else statement does not make sense when translated from English to Hawai’ian. The programming team consulted with native Hawai’ian speakers and community members to find meaningful terms that could be both culturally appropriate and programmatically practical. The result for if/then/else becomes muliwai, the Hawai’ian word for river. The idea of rivers being able to branch from the main waterway and eventually rejoin the main river later provided a better conceptualization of a Hawai’ian context than the English if/then/else statement. This culturally-aware solution in their language was not only inspirational but fundamentally altered how I was approaching the relationships between computing concepts and cultural relevance. Though I recognize that Hawai’ian peoples’ relationship with water is considerably different from those of the Indigenous peoples of the Americas, water is no less important. In Nehiyaw culture, water is a medicine, a provider of life, and is sacred. Therefore, I have come to use river as a conditional branch command. In Nehiyawewin river is sîpiy, and with this root I can then branch an if into sîpîsis, a small river or creek in English. Therefore, a code example might look like the following examples:   
# A series of conditional branch commands in ᐊᒋᒧ
   
```
 ᐊᓱᐘᐦᐁᐤ ᐃᔨᓂᒥᐣ ᒦᓂᓯᐘᐟ  ᓰᐱᐩ ᑭᑿᐩ ᐲᐦᒋᔨᕽ ᒦᓂᓯᐘᐟ  ᓰᐲᓯᐢ ᐃᔨᓂᒥᐣ  ᐊᓱᐘᐦᐁᐤ ᐊᔫᐢᑲᐣ ᒦᓂᓯᐘᐟ᙮  ᓰᐲᓯᐢ ᐊᔫᐢᑲᐣ  ᐊᓱᐘᐦᐁᐤ ᐃᔨᓂᒥᐣ ᒦᓂᓯᐘᐟ  ᐋᓂᐢᑰᓰᐱᐩ  ᓰᐱᐩ ᑮᓯᐸᔨᐤ 
```
     
# [Example 1](#example01) in SRO (Cree#)
   
```
 asiwahew iyinimin mînisiwat  sîpiy kikway pîhciyihk mînisiwat  sîpîsis iyinimin  asiwahew ayôskan mînisiwat.  sîpîsis ayôskan  asiwahew iyinimin mînisiwat  âniskôsîpiy  sîpiy kîsipayiw 
```
     
# The literal English translation of the code block from [Example 1](#example01) or [Example 2](#example02)
   
```
 put the blueberries in the berry bag  [start] a river, what is [in] this bag?  [start] a creek [for] blueberries  put a single raspberry in the berry bag.  [start] a creek [for] a raspberry  put the blueberries in the berry bag  join the river  the river ends 
```
     
  
In this example, the first creek ends with mînisiwat᙮[^8]  where ᙮ terminates and subsequently ends the river-if statement. The second creek ends with âniskôsîpiy[^9]  or rejoin the river, and in this case, it would continue to the following statement in the if code block. In this way, the if statement is fluid. It can branch, terminate, or rejoin the original, reflecting a natural flow or progression.
  
Understanding computer functions in these cultural terms provides a more Indigenous method of relating to the machine. In addition, defining programmatic operations using culturally meaningful metaphoric terminology changes the process of keyword translation to a process of knowledge adaptation, ensuring that a Nehiyaw programmer does not need to language-switch between Nehiyawewin and English to have the computer perform its tasks. Looking at a computer’s code from this metaphoric perspective can also be extended to the binary level of the machine, where a Nehiyaw worldview can reframe the binary understanding of 1 and 0 as animate and inanimate.
  
  
  

## Nehiyaw language construction
  
I felt that morphemes and free word order were characteristics of Nehiyawewin that offered strong potential for programmatic versatility though they did offer some unique challenges.
  
  

## Morphemes
  
Nehiyawewin is intensely metaphoric and descriptive and is a polysynthetic language, meaning the language combines many morphemes, often resulting in lengthy sentence-word constructions [^shirt_etal2022]. A morpheme is a single linguistic unit of meaningful speech. For an English example, without focusing too much on etymology, the word code from the Latin codex can add different suffixes to alter its meaning. One such ending is -ing to change it to coding, representing an active verb. Another is -er to change it to coder, which is a noun meaning a person who codes, and both could be structured in a sentence as the coder is coding. These suffixes are morphemes.
  
A fun example that illustrates how Nehiyawewin morphemes are stringed together is the word for hippopotamus. Nehiyawewin does not have an actual word for hippopotamus because this animal is not native to the Americas, and therefore it is described in language using its most prominent features. In Nehiyawewin, as described by Nehiyaw Elder Solomon Ratt, a hippopotamus is called kihci-kispakasakewi-mistipwâmi-mahkitôni-nîswâpitewi-atâmipeko-pimâtakâwi-kohkôs or in English as  “great, thick-skinned, big-thighed, big-mouthed, two-toothed, underwater, swimming, pig ” [^ogg2019].
  
Another interesting example is the Nehiyawewin translation for the English word pony. In Nehiyawewin, the word atim  [^10]  is the word for dog. When you prefix atim with mist- from the word mistahi-, which means [something] is great/large/big, the resulting word mistatim is formed, which can mean big dog, but is more commonly used to mean horse. Adding the diminutive suffix –osis, meaning [something] is small or little, to atim, the result is acimosis meaning little dog or puppy. We can go one step further and combine all three of these ideas to get mistacimosis. The resulting understanding is a small horse or pony. Though one could argue it also means a very big puppy, the context would clarify what the speaker is referring to.
  
For Ancestral Code, I used these bound morphemes of mistahi- and -osis as ways to make variables increase or decrease in value (i.e., size), even though they may not be semantically or syntactically correct in Nehiyawewin speech. So, for example, using a numeric variable called atim, you can use the following statement:   
```unspecified
atimosis
```
 This is equivalent to the more traditional coding representation of:  
```unspecified
atim = atim - 1;
```
  This usage carries the meaning of increase the size of the dog and reduce the size of the dog or make the dog bigger then smaller. In this example, the variable atim has some value manipulated through a single morpheme-constructed token instead of a more common calculation assignment in other programming languages delimited by spaces to separate each programmatic token. Not to mention the problem with translating the syntax of  
```unspecified
atim = atim + 1
```
  as an assignment command and not a logical statement into Nehiyawewin.
  
  
  

## Free Word Order
  
Free word order means words in a sentence do not necessarily need to be in a rigid sequence. This ordering is especially apparent in something like the cat sees the dog; whereas, in English, you cannot swap the cat and the dog without changing its meaning, as in the dog sees the cat. However, this is not the case in Nehiyawewin, where minôs wâpamew atimwa[^11]  and atimwa wâpamew minôs mean the same thing. This language use is because there is a third-person obviative -wa attached to atim, indicating the dog atim is the object being acted on regardless of where it appears in the sentence in relation to the cat. To say this sentence in English requires modifying the verb to clarify who or what is seeing and identifying who or what is being seen. This sentence is a simplistic example, but as the coding environment for Ancestral Code was designed to be written as a narrative, having this flexibility is something I wanted to be able to use because it is non-linear and changes our perceptions of coding in line-by-line formats. A simple coding example would be the completion command for sîpiy,  
```unspecified
sîpiy kîsipayiw
```
 [^12] . In this case, sîpiy kîsipayiw and kîsipayiw sîpiy mean the same thing. Although, as a coder, I can use end river or river ends, it does not matter the order of the tokens as they are not fixed. A more expanded example uses this same idea but applies to whole lines or activities, as in a looping construction where a character such as Wîsahkecâhk might walk, hop, and talk:   
# Free word order in in ᐊᒋᒧ
   
```
 ᐱᐳᐣ  ᐃᔀᑫᒐᕽ ᐱᒧᐦᑌᐤ  ᓇᐸᑌᒁᐢᑯᐦᑎᐤ ᐃᔀᑫᒐᕽ ᐃᔀᑫᒐᕽ ᐄᑭᐢᑵᐤ 
```
     
# [Example 4](#example04) in SRO (Cree#)
   
```
 pipon  Wisakecahk pimohtew  napate-kwâshohtiw Wisakecahk Wisakecahk pîkiskwew 
```
       
# The literal English translation of the code block from [Example 4](#example04) or [Example 5](#example05)
   
```
 for one winter  Wisakecahk walks  hop Wisakecahk Wisakecahk speaks 
```
     
  
When this block of code runs, the lines that follow pipon are randomized as it is not essential which order those actions execute, as long as the Wîsahkecâhk object variable performs all three actions in this block. By comparison, an equivalent representation of this code in C# might look like this:  
```c#
int winter = 1; do { Random r = new Random(); string[] actions = new string[] { "walk", "hop", "speak" }; actions = actions.OrderBy(x => r.Next()).ToArray(); foreach (string doAction in actions) { makeWisakecahk(doAction); } winter--; } while (winter == 1);
```
   
  
The Ancestral Code keyword for a do loop is  
```unspecified
pipon
```
 [^13] , which translates as a winter. In the next section, I will elaborate on the meaning and cultural significance of the reserved word pipon. But, for this example, if I wanted to perform these actions in sequence and not a random order, I would not bother using the  
```unspecified
pipon 
```
 loop. You may also notice that the lines that direct the Wîsahkecâhk variable to do an action (see [Example 4](#example04), [Example 5](#example05), or [Example 6](#example06)) are in free word order in the Ancestral Code example (as in  
```unspecified
Wîsahkecâhk walks
```
  and  
```unspecified
hop Wîsahkecâhk
```
 ). Unlike many programming languages that must start with a command or keyword followed by variables or parameters, this is not necessary for Ancestral Code, as long as the variable and command are on the same executing line. The programming parser, the part of the programming environment responsible for separating lines of code into smaller elements and individual instructions, will still be able to discern the token from the data, regardless of the position of each in the line. In the next section, I will detail the reasons behind this built-in randomization. Still, in terms of programming language construction, using features of morphemic commands and free word order, are a means to describe the relationships between the programmatic structures of Ancestral Code and Nehiyaw culture.
  
  
  
  
  

## Culture and language == code && code == culture and language
  
Language plays a significant role in the enterprise of computer programming, and these activities are still heavily informed by western culture. Consequently, it is challenging to envision programming as anything but a socio-technical subculture populated with hordes of Benjamin Nugent’s  _Lewis Skolnick-esque_  Type-1 nerds  [^nugent2008].[^14]  This stereotyped and generalized view of programmers and programming was the last challenge I aimed to reformulate, to introduce Indigenous cultural practices as digital metaphorical structures that view programming from Indigenous epistemological and ontological concerns that alter how programming is perceived in its current western context. For example, I admire how Ramsey Nasser describes the algorithms depicted in the Arabic calligraphic forms of his قلب programming language  “as high poetry” [^nasser2012]. I also found that describing western computing ideas in Nehiyawewin often resulted in algorithmically poetic word creations, as evidenced with the concept of river to represent if/then logic. I expand on this analogy-based token use for representing programmatic instructions by applying the same metaphoric treatment to culturally specific understandings as a way of genuinely viewing computer programming as a non-western endeavour. Through this reimagining of computing terms, I highlight how computing concepts already reflect Indigenous cultural teachings, practices, especially ceremony, as I demonstrate in the following specific examples of miyâhkasike[^15] , pipona[^16] , and waniyaw  [^17] .
  
  

## Miyâhkasike and Tisamân
  
One of the most common and essential cultural practices in Nehiyaw culture is the smudge. A smudge is a small, personal ceremonial practice where the burning of an Indigenous medicinal herb such as sweetgrass or sage is used to cleanse and purify the individual. When smudging, people pass their hands or objects to be blessed through the rising smoke trails. In a normal smudge, you use your hands to draw the smoke towards you – blessing your head, ears, eyes, mouth, heart, and body with the smoke. And then, you bless anything else you wish to be cleared of negative energies, such as food, tobacco, eyeglasses, or even your laptop. Essentially, smudging is responsible for blessing anything that can affect any of your four spirits. I have even heard stories from several Nehiyaw and Métis Elders that have physically smudged their laptop to purify it before Googling. In the context of ceremony, this idea of cleansing is something that computers do regularly. Whether it is emptying the trash bin, clearing memory, resetting the graphics display, or deleting a browser’s cache, the intent of all these activities is to remove items that can negatively affect the system’s operation. Therefore, the first command in an Ancestral Code program is  
```unspecified
miyâhkasike
```
  which is to smudge with sage/sweetgrass, or  
```unspecified
tisamân
```
 [^18] , which is to smudge (in general), both serve the same purpose of preparing the system. The choice of which smudge command to use is up to the programmer. However, I personally feel that a program that relates a sacred story or contains culturally specific or significant knowledge in the code would start with  
```unspecified
miyâhkasike
```
 , being more purposeful than the more generic  
```unspecified
tisamân
```
 . These smudging operations include, but are not limited to, clearing any current output on the screen, clearing and readying the program’s libraries and variables, and clearing any cache from a previous execution.
  
Miyâhkasike is an essential piece of code because not only does it have a very real programmatic purpose, but to have the system digitally mirror a user’s physical ceremonial practice transcends the system. It also symbolically provides the computer a spirit that the user can relate to as more of a living being instead of seeing the computer as a subordinate spiritless instrument. From an Indigenous perspective, this kind of human-machine connection is one of collaboration and kinship, and has been explored by several Indigenous scholars and artists [^noori2011]  [^lhirondelle2014]  [^lewis_etal2018].
  
  
  

## Pipon
  
  Pipon literally means winter. It, and its plural form  _pipona,_  along with the lexically related words pipohki (next winter), awasipipon (last winter), and mesakwanipipon (every winter)[^19]  are used in Ancestral Code as for loops.   
```unspecified
Pipon
```
  describes the single execution of a group of lines, and  
```unspecified
pipohki
```
 ,  
```unspecified
awasipipon
```
 , and  
```unspecified
mesakwanipipon
```
  are sub-functions that can only occur inside a repeating  
```unspecified
pipona
```
  loop.
  
You may ask why use pipon as a metaphor for the programmatic loop? Could you not use nîpin (summer) since it also occurs annually? What makes pipon important is its significance to aging and identity in Nehiyaw culture. For example, in Nehiyawewin, I say, I am currently 49 winters old. As heard from respected Nehiyaw culture and language instructor Reuben Quinn, we use winter and not another season because back in the days before comfortable housing in the northern climes of what is now Canada, surviving winter signified your resilience and survival of the most extreme elements of Earth Mother [^quinn2021]. Surviving winter is a valued and personal accomplishment. The symbolism in winter as a programming keyword lies in its representation as a repeatable cycle and in its relationships to aging and resilience that naturally imply increased experience and knowledge. So, similar to when a western-formatted computer program loops through a series of instructions, it often builds upon previously executed statements — the loop ages as it progresses and continues until the loop conditions are met or terminate.
  
  
  

## Waniyaw
  
Waniyaw is a word that can be used for meaning at random. In Ancestral Code, it is a way to simulate the dynamic and unpredictable forces of the natural world. Randomization is fundamental to Ancestral Code because of the generative nature of the outputs it creates. From a cultural perspective, I want the visual outputs to have aspects that are arbitrary and not controllable by the programmer. This environment of chance reflects the aspects of nature we cannot control. Therefore, giving the system some autonomy and decision-making is one way to prevent the programmer from always having complete control. In Nehiyaw culture, it is necessary to allow nature to run its course or recognize that there are elements in our world beyond the individual’s control.
  
  
  

## Randomization
  
In addition to the reserved keyword  
```unspecified
waniyaw
```
 , the words  
```unspecified
pipon
```
 ,  
```unspecified
mihcecis
```
 ,  
```unspecified
mihcet
```
 ,  
```unspecified
mihcetinwa
```
 [^20] , and the bound morpheme misi- incorporate randomization events in one form or another.
  
     
```unspecified
pipon
```
  – is the instruction for do once or literally for one winter, and all lines of code that proceed it are executed in random order until the ᙮  full stop is encountered.     
```unspecified
mihcecis
```
  – means small many and is used to produce a random number between 100 and 1,000.     
```unspecified
mihcet
```
  – means many and is used to produce a random number between 1,000 and 100,000.     
```unspecified
mihcetinwa
```
  – means numerous and is used to produce a random number between 100,000 and 1 million.     
```unspecified
waniyaw
```
  – is used in the context of the entire program or within a  
```unspecified
pipona
```
  loop block.  

  
So, for example, if the programmer wants a statement or series of statements to execute randomly, they would write it like this:  
```unspecified
waniyaw
```
  
```unspecified
 Wisakecahk
```
  
```unspecified
 pimohtew
```
   Ancestral Code interprets this instruction as have Wîsahkecâhk walk at a random interval. If this instruction is in the main body of the code, it will execute for random intervals from that point forward. If this instruction is inside a  
```unspecified
pipona
```
  block, it executes randomly only for as long as that loop is active and ends when the loop ends. In this use, the computer takes on the responsibility of nature, and each time the program is executed, the randomness introduced with  
```unspecified
waniyaw
```
  in the code guarantees the output will always be unique. This uniqueness is similar to how a story is never quite the same when repeated, even by the same storyteller.
  
  
  
  
  

## Conclusion
  
When it comes to coding in any of the thousands of computer programming languages available, a programmer is obliged to subscribe to and accept the social, technological, and cultural attitudes that created that language. Ancestral Code, is no exception, in that it is formulated to be more accessible to Nehiyaw users. However, in contrast to other (i.e., more common/traditional) computing languages, Ancestral Code is built on specific Nehiyaw cultural principles and not necessarily the lineal or logical requirements defined by the system. This difference means that Ancestral Code’s model and programming paradigm can alter computing philosophies and create new opportunities and avenues for Indigenous computer programming pedagogy.
  
 “Survivance,”  as defined by distinguished Indigenous cultural theorist Gerald Vizenor, is  “an active sense of presence, the continuance of native stories, not a mere reaction, or a survivable name. Native survivance stories are renunciations of dominance, tragedy and victimry” [^vizenor2008]. As a project, my intention in creating Ancestral Code was to make a system capable of collaborating with Indigenous knowledges to create a uniquely Indigenous experience within a digital space born from western computational sciences. Through a wholistic and Indigenous approach to computer programming, I have revealed that there can be a deep connection in the human-computer relationship paradigm, one that can advance programming practices to be more culturally informed while remaining relevant and critical to the survivance of Indigenous language and culture.
  
Using theoretical wholistic Indigenous design frameworks and culturally-determined computer programming language like the ones I described in this article, I am encouraging deeper critical discussions on the socio-technical philosophies of computer programming. Ancestral Code can be used as a template that seeks to harmonize cultural epistemologies and ontologies with computing by redefining computing philosophies through a cultural lens. It is a project meant to take a user on a voyage through Nehiyaw knowledges that have developed over millennia and have those knowledges define the relationships and models of modern computing. This journey then changes the relationship from one of human-and-computer to one that is culture-and-computer.
  
I feel this change in philosophy and approach to computer programming rewards both Indigenous and western computing cultures. From my perspective, a programmer’s identity is heavily imbued with western computing practices and personally meaningful relationships with software and the interaction with computing devices. This broadening and augmenting of software and hardware architectures are worthy of further investigation, especially for the potential benefits they can provide as a template for other Indigenous communities who wish to advocate and explore their cultural languages and teachings as programmatic interfaces.
  

  
  
  

## Glossary
    Standard Roman Orthography, IPA (Pronunciation), and Meaning of Nehiyawewin    Standard Roman Orthography  IPA (Pronunciation)  Meaning      âcimow  ʌtʃɪmow  [s/he] narrates [her/his] own story       acimosis   ʌtʃɪmʊsɪs  small dog; puppy      âniskôsîpiy  aːnɪskoːsiːpij  following the river; rejoin the river      atim   ʌtɪm  a dog      atimwa wâpamew minôs  ʌtɪmwʌ waːpʌmew mɪnoːs  the dog + is seen by + the cat      awasipipon   ʌwʌsɪpɪpʊn  last winter      kîsipayiw  kiːsɪpʌyiw  [something] ends or terminates      mâmitoneyihcikanihkân  maːmɪtonejɪhtʃikanɪhkaːn  computer; artificial brain      masinatakan cikastepayicikanis   mʌsɪnʌtʌgʌn tʃɪkʌsteːpajɪtʃikʌnɪs  computer; box of shadows      mesakwanipipon   meːsʌkwʌnɪpɪpʊn  every winter or every year      mihcecis   mɪhtʃeːtʃɪs  several      mihcet   mɪhtʃeːt  many      mihcetinwa   mɪhtʃeːtɪnwʌ  a lot; numerous      mînisiwat  miːnɪsɪwʌt  a bag used for berry picking      minôs  mɪnoːs  a cat      mistacimosis  mɪstʌtʃɪmʊsɪs  a pony      mistahi   mɪstʌhɪ  [something] is big or large      mistatim  mɪstʌtɪm  a horse; or a large dog      miyâhkasike   mijaːhkʌsɪgeː  [s/he] smudges with sweetgrass      nehiyaw  neːhɪyʌw  a Cree person; Cree culture      nehiyawewak  neːhɪyʌweːwʌk  Cree people (plural)      nehiyawewin  neːhɪyʌweːwɪn  Cree Language      nîpin   niːpɪn  summer time      nitâpân  nɪtaːbaːn  my great grandparent (grandmother)      nohkompân   nʊhkʊmbaːn  grandmother + passed on      pipohki   pɪpʊhkɪ  next winter      pipon   pɪpʊn  winter      pipona  pɪpʊnʌ  winters (plural)      sîpihkomipit  siːpɪhkʊmɪpɪt  bluetooth      sîpîsis   siːpiːsɪs  creek (small river)      sîpiy   siːpij  river      tisamân  tɪsʊmaːn  smudge      waniyaw  wʌnɪyʌw  at random; at a random time      wâpamew  waːpʊmew  [s/he] sees [her/him]      wîsahkecâhk  wiːsʌhkeːtʃaːhk  cultural teacher and legendary figure in Nehiyaw culture      
  
  

## Appendix
    Syllabic Numeracy Appendix (Numbers 1 to 100)    Hindu-Arabic Numbers  Nehiyawewin Syllabic-Numerals      1 - 10  l  ll  ᐅ  lᐅ  llᐅ  ᐅᐊ  ᐊ  ᐊl  ᐊll  ᒥ      11 - 20  ᒥl  ᒥll  ᒥᐅ  ᒥlᐅ  ᒥllᐅ  ᒥᐅᐊ  ᒥᐊ  ᒥᐊl  ᒥᐊll  ᓀ      21 - 30  ᓀl  ᓀll  ᓀᐅ  ᓀlᐅ  ᓀllᐅ  ᓀᐅᐊ  ᓀᐊ  ᓀᐊl  ᓀᐊll  ᓂ      31 - 40  ᓂl  ᓂll  ᓂᐅ  ᓂlᐅ  ᓂllᐅ  ᓂᐅᐊ  ᓂᐊ  ᓂᐊl  ᓂᐊll  ᓄ      41 - 50  ᓄl  ᓄll  ᓄᐅ  ᓄlᐅ  ᓄllᐅ  ᓄᐅᐊ  ᓄᐊ  ᓄᐊl  ᓄᐊll  ᓇ      51 - 60  ᓇl  ᓇll  ᓇᐅ  ᓇlᐅ  ᓇllᐅ  ᓇᐅᐊ  ᓇᐊ  ᓇᐊl  ᓇᐊll  ᑯ      61 - 70  ᑯl  ᑯll  ᑯᐅ  ᑯlᐅ  ᑯllᐅ  ᑯᐅᐊ  ᑯᐊ  ᑯᐊl  ᑯᐊll  ᑲ      71 - 80  ᑲl  ᑲll  ᑲᐅ  ᑲlᐅ  ᑲllᐅ  ᑲᐅᐊ  ᑲᐊ  ᑲᐊl  ᑲᐊll  ᑫ      81 - 90  ᑫl  ᑫll  ᑫᐅ  ᑫlᐅ  ᑫllᐅ  ᑫᐅᐊ  ᑫᐊ  ᑫᐊl  ᑫᐊll  ᑭ      91 - 100  ᑭl  ᑭll  ᑭᐅ  ᑭlᐅ  ᑭllᐅ  ᑭᐅᐊ  ᑭᐊ  ᑭᐊl  ᑭᐊll  lᒥᑕ      
  
[^1]: Nohkompan – grandmother who is passed on
[^2]:   Nitâpân  – great-grandmother
[^3]: ᐊᒋᒧ âcimow – story
[^4]: The font can be found at [https://www.evertype.com/emono/](https://www.evertype.com/emono/)
[^5]: See the [Syllabic Numeracy Appendix](#numeracy) for more
[^6]:   mâmitoneyihcikanihkân – one Nehiyaw word for computer, meaning artificial brain.
[^7]:   masinatakan cikastepayicikanis – another Nehiyaw word for computer. Roughly, a book or writing in a box of shadows.
[^8]:   mînisiwat – a berry bag.
[^9]:   âniskôsîpiy – where a river converges.
[^10]: atim, mistatim, acimosis, mistacimosis – dog, puppy, horse, pony; respectively
[^11]:   minôs wâpamew atimwa – the cat sees the dog.
[^12]:   sîpiy, sîpiy kîsipayiw – river, and the river ends
[^13]: pipon – winter 
[^14]:  Lewis Skolnick, portrayed by Robert Carradine, is one of the primary characters from the 1984 film  _Revenge of the Nerds_ .
[^15]:   Miyâhkasike – to smudge with sweetgrass or sage.
[^16]:   pipona – winters (plural of pipon).
[^17]:   waniyaw – random, or randomly.
[^18]:   tisamân – to smudge (in general).
[^19]: pipohki, awasipipon, mesakwanipipon – next winter, last winter, every winter; respectively.
[^20]:   mihcecis, mihcet, mihcetinwa – a few, many, a lot; respectively.  
[^abdelbarr2009]: Abd-El-Barr, Mostafa. (2009)  “Topological Network Design: A Survey.”    _Journal of Network and Computer Applications_  32 (3): 501–9.  
[^abdelnournocera_etal2013]: Abdelnour-Nocera, José, Torkil Clemmensen, and Masaaki Kurosu. (2013)  “Reframing HCI Through Local and Indigenous Perspectives.”    _International Journal of Human–Computer Interaction_  29 (4): 201–4. [https://doi.org/10.1080/10447318.2013.765759](https://doi.org/10.1080/10447318.2013.765759).  
[^absolon2010]: Absolon, Kathy. (2010)  “Indigenous Wholistic Theory: A Knowledge Set for Practice.”    _First Peoples Child & Family Review_  5 (2): 74–87. [https://doi.org/10.7202/1068933ar](https://doi.org/10.7202/1068933ar).  
[^aikin2009]: Aikin, Jim. (2009)  “The Inform 7 Handbook.”   [https://www.musicwords.net/if/I7Handbook8x11.pdf](https://www.musicwords.net/if/I7Handbook8x11.pdf).  
[^ali2014]: Ali, Mustafa. (2014)  “Towards a Decolonial Computing.”  In  _Ambiguous Technologies: Philosophical Issues, Practical Solutions, Human Nature_ , 28–35. Lisbon, Portugal: International Society of Ethics and Information Technology.  
[^arawjo2020]: Arawjo, Ian. (2020)  “To Write Code: The Cultural Fabrication of Programming Notation and Practice.”  In  _CHI ’20: Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems_ , 1–15. Honolulu, HI. [https://doi.org/10.1145/3313831.3376731](https://doi.org/10.1145/3313831.3376731).  
[^ardley2014]: Ardley, Sean. (2014)  “Why Are Monospaced Typefaces Used for Programming? (Answer (1 of 2)).”    _Quora_ . [https://www.quora.com/Why-are-monospaced-typefaces-used-for-programming/answer/Sean-Ardley](https://www.quora.com/Why-are-monospaced-typefaces-used-for-programming/answer/Sean-Ardley).  
[^babaoglu_etal2006]: Babaoglu, Ozalp, Geoffrey Canright, Andreas Deutsch, Gianni A Di Caro, Frederick Ducatelle, Luca M Gambardella, Niloy Ganguly, Márk Jelasity, Roberto Montemanni, and Alberto Montresor. (2006)  “Design Patterns from Biology for Distributed Computing.”    _ACM Transactions on Autonomous and Adaptive Systems (TAAS)_  1 (1): 26–66.  
[^benenson2012]: Benenson, Yaakov. (2012)  “Biomolecular Computing Systems: Principles, Progress and Potential.”    _Nature Reviews Genetics_  13 (7): 455–68.  
[^cormier_etal2018]: Cormier, Paul, and Lana Ray. (2018)  “A Tale of Two Drums: Kinoo’amaadawaad Megwaa Doodamawaad – ‘They Are Learning with Each Other While They Are Doing.’”  In  _Indigenous Research: Theories, Practices, and Relationships_ , edited by Deborah McGregor, Jean-Paul Restoule, and Rochelle Johnston, 112–25. Toronto, Canada: Canadian Scholars’ Press.  
[^dourish_etal2012]: Dourish, Paul, and Scott D Mainwaring. (2012)  “Ubicomp’s Colonial Impulse.”  In  _Proceedings of the 2012 ACM Conference on Ubiquitous Computing_ , 133–42. Pittsburgh, PA: Association for Computing Machinery, New York, NY.  
[^garneau2018]: Garneau, David. (2018)  “Electric Beads: On Indigenous Digital Formalism.”    _Visual Anthropology Review_  34 (1): 77–86.  
[^gca1857]: Gradual Civilization Act. (1857)  _An Act to Encourage the Gradual Civilization of the Indian Tribes in This Province, and to Amend the Laws Respecting Indians_ .  
[^hasselstrom_etal2001]: Hasselström, Karl, and Jon Åslund. (2001)  “The Shakespeare Programming Language.”  6/6/2018. [http://shakespearelang.sourceforge.net/](http://shakespearelang.sourceforge.net/).  
[^heaven2013]: Heaven, Douglas. (2013)  “One Minute with...Ramsey Nasser.”    _New Scientist_  217 (2909): 03–03.  
[^iso2016]: International Standards Organization. (2016)  “ISO/IEC 9995-9:2016 - Information Technology — Keyboard Layouts for Text and Office Systems — Part 9: Multi-Lingual, Multiscript Keyboard Layouts.”  ISO. 2016. [https://www.iso.org/cms/render/live/en/sites/isoorg/contents/data/standard/05/43/54374.html](https://www.iso.org/cms/render/live/en/sites/isoorg/contents/data/standard/05/43/54374.html).  
[^irani_etal2009]: Irani, Lilly C, and Paul Dourish. (2009)  “Postcolonial Interculturality.”  In , 249–52.  
[^irani_etal2010]: Irani, Lilly, Janet Vertesi, Paul Dourish, Kavita Philip, and Rebecca E Grinter. (2010)  “Postcolonial Computing: A Lens on Design and Development.”  In  _CHI ’10: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems_ , 1311–20. Atlanta, GA, USA: Association for Computing Machinery.  
[^king2022]: King, Kevin. (2022)  “Typotheque: Syllabics Typographic Guidelines and Local Typographic Preferences by Kevin King.”    _Typotheque_  (blog). January 24, 2022. [https://www.typotheque.com/articles/syllabics_typographic_guidelines](https://www.typotheque.com/articles/syllabics_typographic_guidelines).  
[^kleinrock_etal1980]: Kleinrock, Leonard, and Farouk Kamoun. (1980)  “Optimal Clustering Structures for Hierarchical Topological Design of Large Computer Networks.”    _Networks_  10 (3): 221–48.  
[^lewis_etal2018]: Lewis, Jason Edward, Noelani Arista, Archer Pechawis, and Suzanne Kite. (2018)  “Making Kin with the Machines.”    _Journal of Design and Science_ . [https://doi.org/10.21428/bfafd97b](https://doi.org/10.21428/bfafd97b).  
[^lhirondelle2014]: L’Hirondelle, Cheryl. (2014)  “Codetalkers Recounting Signals of Survival.”  In  _Coded Territories: Tracing Indigenous Pathways in New Media Art_ , edited by Steven Loft and Kerry Swanson, 147–68. Calgary, AB: University of Calgary Press.  
[^madden_etal2013]: Madden, Brooke, Marc Higgins, and Lisa Korteweg. (2013)  “‘Role Models Can’t Just Be on Posters’: Re/Membering Barriers to Indigenous Community Engagement.”    _Canadian Journal of Education_  36 (2): 212–47.  
[^merritt_etal2011]: Merritt, Samantha, and Shaowen Bardzell. (2011)  “Postcolonial Language and Culture Theory for HCI4D.”  In  _CHI’11 Extended Abstracts on Human Factors in Computing Systems_ , 1675–80.  
[^milloy2008]: Milloy, John. (2008)  “Indian Act Colonialism: A Century Of Dishonour, 1869-1969.”  Research Paper. Canada: National Centre for First Nations Governance.  
[^milloy2017]: Milloy, John S. (2017)  _A National Crime: The Canadian Government and the Residential School System_ . Vol. 11. Univ. of Manitoba Press.  
[^muzyka2018]: Muzyka, Kyle. (2018)  “A Hawaiian Team’s Mission to Translate Programming Language to Their Native Language | CBC Unreserved Radio.”  CBC Unreserved Radio. November 30, 2018. [https://www.cbc.ca/radio/unreserved/indigenous-language-finding-new-ways-to-connect-with-culture-1.4923962/a-hawaiian-team-s-mission-to-translate-programming-language-to-their-native-language-1.4926124](https://www.cbc.ca/radio/unreserved/indigenous-language-finding-new-ways-to-connect-with-culture-1.4923962/a-hawaiian-team-s-mission-to-translate-programming-language-to-their-native-language-1.4926124).  
[^nasser2012]: Nasser, Ramsey. (2012)  “قلب (‘Qalb’).”  2012. [https://nas.sr/%D9%82%D9%84%D8%A8/](https://nas.sr/%D9%82%D9%84%D8%A8/).  
[^noori2011]: Noori, Margaret. (2011)  “Waasechibiiwaabikoonsing Nd’anami’aami," Praying through a Wired Window": Using Technology to Teach Anishinaabemowin.”    _Studies in American Indian Literatures_  23 (2): 1–23.  
[^norman_etal2015]: Norman, Don, and Bruce Tognazzini. (2015)  “How Apple Is Giving Design A Bad Name.”    _Fast Company_  (blog). November 10, 2015. [https://www.fastcompany.com/3053406/how-apple-is-giving-design-a-bad-name](https://www.fastcompany.com/3053406/how-apple-is-giving-design-a-bad-name).  
[^noyes1983]: Noyes, Jan. (1983)  “The QWERTY Keyboard: A Review.”    _International Journal of Man-Machine Studies_  18 (3): 265–81.  
[^nugent2008]: Nugent, Benjamin. (2008)  _American Nerd: The Story of My People_ . Simon and Schuster.  
[^ogg2019]: Ogg, Arden. (2019)  “Hippopotamus in Cree: Solomon Ratt (y-Dialect).”    _Cree Literacy Network_  (blog). December 16, 2019. [https://creeliteracy.org/2019/12/16/hippopotamus-in-cree-solomon-ratt-y-dialect/](https://creeliteracy.org/2019/12/16/hippopotamus-in-cree-solomon-ratt-y-dialect/).  
[^okimasis_etal2008]: Okimasis, Jean, and Arok Wolvengrey. (2008)  _How to Spell It in Cree: The Standard Roman Orthography_ . misāskwatōminihk (Saskatoon): Houghton Boston, miywāsin ink.  
[^ormondparker_etal2013]: Ormond-Parker, Lyndon, Aaron David Samuel Corn, Kazuko Obata, and Sandy O’Sullivan. (2013)  _Information Technology and Indigenous Communities_ . AIATSIS Research Publications Canberra.  
[^philip_etal2012]: Philip, Kavita, Lilly Irani, and Paul Dourish. (2012)  “Postcolonial Computing: A Tactical Survey.”    _Science, Technology, & Human Values_  37 (1): 3–29.  
[^quinn2021]: Quinn, Ruben. (2021)  “Intermediate ᓀᐦᐃᔭᐤ Language Lessons.”  Zoom Course.  
[^risam2018]: Risam, Roopika. (2018)  _New Digital Worlds: Postcolonial Digital Humanities in Theory, Praxis, and Pedagogy_ . Evanston, Illinois, US: Northwestern University Press.  
[^shirt_etal2022]: Shirt, Marilyn, and Tina Wellman, eds. (2022)  _Tânisîsi Kâ-Ôsîtahk Pîkiskwêwinisa : Morphology Dictionary_ . St. Paul, AB: University nuhelot’ine thaiyots’i nistameyimâkanak Blue Quills.  
[^thomas2005]: Thomas, Robina Anne. (2005)  “Honouring the Oral Traditions of My Ancestors through Storytelling.”  In  _Research as Resistance: Critical, Indigenous and Anti-Oppressive Approaches_ , edited by Leslie Brown and Susan Strega, 237–54. Toronto, ON: Canadian Scholars’ Press/Women’s Press.  
[^travers1996]: Travers, Michael David. (1996)  “Programming with Agents: New Metaphors for Thinking About Computation.”  Doctor of Philosophy, Cambridge, MA: Massachusetts Institute of Technology.  
[^unicode2021]: Unicode, Inc. (2021)  “The Unicode Standard, Version 14.0.”  Unicode, Inc. [https://unicode.org/charts/PDF/U1400.pdf](https://unicode.org/charts/PDF/U1400.pdf).  
[^vee2017]: Vee, Annette. (2017)  _Coding Literacy: How Computer Programming Is Changing Writing_ . Mit Press.  
[^venne1981]: Venne, Sharon. (1981)  “Indian Acts and Amendments, 1868-1975.”  An indexed collection. University of Saskatchewan Native Law Centre, Saskatoon.  
[^vizenor2008]: Vizenor, Gerald Robert. (2008)  _Survivance: Narratives of Native Presence_ . U of Nebraska Press.  
[^warschauer1998]: Warschauer, Mark. (1998)  “Technology and Indigenous Language Revitalization: Analyzing the Experience of Hawai’i.”    _Canadian Modern Language Review_  55 (1): 139–59.  
[^wilson2008]: Wilson, Shawn. (2008)  _Research Is Ceremony: Indigenous Research Methods_ . Halifax, NS: Fernwood Publishing.  
[^wolfart1973]: Wolfart, H Christoph. (1973)  “Plains Cree: A Grammatical Study.”    _Transactions of the American Philosophical Society_  63 (5): 1–90.  
[^wolfart_etal1993]: Wolfart, H.C., and Freda Ahenakew, eds. (1993)  _Kinêhiyâwiwininaw Nêhiyawêwin. The Cree Language Is Our Identity: The La Ronge Lectures of Sarah Whitecalf_ . Winnipeg, MB, CA: University of Manitoba Press.  
[^worden_etal2011]: Worden, Keith, Wieslaw J Staszewski, and James J Hensman. 2011.  “Natural Computing for Mechanical Systems Research: A Tutorial Overview.”    _Mechanical Systems and Signal Processing_  25 (1): 4–111.  