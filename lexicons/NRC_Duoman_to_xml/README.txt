###################
README
Cynthia, 15/04/2020
###################

In deze map staat de code om de sentiment lexicons (NRC + Duoman) geannoteerd door Annaïs (zomer 2019) om te zetten naar XML files die ingelezen kunnen worden door Orphées script lexiconmatch.py.

In de code worden woorden weggelaten als ze 1) geen PoS-tag of polarity label hebben, 2) tegenstrijdige polarity labels hebben, 3) een onherkenbare PoS-tag of polarity label hebben.

Extra info:
	* penn_to_lets.py: maakt een mapping dict om Penn Treebank PoS-labels te mappen naar Lets labels (resultaat = penn_to_lets.pkl).
	* SentimentLexiconClass.py: definieert classes, niet rechtstreeks nodig.
	* convert_to_xml.py: leest lexicons en penn_to_lets dict in, mapt labels en schrijft sentiment lexicons (woord, lemma, pos, polarity) uit naar XML file.
	* NRC.csv, Duoman.csv: ruwe lexiconfiles (input voor script convert_to_xml.py)
