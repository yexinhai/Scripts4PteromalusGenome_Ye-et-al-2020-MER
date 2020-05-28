#!/usr/bin/python

from sys import argv

with open(argv[1]) as fasta:
	list1 = fasta.readlines()

import re
reg_ID=re.compile("^>(\S+)$")
reg_chr=re.compile("Scaffold+")

adict = {}

for line in list1:
	line = line.strip()
	if line[0] == '>':
		name = reg_ID.search(line).group(1)
		adict[name] = []
	else:
		adict[name].append(line)

for key in adict:
	a = reg_chr.search(key)
	if a:
		print('>' + str(key))
		seq = ''.join(adict[key])
#		seq1 = str(seq)[31425902:31425970]
		print(seq)

