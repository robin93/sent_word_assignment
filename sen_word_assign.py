import re

print "hello world"

#import the book text
all_text = open('book.txt')

# for line in all_text:
# 	print line

#clean the book text
#clean_txt = re.sub(all_text, "[^a-zA-Z0-9% ._]"," ");

#for line in clean_txt:
#	print line

#parse for sentences
pattern = '[a-zA-Z0-9" ""."]'

#parse for words
word_list = list()
sentence_list = list()

for line in all_text:
	if line.strip():
		line = ''.join(re.findall(pattern,line))
		for sentence in line.split("."):
			sentence_list.append(sentence)

for i in sentence_list:
	print i