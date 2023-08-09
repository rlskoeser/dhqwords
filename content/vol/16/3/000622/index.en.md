---
type: article
dhqtype: article
title: "Studying Large-Scale Behavioral Differences in Auschwitz-Birkenau with Simulation of Gendered Narratives"
date: 2022-06-25
article_id: "000622"
volume: 016
issue: 3
authors:
- Gábor Mihály Tóth
- Tim Hempel
- Krishna Somandepalli
- Shri Narayanan
translationType: original
categories:
- history
- gender
- interdisciplinarity
- data analytics
- cultural heritage
- collaboration
- data modeling
- oral history
abstract: |
   In Auschwitz-Birkenau men and women were detained separately; anecdotal evidence suggests that they behaved differently. However, producing evidence based insights into victims' behavior is challenging. Perpetrators frequently destroyed camp documentations; victims' perspective remains dispersed in thousands of oral history interviews with survivors. Listening to, watching, or reading these thousands of interviews is not viable, and there is no established computational approach to gather systematic evidence from a large number of interviews. In this study, by applying methods and concepts of molecular physics, we developed a conceptual framework and computational approach to study thousands of human stories and we investigated 6628 interviews by survivors of the Auschwitz-Birkenau death camp. We applied the concept of state space and the Markov State Model to model the ensemble of 6628 testimonies. The Markov State Model along with the Transition Path Theory allowed us to compare the way women and men remember their time in the camp. We found that acts of solidarity and social bonds are the most important topics in their testimonies. However, we found that women are much more likely to address these topics. We provide systematic evidence that not only were women more likely to recall solidarity and social relations in their belated testimonies but they were also more likely to perform acts of solidarity and form social bonds in Auschwitz-Birkenau. Oral history interviews with Holocaust survivors constitute an important digital cultural heritage that documents one of the darkest moments in human history; generally, oral history collections are ubiquitous sources of modern history and significant assets of libraries and archives. We anticipate that our conceptual and computational framework will contribute not only to the understanding of gender behavior but also to the exploration of oral history as a cultural heritage, as well as to the computational study of narratives. This paper presents novel synergies between history, computer science, and physics, and it aims to stimulate further collaborations between these fields.
teaser: "Applying methods and concepts from molecular physics to computationally approach over 6000 interviews of Aushwitz-Birkenau survivors."
order: 18
---
  
  

## I. Introduction
  
  

## 1. General background
  
The Auschwitz Concentration Camp Complex was liberated seventy-seven years ago on the 27th January 1945. Since then the camp where an estimated 1.1 million people were murdered has became the symbol of the Holocaust. Despite the large number of studies and memoirs by survivors, the question to what extent solidarity and social bonds existed among victims is still open [^pingel2010]  [^piper2009]. While some survivors claimed that friendships, mutual support, and solidarity among victims thrived, others have vehemently denied it.[^1]  It has been recently argued that solidarity and social bonds were key to survive Nazi concentration camps; no one could survive without the help of others and mutual aid was a form of opposition among victims [^swiebocki2000]  [^bacon2017]. Nevertheless, it has been also noted,  “conditions varied greatly across the vast Auschwitz complex”   [^wachsmann2015]. Some victims were therefore more likely to experience solidarity and form social bonds than others. Based on the close-reading of some victims’ accounts, some researchers have for instance suggested that group cohesion and solidarity were stronger among women, who were detained separately, than among men in Nazi death camps; however, in the lack of evidence, others have rejected this hypothesis [^pingel2010]  [^schwarz1998].
  
Even though a comparative study of how men and women behaved could enhance our understanding of the Holocaust from the victims’ perspective, producing evidence based insights into the world of Nazi concentration camps is challenging. Perpetrators destroyed camp documentation and victims’ perspective of the past is dispersed in tens of thousands of oral history interviews they gave. By watching a handful of interviews, we can gather only anecdotal evidence. At the moment, there is no reliable methodology to gather systematic evidence from a large number of oral history interviews. Traditional methods of corpus and computational linguistics cannot alone address this challenge. To produce systematic evidence from thousands of oral history interviews, it is important to account not only what is discussed but also how it is discussed. In other words, it is necessary to analyze how the narratives in thousands of oral history interviews unfold. We therefore developed a novel conceptual and computational approach adopted from the study of molecular processes. This novel method enabled us to study how narratives unfold in 2500 hours of oral history interviews with Auschwitz survivors. Even more importantly, it provided us with systematic evidence that among women solidarity and social bonds were stronger in Auschwitz.
  
Before presenting the results of our study, we introduce the dataset we worked with, the challenges it raises, and the way we tackled these challenges conceptually and computationally.

  
  

## 2. Our dataset and its historical context
  
In this study we analyzed testimonies given by 6628 Jewish victims (2033 men and 4595 women) born in 13 different countries. The 6628 victims we worked with all stayed in the Birkenau sub-camp of the Auschwitz complex.[^2]  In the Auschwitz camp system, Birkenau was the largest and the most lethal sub-camp where most Jewish victims were housed and perished.[^3]  After arriving at the camp, the SS [ _Die Schutzstaffel_ ], the Nazi paramilitary organization in charge of running death camps, selected those men and women who were able to work. Those who did not pass the arrival selection were murdered with Cyclon-B gas and cremated. Those few people who passed the arrival selection were deprived of their belongings, disinfected, registered (often tattooed) and forced to live in harsh conditions; men and women were housed in different sections of Birkenau. Victims often died due to starvation, various diseases, physical violence, and the extreme cold. During their stay in Birkenau, most victims had to work [^hayes2000]. Sometimes the SS could, however, not keep pace with the influx of new deportees, and victims were waiting to get some work. There was also a large group of victims in Birkenau who never worked. Auschwitz-Birkenau was also a transit camp from where victims were sent to other camps. During the time (which could be quite long) that victims were waiting for transfer, they were, in fact, not given any work; they just hung around in the camp. 
  
Our study is based on a data set that consists of oral history interviews with Holocaust victims. The USC Shoah Foundation provided us with this data set from its collection of approximately 50.000 Holocaust video testimonies recorded between 1981 and 2019. These video testimonies are preserved in the Visual History Archive of the Foundation at the University of Southern California in Los Angeles.[^4]  Precisely, the Foundation gave us access to all of its interviews with Auschwitz survivors, which is a collection of 12200 Interviews in 26 different languages recorded in 47 different countries. We were also provided with basic biodata (gender and place of birth) about each survivor whose testimony is included. Given that we limited our investigation to Jewish victims who stayed in the Birkenau subcamp of the Auschwitz complex, we worked with 6829 interviews from the original data pool. These interviews were conducted in 26 different languages in 43 different countries. 
  
Until today, only a small portion of USC Shoah Foundation’s testimonies have been transcribed and published [^toth2021]. In this study we could not therefore work with interview transcripts. We worked with the topical annotation of testimonies by the Foundation. In the last three decades, the professional staff of the Shoah Foundation indexed the minute based segments of each testimony with topic words from a designated thesaurus or controlled vocabularies. This thesaurus, a very large formally defined set of topic words, has been developed by the Foundation in the 1990s; the goal of the thesaurus is to cover all possible aspects of genocide experiences, including acts of solidarity and memories of social bonds [^gustman1998]. Professional annotators (or indexers as the Foundation calls them) watched testimony videos and indexed their content with the help of topic words from the thesaurus in a purpose-built testimony database; visual and audio features of testimonies were not indexed. 
  
For the purposes of this research the Foundation provided us access to the raw data underlying their testimony database.[^5]  The Foundation has reproduced, specifically for our study, all testimony segments, understood as a set of topic words (see a more technical description in the Implementation section), in which Auschwitz survivors discuss their stay in the camp. In our study, we relied exclusively on the English language topic words. Hence a limitation of our study is given by the fact that we were unable to study how topics related to solidarity and social bonds are discussed across testimonies in different languages. Another limitation of our study is that we were unable to work with the visual and audio aspects of the testimonies (see further discussion of these limitations in the Conclusion section).

  
  

## 3. Two Computational Challenges Related to Survivor Testimonies
  
Since the late 1970s archives and museums have been recording oral history interviews with Holocaust victims [^ecker2007]. The large-scale study of these interviews could offer a unique insight into victims’ experience [^greenspan2012]. Nevertheless, oral history testimonies raise two key computational and conceptual challenges.
  
Researchers would need to account for not only which topics are present in individual testimonies but also how these topics are discussed across thousands of testimonies. On the one hand, survivors’ oral history interviews consist of questions and answers. On the other hand, a survivor testimony is a sequence of topics that together form a narrative about the past. Survivor testimonies can be thus seen as an ensemble of individual narrative processes. Given that interviews unfold over time, the ensemble of narrative processes has an underlying dynamic. The first computational challenge that survivor testimonies raise can be summarized in the following two questions:
  
How can we model the ensemble of narrative processes understood as sequences of topics unfolding over time?  How can we measure the probability and the importance of topics in the ensemble of narrative processes?  

  
The second challenge relates to the latter question. Survivor testimonies are mediated. Survivors gave testimonies decades after their liberation; their testimonies may have been shaped by post-Holocaust culture, including films and novels. Furthermore, survivors recall deeply traumatic memories, which are characterized by flashbacks and the suppression of certain particularly painful themes [^langer1993]. Some survivors might overemphasize the significance of certain topics such as solidarity and social bonds, while others might underestimate it. Finally, the existing oral history testimonies are only the tip of the iceberg. The overwhelming majority of victims never had the chance to speak. For all these reasons, we needed a computational model that can take the mediated nature of survivor testimonies into account when measuring the probability and the importance of topics in narrative processes. 

  
  
  

## II. Methodology
  
  

## 1. Our Conceptual Framework
  
We developed a conceptual framework to tackle the problems above that is centered around three aspects: narrative system, narrative flux, and narrative pathway.
  
We define the narrative system as the ensemble of all possible topics that survivors address, including transitions between these topics. We represent the narrative system as a state space with topics as discrete states [^alpay2006]. Each interview, which is viewed as a sequence of consecutive topics, is a walking over the state space. In other words, each interview is a possible realization of the narrative system. Once all possible realizations were learned (see below), we could estimate the probability of each topic in the ensemble of all interviews. This approach also allowed us to compare testimonies of men and women. We viewed the interviews of each gender group as different instances of the same narrative system; we could thus compare the probabilities of topics that different instances yield (see the Implementation section).
  
To get insights into dynamics underlying narratives of survivors, we drew on the concepts of narrative pathway and narrative flux. In our conceptual framework, the narrative pathway describes a given sequence of states (i.e., topics) connecting two topics. The narrative flux quantifies the relative amount (percentage) of traffic going through a given narrative pathway. Consider the following example. 
  
Two key topics in testimonies are arrival at a death camp (arrival) and discussion of social relations ( _social bonds_ ). Testimonies can get from the topic arrival to the topic social bonds in many different ways. For instance, after discussing arrival, they can discuss the topic selection, and then social bonds. This corresponds to the narrative pathway  _arrival → selections → _ social bonds. The narrative flux considers all possible pathways between  _arrival_  and social bonds in the ensemble of all interviews (or interviews of women and interviews of men); then it tells us what fraction percentage goes through  _selections_ . In short, through the notion of narrative pathway and narrative flux, we can get insight into how narrative processes are likely to unfold in the ensemble of many testimonies.

  
  

## 2. Our Computational Model
  
From molecular physics we adopt the Markov State Model (MSM) and we perform a computational analysis of the ensemble of all interviews as a narrative system [^chodera2014]  [^husic2018]. Specifically, we use the Transition Path Theory (TPT) framework to model the dynamics of a narrative system [^vanden2006].
  
In the context of our research, we interpret the ensemble of interviews as realizations of a Markovian dynamic system; this is defined over a state space consisting of all topics that survivors address. By drawing on the Markov State Model we obtain the stationary probability (also known as equilibrium state or stable probability) of each topic. In simple terms, this describes the overall probability of hearing a survivor mentioning a topic if we keep listening to interviews for a reasonably long time (see the Implementation section for technical details on and definition of overall probability). 
  
We uncovered narrative pathways and quantified narrative flux by using the TPT, a quantitative framework based on MSMs [^metzner2009]. In the context of studying narrations with MSMs, TPT is used as a means to organize and summarize large numbers of individual narrations (i.e. sequences of consecutive topics or narrative pathways as realized in thousands of interviews) and to make them accessible to our interpretation. In practice, TPT associates a number value (called the flux) to any possible narration (or any possible sequence of topics). This number tells us how prevalent a given narrative pathway is in the underlying corpus of interviews, i.e., it summarizes how likely it is that an interviewee reported about topics in a certain order. We can therefore use TPT to sort narrations by their prevalence, which also allows us to identify the most common narrations from the data. 
  
This method was borrowed from dynamic systems modelling of molecular processes where TPT studies ensembles of reactive trajectories, i.e., trajectories that make transitions between defined starting state A and end state B. 
  
In our work, we considered interviews as such trajectories. TPT therefore analyses narrations from a starting to an ending topic. We have chosen topics associated with camp detention as the starting and topics associated with liberation as the ending points. The narrations are therefore handled consistently and our results show prevalent narrations that are aligned to the Auschwitz-Birkenau experiences.
  
We used the technique of pathway decomposition, elaborated as part of TPT, to uncover the most important sequences of states (narrative pathways in our research) and to quantify the amount of traffic (or flux) that goes through a certain sequence of states. As a whole, we used the TPT to decompose the ensemble of all possible narrative pathways by ranking each of the pathways by their flux. This enabled us to identify the busiest narrative pathways that men and women used between a pair of topics. 
  
Finally, based on our TPT analysis, we also model the narrative system as a directed graph. In this graph each topic (or a state in the state space model described above) is a node; the move of interviews from topic A to topic B is represented as an edge, which is weighted in terms of the probability of moving to topic B after topic A. To measure the importance and influence of each topic within the narrative system represented as a directed graph, we apply two different metrics. First, we measure the PageRank value of each topic as a node in the directed graph. The PageRank value is often used to measure the influence of humans in social networks, as well as the importance of webpages in Google search algorithms. By the same token as the PageRank value gives insight into the importance of webpages by modelling internet users movements from webpage to webpage, it reveals the importance of topics in survivor testimonies by modelling how these topics follow each other in testimonies. Actually, the PageRank values of nodes in a directed graph are closely related to the stationary probabilities described above; if a weighted directed graph represents a Markovian dynamic system, the PageRank values of nodes in the graph are the dumped stationary probabilities of states in the corresponding Markovian system [^page1999]. The major advantage of the PageRank value is that it takes into consideration inbound and outbound links to a given node (topic in the context of our research), as well as the importance of connected nodes; hence the PageRank value expresses how embedded a given node is in the entire network [^lee2013]. Second, we calculate the normalized closeness centrality of each node. This evaluates importance by summing the shortest paths from a given node; in other words, it expresses how connected a given node (or topic in the context of our research) is [^freeman1978].

  
  
  

## III. Our Results
  
  

## 1. Understanding the significance of topics related to solidarity and social bonds in survivor narratives
  
The 6628 Birkenau survivors we worked with discuss hundreds of topics when recalling their stay in the death camp; these topics cover many different aspects of camp life ranging from sanitary conditions to everyday interactions. As explained above, in the last three decades the Shoah Foundations’ indexer team watched these testimonies and annotated each testimony segment by means of topic words from the Foundation’s topical thesaurus. In total, there are 727 different topic words attached to interview segments related to Birkenau. However, many of these topics occur only in a few interviews. As a first step, a human agent with domain knowledge analyzed the 727 topic words and reduced them to 101 higher level topics (see Methodology). Next, we estimated the stationary probability of each higher level topic (when using probability we always mean the stationary probability of a topic). We specifically focused on two higher level topics: social bonds and aid giving. The former includes topics discussing social relations (friendships, camaraderie, non-intimate social relations etc.) in the camp; the latter relates to various acts of solidarity (food sharing, clothing provision, sustenance provision, etc.) We also calculated their closeness centrality and PageRank Value.
  
In the following, we ranked the topics according to stationary probability in descending order. This allowed us to identify the most probable topics in survivor narratives (see Figure 1). 
  
{{< figure src="resources/images/100002010000048000000480B51348C940EA26FD.png" caption="Wordcloud featuring the most probable topics in testimonies of Auschwitz-Birkenau survivors identified with a Markov State Model. The font size of topics is adjusted according to their stationary probability. The wordcloud demonstrates that two key topics related to solidarity and social bonds (aid giving and social bonds in red) are among the most probable topics. The word cloud also demonstrates that they are as probable as tattoo and more probable than clothing (in red)." alt="Image of a wordcloud"  >}}

  
Not surprisingly, one of the most probable topics that survivors discuss is  _selections_ . This is the third most common topic after living conditions and camp procedures. Selection was a wanton and highly feared practice in Nazi death camps. All victims arriving at camps first underwent a selection procedure. Selection was also a daily routine in Nazi concentration camps; the SS kept eliminating the unfit and sending them to gas chambers. Since selection was a highly probable event, we used it as a reference point to assess the probability of topics describing solidarity and social relations. Compared to  _social bonds_ , the probability of  _selections_  is 3.4 times higher. Compared to  _aid giving_ , the probability of  _selection_ s is 2.28 times higher.  _Aid giving_  and  _social bonds_  are not as probable as  _selections_ . But they are still very probable if we take into consideration that on average  _selections_  is 92 times more probable than any other topic. The overall importance of  _social relations_  and  _aid giving_  are also demonstrated by the fact that they are part of the upper quantile in the ranking of all topics in terms of their stationary probabilities.  _Aid giving _ is the 14th most probable topic and  _social bonds _ is the 18th most probable topic. The ranking of topics by PageRank value resulted in similar results.
  
We also measured the normalized closeness centrality of  _social bonds_  and  _aid giving _ in the directed graph representing the narrative system. We found that the topic  _aid giving _ is the 4th most important element of survivor narratives and  _social bonds_  is the 20th most important element in survivor narratives. They are both part of the upper quantile.
  
Due to the limitations of the Markovian framework (see Implementation section), we could not harness specific forms of social bonds and acts of solidarity. Our approach was restricted to broader topics. In the next section, as part of a comparative analysis of narratives by women and men, we will combine the Markovian framework with inferential statistics, which will give insights into details of social relations and acts of solidarity.
  
Our findings highlight that survivors discuss a great deal of social activity and solidarity when recalling memories of Birkenau. It is important to underline that survivors were not asked by interviewers to address solidarity and social bonds in the camp. It was the survivors' own decision to address these topics. In light of this, we think that what is recalled in the following testimony excerpt cannot be viewed as an anecdotal or nostalgic memory but in fact describes a relatively common experience:
  
> We became friends with everybody — anybody and everybody. We — we — we really cared for each other. We did everything possible to try and encourage each other. If somebody wanted to hang themselves because they couldn't take it any more; we somehow talked 'em out of it. If somebody, for instance, said, I'm giving up, I can't do it any more, we somehow talked them out of it. We maybe shared a little piece of bread. The bread was mostly made out of sawdust, but somehow we put a little piece of bread in his mouth. We did all kinds of those kinds of things.
  [^gross1996]  
  
  

## 2. Comparative analysis of solidarity and social relations in narratives of men and women
  
Men and women were detained and housed in different sections of Birkenau. We therefore examined and compared the probability of topics related to acts of solidarity and social bonds in narratives of women and men (see the Methodology section). To prove that differences were not due to either chance or sample bias, we used the method of bootstrapping (see below and the Methodology section) [^efron2004]. Again, we compared the importance of topics related to acts of solidarity and social bonds in narratives of men and women by drawing on normalized closeness centrality and the PageRank value. We also used the Fisher’s exact test to assess whether the difference is statistically significant (p value 0.05) [^fisher1922]. Finally, we measured the strength of association between gender and each topic with odds ratio analysis (Morris and Gardner, 1988). This enabled us to focus on specific forms of social bonds and acts of solidarity (see Figure 2).
  
{{< figure src="resources/images/10000201000004420000032908D2563EED142121.png" caption="Topics more likely to be discussed by women. Strength of association of topic words for gender of Auschwitz-Birkenau survivors was obtained by using odds ratio analysis; topic words are positively or negatively correlated for strengths of association >1 or <1, respectively; dot line shows a degree of association equals to one; the difference is statistically significant (p <0.05)." alt="Image of a bar graph"  >}}

  
{{< figure src="resources/images/10000201000004540000033C9E7F3B6ECB7F89D6.png" caption="Topics more likely to be discussed by men. Strength of association of topic words for gender of Auschwitz-Birkenau survivors was obtained by using odds ratio analysis; topic words are positively or negatively correlated for strengths of association >1 or <1, respectively; dot line shows a degree of association equals to one; the difference is statistically significant (p <0.05)." alt="Image of a bar graph"  >}}

  
We found that the topic  _social bonds _ is much more probable in testimonies of women; in their testimonies we are significantly more likely to hear about discussions of social relations in the camp. Our findings through bootstrapping is particularly revealing (see Figure 3). In short, over thousands of times we randomly sampled testimonies of women and men; each time we trained two Markov State Models over the same state space and measured the stationary probability of every topic. We observed that even if we randomly select testimonies of men and women, in the testimonies of women  _social bonds_  will always be more probable. The measurement of strength of association also confirmed this finding.  _Social bonds_  is positively correlated with women and negatively correlated with men. Finally, the normalized closeness centrality and the PagreRank value are also higher when testimonies of men and women are modeled as directed graphs. 
  
In the case of the topic  _aid giving_  the difference between men and women is less strong. The probability of this topic is only by 7 percent higher in testimonies of women, even though the difference between men and women is statistically significant and remains consistent through the randomized sampling (see Figure 3). Similarly, the normalized closeness centrality and the PageRank value are higher for women.
  
{{< figure src="resources/images/10000201000002C0000002AF77C61B34FEFC9AAA.png" caption="Bootstrap sample distributions for stationary probabilities for aid giving. The orange represents women, the blue men, and the dotted line the model estimate. Note that the distributions do not overlap. On the one hand, this means that the difference between stationary probabilities is significant given our model. On the other hand, it shows that if we randomly sample interviews by men and women over thousands of times, the stationary probability of topics above will always be higher in the women sample. In other words, the difference between men and women is consistent and not due to sample bias." alt="Image of plotted bars, some orange some blue."  >}}

  
{{< figure src="resources/images/10000201000002D0000002AF17A50E4147AA109A.png" caption="Bootstrap sample distributions for stationary probabilities for social bonds. Note that the distributions do not overlap. The orange represents women, the blue men, and the dotted line the model estimate. On the one hand, this means that the difference between stationary probabilities is significant given our model. On the other hand, it shows that if we randomly sample interviews by men and women over thousands of times, the stationary probability of topics above will always be higher in the women sample. In other words, the difference between men and women is consistent and not due to sample bias." alt="Image of plotted bars, some orange some blue."  >}}

  
With the help of statistical significance testing and odds ratio analysis, we also examined specific forms of solidarity and social bonds (see Figure 2 and 3). The Shoah Foundation’s keyword thesaurus has various terms to describe different types of solidarity. For instance, the topic word  _food sharing _ describes moments when a survivor recalls an episode of food sharing in the camp. We found that in testimonies of women we are much more likely to hear about episodes of food sharing. Similarly, women are more likely to discuss memories about another person providing them with clothes (the topic of  _clothing provision_ ). Other topics related to solidarity, such as for instance  _medical care provision _ and  _sustenance provision,_  are also positively correlated with women, though they lack statistical significance. As a whole, we were unable to find any topic related to solidarity, which is positively correlated with men.
  
The Shoah Foundation’s keyword thesaurus is less rich in terms of details about social bonds. Its keywords  _friends _ and  _friendships _ describe moments when survivors discuss intimate bonds in the camp. Again, we found a very strong and statistically significant positive correlation with women and a negative correlation with men. Similarly, women are more likely to recall less intimate social bonds from the camp. Other topics related to sociability and solidarity feature a similar difference. For instance, topics describing cultural activity, or rumors are all positively correlated with women (see Figure 2) and feature statistical significance. Women are also more likely to discuss suicide attempts in the camp.
  
At the same time, we also found interesting commonalities between men and women. It is a leitmotif in testimonies that victims warned each other. We did not find a significant difference in terms of the probability of hearing about this topic (see Figure 7). Another commonality is stealing (see Figure 6); victims often discuss memories about other victims stealing from them; men and women are equally likely to recall this experience. Finally, preferential treatment by camp functionaries is also equally likely to be recalled by both men and women (see Figure 8).
  
{{< figure src="resources/images/10000201000002C7000002AF3140CF882B872B14.png" caption="Bootstrap sample distributions for stationary probabilities for stealing. The orange represents women, the blue men, and the dotted line the model estimate. Note that the distributions overlap. This means that the difference between stationary probabilities is not significant given our model. If we randomly sample interviews by men and women over thousands of times, the stationary probability of topics above will sometimes be equal in the two samples." alt="Image of plotted bars, some orange some blue."  >}}

  
{{< figure src="resources/images/10000201000002C0000002AF1FE89702D25E3292.png" caption="Bootstrap sample distributions for stationary probabilities for warning. The orange represents women, the blue men, and the dotted line the model estimate. Note that the distributions overlap. This means that the difference between stationary probabilities is not significant given our model. If we randomly sample interviews by men and women over thousands of times, the stationary probability of topics above will sometimes be equal in the two samples." alt="Image of plotted bars, some orange some blue."  >}}

  
{{< figure src="resources/images/10000201000002C0000002AF1EFC6CDD52E44572.png" caption="Bootstrap sample distributions for stationary probabilities for preferential treatment. The orange represents women, the blue men, and the dotted line the model estimate. Note that the distributions overlap. This means that the difference between stationary probabilities is not significant given our model. If we randomly sample interviews by men and women over thousands of times, the stationary probability of topics above will sometimes be equal in the two samples." alt="Image of plotted bars, some orange some blue."  >}}

  
We also looked at those topics that dominate men's recalling of Auschwitz-Birkenau (see Figure 3). We found that men are more likely to recall topics related to physical violence (killings, beatings, executions, etc). Furthermore, we found that topics related to various clandestine activities (bribery, resistance, covert activities) are also more correlated with men than with women.
  
Furthermore, we examined whether the difference between women and men can be also observed if we compare men and women of the same nationalities. We found that the probability of topics related to social bonds and solidarity are either higher for women or there is no difference. We were unable to find any nationality where the probability of topics related to solidarity and social bonds would be higher for men. 
  
By further partitioning the data, we also surveyed women and men who did not work while they were in Birkenau. We observed the same trend as above. In narratives of women who did not report any forced labour activity, topics related to solidarity and social bonds are more probable.
  
Finally, we also studied the testimonies of those women and men who had to work. Given that the forced labour type and its difficulty varied a lot in Nazi death camps, we first divided the forced labour activities into three groups based on physical effort demands: easy work (secretarial work, science/research-related forced labor, translation etc), medium hard work (tattooing, factory work, gas chamber cleaning, etc), very hard physical work (mining, road and rail construction, etc). In our dataset, percentages of women and men who did the same type of work are quite similar. The majority of men (16.5% of all men survivors) and women survivors (14.5% of all women survivors) reported medium hard work. Even when comparing the working population of Birkenau, we could observe the trend that in narratives of women, topics related to social relations, friendships, and food sharing are more probable. However, there was no difference in the probability of the topic  _aid giving_ . This is equally probable in narratives of men and women who worked while they stayed in Birkenau.

  
  

## 3. Narrative pathways leading to and from topics of solidarity and social bonds
  
Using TPT, we found that both men and women discuss solidarity in the context of the everyday living environment (i.e., camp barrack) and forced labour activity, which is an interesting commonality. However, when we examined the narrative flux that goes through the most important narrative pathways leading to acts of solidarity in narratives of women and men, we found an important difference: women are more likely than men to discuss acts of solidarity in the context of camp barracks (see Figure 10 and Figure 12).
  
{{< figure src="resources/images/10000201000001B000000120D3FFA31BD5AB454C.png" caption="Topics related to solidarity following topics related to forced labour. Assessing the narrational context of topics related to solidarity and to social bonds by simulating how likely they are followed by topics related to forced labour activity in testimonies of women and men as a function of time lag. The plots show that women are more likely to discuss social bonds and acts of solidarity following the discussion of the everyday living environment in Auschwitz than men; whereas men are more likely to address these topics after addressing forced labor activity. Probabilities converge after a time lag of 3-5 minutes; hence, the plots highlight that the difference between men and women can be also observed once the dynamical systems representing the narratives of men and women reach equilibrium." alt="Image of line chart, some orange some blue."  >}}

  
{{< figure src="resources/images/10000201000001B000000120F63E3F022A034E7C.png" caption="Topics related to solidarity following topics related to living environment. Assessing the narrational context of topics related to solidarity and to social bonds by simulating how likely they are followed by topics related to the everyday living environment in testimonies of women and men as a function of time lag. The plots show that women are more likely to discuss social bonds and acts of solidarity following the discussion of the everyday living environment in Auschwitz than men; whereas men are more likely to address these topics after addressing forced labor activity. Probabilities converge after a time lag of 3-5 minutes; hence, the plots highlight that the difference between men and women can be also observed once the dynamical systems representing the narratives of men and women reach equilibrium." alt="Image of line chart, some orange some blue."  >}}

  
{{< figure src="resources/images/10000201000001B000000120D3FFA31BD5AB454C.png" caption="Topics related to social bonds following topics related to forced labour. Assessing the narrational context of topics related to solidarity and to social bonds by simulating how likely they are followed by topics related to forced labour activity in testimonies of women and men as a function of time lag. The plots show that women are more likely to discuss social bonds and acts of solidarity following the discussion of the everyday living environment in Auschwitz than men; whereas men are more likely to address these topics after addressing forced labor activity. Probabilities converge after a time lag of 3-5 minutes; hence, the plots highlight that the difference between men and women can be also observed once the dynamical systems representing the narratives of men and women reach equilibrium." alt="Image of line chart, some orange some blue."  >}}

  
{{< figure src="resources/images/10000201000001B000000120E9DF8A2616BEDBD1.png" caption="Topics related to social bonds following topics related to living environment. Assessing the narrational context of topics related to solidarity and to social bonds by simulating how likely they are followed by topics related to the everyday living environment in testimonies of women and men as a function of time lag. The plots show that women are more likely to discuss social bonds and acts of solidarity following the discussion of the everyday living environment in Auschwitz than men; whereas men are more likely to address these topics after addressing forced labor activity. Probabilities converge after a time lag of 3-5 minutes; hence, the plots highlight that the difference between men and women can be also observed once the dynamical systems representing the narratives of men and women reach equilibrium." alt="Image of line chart, some orange some blue."  >}}

  
We examined all possible pathways leading from the topic  _arrival_  to the topic  _aid giving_  in narratives of men and women. In narratives of women, more traffic is found going through the pathways in which  _aid giving_  is preceded by the topic  _living conditions._  For instance, the following narrative pathway is present in both men and women testimonies, but again, in testimonies of women the narrative flux (7.8%) is higher than in testimonies of men (5.2%):
  
   _arrival _ →  _selections _ →  _intake procedures _ →  _living conditions _ →  _aid giving_   
  
The investigation of narrative pathways connecting the topic  _living conditions_  with the topic  _aid giving_  also confirmed that women are more likely to connect solidarity with the world of their barracks.
  
We also found that in testimonies of women the discussion of social relations is more likely to be preceded by the discussion of living environments. The following narrative pathway is present in testimonies of both men and women. However, in testimonies of women the amount of narrative flux is much higher (14.12%) than in testimonies of men (9.7%).
  
   _arrival _ →  _ selections_ →  _camp procedures _ →  _living conditions _ →  _social bonds _   
  
Even though both men and women often discuss social relations and solidarity following forced labour activity, the narrative flux is much higher in the case of men (see Figure 9 and Figure 11). For instance, we examined all possible narrative pathways that connect the topic  _arrival_  with the
  
{{< figure src="resources/images/10000201000002D0000002D06925A6962E7159EF.png" caption="Network depiction of narrative pathways connecting the topic Arrival to Auschwitz with Social bonds in testimonies of women as extracted from Transition Path Theory pathway decomposition analysis. Circle sizes are adjusted according to the stationary probabilities of topics and connection arrow strengths visualize the amount of narrative flux going through a link. In testimonies of men most of the narrative flux is going from forced labor and living conditions to social relations, in testimonies of women, most of the narrative flux is going from food and living conditions to social relations." alt="Image of orange network graph."  >}}

  
{{< figure src="resources/images/10000201000002D0000002D028E6F8DE3A6F0373.png" caption="Network depiction of narrative pathways connecting the topic Arrival to Auschwitz with Social bonds in testimonies of men as extracted from Transition Path Theory pathway decomposition analysis. Circle sizes are adjusted according to the stationary probabilities of topics and connection arrow strengths visualize the amount of narrative flux going through a link. In testimonies of men most of the narrative flux is going from forced labor and living conditions to social relations, in testimonies of women, most of the narrative flux is going from food and living conditions to social relations." alt="Image of blue network graph."  >}}

  
topic  _social relations_  and involve  _forced labor_  priming social relations (see Figure 13 and Figure 14). In case of women, the following path is the most important one (the narrative flux is 3.6%):
  
   _arrival_ → _camp procedures_ → _living conditions_ → _forced labor_ → _social relations_   
  
In the case of men, the following path is the most important one (the narrative flux going through them is 6.8%).
  
   _arrival_ → _selections_ → _camp procedures_ → _tattoos_ → _forced labor _ → _social relations_   
  
To sum up, the way men and women discuss social relations and solidarity feature notable similarities. They both tend to discuss them following topics related to living and housing conditions and forced labor. Nevertheless, we also found that women are more likely to discuss social activity and acts of solidarity in the context of the everyday living environment; by contrast men tend to discuss solidarity and social relations in the context of forced labour. All this suggests that women mainly socialized in their barracks, whereas men experienced solidarity and social interactions in the working environment.

  
  
  

## 3. Conclusion
  
  

## 1. Discussion of results
  
The availability of large survivor testimony datasets is now making it possible to accomplish evidence based studies of victims’ experience during the Holocaust. A key problem has been how best to study thousands of testimonies together and produce systematic evidence. We modeled the testimonies of 6628 Auschwitz-Birkenau survivors with MSM, which 'summarized' the narratives underlying these testimonies. This gave us an unprecedented insight into victims’ experience.
  
We found that acts of solidarity and social ties among victims were not at all uncommon in Auschwitz-Birkenau. The significance of this finding can be understood in light of what researchers and survivors often described as dehumanization. The following words by a Hungarian survivor, demonstrate what dehumanization meant in Auschwitz-Birkenau:
  
> And, you know, it's very hard to explain how logic or emotion doesn't come into it. You're fighting for your life. You're fighting for a piece of bread. You don't think, now what do I think is happening? It's happening. You're glad today you weren't beaten. You're glad yesterday you had a mouthful more bread. You — you don't speculate. So this one was run onto the wire and got killed. Fine, she's. She's lucky. I'm not lucky. Because I haven't got the guts to do it. So that is the mentality. You know, that's how you live. You're not a human. You're dehumanized. You don't think. You follow instructions like an animal, not even — an animal wouldn't listen to it. So you become a piece of robot really, which if you don't where emotions and hunger meets or takes over.
  [^neumann1996]    
By reducing victims into a dehumanized state, the SS deliberately thwarted victims’ otherwise natural effort to take care of each other. Furthermore, the SS deliberately undermined social bonds between victims by frequently transferring them between forced labour squads, camps, and barracks. As the historian, Gideon Greif, has put it,  “the Nazi camp system aimed to break down all solidarity human relations as well as the belief in the possibility of self-determined actions”   [^greif1999]. The question whether some form of solidarity and sociability could still exist in Auschwitz-Birkenau therefore translates into the question of how successful the SS was in its effort to destroy the human nature of victims. Accounts such as the one above or the testimony excerpt cited at the beginning of this paper have often convinced researchers that solidarity and deeper human ties were actually anomalies in Auschwitz. For instance, the sociologist, Wolfgang Sofsky, has recently described the Nazi death camp as a place where victims lived in  “a social state of nature in which the person who prevailed was the one who was stronger”   [^sofsky2013]. This view is in contrast with the accounts of many survivors and with the findings of some historians. Again, as one survivor cited above said,  “we did everything possible to try and encourage each other.”  The hypothesis that solidarity and social bonds among victims were just anomalies in Auschwitz is also in contrast with our findings. 
  
In fact, the 6628 survivors in our dataset do speak about a great deal of solidarity and social interactions. Acts of solidarity and memories of social life are highly important elements of their memories. Their importance and high probability within the narrative system indicates that they were also significant and relatively frequent elements of camp life. Even if statistical frequencies and probabilities of topics measured by modelling thousands of narratives cannot be equated with the broader and non-statistical concept of importance, they can still be treated as reliable indicators giving information about the world that these narratives recall. As a matter of fact, we will never know how victims lived in Nazi death camps. But by analyzing thousands of survivor narratives, we can attempt to construct estimates about basic aspects of life in Nazi death camps. 
  
Our computational approach also allowed us to compare the narratives of women and men and to shed light on a key difference: in testimonies of women solidarity and social relations are more probable and more important topics than in testimonies of men. Based on the close reading of a handful of testimonies, this gender difference has been already noticed but lacked the backing of wide-scale quantitative evidence. In this study, we provide systematic evidence that in narratives of women survivors of Auschwitz-Birkenau solidarity and social relations are much more important topics. 
  
Nevertheless, this finding leads to a key problem that any study of belated memories about a past event involves. Memory sometimes alters the way humans see their past; therefore, we need to ask how can we produce evidence about the past by drawing on belated memories? Taking this question into the context of this study, to what extent does the fact that in belated memories of women solidarity and social bonds are more probable, indicate that they were also more prevalent in the women sections of Birkenau? We tackled this problem with the help of bootstrapping, i.e., with the help of randomized trials. It is possible that some women overestimate the importance of solidarity and social relations in the past and some men underestimate their significance; it is possible that memory and post-Holocaust experience (including watching specific films and reading Holocaust novels) have "sweetened" the experiences made in the past for some women and triggered bitterness in some men. Nevertheless, with the help of randomized samples we pointed out that the difference between men and women is consistent. If our initial finding that solidarity and social relations are more probable in narratives of women would have been due to the sweetening effect of nostalgic memory or due to sampling bias, the difference between men and women would have faded over thousands of randomized trials.
  
Our findings suggest that women generally tend to show more solidarity in extreme circumstances such as detainment. However, it is important to highlight a historical factor as a result of which social adaptation for Jewish men in Birkenau must have been particularly difficult. By the time that mass deportations of European Jewry to Auschwitz-Birkenau began, many of the young and middle aged Jewish men had already been in forced labour service [^gruner2006]. Most of the men who were deported to Auschwitz-Birkenau were older men; they had therefore very slim chances to survive the selection process at the arrival. As a result, most probably there were more women of the same nationalities than men of the same nationalities. Being surrounded by women of the same nationality, a woman could find solidarity and friends much easier than a man. To corroborate this explanation, we would however need to know more about whom women formed friendships with and who offered solidarity and help to them.[^6]   

  
  

## 2. Limitations of our methodology
  
This points out the limitation of this study. We could study only those topics that the Shoah Foundation’s index system covers. Unfortunately, the index system does not offer any information about whom victims were friends with. Neither does it contain keywords that signal conflicts between victims. We could not therefore study whether men or women are more likely to recall animosity. Similarly, the use of generalized keywords to describe human behavior has its own limitations since they cannot describe the richness and subtleties of human behavior. For instance, friendship and aid giving are complex concepts and behavioral patterns with many different possible meanings and nuances that a general keyword cannot describe. This limitation can in part explain the difference between men and women. When discussing social relations in the camp, women and men might express their ideas and memories very differently. Where women use friendship, men might for instance use other words that suggest less intimate social bonds. Unfortunately, the unified keyword system cannot account for such differences and the close-listening of 2500 hours of survivor testimonies is not viable. 
  
Another limitation of our study is that we could not work with interview transcripts in the original languages. Interviewees of different languages might have expressed similar experiences in different ways, which in turn might have produced unevenness in the topical annotation. For instance, victims of different linguistic backgrounds may use very different linguistic strategies to account experiences of social bonds and aid giving. 
  
Finally, topical annotation cannot address a key feature of traumatic narration. This is silence. Traumatic memories often remain suppressed and speakers lack the linguistic ability to articulate them. Hence, the bulk of traumatic memory can hardly be described with unified topic words. 

  
  

## 3. Implications for future research
  
Despite these limitations, the use of the Markov State Model has helped to tackle an old problem that among others, the Italian survivor of Auschwitz and the author of many Holocaust novels, Primo Levi (1917 - 1987), has pinpointed. This is the fallacy of the individual memory of a survivor. As Levi said, the human memory is a marvelous instrument but it makes mistakes [^levi1986]. The fallacy of individual memories can be counterbalanced with the study of the memory of many survivors. But the study of many individual memories poses its own challenges: testimonies are mediated and unbalanced in terms of gender for instance; they miss the voice of those who did not survive or did not give a testimony. To face these challenges, in this paper we applied the Markov State Model combined with the Transition Path Theory. This enabled us to approach thousands of individual testimonies as expressions of the collective experience. Most importantly, it enabled us to compare narratives of women and men. Future work can use the methods we present in this paper to study victims’ experience in other Nazi death camps. 
  
Future work can also rely on our methodological and conceptual approach to study a great variety of big data involving sequences of states in the humanities. Such datasets are ubiquitous in history and in other humanities fields. Datasets of national biographies, for instance the Oxford Dictionary of National Biography, could be studied by representing historical actors’ life trajectories as sequences of states. Similarly, the circulation of artistic objects among different owners (so-called object biographies) can be represented as sequences of states. The concept of state space and the Markov State Model can be applied to model and analyze these sequences of states. Most importantly, a methodology and conceptual framework applied to understand processes both in nature and in human civilizations can offer new bridges between science and humanities in the future.
  
  
  
  

## IV. Implementation
  
  

## 1. Introduction
  
In this paper we discuss our methodology and its implementation in two different sections. The Methodology section above aimed to offer a general overview of our methodology. Here we describe step-by-step how we implemented our methodology. In addition to the step-by-step description, Figure 15 and 16 also help understand the key steps in the implementation process. At the same time, for a complete understanding of the implementation, readers might need some background in probabilistic modeling, which we cannot provide here. 
  
{{< figure src="resources/images/1000000000000546000001F421C33AF51338077E.jpg" caption="Methodological Overview 1: From individual interviews to the modelling of 6628 interviews as a Markovian dynamic system. A, a single interview is processed into 1 minute segments that are assigned to topic terms each (color-coded). Interviews are therefore represented as sequences of consecutive topics (or narrative pathways). B The whole interview corpus consists of 6628 interviews that are converted into 6628 series of topic terms. B, Transition matrix that summarises the probabilities of hearing about a given topic following another topic as learned from all available interviews. The transition matrix can also be represented as a directed graph; nodes are the topics and the edge weights are the probabilities that an interviewee move from one topic to another, it therefore stores all possible narrative trajectories that a recalling of Auschwitz can follow in the corpus of all interviews. D. The “busiest” (or the most prevalent) narrative pathways obtained by means of Transition path theory (TPT). TPT extracts prevalent narrations from the MSM transition matrix; a narration is here depicted as a (possibly non-linear) sequence of topics that goes from left to right. Please note that this figure is a conceptual overview and does not represent real interview data." alt="Image of and overview of the methodology, this includes a network map, a probability chart and word selection."  >}}

  
{{< figure src="resources/images/100000000000034A000002535B983734ACF4184B.jpg" caption="Methodological Overview 2: Key steps to train and analyse a Markov State Model representing narratives of Auschwitz survivors." alt="Image of and overview of the methodology, this includes flow chart."  >}}

  
  
  

## 2. Preprocessing
  
In this research project we worked with the topic words that the trained expert human annotators of the Shoah Foundation had assigned to minute based segments of interviews in our data set. As a first step, we applied a feature engineering procedure; we grouped topic words and formed higher level topics. In total, we identified 101 higher level topics. Our feature selection procedure followed the keyword thesaurus of the Shoah Foundation. In this thesaurus each topic is clearly defined and formally not overlapping.
  
The interview dataset we worked with is a set of matrices. Each matrix represents an interview; the rows correspond to minute-based interview segments and the columns represent the topic words associated (higher level topics as described above) with segments as a “one-hot-encoding”. This segment-topic word matrix is similar to document-term matrices used in bag-of-words models of document collections in text mining. We can also view each segment-topic word matrix as a sequence of topics that form a discrete narrative pathway; hence we first represented the interviews as sets of consecutive topics.
  
Interview_1 = {topic 3, topic 1, topic 2 ………. topic n}
  
Interview_2 = {topic 4, topic 3, topic 2 ………. topic n}
  
Sometimes an interview segment can feature multiple topics. Consider the following example:
  
Interview_3 = {topic 3 -> topic 1, topic 4 -> topic 2}
  
Given that multiple topics may be assigned to certain segments, there is a fuzziness in the interview topic assignment. We address this fuzziness by randomly sampling from the topics of multi-topic segments. For instance, in case two topics are assigned to a segment, we treat it such that they could have occurred with either topic.
  
Interview_3_A = {topic 3 -> topic 1-> topic 2}
  
Interview_3_B = {topic 3 -> topic 4-> topic 2}
  
As we do not alter the sequence of topics, the dynamics is conserved. In other words, we interpret an interview as a set of pathways that are compressed into a single pathway with multi-topic segments, and therefore disentangle it into single pathways.

  
  

## 3. The construction of a state space and its Markov modelling
  
Next, we construct a state space from the sets of discrete narrative pathways. Each topic term is assigned a state number to allow further numerical processing; the topics are interpreted as discrete states of the state space. We treat each narrative pathway (i.e., interview) as walking over a state space that is spanned by the topic terms. The transition probabilities between discrete states are stored in a transition (probability) matrix. This is an n-by-n square matrix with n corresponding to the number of discrete states. The  _ij-_ th element of our transition matrix describes the probability that an interview discusses topic  _i_  after having addressed topic  _j_ . In molecular kinetics, this is called a conditional probability [^prinz2011]. In the context of our research, the transition (probability) matrix models the narrative system consisting of discrete states that are the topic terms; it also represents the way interviews are likely to move from one topic to another topic. We also use the transition matrix as an adjacency matrix; from this we construct the directed graph representing the narrative network of topics.
  
The transition matrix is the central object of the MSM. However, as the transition matrix describes the probability of hearing topic  _i _ in the future _, conditioned on topic j in the present, _ it does not tell the (unconditional) probability of topic  _i_  irrespectively of the previous topic. We can however estimate the unconditional probability, also referred to as stationary and equilibrium state probability earlier, by noting that it is the stable state that the system converges to in the limit of infinite time. It is often denoted by π and follows from applying the dynamics n → ∞ times, i.e. π = lim n → ∞ p0. It can be computed either by calculating the limit explicitly, or as the left eigenvector of the transition matrix that corresponds to eigenvalue 1. We applied this latter technique, also known as spectral decomposition of the transition matrix [^prinz2011]; specifically, we used the pyemma software package [^scherer2015]. The resulting MSM stationary distribution can be approached as an estimator of the unconditional probability of a dynamic system in equilibrium. In the context of our research, the unconditional probability of a topic gives the overall probability that we will hear about this topic irrespectively of the preceding topic. 

  
  

## 4. Application of TPT for the study of narrative pathways
  
To shed light upon the full network of narrations, we compute the TPT flux network between start topic A and end topic B [^scherer2015]. In brief, TPT defines the committor  _q_ + as the probability that on a pathway from A to B, at a given intermediate step of that pathway, we reach B before going back to A. In the context of this manuscript, the committor thus describes the probability that during a specific narration (defined by its starting topic A and ending topic B), the narrator speaking about an intermediate topic first reaches the end topic B before talking about the start topic A again. The backward committor analogously describes the probability to go back to A before visiting B. From these two definitions, the current (usually referred to as the reactive flux) between two topics  _i _ and  _j_  can be computed by multiplying the backward committor of  _i_  with the stationary probability of that topic and with the transition probability to change from that topic  _i_  to another topic  _j_ , multiplied by the committor of  _j_ .
  
To span the full flux network, this expression is evaluated between all topic terms for a given narration. In order to simplify the presented networks, we choose a cutoff of 0.25 below which we do not display a given link. The graph layout is conducted using a few-step general graph-layout algorithm (Fruchtermann-Reingold) started from points distributed according to their committor probability on the x-axis [^fruchterman1991].

  
  

## 5. Comparative analysis of narratives by women and men
  
To assess different kinds of sub-samples (e.g. women or men), the initial sets of narrative pathways are split according to biographical information known about the interviewee. Independent MSM estimates are established for each of these data sets. We compare unconditional probabilities per topic between different datasets by computing the ratio between them. This is possible as the full state spaces of the compared MSMs are spanned by the same set of topics. Furthermore, converged MSM estimates of unconditional probabilities do not depend on sample size. The estimates are thus not biased by different sample sizes as long as they are converged. Topics that are not in the active set of either MSM are not used for comparison. We estimate the error of probability estimates by bootstrapping of trajectories, i.e., we have re-evaluated the investigated models by drawing the same number of interviews from our database at random (with replacement). This is repeated 1000 times to estimate a posterior distribution of the MSM stationary probabilities. 

  
  

## 6. Validation of results
  
To validate our findings, on the one hand we use the implied timescales test [^wehmeyer2019]  [^bowman2014]. This tests for the convergence of the model with the chosen lag time, which is a necessary condition for the data’s Markovianity. On the other hand, to validate our results with a different method, we also drew on the direct counting of how many times a given topic occurs in testimonies of men and women. We compared the proportion of women who mention a given topic to the proportion of men who also mention that topic. We divided the data sample into men and women on the one hand, to those that mention and do not mention a topic on the other. For each topic this produced a 2x2 contingency table: number of women mentioning a topic, number of women not mentioning a topic; number of men mentioning a topic, number of men not mentioning a topic. To assess whether the difference between men and women is significant, we applied the Fisher exact test on the contingency tables representing each topic (p-value 0.05). This revealed whether the difference between men and women is due to chance (null-hypothesis) or whether there is a correlation between gender and the fact that a topic word is mentioned. Finally, we measured the strength of correlation between gender and a topic word with the help of odds ratio analysis [^morris1988].
  
  
  
  

## Funding
  
This research was funded by the Google Foundation.
  
  
  

## Acknowledgements
  
We are thankful to the USC Shoah Foundation for giving access to the dataset; we are particularly thankful to Sam Gustman, the Chief IT Officer, and to staff members of the Foundation for providing consultancy about the dataset. We are also grateful to prof. Wolf Gruener, director of the Center for Advanced Genocide Research (CAGR) at the USC Shoah Foundation, for reviewing and commenting this paper.
  
Data Availability
  
Original interviews can be retrieved from the designated website of the Visual History Archive of the Shoah Foundation: [https://vhaonline.usc.edu/](https://vhaonline.usc.edu/). The raw data used for this research can be downloaded from Harvard Dataverse:
  
Toth, Gabor Mihaly, 2021, "Replication Data for the VHA Auschwitz Report Project", https://doi.org/10.7910/DVN/JFH2BJ, Harvard Dataverse, V1
  
Code Availability
  
All research code (including data analysis in Python Jupyter Notebooks) to reproduce this project is available in the following repository: [https://github.com/toth12/vha_auschwitz_report](https://github.com/toth12/vha_auschwitz_report). 
  
  
  

## Author Contributions
  
Gábor Mihály Tóth conceived of, designed, and led this project. He processed the dataset, developed the computational model, and accomplished the data analysis. With assistance of the co-authors he wrote this paper.
  
Tim Hempel contributed to research design, data processing, and computational modeling. He revised the manuscript, in particular the Methods section, and created Figure 15.
  
Krishna Somandapelli contributed to the research design and edited the paper.
  
Shri Narayan contributed to the research design, edited, and revised this paper. He secured funding for the project.
  
  
[^1]:  The following account by a German Jewish survivor of Auschwitz illustrates the sharp contrast between the two opinions:  “And I should preface this by saying, in general, you know, I've read a lot — a lot of claims about the solidarity of prisoners under those conditions. And I must tell you I've never seen it. I've heard about solidarity in the block occupied by Russian officers, Red Army officers. But I'm pretty sure that was the only — if — if at all, that was the only group that showed any solidarity whatsoever. The atmosphere in the camp was such that everybody was out for their own survival. And if it was a question of — of listening in to what your neighbors in the bed said, it would immediately be handed on so that — for personal profit. You couldn't trust anybody. And nobody trusted anybody.”   [^chrambach1996]. See a very different view in the memoir of the Polish sociologist [^pawełczyńska1973].
[^2]:  The Auschwitz complex came to existence in the Spring of 1940 in Southern Poland (that time part of Nazi Germany) about 70 km from Cracow. Over the subsequent years, the complex continued to grow incorporating various sub-camps.
[^3]:  The construction of Auschwitz-Birkenau (renamed Auschwitz II in November, 1943) began in the Autumn of 1941 and started to receive deportees from the Spring of 1942. In addition to an extremely large Jewish population, Birkenau also housed Polish and Roma victims. It was both a killing center, equipped with gas chambers and crematoria, and a work camp where victims were forced to slave labour. Victims were transported by trains to Birkenau from various European countries.
[^4]:  For more details see the website of Shoah Foundation,[https://sfi.usc.edu/](https://sfi.usc.edu/).
[^5]:  Upon registration, the dataset we worked on is accessible through the purpose built webinterface of the Visual History Archive, see [https://vhaonline.usc.edu](https://vhaonline.usc.edu).
[^6]: For instance, the mass deportations of the Hungarian Jewry began in the Spring of 1944. Hungarian Jewish men had been taken to forced labour from 1941. The vast majority of younger Hungarian Jewish men were not deported to Auschwitz [^braham1977]  [^michelbacher2020].  
[^alpay2006]:  Alpay, D., Gohberg, I.  _The State Space Method: Generalizations and Applications_ . Birkhäuser Verlag, Basel (2006).  
[^bacon2017]:  Bacon, E. K.  _Saving Lives in Auschwitz: The Prisoners Hospital in Buna-Monowitz_ . Purdue University Press, West Lafayette (2017).  
[^bowman2014]: ] Bowman, G. R., Noé, F.  “Software for Building Markov State Models”  In  _Advances in Experimental Medicine and Biology_ . Springer Netherlands, Dordrecht (2014), pp. 139–139.  
[^braham1977]:  Braham, R. L.  “The Hungarian Labor Service System, 1939-1945.”    _East European Quarterly_ , Boulder (Co) (1977).  
[^chodera2014]:  Chodera, J.D., Noé, F.  “Markov state models of biomolecular conformational dynamics,”    _Current Opinion in Structural Biology_ , 25 (2014): 135–144.  
[^chrambach1996]:  Chrambach, A.  “Oral History Interview.”  USC, Shoah Foundation,  _Visual History Archive_ , 23428, Los Angeles, (1996).  
[^ecker2007]:  Ecker, M.  “Verbalizing the Holocaust: Oral / Audivisual Testimonies of Holocaust Survivors.”  In M. L. Davies and C. W. Szejnmann (eds),  _How the Holocaust Looks Now: International Perspectives_ , Palgrave Macmillan, New York (2007), pp. 41–49.  
[^efron2004]:  Efron, B. Rogosa, D. and Tibshirani, R.  “ Resampling methods of estimation.”  In J. D. Wright (ed.),  _International Encyclopedia of the Social & Behavioral Sciences_ , Elsevier, Amsterdam (2004), pp. 492 - 495.  
[^fisher1922]:  Fisher, R. A.  “On the Interpretation of χ 2 from Contingency Tables, and the Calculation of P” ,  _Journal of the Royal Statistical Society_  85 (1922): 87-94.  
[^freeman1978]:  Freeman, L. C.  “Centrality in social networks conceptual clarification” ,  _Social Networks_  1 (1978): 215–239.   
[^fruchterman1991]:  Fruchterman, T. M. J. and Reingold, E. M. 1991.  “Graph drawing by force-directed placement” ,  _Software: Practice and Experience_  21 (1991): 1129–1164.   
[^greenspan2012]:  Greenspan, H.  “Survivors’ Accounts.”  In P. Hayes and J. K. Roth (eds),  _The Oxford Handbook of Holocaust Studies_ , Oxford University Press, Oxford (2012), 10.1093/oxfordhb/9780199211869.003.0028.  
[^greif1999]:  Greif, G.  “Solidarity and Animosity among Sonderkommando Prisoners in Auschwitz-Birkenau” ,  _The Journal of Holocaust Research_ , 33:4 (1999): 239-253.  
[^gross1996]:  Gross, A.  “Oral History Interview,”  USC, Shoah Foundation,  _Visual History Archive_ , 11272, Los Angeles (1996).  
[^gruner2006]:  Gruner, W.  _Jewish Forced Labor Under the Nazis: Economic Needs and Racial Aims, 1938-1944._  Cambridge University Press, Cambridge (2006).  
[^gustman1998]:  Gustman, S.  “Method and Apparatus for Cataloguing Multimedia Data,”  U.S. Patent 5,832,495190 (Nov. 3, 1998).  
[^hayes2000]:  Hayes, P.  _Industry and Ideology: I. G. Farben in the Nazi Era._  Cambridge University Press, Cambridge (2000).  
[^husic2018]:  Husic, B. E. and Pande, V. S.  “Markov State Models: From an Art to a Science” ,  _Journal of the American Chemical Society_ , 140 (2018): 2386–2396.  
[^langer1993]:  Langer, L. L.  _Holocaust Testimonies: The Ruins of Memory_ . Yale University Press, New Haven (1993).  
[^lee2013]:  Lee, C., Ozdaglar, A. and Shah. D.  “Computing the Stationary Distribution Locally.”  In  _Advances in Neural Information Processing Systems_  (2013): 1376-1384.  
[^levi1986]:  Levi, P.  _I sommersi e i salvati._  Einaudi, Torino (1986).  
[^metzner2009]:  Metzner, P., Schütte, C., Vanden-Eijnden, E.  “Transition Path Theory for Markov Jump Processes” ,  _Multiscale Modeling & Simulation_ , 7 (2009): 1192–1219.  
[^michelbacher2020]:  Michelbacher, D.  _Jewish Forced Labor in Romania, 1940–1944._  Indiana University Press, Bloomington (2020).  
[^morris1988]:  Morris, J. A. and Gardner, M. J.  “Statistics in Medicine: Calculating confidence intervals for relative risks (odds ratios) and standardised ratios and rates”    _BMJ_ , 296 (1988): 1313–1316.  
[^neumann1996]:  Neumann, E.  “Oral History Interview,”  USC, Shoah Foundation,  _Visual History Archive_ , 15938, Los Angeles, (1996).  
[^page1999]:  Page, L., Brin, S. and Winograd, T.  “The PageRank Citation Ranking: Bringing Order to the Web” ,  _Stanford InfoLab Publication Server_  (1999): http://ilpubs.stanford.edu:8090/422/  
[^pawełczyńska1973]:  Pawełczyńska, A.  _Wartości a przemoc: Zarys socjologicznej problematyki Oświe̜cimia._  PWN, Warschau (1973).  
[^pingel2010]:  Pingel, F.  “Social life in an unsocial environment: the inmates’ struggle for survival.”  In Wachsmann N. and Caplan, J. (eds)  _Concentration Camps in Nazi Germany: The New Histories_ , Routledge, London (2010): pp. 58–82.  
[^piper2009]:  Piper, F.  “Auschwitz.”  In Megargee, G. P. (ed.)  _The United States Holocaust Memorial Museum Encyclopedia of Camps and Ghettos, 1933-1945_ . Indiana UP in Association with the United States Holocaust Memorial Museum, Bloomington (2009): pp. 203–214.  
[^prinz2011]:  Prinz, J. H., Wu, H., Sarich, M., Keller, B., Senne, M., Held, M., Chodera, J.D., Schütte, C., Noé, F.  “Markov models of molecular kinetics: Generation and validation,”    _The Journal of Chemical Physics_  134, 174105 (2011): https://doi.org/10.1063/1.3565032.  
[^scherer2015]:  Scherer, M. K., Trendelkamp-Schroer, B., Paul, F., Pérez-Hernández, G., Hoffmann, M., Plattner, N., Wehmeyer, C., Prinz, J.-H., Noé, F.,  “PyEMMA 2: A Software Package for Estimation, Validation, and Analysis of Markov Models,”    _Journal of Chemical Theory and Computation_ , 11 (2015): 5525–5542.  
[^schwarz1998]:  Schwarz, G.  “Frauen in Konzentrationslager – Täterinnen und Zuschauerinnen.”  In Herbert, U., Orth, K., Dieckmann, C. (eds) Die  _Nationalsozialistischen Konzentrationslager: Entwicklung Und Struktur, Wallstein Verlag, Göttingen_  (1998): pp. 800–821.  
[^toth2021]:  Toth. G. M.  _In Search of the Drowned: Testimonies and Testimonial Fragments of the Holocaust._  Yale Fortunoff Archive, New Haven (2021), lts.fortunoff.library.yale.edu, lGabor Toth2022-03-04T12:51:22, last accessed, 1 March, 2022.  
[^sofsky2013]:  Sofsky, W.  _The Order of Terror: The Concentration Camp._  Princeton University Press, Princeton (2013).  
[^usc2022]:  USC Shoah Foundation, [https://sfi.usc.edu/](https://sfi.usc.edu/), last accessed, 1 March, 2022.  
[^vanden2006]:  Vanden-Eijnden, E.  “Transition Path Theory.”  In Ferrario, M., Ciccotti, G., Binder K. (eds),  _Computer Simulations in Condensed Matter Systems: From Materials to Chemical Biology Volume 1. Lecture Notes in Physics_ . Springer, Berlin (2006): pp. 453 - 493.  
[^visualhistoryarchive]:  Visual History Archive, USC Shoah Foundation, [https://vhaonline.usc.edu/about/archive](https://vhaonline.usc.edu/about/archive), last accessed, 1 March, 2022.  
[^wehmeyer2019]:  Wehmeyer, C., Scherer, M. K., Hempel, T., Husic, B. E., Olsson, S., Noé, F.  “Introduction to Markov state modeling with the PyEMMA software” ,  _Living Journal of Computational Molecular Science_  1 (2019): [https://doi.org/10.33011/livecoms.1.1.5965](https://doi.org/10.33011/livecoms.1.1.5965)    
[^wachsmann2015]:  Wachsmann, N.  _KL: A History of the Nazi Concentration Camps._  Macmillan, New York, (2015).  
[^swiebocki2000]:  Swiebocki, H.  _Auschwitz: 1940-1945 ; central issues in the history of the camp Volume IV._  Auschwitz-Birkenau State Museum, Oswiecim (2000).  