import os

file1 = open('english.txt', 'r')
file2 = open('Final.txt','a')
for x in file1:
	x = x.split('\n')[0]
	file2.write(x + ' ')

file1.close()
file2.close()