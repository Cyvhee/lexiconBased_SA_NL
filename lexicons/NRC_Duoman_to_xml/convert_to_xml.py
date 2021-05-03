#!/usr/bin/env python

import codecs
import xml.etree.cElementTree as ET
import xml.dom.minidom
import os
import pickle

from SentimentLexiconClass import SentimentLexicon, LexiconEntry
'''
Script converts Duoman and NRC lexicons (CSV format) into XML files.
Needs: NRC.csv, Duoman.csv, penn_to_lets.pkl
Outputs: NRC.xml, Duoman.xml
'''


pkl_file = open('penn_to_lets.pkl', 'rb')
penn_to_lets_dict = pickle.load(pkl_file)


def read_NRC_file(nrcfile):
	'''
	Read the NRC sentiment lexicon file and create an NRC sentiment object
	'''
	entries = []
	file = codecs.open(nrcfile, 'r').readlines()
	for line in file[1:]: #Discard metadata
		splits = line.split('\t')
		word, postag, pos, neg = splits[1:5]
		# print(word,postag,pos,neg)
		postag = postag.split(' ')[0]
		if len(word.split(' ')) == 1: #Discard entries without a translation and multiwords
			if postag in penn_to_lets_dict: #Discard invalid PoS-tags
				letstag = penn_to_lets_dict[postag] #Map Penn PoS-tag to Lets PoS-tag
				polarity = None
				if pos == '1' and neg == '0':
					polarity = 'positive'
				elif pos == '0' and neg == '1':
					polarity = 'negative'
				elif pos == '0' and neg == '0':
					polarity = 'neutral'
				if polarity: #Discard entries with positive and negative polarity
					entries.append(LexiconEntry(word, letstag, polarity))
	return SentimentLexicon('NRC', entries)


def read_Duoman_file(duomanfile):
	'''
	Read the Duoman sentiment lexicon file and create a Duoman sentiment object
	'''
	entries = []
	file = codecs.open(duomanfile, 'r').readlines()
	for line in file[1:]: #Discard metadata
		splits = line.strip().split('\t')
		if len(splits) == 4:
			word = splits[0]
			postag = splits[2].split(' ')[0]
			pol = splits[3]
			if len(word.split(' ')) == 1:
				if postag in penn_to_lets_dict:
					letstag = penn_to_lets_dict[postag]
					polarity = None
					if pol == '+':
						polarity = 'positive'
					elif pol == '++':
						polarity = 'very_positive'
					elif pol == '-':
						polarity = 'negative'
					elif pol == '--':
						polarity = 'very_negative'
					elif pol == '0':
						polarity = 'neutral'
					if polarity:
						entries.append(LexiconEntry(word, letstag, polarity))
	return SentimentLexicon('Duoman', entries)


def write_xml(sentimentlexiconentries, outfile):
	root = ET.Element("Lexicon", domain=sentimentlexiconentries.name)
	doc = ET.SubElement(root, "train-items")

	for item in sentimentlexiconentries.entries:
		ET.SubElement(doc, "lexitem", polarity=item.polarity, wordform=item.word, instances="1", lemma="", pos=item.postag)
		tree = ET.ElementTree(root)
		# tree.write(outfile)
	pretty_print_xml_given_root(root, outfile)

def pretty_print_xml_given_root(root, output_xml):
	"""
	Useful for when you are editing xml data on the fly
	"""
	xml_string = xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml()
	xml_string = os.linesep.join([s for s in xml_string.splitlines() if s.strip()]) # remove the weird newline issue
	with open(output_xml, "w") as file_out:
		file_out.write(xml_string)

# def pretty_print_xml_given_file(input_xml, output_xml):
# 	"""
# 	Useful for when you want to reformat an already existing xml file
# 	"""
# 	tree = ET.parse(input_xml)
# 	root = tree.getroot()
# 	pretty_print_xml_given_root(root, output_xml)


def main():
	NRC_object = read_NRC_file("NRC.csv")
	Duoman_object = read_Duoman_file("Duoman.csv")
	write_xml(NRC_object, "NRC.xml")
	write_xml(Duoman_object, "Duoman.xml")


if __name__ == "__main__":
    main()





