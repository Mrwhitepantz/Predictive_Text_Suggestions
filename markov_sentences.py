import os
import re
import random

seq_list = []

def main():
#	src_file = input("where is the model? ")
	numwords = int(input("how many words to generate? "))
	src_file = "separated_war_peace.txt"
	
	with open(src_file,"r") as file:
		for line in file:
			seq_list.append(line)
	seed = random.choice(seq_list)
	line1 = " ".join(seed.split()[-3:])
	print(line1, end=" ")
	i = 0
	while (i<numwords):
		line1 = line1.strip()
		line2 = ""
		poss_seq = []
		poss_word = []
		word_dict = {}
		for seq in seq_list:
			if (line1.split()[0:3] == seq.split()[0:3]):
				poss_seq.append(seq)
				poss_word.append(seq.split()[-1])
		for word in poss_word:
			if word in word_dict.keys():
				word_dict[word] += 1
			else:
				word_dict[word] = 1
		print(poss_seq, end=" ")
		next_seq = random.choice(poss_seq)
		line2 = " ".join(next_seq.split()[-3:])
		next_word = " ".join(line2.split()[-1:])
		print(next_word, end=" ")
		line1 = line2
		i+=1

main()
