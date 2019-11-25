
import os
import csv
import re

word_count = 0
sentence_count = 0
letters_count = 0
s_length = 0

# Input files available for this test - "paragraph_1.txt" / "paragraph_2.txt"

# Choose option 1 or 2
fileNum = 1

in_file = os.path.join('Input & Output','paragraph_' + str(fileNum) + '.txt')
out_file = os.path.join('Input & Output', 'paragraph_' + str(fileNum) + '_analysis' '.txt')


with open(in_file, "r") as in_file:
	
	paragraph = in_file.read()

	# Counting hyphenated words as two (splitting on space (\s) or '-')
	words = re.split(r'[\s | -]', paragraph)  
	word_count = len(words) 
	

	# Counting the number of sentences using regEx string from Stack Overflow
	myRegEx = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s')
	sentences = myRegEx.split(paragraph)
	sentence_count = len(sentences)

	
	# Calculating the average letter count and average sentence length 
	for each_word in words:
		letters_count = letters_count + len(each_word)

	avg_letter_count = round((letters_count/word_count), 1)

	avg_sentence_len = round((len(words)/sentence_count), 0)


# Preparing the summary of output
result = (f'Paragraph Analysis' '\n-----------------------------' 
		  f'\nApproximate Word Count: {word_count}' 
		  f'\nApproximate Sentence Count: {sentence_count}'
		  f'\nAverage Letter Count: {avg_letter_count}' 
		  f'\nAverage Sentence Length: {avg_sentence_len}' '\n------------------------------')
	

# Printing result to the terminal	
print(result)


# Printing result to the output file
with open(out_file, 'w+') as out_text:
	out_text.write(result)
	 