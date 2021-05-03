#!/usr/bin/env python


class SentimentLexicon:
	def __init__(self, name, entries):
		self.name = name
		self.entries = entries

class LexiconEntry:
	def __init__(self, word, postag, polarity):
		self.word = word
		self.postag = postag
		self.polarity = polarity



