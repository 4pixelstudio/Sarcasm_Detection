# Imports
from nltk import word_tokenize
from nltk.corpus import stopwords

stop = set(stopwords.words('english'))

text = 'tyvm u helped me a lot @ the museum! #Sarcasm'

process = [i for i in text.lower().split() if i not in stop]

# Initialization to track the indexes used in abbreviation conversion
index_used = set()

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


process = removeAbbr(process)
process = removeSlangs(process)

Normalized = ' '.join(process)

# Remove Stopwords from Normalized String
Normalized = [i for i in Normalized.lower().split() if i not in stop]
Normalized = ' '.join(Normalized)

print(Normalized)