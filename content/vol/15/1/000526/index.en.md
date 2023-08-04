---
type: article
dhqtype: article
title: "Using an Advanced Text Index Structure for Corpus Exploration in Digital Humanities"
date: 2021-05-21
article_id: "000526"
volume: 015
issue: 1
authors:
- Tobias Englmeier
- Marco Büchler
- Stefan Gerdjikov
- Klaus U. Schulz
translationType: 
tags:
- corpus exploration
- metadata
- phrase extraction
- text alignment
- SCDAWG
- index structures
abstract: |
   With suitable index structures many corpus exploration tasks can be solved in an efficient way without rescanning the text repository in an online manner. In this paper we show that symmetric compacted directed acyclic word graphs (SCDAWGs) - a refinement of suffix trees - offer an ideal basis for corpus exploration, helping to answer many of the questions raised in DH research in an elegant way. From a simplified point of view, the advantages of SCDAWGs rely on two properties. First, needing linear computation time, the index offers a joint view on the similarities (in terms of common substrings) and differences between all text. Second, structural regularities of the index help to mine interesting portions of texts (such as phrases and concept names) and their relationship in a language independent way without using prior linguistic knowledge. As a demonstration of the power of these principles we look at text alignment, text reuse in distinct texts or between distinct authors, automated detection of concepts, temporal distribution of phrases in diachronic corpora, and related problems.
teaser: "A study investigating the application of the SCDAWG index structure for large scale corpus exploration"
order: 29
cluster: "Göttingen Dialogues in Digital Humanities"
---
## Bibliography

<ul>
<li id="blumer1987">Blumer, A., Blumer, J., Haussler, D., McConnell, R., and Ehrenfeucht, A. “Complete inverted files for efficient text retrieval and analysis” . _Journal of the ACM (JACM)_ 34 (1987): 578-595.
</li>
<li id="büchler2012">Büchler, M., Crane, G., Moritz, M., and Babeu, A. “Increasing recall for text re-use in historical documents to support research in the humanities” . In _Proceedings of 16th International Conference on Theory and Practice of Digital Libraries, (tpdl 2012):_ pp. 95–100 _Springer Berlin Heidelberg_ .
</li>
<li id="gerdjikov2013">Gerdjikov, S. and Mihov, S. and Nenchev, V. “Extraction of spelling variations from language structure for noisy text correction” . In _Proc. Int. Conf. for Document Analysis and Recognition_ (2013): 324-328.
</li>
<li id="gerdjikov2016">Gerdjikov, S., and Schulz, K. U. “Corpus analysis without prior linguistic knowledge-unsupervised mining of phrases and subphrase structure” . _ArXiv e-prints_ (2016): 1602.05772.
</li>
<li id="gusfield1997">Gusfield, D. _Algorithms on strings, trees and sequences: computer science and computational biology_ . Cambridge university press, Cambridge, 1997.
</li>
<li id="inenaga2005">Inenaga, S., Hoshino, H., Shinohara, A., Takeda, M., Arikawa, S., Mauri, G., and Pavesi, G. “On-line construction of compact directed acyclic word graphs” . _Discrete Applied Mathematics_ 146 (2005): 156-179.
</li>
<li id="mccreight1976">McCreight, Edward M. “A space-economical suffix tree construction algorithm” . _Journal of the ACM (JACM)_ 23 (1976): 262-272.
</li>
<li id="mitankin2014">Mitankin, P. and Gerdjikov, S. and Mihov, S. “An approach to unsupervised historical text normalization” . In _Proceedings of the First International Conference on Digital Access to Textual Cultural Heritage:_ (2014) 29-34.
</li>
<li id="needleman1970">Needleman, S. B., and Wunsch, C. D. “A general method applicable to the search for similarities in the amino acid sequence of two proteins.” . _Journal of molecular biology_ 48 (1970): 443-453.
</li>
<li id="okanohara2009">Okanohara, Daisuke and Tsujii, Jun'ichi “Text categorization with all substring features” . In _Proceedings of the 2009 SIAM International Conference on Data Mining:_ (2009) 839-846.
</li>
<li id="sariev2014">Sariev, Andrei and Nenchev, Vladislav and Gerdjikov, Stefan and Mitankin, Petar and Ganchev, Hristo and Mihov, Stoyan and Tinchev, Tinko “Flexible noisy text correction” . In _Proceedings of Document Analysis Systems:_ (2014)
</li>
<li id="schütze1993">Schütze, H., and Pedersen, J. “A vector model for syntagmatic and paradigmatic relatedness” . In _Proceedings of the 9th Annual Conference of the UW Centre for the New OED and Text Research, (oed 1993):_ pp. 104–113.
</li>
<li id="storjohann2010">Storjohann, P. (Ed.) _Lexical-semantic relations: theoretical and practical perspectives (Vol. 28)_ . John Benjamins Publishing, Cambridge, 2010.
</li>
<li id="ukkonen95">Ukkonen, Esko. “On-line construction of suffix trees” . _Algorithmica_ 14 (1995): 249-260.
</li>
<li id="weiner1973">Weiner, P. “Linear pattern matching algorithms” . In _Proceedings of 14th Annual Symposium on Switching and Automata Theory, (swat 1973):_ pp. 1–11 _IEEE_ .
</li>

</ul>
