#Assignment 11 Extracting Data With Regular Expressions

name = raw_input("Enter file:")
if len(name) < 1 : name = "data.txt"
handle = open(name)
inp = handle.read()


import re
x = re.findall('[0-9]+', inp)

lst = list()	
for num in x:	
	num = float(num)
	lst.append(num)

print sum(lst)



