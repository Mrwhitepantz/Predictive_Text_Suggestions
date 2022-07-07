import numpy
import random
import re

def main():
	file_path = "lorem.txt"
	numwords = int(input("How many words to generate? "))
	with open(file_path) as file:
		for line in file:
			for word in line.split():
				word = re.sub(r'[^\w]', '', word).lower() # strip punctuation and make all lower case.
		corpus = file.read().split()
		seqs = make_seqs(corpus)
		word_dict = {}
		# This loop populates the dictionary with keys made of tuples generated from make_seqs
		# and values of the 4th word from make_seqs.
		for seq_tuple, word4 in seqs:
			if seq_tuple in word_dict.keys():
				word_dict[seq_tuple].append(word4)
			else:
				word_dict[seq_tuple] = word4
		seed = numpy.random.choice([word_dict.keys()])
		print(word_dict[lorem ipsum dolor])

# dictionary idea and make_seqs code from b at
# https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6
# make_seqs prepares a four word sequence in the form of a tuple for the first three words and string for the last word.

def make_seqs(corpus):
	for i in range(len(corpus)-1):
		word_tuple = (corpus[i],corpus[i+1],corpus[i+2])
		yield(word_tuple,corpus[i+3])

main()