import os
import re
import random

def main():
#	src_file = input("where is the model? ")
	numwords = input("how many words to generate? ")
	src_file = "separated_lorem.txt"
	seq_list = []
	with open(src_file) as file:
		for line in file:
			seq_list.append(line)
		# for count, line in enumerate(file):
		# 	pass
		# seq_list = [[]*4 for i in range(count+1)]
		# i=0	
		# for line in file:
		# 	for word in line:
		# 		seq_list[0].append(word)
		# 	i+=1
		type(seq_list.copy(),numwords)
	
def type(seed,length):
	random.shuffle(seed)
	line = seed[0]
	i = 0
	while (i<length):
		
main()