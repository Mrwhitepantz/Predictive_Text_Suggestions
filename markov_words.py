import os
import re

def main():
	file_path_input = "lorem.txt"
	file_path_output = "separated_" + file_path_input
	word1 = "****"
	word2 = "***"
	word3 = "**"
	word4 = "*"

	with open(file_path_input) as file:
		for line in file:
			for word in line.split():
				word = re.sub(r'[^\w]', '', word).lower()
				word1 = word2
				word2 = word3
				word3 = word4
				word4 = word
				with open(file_path_output, 'a') as file2:
					file2.write("%s %s %s %s\n" %(word1,word2,word3,word4))

main()
