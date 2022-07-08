import os
from os import path
import re

def main():
	file_path_input = input("which file to break up? ")
	fHead, fTail = path.split(file_path_input)
	file_path_output = "models/" + fTail
	word1 = "***"
	word2 = "**"
	word3 = "*"

	with open(file_path_input,encoding='utf8') as file:
		for line in file:
			for word in line.split():
				word = re.sub(r'[^\w]', '', word).lower()
				word1 = word2
				word2 = word3
				word3 = word

				with open(file_path_output, 'a') as file2:
					file2.write("%s %s %s\n" %(word1,word2,word3))

main()