# Exercise 10.3 Write a program that reads a file and prints the letters in decreasing
# order of frequency. Your program should convert all the input to lower case and
# only count the letters a-z. Your program should not count spaces, digits, punctuation,
# or anything other than the letters a-z. Find text samples from several different
# languages and see how letter frequency varies between languages. Compare your
# results with the tables at wikipedia.org/wiki/Letter_frequencies'

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

letters = dict()
for line in handle:
	line = line.lower()
	words = line.rstrip()
	for letter in words:
		letters[letter] = letters.get(letter,0) + 1

lst = list()
for count, letter in letters.items():
	lst.append( (letter, count) )

lst.sort(reverse=True)

for count, letter in lst :
	print letter, count

#Don't know how to isolate punctuation and  digits
