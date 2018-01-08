# Imports
import collections
from collections import Counter
import itertools
from string import ascii_lowercase
import difflib
from nltk import word_tokenize
from nltk.corpus import stopwords

# User Input
print('Enter Raw String:')
print('Eg: tyvm u helped me a lotttt @ the museum! #sarcasm')
string = input()

# Function that returns all possible combinations of a word
def RepeatedLettersInTheWord(word):
	file = open('Dictionaries/english.txt')
	word_list = file.readlines()
	word_list = word_list[0].split()
	word = word.lower()
	if len(word) != 1:
		if word in word_list:
			return word
		else:
			FrequencyOfLetters = collections.Counter(word)
			conv1 = list(FrequencyOfLetters.elements())
			LengthOfConv = len(conv1)

			HighestFrequencyLetter = FrequencyOfLetters.most_common(1)[0]
			HighestFrequency = HighestFrequencyLetter[1]
			count=0
			count1=0

			flag = False
			y = []

			for x in range(0,LengthOfConv-1):
				if conv1[x]!=conv1[x+1]:
					y.extend(conv1[x])
					count = count + 1 
				else:
					if flag==False:
						count1=count1 + 1
						flag=True
					if flag==True:
						continue
			if(HighestFrequency >= 3):
				flag = 1
			else:
				flag = 0
				return word
			   
			y.extend(conv1[x+1])
			y = ''.join(y)
			string_list = difflib.get_close_matches(y, word_list)
			print('\nPossible Words for '+word+':')
			print(string_list)
			return string_list
	else:
		return word

# Function that returns all possible combinations of a string
def RepeatedWordsInTheString(string):
	FrequencyOfWords = collections.Counter(string.split())
	conv = list(FrequencyOfWords.elements())
	word = ''
	possible_strings = ['']
	for x in conv:
		word = RepeatedLettersInTheWord(x)
		if isinstance(word,str):
			for x in range(0,len(possible_strings)):
				possible_strings[x] = possible_strings[x] + ' ' + word
		elif isinstance(word,list):
			temp = []
			for y in possible_strings:
				for x in word:
					temp.insert(len(possible_strings), y + ' ' + x)
		
			possible_strings = temp
	
	return possible_strings

# Function call to remove 'wordplays'
intermediate = RepeatedWordsInTheString(string)
print('\nPossible Strings after removing wordplays:')
print(intermediate)

# List of stop words
stop = set(stopwords.words('english'))

# Code to remove abbreviations
def removeAbbr(process):
	index = 0
	for x in process:
		with open("Dictionaries/abbreviations.txt") as fh:
			for line in fh:
				if line.startswith(x):
					line = line.rsplit(' ',1)[0]
					if x == line.split()[0]:
						process[index] = line.split(' ',1)[1]
						index_used.add(index)
						break
		index = index + 1
	return process

# Code to remove Slangs
def removeSlangs(process):
	index = 0
	for x in process:
		if index in index_used:
			index = index + 1
		else:
			with open("Dictionaries/slangs.txt") as fh:
				for line in fh:
					if line.startswith(x):
						line = line.rsplit(' ',1)[0]
						if x == line.split()[0]:
							process[index] = line.split(' ',1)[1]
							index_used.add(index)
							break
			index = index + 1
	return process

Output = []

for text in intermediate:
	process = [i for i in text.lower().split() if i not in stop]

	# Initialization to track the indexes used in abbreviation conversion
	index_used = set()

	process = removeAbbr(process)
	process = removeSlangs(process)

	Normalized = ' '.join(process)

	# Remove Stopwords from Normalized String
	Normalized = [i for i in Normalized.lower().split() if i not in stop]
	Normalized = ' '.join(Normalized)

	Output.insert(len(Output), Normalized) 

print('\nNormalized Strings:')
print(Output)