
#!/usr/bin/python

import re, collections

def words(text):
	return re.findall('[a-z]+', text.lower())

def train(features):
	model = collections.defaultdict(lambda: 1)
	for f in features:
		model[f] += 1
	return model

NWORDS = train(words(file('big.txt').read()))

alphabet = 'abcdefghijklmnopqrstxyz'

def edist1(word):
	n = len(word)
	return set([word[0:i]+word[i+1: ] for i in range(n)] +						#deletion
			   [word[0:i]+word[i+1]+word[i]+word[i+2: ] for i in range(n-1)] +	#transposition
			   [word[0:i]+c+word[i+1: ] for i in range(n) for c in alphabet] +	#alteration
			   [word[0:i]+c+word[i: ] for i in range(n+1) for c in alphabet])	#insertion

def known_edist2(word):
	return set(e2 for e1 in edist1(word) for e2 in edist1(e1) if e2 in NWORDS)

# python www.iplaypy.com 教程
def known(words):
	return set(w for w in words if w in NWORDS)

def correct(word):
	candidates = known([word]) or known(edist1(word)) or known_edist2(word) or [word]
	return max(candidates, key=lambda w:NWORDS[w])

print('thew => ' + correct('thew'))
print('spak => ' + correct('spak'))
print('goof => ' + correct('goof'))
print('babyu => ' + correct('babyu'))
print('spalling => ' + correct('spalling'))
