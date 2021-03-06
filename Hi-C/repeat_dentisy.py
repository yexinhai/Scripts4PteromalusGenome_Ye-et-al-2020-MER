#!/usr/bin/python
# Ye Xinhai, yexinhai@zju.edu.cn, let me know if you have any question.

from sys import argv

import re
reg_ID=re.compile("^>(\S+)$")


with open(argv[1]) as fasta:
	list1 = fasta.readlines()
adict = {}
for line in list1:
	line = line.strip()
	if line[0] == '>':
		name = reg_ID.search(line).group(1)
		adict[name] = []
	else:
		adict[name].append(line)

len_dict = {}

for key in adict:
	seq = ''.join(adict[key])
	len_dict[key] = len(seq)


with open (argv[2]) as repeat:
	list2 = repeat.readlines()

repeat_den_dict = {}

for line in list2:
	line = line.strip()
	a = line.split('\t')
	chr_num = a[0]
	gene_start = a[1]
	group = str(int(int(gene_start)/100000))
	repeat_den_dict.setdefault(chr_num, []).append(group)

for key in repeat_den_dict:
	num = int(len_dict[key]/100000) + 1
	for i in range(num):
		if (i+1)*100000 <= len_dict[key]:
			print (str(key) + '\t' + str(i*100000+1) + '\t' + str((i+1)*100000) + '\t' + str(repeat_den_dict[key].count(str(i))))
		else:
			print (str(key) + '\t' + str(i*100000+1) + '\t' + str(len_dict[key]) + '\t' + str(repeat_den_dict[key].count(str(i))))
