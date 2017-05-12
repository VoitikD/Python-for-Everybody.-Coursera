name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


d = dict()
for line in handle:
	line = line.rstrip()
	if not line.startswith('From ') : continue
	words = line.split()
	time = words[5]
	hour = time.split(':')
	h = hour[0]
	d[h] = d.get(h,0) + 1

lst = list()
for h, v in d.items():
	lst.append( (h, v) )

lst.sort()

for h, v in lst :
	print h, v
