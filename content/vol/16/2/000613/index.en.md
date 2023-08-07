---
type: article
dhqtype: article
title: "Rediscussing the Political Struggle in the Light of Reform in Late 11th Century China under the View of Digital Humanities"
date: 2022-04-21
article_id: "000613"
volume: 016
issue: 2
authors:
- Wenyi Shang
- Winbin Huang
translationType: original
tags:
- digital humanities
- political struggle
- literati politics
- Northern Song dynasty
- Reform of Wang Anshi
abstract: |
   In late 11th century, a reform carried out by Wang Anshi (1021–1086) brought about controversies and initiated a series of political struggles between factionalized reformers and anti-reformers. The origin and nature of these factionalized struggles have been discussed for a long time among scholars. In this paper, we discuss the issue based on the literary and political relationships among people in the era of the reform. First, two matrices are respectively constructed of the literary and political relations among these people based on the data collected from CBDB (China Biographical Database). Then a Poission-Gamma factorization model is adopted to obtain the key factors of the matrices, and the Louvain Modularity algorithm is used for community detection. The results show that people engaging in similar literary pursuits were more likely to share political interests and people belonging to the same literary groups were more likely to join in the same political groups, suggesting. Ensuing discussions illustrate that people’s differing academic views indeed played a shaping role in the formation and exacerbation of factionalized struggle, for which the mechanism unfolded herein of “literati politics” was highly responsible.
teaser: "Illustrating a feature of “literati politics” which was prominent in 11th century China via a Poission-Gamma factorization model and the Louvain Modularity algorithm."
order: 20
---
  
  

## 1 Introduction
  
The political struggle among factions in the light of the reform in late 11th century China is considered as a decisive period in the Northern Song dynasty (960–1127). Beginning in 1069, Wang Anshi carried out the  _Wang Anshi bianfa _ [Reform of Wang Anshi] under the support of Emperor Shenzong (r. 1067–1085), aiming at changing the  _jipinjiruo_  [unceasingly impoverished and weakened] situation of the state. The  _xinfa_  [new policies] initiated in the reform include a group of financial, social, and military policies that enormously changed the state’s political mechanism, thus resulting in severe resistance from the conservative officials and a long-lasting political dispute. In 1085, when Emperor Shenzong died, the Empress Dowager Gao (1032–1093) came into power. During her reign, all reform policies were abolished and most pro-reform officials were exiled. However, when she died and Emperor Zhezong (r. 1085–1100), a firm supporter of the reform, took authority, the reform policies were continued and the anti-reformers were persecuted, and this tug of war had its culmination in the uncontrollable political strife during the reign of Emperor Huizong (r. 1100–1126).
  
Because of the controversial nature of the reform, debates on it have never stopped. Since the reform was a decisive political issue of that time, all contemporary officials had to take their sides, and many of them had a fairly radical stance. For example, one anti-reformer, Yang Shi (1053–1135) claimed that  “the origin of the disaster today was because of Wang Anshi”   [^tuotuo1985], and imputed the collapse of Northern Song to the reform. However, many 20th century scholars argued that the reform was the only way to save the corrupt government and bring prosperity to the state. For instance, Liang Qichao held the view that Wang Anshi’s effort was a response to the need of his time, and a recuperation from the crisis [^liang1993]. No matter how scholars’ views differ on the reform, its significance was undoubted, and there is a consensus that the political struggle following the reform was the direct cause of the fall of the empire.
  
The historical and cultural context of the reform should also be addressed. The Song dynasty featured  “literati politics” , a regime in which the government officials mostly came from the scholar-gentry who had earned academic degrees. Under this regime, the officials are known as scholar-officials and are both active in political and literary circles. According to the enduringly influential and widely accepted model Tang-Song transition by Naito Konan [^fogel1984], the Song dynasty is considered as a decisive period of the development of the literati politics, a period when government openings began to be widely occupied by scholar-officials. The Song dynasty also witnessed an unprecedented prosperity of  _Daoxue_  [Neo-Confucianism], in which scholars were affiliated to different schools of  _Daoxue_  and held different academic and ideological views. During the reform, these scholar-officials with different academic inclinations also tended to hold different views about the reform. The shaping power of the literati’s academic backgrounds on their stances toward the reform was discussed by a 20th century scholar Cheng Yangzhi, who considered that the dispute between the reformers and the anti-reformers was rooted in their different academic opinions [^cheng1942].
  
But this view is still not widely accepted, and the debate on the origin of the political struggle among factions in the light of the reform is not yet settled. Different scholarly views chiefly rise from different interpretations of existing historical sources, which are themselves not sufficient enough in many cases to serve as concrete pieces of evidence. By introducing digital methods and observing existing historical data in a more comprehensive way, however, it is possible to gain more solid arguments for the problem.
  
Thanks to the proliferation of digitized historical records, digital methods have been adopted in many studies of Sinology. Specifically, a relational database for Sinology, CBDB (China Biographical Database) [^harvarduniversity2018] has inspired much research, among which the political factions in the Song dynasty (960–1279) have attracted a wealth of attention. For instance, Hilde De Weerdt et al. investigated the structure of Song dynasty faction lists on the basis of large-scale network analysis with the help of CBDB data [^deweerdt2019], while one of our previous studies focused on the relationship between scholars and politicians in the Yuanyou Era (1086–1094) based exclusively on the data harvested from CBDB [^shang2018]. Following the direction opened up by previous work, this article investigates the experimental data from CBDB with exploratory statistical methods to revisit the debates around the origin of the factionalized struggle. In this sense, our research can be considered as an attempt from the community of digital humanities to facilitate the study of premodern Chinese history.
  
Following Cheng Yangzhi, but based on a totally different methodology, we try to provide a supplement to understand how close the links among scholars and politicians are by investigating the relationships among people who are active in late 11th century when the reform took place. Our study tries to verify the following hypotheses: 
  

 * a. People who were engaged in common literary pursuits tended to share political interests [^1] .  
 * b. People in common literary groups were likely to belong to the same political groups.  
 * c. Literati politics and political struggle in the Northern Song dynasty interrelated with each other.

  
Here, the first two hypotheses can be directly tested with exploratory experiments. Verifying them with quantitative evidence would strongly suggest the existence of the feature of  “literati politics” , where scholar-officials are active in both literary and political groups that formed around common literary pursuits and political interests. And since the opinion leaders in the literary world and the leaders of prominent philosophical schools in the Northern Song dynasty, such as Wang Anshi, Su Shi, and Cheng Yi, were also important politicians who carried out and resisted the reform, confirming the concomitance between political and literary relations would shed light on the origin and nature of the political struggle. In order to gain insights into it, the last hypothesis is discussed based on primary historical sources to demonstrate how the mechanism of “literati politics” actually influenced the political struggle.
  
We use quantitative methods to explore and texture literary and political affiliations among people. First, two correlation matrices constructed from the data collected from CBDB indicate their connections in literary and in political aspects, respectively. The features of the matrices, having been processed by dimensionality reduction, are then extracted as literary pursuits and political interests. Afterwards, Louvain Modularity is applied for community detection. Our experiment results in some interesting points, which can also be confirmed with primary historical sources.
  
We present a literature review on discussions of the origin and nature of the political struggle and the literati politics in part two. Our method is outlined in part three, including data collection, dimensionality reduction and community detection. The findings are shown in part four based on our results, and discussion in the context of the primary historical sources is given in part five. We offer a conclusion in part six.

  
  

## 2 Literature Review
  
  

## 2.1 Origin and Nature of the Struggle among Political Factions in the Light of Reform
  
There are four typical views towards the origin and nature of the factionalized struggle in the light of the reform. The dominant view in the late 20th century Chinese academic world is that the struggle was rooted in different class interests. Yang Rongguo is a representative scholar holding the view [^yang1946]. He and other scholars holding this view frequently cite the remonstration of Wen Yanbo (1006–1097) to Emperor Shenzong,  “Your majesty rules the nation with the scholar-officials, instead of the ordinary people”   [^li2004]
  
The second view, chiefly held by Liang Qichao, imputes the political struggle to emotionality, and his main point is  “the members of each faction weren’t necessary to combine with each other purposefully. However, they will raise disputes whenever an issue occurs. If there is one person initiating an argument, there will be hundreds of henchmen following him. In a word, they just acted out of emotionality”   [^liang1993]. Liang’s opinion had a great influence on later scholars although his attribution of the political struggle to “emotionality” is criticized as oversimplifying the problem.
  
The third view is to attribute the problem to different regional ideas. It is proposed by Hu Shi in his comments on Li Gou (1009–1059), a philosopher and a countryman of Wang Anshi.  “Both Li Gou and Wang Anshi were from Jiangxi, and Wang’s thought was an inheritance of Li”   [^hu1921]. And it is developed by Qian Mu, who further argues that  “(the criticism of the anti-reformers to Wang Anshi) was actually based on different views of the south and the north,”  and that  “the southern literati are considered frivolous while the northern literati are thought to be esteemed, thus Sima Guang (1019–1086) and his followers were incompatible with Lü Huiqing and his followers”   [^qian1936]. This view became very influential because of Qian Mu’s widespread work,  _Guoshi dagang _ [A General History of China] [^qian2013].
  
The last view, held by Cheng Yangzhi, is to ascribe the problem to different academic opinions. He states that  “Sima Guang’s opposition to Wang Anshi’s reform was because of his political belief and his basic principle, the  _Dao_ , was different from that of Wang. Wang believed that the  _Dao _ of human was separated from but based on the  _Dao_  of nature. The  _Dao _ of nature tends to change, and so should that of human. However, Sima believed the two types of  _Dao _ cannot be separated. The Dao of nature doesn’t change, and neither should that of human”   [^cheng1942].
  
All of the views above were proposed in the first half of the 20th century, and many later scholars stayed within the bounds they suggest. Luo Jiaxiang, who wrote a group of papers on this in the 1980s and 1990s, defines the reformers as  “those who take the responsibility of the nation”  and the anti-reformers as  “the political group which is both decadent and inert”   [^luo1985]. From there he proposes the innovative interpretation that  “they are both the representative of the whole class of landed gentry”   [^luo1984], rather than considering them as different social classes. Moreover, he notices the importance of censors, the  _Taijian_  officials, claiming that they composed another significant part of the anti-reformers other than the  “decadent and inert senior politicians”   [^luo1993].
  
Recent scholars have proposed new perspectives. Li Xianchen thoroughly opposes the traditional view about different class interests, arguing that  “The dispute between Wang Anshi and Sima Guang was one within the reformers. Both of them advocated reformation, and they were just different in specific methods of reform”   [^li1986]. Likewise, Luo Xiaosheng claims that  “Both _ Wengong_  (honorific title of Sima Guang) and  _Jinggong_  (honorific title of Wang Anshi) had an ideal of taking the responsibility of the nation, and they both proposed a scheme of reform respectively”   [^luo1987].
  
Finally, most of the scholars agree that the political struggle among factions in the light of the reform made a profound impact on the Northern Song politics no matter what they think the reason was. For example, Chen Zhenyang attributes the failure of the reform to the struggle among factions. He states that  “[the anti-reformers] were glad of the increment of the disadvantages of the reform and the nonfulfillment of its advantages furtively,”  and that  “Wang Anshi’s reform was in trouble because of it”   [^chen1943]. Besides, apart from the disputes between the anti-reformers and the reformers, in the Yuanyou Era, there were also debates among the anti-reformers themselves. The dispute between _ Luodang_  [the party of  _Luo_ ] [^2]  and  _Shudang_  [the party of  _Shu_ ] [^3] , which was named as  “ _Luoshu Dangzheng_ ”  [ _Luo_ - _Shu_  faction struggle], was also of significant influence. Cheng Ruizhao believes the struggle’s influence lasted until 1155 when Qin Hui (1091–1155) dead, and even to 1224 when Emperor Lizong (r. 1224–1264) ascended to the throne [^cheng1998].

  
  

## 2.2 Literati Politics in the Song Dynasty
  
A distinct feature of premodern Chinese government (which became an autocratic monarchy governed by scholar-officials in the Ming and Qing dynasties), literati politics played a crucial role in the cultural-political life of the Song Dynasty. For example, in a case study on the Huizhou, in the period of 1200–1550, local literati’s spatial imagination resembled a mode that  “every local place was a microcosm of ‘all-under-heaven’, and thus they practiced political ideas on their local governance”   [^du2012]. But it was in the Northern Song dynasty (960–1127) when the tendency of the importance of literati on imperial politics mushroomed notably: these scholar-officials occupied most of the government openings. This feature is considered as a part of the Tang-Song transition by the academic world.
  
The idea of the Tang-Song transition was brought up by Naitō Konan, who argues that  “the fall of the Tang dynasty was the collapse of aristocratic government in China, and the rise of monarchial autocracy and populism”   [^fogel1984]. According to this model, the Song dynasty was a period when the  “local elite gentry families”  replaced the  “semi-hereditary professional bureaucracy”   [^luo2005].
  
The influence of the literati on imperial politics was prevalent in the Song dynasty. Hilde De Weerdt finds that  _Daoxue_ , the ideology held by the literati, became the official ideology in the Southern Song (1127–1279) when it adapted itself to the convention of examination culture [^deweerdt1998]. Besides, Ong’s study on Guanxue, a school of Daoxue, finds it to be a bond between  “the monarch, the court, the local officials, the  _shi _ [^4] , and the ordinary people”   [^ong2005]. Deng and Lamouroux focus their attention on the importance of the literati in their study on the  _zuzong jiafa _ [ancestors’ family instruction], claiming that they  “invoked the image of a turning point in the Family Instructions”   [^deng2005].
  
Moreover, in the Northern Song, the development of the literati politics also effectively carried cultural interactions among literati into the realm of politics. For example, Amy McNair finds that many eminent scholar-officials active in the eleventh century, including Fan Zhongyan (989–1052), Ouyang Xiu (1007–1072), Su Shi (1037–1101) and many others, promoted the calligraphy style of Yan Zhenqing (709–784) because of ideological considerations [^mcnair1998]. For another instance, Zhang’s study on the Inn-wall writings during the Song dynasty finds them to point at  “the centrality of travel in the lives of the scholar-officials and the travelers’ representations of their experiences”   [^zhang2005].
  
The commonness and impact of the literati’s practice of writing prefaces and postscripts to each other is attested in the idea of  _wen yi xu chuan_  [writings are disseminated because of the prefaces], which is another manifestation of the cultural-political relationships of the literati. The literati changed the function and significance of the genres of prefaces and postscripts to gradually endow them with robust political significance, especially when they wrote prefaces or postscripts for political memorials [^mei2015].
  
These phenomena also influenced the political struggle among factions. For scholar-officials, their academic views were intimately related to their political views, exerting a deep influence on the political struggle in late 11th century. Liang Qichao noticed their relationship. In his analysis on  _Xinxue _ [the new school of  _Daoxue_ ] [^5] , he described it as follows:  “Whatever useful for molding the character of oneself or exerting an influence on politics are all included in his academics”   [^liang1993]. Since Wang’s philosophical ideas were intimately connected with his political ideas, his criticizers opposed it as well. Qiu Hansheng associated the academic disputation with the theory of class conflict, arguing that  “the opposition to  _Xinxue _ academically has the same meaning as the opposition to reform politically, which is class conflict”   [^qiu1959]. The remarkable concomitancy between academics and politics was even thought to be the reason why  _Xinxue_  failed to prosper after Wang’s death by Deng Guangming, who assumed that  “if Wang Anshi had not come into power or enacted a reform, his academic ideas…would certainly have been inherited by the Confucianists working on Confucianism principles for a long time”   [^deng1994].
  
In conclusion, with literati politics, a regime in which scholar-officials dominated political life, culture and politics formed a dynamic and interactive relationship during the Song dynasty. In the case of the large-scale political struggles among factions after Wang Anshi’s reform, the interaction between literati and politicians, as well as the political nature of various literary activities, can throw light on the ensuing debates concerning their origin and nature. In the following sections, we will therefore start by studying the literary and the political relationships among the contemporaries during the reform and discuss the origin and nature of the political struggle.

  
  
  

## 3 Methods
  
A framework including four data processing steps used in our study is shown in Figure 1. In the first stage, data collection, a list of people active in the era of reform is generated from CBDB, which is a relational database developed from primary historical sources. Based on the list, the data about relationships among them are extracted, which act as original data in the next stage. In the second stage, matrix construction, the relationship data of literature and politics are processed and constructed into the literary and political matrix respectively. The matrices are operated under the third stage, dimensionality reduction, which mainly extracts the feature factors of the two matrices, and the fourth stage, community detection, where communities are detected from these matrices with Louvain Modularity. Both the results of the third and the fourth stages are visualized and compared, while in the fourth stage, relation analysis is adopted after comparison. Afterwards, the overall results are interpreted and discussed. The details of the frameworks are discussed hereinafter [^6] .
  
{{< figure src="resources/images/Figure1_updated.jpg" caption="The framework of data processing" alt="The framework of data processing"  >}}

  
  

## 3.1 Data Collection and Matrix Construction
  
In the stage of data collection, we first generate a list of people active in the era of reform. Since people recorded in CBDB are arranged chronologically from various dynasties, we selected from the database only those who were active in the era of reform from the second year of Xining (1069) to the last year of Yuanyou (1094), 1064 being the year when Wang Anshi started the reform and 1094 the year before factional struggles turned into thorough political persecutions. Furthermore, the people selected must be at least 15 years old in 1094 since the age of 15, called  “ _zhi xue zhi nian_ ”  [an age of aspiring to learn] in Chinese culture [^yang1980], is considered the threshold of adulthood, after which one can actively participate in literature and politics. As a result, people born before 1080 (or at 1080) and dead after 1069 (or at 1069) are selected in our experiment.
  
After generating the list, we continue to extract the relation data among the people in the list generated from CBDB. In order to collect the literary relations among the people selected, the concept of bibliographic coupling [^kessler1963] in the field of informetrics is adopted and adapted as  “two people who have active literary relation to a common third person”  in our study. Here,  “active literary relation”  means the person is writing (prefaces and postscripts, for instance) rather than being written for. Two people writing for a common third person implies that they share a mutual favor of this person, suggesting a closer literary bond. However, in the case of two people being written for by a common third person, there isn’t necessarily any such bond, since the third person may do this simply out of the two other people’s great reputations.
  
The method of extracting data about political relations is similar to that for literary relations, but data of direct interactions between two people, rather than their relations with common third person, are collected. Besides, these interactions are further divided into three types: explicit positive relations, implicit positive relations and negative relations. Explicit positive relations include supportive political associations, recommendation and sponsorship and part of connections via office (the connections that directly indicate intimacy), implicit positive relations include most of connections via office (the connections that do not directly indicate intimacy, such as simple colleagueship), and negative relations include oppositional political associations. 
  
After data collection, the data extracted are used for matrix construction. Two correlation matrices — a literary matrix and a political matrix — are constructed, based on the data of literary relations and political relations respectively. Assume that there are  _n _ people selected from CBDB and the literary matrix can be noted as  _L nn _ . Only the relations between the  _i-th_  and the  _j-th_  people who write for (rather are written for) by a common third person are counted in the literary matrix. Whenever the  _i-th _ and the  _j-th_  people have a active literary relation with a common third person, the value of _ l ji _  in the correlation matrix is added by one. The diagonal of the matrix is set as zero due to unmeaningful relationships between the person and himself. 
  
Similarly, the political matrix is noted as  _P nn _  and the value of  _p ij _  is formulated as follows.
  
        p      i  j      =      p      j  i      =      e  p  r      i  j      ×  2  +      i  p  r      i  j      -      n  r      i  j       (Equation 1)
  
where       e  p  r      i  j       is the number of explicit positive relations,       i  p  r      i  j       is that of implicit positive relations, and       n  r      i  j       is that of negative relations between the  _i-th_  and the  _j-th_  people. 
  
In total, 5436 records of literary relations were collected, involving 144 people who act as the person to write for another person, and 2504 people who act as the person to be written for. 1453 records of political relations among the people were collected, with ninety-six people involved.

  
  

## 3.2 Dimensionality Reduction
  
Next, both matrices are operated under dimensionality reduction, which discovers  “compact representations of high-dimensional data”  by generating a set of factors [^roweis2000]. Since the data in both matrices are discrete and sparse (containing many exact zeros), a Poisson-Gamma factorization model is suitable and is thus adopted for the task [^7] .
  
After running the model, twelve factors were obtained from each matrix. Similar to co-citation and bibliographic coupling analysis, where key factors are explained as an academic interest shared by a group of scholars, the historical meaning of the factors can be preliminarily explained as literary pursuits and political interests respectively. This interpretation is based on the following considerations: when two or more people share literary relationships with many common people, it is likely that they are driven by a common literary pursuit; likewise, when two or more people frequently offer political aids to each other, it is highly possible that they share a certain political interest. Furthermore, the mathematical meaning of factors that a single point could have a notable value in different factors matches with the fact that a person could have various literary pursuits and could be connected to different political groups through different political interests.
  
Therefore, the people sharing a common factor can be interpretated as engaging in a common literary pursuit and sharing a certain political interest respectively, despite the fact that the precise meaning of the key factors requires further elaboration. The first extracted factors explain higher variance, and therefore are chosen as the objects of evaluation. We first discuss the people with the highest value in each factor, and offer visualizations of the results afterwards. Finally, we compare the results of dimensionality reduction of the two matrices.

  
  

## 3.3 Community Detection
  
The last stage is community detection, which is also based on the two matrices. As a process of investigating the structure in a complex network, the method can aggregate and integrate all relation data among the people. Therefore, rather than adopting basic statistical methods, which separately analyze the relationships between each pair of people, community detection is capable of treating the entire social network in the reform era as a whole and analyzing it comprehensively. In this way, the results of community detection and dimensionality reduction, which suggest possible relationships among people regarding literary pursuits and political interests, can be complementary, providing a more comprehensive view of relationships among the people active in the era of the reform.
  
In community detection, for the purpose of eliminating the algorithmic bias caused by negative values, since the minimum value in the political matrix is minus four, each element is increased by a constant four so that all elements would be non-negative. Then the matrices are converted into social networks, where the weight of edge between the  _i-th_  and the  _j-th_  people is the value of  _l ji _  and  _p ji _  of the literary matrix and political matrix respectively. Next, community detection is carried out in Gephi, which is an open-source software for graph and network analysis [^bastian2009]. We lay out the original network by Yifan Hu multilevel layout [^hu2005], partition it using Louvain Modularity [^blondel2008]  [^8] , and determine the number of communities based on the resolution value from Laplacian dynamics [^lambiotte2005]  [^9] . Finally, the communities detected are considered as literary and political groups respectively. There are four core communities detected in the literary network and seven in the political network.
  
Similar to dimensionality reduction, the results of community detection are analyzed separately and comparatively. When comparing the results of literary groups and political groups, the research adopts methods of relation analysis, referring to the main idea of association rule learning to evaluate the similarity between them. Association rule learning is intended to identify strong rules discovered in databases using measures of interestingness [^piateskyshapiro1991]. In this article, each person is considered as a one-item set, in order to study the distribution of the people in different literary groups and political groups. Specifically, the research defines frequency (referencing to the concept of support in association rule learning) of a certain literary group  _x 0 _  and a political group  _y 0 _  as the ratio of the number of people who appear in both of the groups, to the total number of people who appear in any literary group and any political group. The formula is as follows:
  
    f  (      x      0      ,      y      0      )  =      N  (      x      0      ,      y      0      )        ∑    x  ⊂  X  ,  y  ⊂  Y          N  (  x  ,  y  )       (Equation 2)
  
And it defines the ratio of the political group (referring to the concept of confidence in association rule learning) of a certain literary group  _x 0 _  and a political group  _y 0 _  as the ratio of the number of people who appeared in both of the groups, to the total number of people who appear in any literary group and the specific political group. The formula is as follows:
  
    r  (      x      0      ,      y      0      )  =      N  (      x      0      ,      y      0      )        ∑    x  ⊂  X          N  (  x  ,      y      0      )       (Equation 3)
  
According to the basic idea of association rule learning, association rules are required to satisfy both a minimum support and a minimum confidence constraint at the same time [^hahsler2005]. Therefore, based on the formulae above, literary group  _x 0 _  and political group  _y 0 _  are considered as related if parameters   f          x      0      ,      y      0           and   r          x      0      ,      y      0           satisfy a threshold constraint at the same time. After experiments, we find setting threshold constraints of       f      m  i  n      =3% and       r      m  i  n      =25% reasonable, therefore the groups that satisfy the constraints will be considered as related.

  
  
  

## 4 Experimental Results and Analysis
  
  

## 4.1 Dimensionality Reduction
  
Twelve key factors of a matrix are produced after dimensionality reduction on the literary matrix. Mean squared error (MSE) is adopted to measure the difference between the estimator and what is estimated, the factors that are extracted from the original matrix. Randomness or unaccountable information in the estimator is the major cause of the difference, thus the value of the MSE is positively related to the error [^lehmann1998].
  
The algorithm is run iteratively 400 times, and the MSE of dimensionality reduction of the literary matrix is 0.233. Since the first extracted factor is not interpretable as all people have the same value on it, we chose to evaluate the factors ranking from second to fourth. And for each factor, we picked the ten people with the highest values. The factor matrix is shown in Table 1.
    People that have the highest values in the literary matrix after dimensionality reduction    Factor  Name      2  Su Shi, Huang Tingjian, Su Zhe, Wang Anshi, Bi Zhongyou, Chao Yuezhi, Su Song, Zhang Lei, Qiang Zhi, Han Qi      3  Yang Shi, Hu Anguo, Liao Gang, Luo Congyan, Ye Mengde, Su Zhe, Chen Guan, Cheng Ju, Yin Tun, Cheng Yi      4  Yang Shi, You Zuo, Cheng Yi, Cheng Hao, Li Guang, Chao Yuezhi, Han Wei, Chen Guan, Yin Tun, Zhu Guangting      
Through the results of dimensional reduction of literary relations, people who have the highest value in factors listed in Table 1 can be explained as  “engaged in common literary interests” .
  
People with the highest values in factor  _2_  include Su Shi (1037–1101), his brother Su Zhe (1039–1112), his students Huang Tingjian (1045–1105) and Zhang Lei (1054–1114), and his close friends Bi Zhongyou (1047–1121) and Chao Yuezhi (1059–1129). Therefore, this factor indicates a group highly related to Su Shi, the leader of  _Shuxue _ [the school of  _Shu_ ] [^10]  and it can be explained as literary interest of  _Shuxue_ .
  
People with the highest values in factor  _3_  and  _4 _ include Cheng Hao (1032–1185), Cheng Yi (1033–1107), their students Yang Shi (1053–1135), You Zuo (1053–1123), Zhu Guangting (1037–1094) and Yin Tun (1071–1142), the students of Yang Shi, Hu Anguo (1074–1138), Liao Gang (1070–1143) and Luo Congyan (1072–1135), and academics such as Chen Guan (1057–1124). Yang Shi and You Zuo are among the  _Chengmen si xiansheng_  [four outstanding students of the Cheng’s school] and Chen Guan is also deeply influenced by the two Chengs (Cheng Hao and Cheng Yi). Thus, the factors  _3 _ and  _4_  can be explained as literary interest of  _Luoxue _ [the school of  _Luo_ ] [^11] .
  
The result of dimensionality reduction of literary matrix with factor  _2_ ,  _3_ , and  _4_  is shown in Figure 2. It is divided into three sections: 1) Sect.  _A_  (includes people with high values in factor  _3 _ and  _4_ ) representing  _Luoxue_ , 2) Sect.  _B_  representing  _Shuxue_  (includes people with high value in factor  _2_ ), and 3) Sect.  _C_  representing  _Xinxue _ (includes people with no high value in factor  _2_ ,  _3_  or  _4_ ). 
  
{{< figure src="resources/images/Research+Results,+Figure+2.jpg" caption="Visualization of the dimensionality reduction result of the literary matrix" alt="Visualization of the dimensionality reduction result of literary matrix"  >}}

  
The political matrix is also reduced to twelve factors, which are explained as political interests. The algorithm is run iteratively 400 times and the MSE of dimensionality reduction of the political matrix was 0.395. The first-extracted two factors are selected and the ten people with the highest value are picked.
    People that have the highest values in the political matrix after dimensionality reduction    Factor  Name      1  Sima Guang, Wang Gongchen, Zhao Bian, Cheng Yi, Sun Yong, Su Shi, Fan Chunli, Yin Tun, Mei Zhili, Wang Anli      2  Lü Huiqing, Lü Gongzhu, Zhang Dun, Wang Gongchen, Shao Yong, Emperor Shenzong, Sun Jue, Cai Jing, Wang Anguo, Li Qingchen      
People with the highest values in factor  _1_  are mostly anti-reformers, including Sima Guang, Wang Gongchen (1012–1085), Zhao Bian (1008–1084), Cheng Yi, Sun Yong (1019–1086), Su Shi and Fan Chunli (1031–1106). Among them, Sima Guang, Cheng Yi, Su Shi and Fan Chunli are listed in the  _Yuanyou dangji bei_  [Stele of the  _Yuanyou_  Faction Members] [^12] . Furthermore, Sima Guang was the leader of the anti-reformers, Cheng Yi was the leader of  _Luodang_ , and Su Shi was the leader of  _Shudang_ .
  
People with the highest values in factor  _2_  include Emperor Shenzong, who was the emperor to carry out the reform, Zhang Dun (1035–1105), Lü Huiqing (1032–1111), Cai Jing (1047–1126) and Li Qingchen (1032–1102), who were all reformers and among whom Zhang Dun and Lü Huiqing were listed in the  _Wang Anshi qindang_  [accomplice of Wang Anshi] by Liang Tao (1034–1097) [^bi1957].
  
The result of dimensionality reduction of the political matrix with factor _ 1_  and  _2_  is shown in Figure 3. It is divided into four sections. Sect.  _A_  and  _B _ represent reformers, and Sect.  _C_  and  _D_  represents anti-reformers. Moreover, different sects of reformers and anti-reformers are also separated. Relatively mild reformers, Emperor Shenzong (named Zhao Xu, who both supported the reform and respected the anti-reformers), and Cai Jing (he hovered between reformers and anti-reformers before coming to power) are in Sect.  _B_  while more radical reformers, Zhang Dun and Lü Huiqing are in Sect.  _A_ . Among the anti-reformers, the members of  _Shudang_ , who had relatively mild political views, are mostly in Sect.  _C_ , including Su Zhe, Lü Tao (1028–1104) and Kong Wenzhong (1038–1088) [^13] . And those who had more radical political views, are mostly in Sect.  _D_ . The transition from Sect.  _A _ to Sect.  _D _ corresponds with the transition of political views from radical reformers to radical anti-reformers.
  
{{< figure src="resources/images/Figure3(currentFigure5)_updated.jpg" caption="Visualization of the dimensionality reduction result of the political matrix" alt="Visualization of the dimensionality reduction result of political matrix"  >}}

  
Synthesizing the results above, we find that the reformers are all mostly in Sect.  _C_  in Figure 2 and in Sect.  _A _ and  _B_  in Figure 3, while among the anti-reformers, followers of  _Shuxue_  are mostly in Sect.  _B _ in Figure 2 and Sect.  _C _ in Figure 3, those of _ Luoxue_  are mostly in Sect.  _A_  in Figure 2 and Sect.  _D_  in Figure 3. Therefore, we can confirm our original hypothesis that those who were engaged in common literary pursuits usually shared political interests with each other.

  
  

## 4.2 Community Detection
  
The correlation matrices are operated under Gephi, and a literary network and a political network are generated based on the data of the matrices respectively. After laying out and partitioning the networks, they are divided into several communities. The result of community detection of literary network is shown in Figure 4, with the size of the nodes representing the importance of the person:
  
{{< figure src="resources/images/Research+Results,+Figure+4.jpg" caption="Literary groups detected" alt="Literary groups detected"  >}}

  
There are four core communities detected in the network, each representing a group of literati. Other communities are dispersed in the edge of the network and consist of only one component, thus should be considered as unimportant. The findings are as follows:
  

 * a. Su Shi, Huang Tingjian, Sima Guang, Su Zhe, Wang Anshi and Fan Chunren (1021–1101) are all attributed to Group  _A_ , which can be considered a core literary group.  
 * b. Although the components of Group  _A_  are complicated, Su Shi plays an extremely important role in it. Many of his family members (his brother Su Zhe and son Su Guo (1072–1123)), his students (Huang Tingjian, Zhang Lei, Chen Shidao (1053–1102) and Li Zhi (1059–1109)), his friends (Bi Zhongyou (1047–1121), Shi Huihong (1071–1128) and Mi Fu (1051–1107)), and his political allies (Lü Tao and Kong Wenzhong) are in the group. Most people in group A are mild anti-reformers, and many of them are followers of  _Shuxue_ .  
 * c. Most components of Group  _B_  are firm anti-reformers, including Liu Anshi (1048–1125) and many followers of  _Luoxue_  (Cheng Yi, Cheng Hao, Yang Shi, You Zuo, Zhu Guangting, Yin Tun, Hu Anguo, Liao Gang and Luo Congyan).  
 * d. Most components of Group  _C_  are reformers or have sympathy for reform. Those people include Zhang Dun, Lü Huiqing, Peng Ruli (1041–1095), Cai Bian (1048–1117), who were typical reformers and were listed in  _Wang Anshi qindang_  by Liang Tao [^bi1957], and Liu Yan (1048–1102), who was neither reformers nor anti-reformers but was friendly to reformers. Besides, most followers of  _Xinxue_  are in it.  
 * e. The components of Group  _D_  are mostly senior politicians active during the reign of Emperor Renzong (r. 1022–1063), including Han Qi (1008–1075), Fu Bi (1004–1083), Wen Yanbo (1006–1097), Wang Gui (1019–1085), Zhang Fangping (1007–1091) and Qiang Zhi (1022–1076).

  
Of course, this categorization is reductive: people cannot be categorized into merely one or another literary or political group. However, as found above, despite some exceptions (such as the leader of reformers, Wang Anshi, is in the core group  _A_ , instead of Group  _C_ ), the groups detected by the modularity algorithm still imply analytically-durable literary and political relations. These findings suggest the literary group a person belongs to corresponds to the person’s political views. Moreover, an interesting discovery is that the position in Figure 4 (which represents the position of the person in literary network) correlates to the person’s views on reform.
  
The modularity of the political network is similar to that of the literary network. Since the matrix is high-density and most of the values in the matrix are around four (if two people don’t have associations in politics, the value of the element demonstrating the strength of their relation is four owing to our normalization during preprocessing), the degree range of the filter is set to be “greater than four” so that all of the edges shown connect two people that are positively related in politics. The result are as follows:
  
{{< figure src="resources/images/Figure5(currentFigure7)_updated.jpg" caption="Political groups detected" alt="Political groups"  >}}

  
Figure 5 shows fifty-four people in seven core communities. In a manner similar to the literary network, other unimportant communities are dispersed in the edge of the network and consist of very few components (at most three). The constituents of the seven core communities all have positive political relations with at least one person in the network.
  
The communities, each representing a political group, are reasonably clear. Following the labels shown in Figure 5, the analyses of Group  _A_ ,  _B_ ,  _C_ ,  _D_  and  _E _ are as follows (size of group  _F_  and  _G_  being too small to analyze):
  

 * Most people in  **Group  _A_ **  are firm anti-reformers, including Sima Guang, Fan Chunren, Fan Chunli (1031–1106), Cheng Yi, Zhu Guangting, Liu Anshi (the above six people are listed in the  _Yuanyou dangji bei_ ), and Liu Shu. Sima Guang is the most important person in the group and the two distinct members of  _Luodang _ are both in it.  
 * Most people in  **Group  _B _ ** are radical reformers, including Zhang Dun, Zeng Bu (1036–1107), Cai Jing, Cai Bian, Zhao Tingzhi (1040–1107) and Zhang Shangying (1043–1121), all of the above people were listed in the  _Wang Anshi qindang_   [^bi1957]. Zhang Dun is the most important person in the group.  
 * The leading figure in  **Group  _C_ **  is Su Shi. Most of people in it are mild anti-reformers, including many  _Shudang_  members. It contains Su Shi, his students (Huang Tingjian and Chen Shidao), his political ally (Kong Wenzhong), and also Wang Anli (1034–1095), brother of Wang Anshi.  
 * The leading figure in  **Group  _D_ **  is Wang Anshi. It contains reformers (Lü Huiqing), and also Emperor Shenzong (named Zhao Xu).   
 * Most people in  **Group  _E _ ** are senior politicians and anti-reformers, including Han Qi, Fu Bi, Su Song (1020–1101), Qiang Zhi and Feng Jing (1021–1094).

  
These findings demonstrate the reliability of the data in the political matrix, and the network accurately reflects the political situation in the era of reform. An exception can be found in group  _C_ , where a mild reformer, Wang Anli, appears in the group of mild anti-reformers. This is considered as an outlier of the network, which will be discussed in part 5.1.
  
Finally, we analyze the relations between literary groups and political groups referring to the main idea of association rule learning. The groups considered as related are shown in Table 3:
    Related literary groups and political groups    Political Group  Literary Group  Frequency  Ratio of the Political Group      A   A  9.80%  38.46%      A  B  13.73%  53.85%      B  A  5.88%  33.33%      B  C  5.88%  33.33%      C  A  13.73%  77.78%      D  A  3.92%  28.57%      D  C  3.92%  28.57%      D  D  3.92%  28.57%      E  A  5.88%  50.00%      E  D  5.88%  50.00%      F  A  3.92%  50.00%      G  B  5.88%  75.00%      
The results of relation analysis show twelve pairs of related political and literary groups, and they imply a close relationship between these groups. For example, political group  _A_  (firm anti-reformers) is related to literary group  _A_  (core group) and  _B_  (anti-reformers), and political group  _B_  (radical reformers) is related to literary group  _A_  (core group) and  _C_  (reformers). Specifically, those who were followers of  _Luoxue_  are mostly in literary group  _B_ , and members of  _Luodang_  are mostly in political group  _A_ , which are strongly related (highest  _f _ 13.73% and third-highest  _r_  53.85%). Similarly, those who were followers of  _Shuxue_  are mostly in literary group  _A_ , and members of  _Shudang_  are mostly in political group  _C_ , which are also strongly related (highest  _f _ 13.73% and highest  _r_  77.78%).
  
In general, the results confirm our original hypothesis that those who shared a literary group were more likely to share a political group.

  
  
  

## 5 Discussion
  
  

## 5.1 Positive Interactions between Reformers and Anti-Reformers
  
In Figure 5, there is an outlier in the political network: Wang Anli is found to appear in the group of mild anti-reformers. This outlier is derived from the following historical record:
  
> Su Shi was imprisoned in the jail of the Censorate. He was in extreme danger and no one dared to save him. Wang Anli said (to Emperor Shenzong) calmly, ‘since ancient times, magnanimous emperors do not convict others because of their sayings.…If Your Majesty sentenced him (Su Shi) strictly according to the law, I am afraid that Your Majesty will be criticized by later generations as intolerant to the talents.’…Thus Su Shi was only punished lightly
. [^tuotuo1985]  
This is far from the only record showing positive interactions between reformers and anti-reformers. Actually, Su Shi, the leader of  _Shudang_ , and Wang Anshi, the leader of the reformers, showed respect to each other. When Su was relegated and went past Jinling [^14] , he advised Wang to exhort the emperor in return for being thought highly by the emperor. Feeling respected, Wang accepted his advice and warned him not to tell anybody else [^tuotuo1985]. In the record, it is clear that Su thought highly of Wang, and Wang trusted Su and treated him as an intimate friend.
  
Wang also listened to the advice of Su Zhe, who was the brother of Su Shi. When he carried out the reform policies, he asked for the opinion of Su Zhe on the  _qingmiaofa _ [green sprouts policy] [^15] . When Su proposed objection, Wang answered:  “What you said was really reasonable, I should rethink it carefully.”  And he stopped talking about  _qingmiaofa _ for several months [^tuotuo1985].
  
Similar records are not only found in those concerning the amiable relations between the reformers and the members of  _Shudang_ , who held relatively mild attitudes towards the reform, but also between reformers and other more radical anti-reformers. During the reign of Emperor Shenzong, who was the main supporter of the reform, the firm anti-reformers were still high-rank officials. Fu Bi, Wu Chong (1021–1080), Feng Jing, Wen Yanbo, Lü Gongbi (1007–1073) had all assumed offices of what was equivalent to the prime minister [^li2013]. Emperor Shenzong showed great tolerance and respect for the anti-reformers despite their political views, enabling positive and amiable interactions.
  
Moreover, even the firmest anti-reformers tried to mediate with the reformers. In the fifth year of Yuanyou (1090), Liu Zhi (1030–1098), the leader of  _Shuodang _ [the party of  _Shuo_ ] [^16] , together with Lü Dafang (1027–1097) advised appointing the reformers as officials in order to alleviate the existing resentment between the reformers and anti-reformers. And they called it mediation  [^li2004]. In spite of factions, struggles and disputes, there are still a number of records showing positive interactions between reformers and anti-reformers, especially those of  _Shudang_ . 

  
  

## 5.2 Anti-Reformers’ Views on the Reform
  
We next investigated the difference between the reformers’ and the anti-reformers’ political views, in order to discover to what extent they really hold irreconcilable political views.
  
The anti-reformers who held the least radical views on the reform were still the members of  _Shudang_ . During the reign of Emperor Renzong, Su Shi wrote a memorial to the Emperor stating the urgency of the reform.  “Nowadays, if we do not cleanse the old, we will not be able to establish something eminent”   [^su1986]. In his early years, Su Shi strongly approved of the reform and was taunted by Zhu Xi (1130–1200) because of it. Zhu criticized that Su  “talked about improving government finance in his early years, but never talked about it after seeing the failure of _ qingmiaofa_ . He talked about military actions in his early years…but never talked about it after seeing the failure of Wang Anshi’s military actions.”   [^li1994]
  
Su Shi was not the only one who urged reform. Although criticizing Su Shi, Zhu Xi admitted that  “not only  _Jinggong_  (Wang Anshi) wanted to reform, but all of the wise men then had an intention for reform”   [^li1994] when discussing the situation of the era before the reform. Therefore, we can conclude that there was a consensus among officials on the eve of the era of reform, whether reformers or anti-reformers, when the reform was carried out by Wang Anshi.
  
Moreover, during the era of the reform, members of  _Shudang_  still held relatively mild attitudes, even if they opposed it in general. When Sima Guang came into power and tried to abolish Wang Anshi’s policies, some members of  _Shudang_  argued against it. For instance, in the Yuanyou Era, Sima Guang planned to change the standard of imperial examination set by Wang Anshi. Su Zhe argued that since the next examination would take place very soon, it would be difficult for the examinees to adapt to the new standard. So he advised Sima to follow the standard set by Wang Anshi in the next year and consider changes afterwards [^tuotuo1985]. Although Sima Guang didn’t take his advice, it was clear that Su Zhe held a relatively neutral view on the reform even in the Yuanyou Era, when political struggle grew more severe.
  
In conclusion, before the era of the reform, most anti-reformers still approved of reform to a certain degree. And during the era of the reform, the members of  _Shudang _ still held relatively mild views on it. The mild perspectives held by anti-reformers and the positive interactions between them and reformers imply that in the early period of the reform, political struggle among factions was controllable and rational to some extent, and that there were no irreconcilable conflicts between the reformers and anti-reformers despite their differences.

  
  

## 5.3 Worsened Political Situation
  
Nevertheless, the situation worsened as time went on. The first to be persecuted were the members of  _Shudang_ , especially Su Shi, who was described by Liu Anshi as:
    
> In the Yuanfeng Era (1078–1085), the reformers were intolerant of him and wanted to kill him. In the Yuanyou Era, there was also dissension between him and the old gentlemen (i.e. the anti-reformers). He is not a man to fluctuate as situation changes.
  [^ma1985]  
As a result, he was relegated in the Xining Era (1068–1077) and the Yuanfeng Era when the reformers were in power, and was also forced to leave the capital in the Yuanyou Era when the anti-reformers were in power.
  
The members of  _Shudang _ were not the only ones persecuted when the political struggle worsened. In the Yuanyou Era, reformers were massively persecuted. Fan Chunren, one of the anti-reformers, summed up the situation of political persecution as follows:  “In my opinion, the origin of the factions is because of political views. Those who have the same view with me are considered to be righteous, while those who have different views are doubted to be devious”   [^li2004].
  
In the Southern Song dynasty, when the arguments around the reform came to the definitive conclusion that the reform had been a mistake, people’s judgement on reformers and anti-reformers completely depended on their political views: the anti-reformers received praises and honors, while the reformers, no matter who they were, were severely criticized. In  _Guochao zhu chen zouyi _ [Memorials of All Ministers of Our Dynasty] edited by Zhao Ruyu (1140–1196), which was a collection of political memorials, the number of memorials of each person selected showed an overt relationship with their political views. Firm anti-reformers had the most memorials selected, for example, Sima Guang had 146, Lü Hui (1014–1071) had forty-five, Fu Bi had forty-four, Liu Zhi had thirty-four. Members of  _Shudang_  had less than that, with Su Zhe having twenty-four, and Su Shi having twenty-three. The memorials of the reformers were rarely selected. Wang Anshi had only six, while none of those written by Lü Huiqing, Zhang Dun or Zeng Bu were selected [^zhao1999]. Only the anti-reformers were able to have their works memorialized, and the reformers were officially forgotten.

  
  

## 5.4 Influence of Literati Politics on Political Struggle
  
In 5.1 and 5.2 we discussed positive interactions between reformers and anti-reformers and the anti-reformers’ views of the reform. We concluded that, at first, there were no irreconcilable conflicts between reformers and anti-reformers. But we found that conditions of political civility deteriorated in the last decades of 12th century, and the findings in part 4 offer a persuasive explanation for this: what we have called throughout literati politics. We conclude that those engaged in common literary pursuits were more likely to share political goals, and that shared affiliation to literary groups is likely to indicate shared affiliation to political groups. Both conclusions suggest the basic constitution of literati politics, which in turn exerts a deep influence on factionalized struggle.
  
The relatively mild view held by members of  _Shudang_  on the reform corresponded to the similarity of their academic views to those avowed by reformers. In the epitaph of his brother Su Shi, Su Zhe recalled that when Su Shi read  _Zhuangzi _ [^17] , he found it resonant with his own ideas. And when he read the Sutras, he likewise reconciled it with Confucianism and Taoism [^su1990]. The idea of fusing Confucianism with Taoism and Buddhism to a certain degree was identical to the proposals made by Wang Anshi. Therefore, both were criticized as profaning orthodox Confucianism.
  
Zhu Xi, a representative of the orthodox Confucianists, stated that  “Wang Anshi and Su Shi regarded the Buddha and Laozi [^18]  as sages, and thus their academics were not pure Confucianism academics”   [^zhu2006]. Therefore, he criticized both of them that  “the academics of both of them were illicit.”   [^li1994]. And he also extended the criticism to politics.  “If Su Shi had been the prime minister, and invited Qin Guan (1049–1100), Huang Tingjian and other companies to assist him, things would have become worse (than what was caused by Wang Anshi)”   [^li1994].
  
The similarities between the philosophical perspectives of the members of  _Shudang_  and reformers correlates to the  _Shudang_  members’ mild attitude towards the reform. And since their academics,  _Shuxue_ , was quite different from  _Luoxue_ , they were in dispute with the members of  _Luodang_  in the Yuanyou Era when anti-reformers came into power. Similarly, the dispute between the reformers and the anti-reformers can also be explained by their differences in academic inclinations.
  
The distinct features of literati politics in the Song dynasty led to the extremely important social status of the literati. The actions of scholar-officials tended to be value-rational instead of instrumentally rational  [^19] . Unlike officials in a typical bureaucratic government, they took actions based on their own senses of value, which was a natural result of the prosperity of  _Daoxue_ . It made the Song dynasty a golden age for the literati. However, it also resulted in inevitable disputes among the scholar-officials who held different academic views. Since the scholar-officials had the identity of literatus and official at the same time, their academic views would strongly influence their political views, which brought about political struggles. Even worse, the scholar-officials in the Song dynasty were concerned with Confucianism, which itself pertained largely to value judgements. Therefore, they criticized those who held different academic views, and eventually gave moral judgements on them. This was the chief reason why normal political struggles would turn into disastrous persecutions according to [^xiao1998]. The findings of this paper on the extreme intimacy between the literary relations and political relations among the people active in the era of reform strongly reinforce this interpretation of the period.
  
Nevertheless, a paradox remains, namely that in the Southern Song dynasty, the dispute between  _Luoxue_  and  _Shuxue _ finally turned into the fusion of different ideas and ideologies. Scholars such as Liu Guangzu (1142–1222) and Wei Liaoweng (1178–1237) worked to bring about the fusion of  _Luoxue _ and  _Shuxue_ . To some extent, Zhu Xi, who epitomized the idea of  _Luoxue_  and critically inherited  _Shuxue_ , also carried on the process [^su1997]. In this way, academic disputes were solved. However, the political disputes which had their roots in those academic disputes were never successfully mitigated, and finally they accelerated the collapse of the Northern Song dynasty.

  
  
  

## 6 Conclusion
  
With the help of digital methods, this article preliminarily confirms that it was the literati’s different academic views that caused and exacerbated the political struggle, and the regime of literati politics was largely responsible for it. In part four we have found a distinct feature of literati politics from the results of our data analysis. And in part five, beginning with an outlier found in the automatically generated social network, we went back to the primary historical sources, and found that there were not irreconcilable conflicts between the reformers and anti-reformers at first. Further, in order to explain the reason why the political struggle worsened, we found that the development of literati politics in the Song dynasty offered a persuasive cause.
  
In this article, the original data obtained from CBDB are entirely based on historical records, and the reliability of the findings generated by digital methods that distantly aggregate historical sources are further validated by traditional methods that closely look through such sources. This is particularly necessary as both dimensionality reduction and community detection algorithms adopted in this article belong to the class of unsupervised learning. However, it should be noted that, without access to the workings of CBDB, work in this field would be held back. Moreover, the specific ways in which literati politics impacted political struggle still need elaboration in further studies, and our methodology can also be adapted by researchers in other fields such as exploring correlations between economic and political perspectives.
  
With the above caveats in place, we can conclude that, as found in part four, although literary relations and political relations among people have their own characteristics, they have many clear connections during the era of the reform, making it a typical era with highly-related culture and politics. Therefore, based on the suggestiveness of the data and the confirmation offered by the primary historical records, this article reinforces the view held by Cheng Yangzhi on the origin and nature of political struggle surrounding the issue of reform, ascribing the problem to different academic opinions [^cheng1942].
  
This result may shed light on further studies on the origin of the political struggle. This paper offers one way to bring to a close the debate on the origin and nature of the struggle among political factions in the reform era. Of course, other factors such as class interests, regionalism and simple emotionality still have weight, but literati politics offers the most comprehensive probative value of any of the possible explanations. Moreover, our paper also proves the explanatory force of the Tang-Song transition model [^fogel1984] on Song politics. Scholars of ancient and medieval history have formed a critical tradition of analyzing and interpreting the limited sources available to them. We emphasize that the digital methods in this article are the intellectual successors to, and share in, this spirit of critical imagination.
  
Niu Xi imputed the origin of the political struggle among  _Luodang_ ,  _Shudang_  and  _Shuodang_  as follows:  “The disputation had nothing to do with policies, nor with principles. It was just a disputation based on regionalism, parochialism, companionship between teachers and students, and academic styles”   [^niu1931]. This statement is not only applicable for this specific political struggle among the anti-reformers. In the whole process of the political struggle among factions around reform, neither the disputations between the reformers and anti-reformers, nor those among anti-reformers, were fundamentally irreconcilable.
  
It is generally acknowledged that the relation between the scholars and politicians became increasingly close in medieval China, and the feature of literati politics became more and more significant through the dynasties. Consequently, China eventually transformed into an autocratic monarchy governed by scholar-officials in the Ming and Qing dynasties. The Song dynasty acted as a pivotal period of the transformation with its distinct feature of literati politics, under the rubric of which scholar-officials holding different academic views criticized the political opinions of others, such that even political persecutions could be entirely driven by moral judgements.

  
[^1]: We already expected this hypothesis to be verified, as our previous work has proved this to hold true for scholar-officials who were active in the Yuanyou Era (1086–1094), a period covered by the investigation of this article, the range of which is between 1069 and 1094 [^shang2018].
[^2]: A political group in the Yuanyou Era led by Cheng Yi (1033–1107).
[^3]: A political group in the Yuanyou Era led by Su Shi (1037–1101).
[^4]: A concept raised in the Zhou dynasty (1046–256 BCE) which was later explained as scholar-officials. According to [^hucker1985],  _shi_  means elite, and is  “a broad generic reference to the group dominant in government, which also was the paramount group in society.”  The concept gradually transformed from  “a warrior caste…into a non-hereditary, ill-defined class of bureaucrats among whom litterateurs were most highly esteemed”  (421, item 5200).
[^5]: A philosophical school led by Wang Anshi, thus also called  _Jinggong Xinxue_  [the new school of  _Daoxue _ of  _Jinggong_  (Wang Anshi)].
[^6]: Three parts of the framework: data collection, matrix construction, and dimensionality reduction adopt the basic idea of our previous work [^shang2018]. However, as the two articles focus on different topics, their data are different, and their strategies of selecting factors to be discussed after dimensionality reduction are also different. Please refer to part three of that previous article for details.
[^7]: The basic idea of the Poisson-Gamma factorization model is to place a gamma process prior to a Poisson process, so that a hierarchical structure that shares statistical strength between groups of data can be obtained. This model is proved to be theoretically and empirically more sound in analyzing data with exact zero values [^brown2011], as is the case of this article. Specifically, we use the formulae introduced by Zhou Mingyuan et al. in constructing the model [^zhou2012].
[^8]: The Louvain method is a heuristic method based on modularity optimization. Due to its high quality, which is proved to outperform other widely used algorithms including CNM, PL, and WT [^blondel2008], it is implemented in social network platforms such as Gephi and NeworkX. Besides, as a hierarchical algorithm, it allows a further dynamical process that only changes the level of detail without affecting the nature of modularity.
[^9]: The Laplacian dynamics is used to measure the quality of network partition. In both networks, the resolution value, which determines the granularity of the communities, is set as 1.0, so that the stability of the networks is optimized.
[^10]: A philosophical school led by Su Shi. It was name after his hometown Sichuan, which was called  _Shu_  in premodern China.
[^11]: A philosophical school led by Cheng Hao and Cheng Yi. It was name after their hometown Luoyang, which was abbreviated as  _Luo_ .
[^12]: The  _Yuanyou dangji bei_  was created in 1104, and allegedly aimed at  “marking the officials who harm the politics in Yuanyou Era”  (i.e. the anti-reformers). However, it has a complex nature. Because of the monopolization of Cai Jing, the prime minister who created the stele, the 309 officials listed in the stele were actually far beyond merely anti-reformers. Rather, Cai Jing used the stele as a tool to suppress his political opponents. Even one of the firmest reformers, Zhang Dun, was listed in it because of his hostility to Cai Jing. Therefore, it shouldn’t be considered as an objective tool to distinguish the anti-reformers, although it is the only available historical source which stated to list the anti-reformers.
[^13]: The members of  _Shudang_  and  _Luodang_  were distinguished by Huang Zhen (1213–1281), see [^huang2013]. The subject was also studied by Zhuge Yibing, who included Kong Wenzhong into the list of  _Shudang_ , see [^zhuge1996].
[^14]: Current Nanjing.
[^15]: One of the most important policies of the reform, which provided direct government loan to farmers during planting seasons and to be repaid at harvest.
[^16]: A political group in the Yuanyou Era led by Liu Zhi. It was considered as the direct political successor of Sima Guang and held the most radical view against the reform. Most of its members are from northern China, which was called  _Shuo _ in premodern China. The members of Shuodang were also distinguished by Huang Zhen, see [^huang2013].
[^17]: A philosophical work written by Zhuang Zhou and considered as a scripture of Taoism.
[^18]: Founder of the Taoism philosophy and was worshiped in the Taoism religion.
[^19]: The definitions of the phrases refer to Max Weber, see [^weber1978].  
[^bastian2009]:  Bastian, M., Heymann, S. and Jacomy, M.  “Gephi: An Open Source Software for Exploring and Manipulating Networks.”    _International AAAI Conference on Weblogs and Social Media_ , San Jose, California, May 2009.  
[^bi1957]:  Bi, Y. Xu zizhi tongjian [Continuation to the Comprehensive Mirror to Aid in Government]. Zhonghua shuju, Beijing (1957).  
[^blondel2008]:  Blondel, V. D, Guillaume, J.-L., Lambiotte, R and Lefebvre, E.  “Fast Unfolding of Communities in Large Networks” ,  _Journal of Statistical Mechanics Theory & Experiment_ , 10 (2008): 155–68.  
[^brown2011]:  Brown, J. E. and Dunn, P. K.  “Comparisons of Tobit, Linear, and Poisson-Gamma Regression Models: An Application of Time Use Data” ,  _Sociological Methods & Research_ , 40.3 (2011): 511–35.  
[^chen1943]:  Chen, Z.  “Lun Wang Jinggong zhi licai”  [On Financing of Wang Jinggong (Wang Anshi)],  _Junshi yu zhengzhi_ , 5.3–4 (1943).  
[^cheng1942]:  Cheng, Y.  “Wang Anshi yu Sima Guang”  [Wang Anshi and Sima Guang], _ Wen shi zazhi_ , 2.1 (1942).  
[^cheng1998]:  Cheng, R.  “Lun Luo Shu dangzheng”  [On the Luo-Shu Political Struggle]. In  _Mianxiang ershiyi shiji: zhong wai wenhua chongtu yu ronghe xueshu yantaohui lunwenji_  [Towards 21st century: Proceedings of Symposium on Collision and Integration of Chinese and Western Culture], Beijing (1998), pp. 46–66.  
[^deweerdt1998]:  De Weerdt, H.  _The Composition of Examination Standards: Daoxue and Southern Song Dynasty Examination Culture. _ Ph.D thesis, Harvard University (1998).  
[^deweerdt2019]:  De Weerdt, H., Ho, B., Wagner, A., Qiao, J. and Chu, M.  “Is There a Faction in This List?” ,  _Journal of Chinese History_ , 4 (2019): 347–89.  
[^deng1994]:  Deng, G.  “Deng Guangming xueshu lunzhu zixuanji”  [The Self-Selected Academic Writings by Deng Guangming].  _Shoudu shifan daxue chubanshe_ , Beijing (1994).  
[^deng2005]:  Deng, X. and Lamouroux, C.  “The ‘Ancestors’ Family Instructions’: Authority and Sovereignty in Song China” ,  _Journal of Song-Yuan Studies_ , 35 (2005): 79–97.  
[^du2012]:  Du, Y.  “Locality, Literati, and the Imagined Spatial Order: A Case of Huizhou, 1200–1550” ,  _Journal of Song-Yuan Studies_ , 42 (2012): 407–44.  
[^fogel1984]:  Fogel, J. A.  _Politics and Sinology:The Case of Naito Konan. _ Harvard University Press, Cambridge (1984).  
[^hahsler2005]:  Hahsler, M., Grün, B. and Hornik, K.  “Introduction to Arules – A Computational Environment for Mining Association Rules and Frequent Item Sets” ,  _Journal of Statistical Software_ , 14.15 (2005): 1–25.  
[^harvarduniversity2018]:  Harvard University, Academia Sinica and Peking University.  _China Biographical Database_  (2018). [https://projects.iq.harvard.edu/cbdb](https://projects.iq.harvard.edu/cbdb).  
[^hu1921]:  Hu, S.  “Ji Li Gou de xueshuo”  [A Description of Li Gou’s Theory]. In  _Hu Shi wen cun _ [Writings of Hu Shi], Yadong tushuguan, Shanghai (1921), set. 2, vol. 1.  
[^hu2005]:  Hu, Y. F.  “Efficient and High Quality Force-Directed Graph Drawing” .  _The Mathematica Journal_ , 10.1 (2005): 37–71.  
[^huang2013]:  Huang, Z.  “Gu jin jiyao”  [Records of Important Events in Ancient and Modern Times]. In Zhang W. and He Z. (eds),  _Huang Zhen quanji_  [Complete Works of Huang Zhen], Zhejiang daxue chubanshe, Hangzhou (2013).  
[^hucker1985]:  Hucker, C. O.  _A Dictionary of Official Titles in Imperial China_ . Stanford University Press, Redwood City (1985).   
[^kessler1963]:  Kessler, M. M.  “Bibliographic coupling between scientific papers” ,  _American Documentation_ , 14 (1963): 10–25.  
[^lambiotte2005]:  Lambiotte, R., Delvenne, J.-C. and Barahona, M.  “Laplacian Dynamics and Multiscale Modular Structure in Networks,”  _ IEEE Transactions on Network Science and Engineering_ , 1.2 (2005): 76–90.  
[^lehmann1998]:  Lehmann, E. L. and Casella, G.  _Theory of Point Estimation_ . 2nd ed. Springer, New York (1998).  
[^li1994]:  Li, J.  _Zhuzi yulei_  [Thematic Discourses of Master  _Zhu_ ], annotated by Wang X. Zhonghua shuju, Beijing (1994).  
[^li2004]:  Li, T.  _Xu zizhi tongjian changbian _ [Extended Continuation to the Comprehensive Mirror to Aid in Government]. 2nd ed. Zhonghua shuju, Beijing (2004).  
[^li1986]:  Li, X.  “Xining zhi zheng de xingzhi chuyi: cong  _da Sima Jianyi shu_  tanqi”  [A Preliminary Discussion on the Nature of Disputation in the Xining Era: Talking from  _Answering Sima Jianyi_ ],  _Shixue yuekan_ , 6 (1986): 20–5.  
[^li2013]:  Li, Z.  _Huang Song shi chao gangyao jiaozheng _ [Correction of Important Matters from the Ten Reigns of the August Song Dynasty], edited by Yan Y. Zhonghua shuju, Beijing (2013).  
[^liang1993]:  Liang, Q.  _Wang Anshi zhuan_  [A Bibliography of Wang Anshi]. Hainan chubanshe, Haikou (1993).  
[^luo1984]:  Luo, J.  “Shi lun liang Song dangzheng”  [On the Political Struggles in the Northern Song and Southern Song Dynasties],  _Huazhong shifan daxue xuebao_  (renwen shehui kexue ban), 5 (1984): 48–54.  
[^luo1985]:  Luo, J.  “Yuanyou xin jiu dangzheng qiyin tanyuan”  [Investigating the Reason of the Political Struggle Between the Reformers and Anti-Reformers in the Yuanyou Era],  _Jianghan luntan_ , 9 (1985): 69–74.  
[^luo1993]:  Luo, J.  “Xi–Feng bianfa zhi chu liang pai fenzheng yuanqi xin tan”  [A New Investigation on the Reason of the Political Struggle in the Beginning of the Reform in the Xining and Yuanfeng Eras],  _Huazhong shifan daxue xuebao_  (renwen shehui kexue ban), 3 (1993): 96–101.  
[^luo1987]:  Luo, X.  “Wengong yu Jinggong bianfa sixiang zhi bijiao”  [A Comparison of the Reform Thoughts of Wengong (Sima Guang) and Jinggong (Wang Anshi)],  _Hubei daxue xuebao_  (zhexue shehui kexue ban), 6 (1987): 82–6.  
[^luo2005]:  Luo, Y.  “A Study of the Changes in the Tang-Song Transition Model” ,  _Journal of Song-Yuan Studies_ , 35 (2005): 99–127.  
[^ma1985]:  Ma, Y.  _Yuancheng yulu jie_  [Explanation of Thematic Discourses of Yuancheng (Liu Anshi)]. Integrated series (new edition), annotated by Wang C. Xin wenfeng chuban gongsi, Taipei (1985).  
[^mcnair1998]:  McNair, A.  _The Upright Brush: Yan Zhenqing’s Calligraphy and Song Literati Politics._  University of Hawai’i Press, Honolulu (1998).  
[^mei2015]:  Mei, H.  “Wen yi xu chuan: wenren wenji xu ba yishi zijuehua ji qi yingxiang”  [Anthologies Relying on Prefaces: Consciousness of Song Dynasty’s Anthology Prefaces and Influence],  _Anhui shifan daxue xuebao_  (renwen sheke ban), 43.1 (2015): 69–75.  
[^niu1931]:  Niu, Xi.  “Beisong dangzheng de jingguo ji qi beijing”  [The Process and Background of the Political Struggle in the Northern Song dynasty],  _Qinghua zhoukan_ , 38.7 (1931).   
[^ong2005]:  Ong, C. W.  “We are One Family: The Vision of ‘Guanxue’ in the Northern Song” ,  _Journal of Song-Yuan Studies_ , 35 (2005): 29–57.  
[^piateskyshapiro1991]:  Piatesky-Shapiro, G. and Frawley, W. J.  _Knowledge Discovery in Databases_ . AAAI/MIT Press, Cambridge (1991).  
[^qian1936]:  Qian, M.  “Lun guanyu Jinggong chuanshuo zhi wen que, bian jian liang an”  [A Discussion on Allusions of ‘Hearing the Cuckoos’ and ‘a Thesis on Discerning the Villain’ about Jinggong (Wang Anshi)].  _Yi shi bao_ , November 5 (1936).  
[^qian2013]:  Qian, M.  _Guoshi dagang_  [A General History of China]. Shangwu yinshu guan, Beijing (2013).  
[^qiu1959]:  Qiu, H.  “Wang Anshi de Xinxue he bianfa sixiang de yuanze”  [The Xinxue and the Principles of Reformation of Wang Anshi],  _Lishi jiaoxue_ , 3 (1959): 28–36.  
[^roweis2000]:  Roweis, S. T. and Saul, L. K.  “Nonlinear Dimensionality Reduction by Locally Linear Embedding” ,  _Science_ , 290.5500 (2000): 2323–6.  
[^shang2018]:  Shang, W. and Huang, W.  “Investigating the Relationships between Scholars and Politicians in Ancient China: Taking the Yuanyou Era as an Example” ,  _Journal of the Japanese Association for Digital Humanities_ , 3.1 (2018): 33–48.  
[^su1986]:  Su, S.  “Celüe yi”  [Strategy One]. In Kong F. (ed.),  _Su Shi wenji _ [Collected Works of Su Shi], Zhonghua shuju (1986), p. 227.  
[^su1990]:  Su, Z.  “Wang xiong Zizhan Duanming muzhiming”  [Epitaph of My Dead Brother, Zizhan, Master of Duanming Palace]. In Chen H. and Gao H. (eds.),  _Su Zhe ji _ [Collected Works of Su Zhe], Zhonghua shuju, Beijing (1990), p. 1126.  
[^su1997]:  Su, P.  “Shilun ‘Luo Shu huitong’”  [On the ‘Fusion of Luoxue and Shuxue’],  _Xinan daxue xuebao_  (shehui kexue ban), 3 (1997): 97–100.  
[^tuotuo1985]:  Tuotuo.  _Song shi_  [History of Song]. Zhonghua shuju, Beijing (1985).  
[^weber1978]:  Weber, M.  _Economy and Society_ . University of California Press, Oakland (1978).  
[^xiao1998]:  Xiao, Q.  “Xi–Feng, Yuanyou dangzheng de xingzhi ji qi tuibian”  [The Concept and Transformation of the Political Struggle in the Xining, Yuanfeng and Yuanyou Eras],  _Gannan shifan xueyuan xuebao_ , 4 (1998): 61–66.  
[^yang1980]:  Yang, B.  _Lunyu yi zhu_  [Translations and Annotations of the  _Analects_ ]. Zhonghua shuju, Beijing (1980).  
[^yang1946]:  Yang, R.  “Zhi Songshi yu qingfu zhe Wang Anshi xinfa hu?”  [Was the Reform of Wang Anshi that Caused the Collapse of Song?],  _Zhongguo xueshu_ , 1.1 (1946).  
[^zhang2005]:  Zhang, C.  “Communication, Collaboration, and Community: Inn-Wall Writing During the Song (960–1279)” ,  _Journal of Song-Yuan Studies_ , 35 (2005): 1–27.  
[^zhao1999]:  Zhao, R.  _Songchao zhu chen zouyi _ [Memorials of All Ministers of Song Dynasty]. Shanghai guji chubanshe, Shanghai (1999).  
[^zhou2012]:  Zhou, M., Hannah, L. A., Dunson, D. B. and Carin, L.  “Beta-Negative Binomial Process and Poisson Factor Analysis” ,  _Statistics_  (2012): 1462–71.  
[^zhu2006]:  Zhu, X.  “Da Wang Shangshu (si)”  [Answering Minister Wang (Four)]. In Zhu X.,  _Hui’an Xiansheng Zhu Wengong quanji _ [Collected works of Hui’an Xiansheng Zhu Wengong (Zhu Xi)], Guojia tushuguan chubanshe, Beijing (2006), vol. 30.  
[^zhuge1996]:  Zhuge, Y.  “Luo Shu dangzheng bianxi”  [A Discrimination of the Luo-Shu Political Struggle], Nanjing shida xuebao (shehui kexue ban), 4 (1996): 100–5.  