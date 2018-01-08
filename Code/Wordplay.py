# Imports
import collections
from collections import Counter
import itertools
from string import ascii_lowercase
import difflib

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
			return string_list

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

word = RepeatedLettersInTheWord("Goddddd")
print(word)

string = RepeatedWordsInTheString('My god you are gooooooddddd')
print(string)