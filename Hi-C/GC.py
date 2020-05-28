#!/usr/bin/python
# Ye Xinhai, yexinhai@zju.edu.cn, let me know if you have any question.

from sys import argv

def Slide_Window(sequence, window_size):
	result=[]
	split_num = len(sequence)/window_size
	for i in range(int(split_num) + 1):
		result.append(sequence[i*window_size : (i+1)*window_size])
	return result

def GC_ratio(sequence):
	seq_change = sequence.upper()
	GC_R = float((seq_change.count('G') + seq_change.count('C')))/len(seq_change)
	return GC_R

#with open(argv[1]) as fasta:
#	list1 = fasta.readlines()

import re
reg_ID=re.compile("^>(\S+)$")

if __name__ == '__main__':
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

	for key in adict:
		seq = ''.join(adict[key])
		a = Slide_Window(seq,100000)
		for i in a:
			gc = GC_ratio(i)
			if (int(a.index(i))+1)*100000 <= len_dict[key]:
				print (str(key) + '\t' + str((int(a.index(i))*100000)+1) + '\t' +  str((int(a.index(i))+1)*100000) + '\t' + str(gc))
			else:
				print (str(key) + '\t' + str((int(a.index(i))*100000)+1) + '\t' +  str(len_dict[key]) + '\t' + str(gc))


#	seq = 'AGAAAACCCCCCFFGFFFSSSGSSEGEEEEQQgQcQRRR'
#	a = Slide_Window(seq, 6)
#	for i in a:
#		gc = GC_ratio(i)
#		print (str(a.index(i)) + '\t' + str(gc))
