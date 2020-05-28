#!/usr/bin/python

from sys import argv

with open(argv[1]) as agp:
	list1 = agp.readlines()

agp_dict={}

'''
for line in list1:
	line = line.strip()
	chr_list = line.split('\t')
	if (chr_list[0] != 'Chromosome' and chr_list[4] == 'W'):
		scaffold = chr_list[5]
		fangxiang = chr_list[-1]
		chr_num = chr_list[0]
		chr_start = chr_list[1]
		chr_end = chr_list[2]
		agp_dict.setdefault(scaffold, {})["Fangxiang"] = fangxiang
		agp_dict.setdefault(scaffold, {})["Chr_num"] = chr_num
		agp_dict.setdefault(scaffold, {})["Chr_start"] = chr_start
		agp_dict.setdefault(scaffold, {})["Chr_end"] = chr_end
'''
for line in list1:
	line = line.strip()
	chr_list = line.split('\t')
	scaffold = chr_list[3]
	scaffold_start = chr_list[-2]
	scaffold_end = chr_list[-1]
	sacffold_taq = str(scaffold) + "-" + str(scaffold_start) + "-" + str(scaffold_end)
	fangxiang = chr_list[-3]
	chr_num = chr_list[0]
	chr_start = chr_list[1]
	chr_end = chr_list[2]
	agp_dict.setdefault(sacffold_taq, {})["Fangxiang"] = fangxiang
	agp_dict.setdefault(sacffold_taq, {})["Chr_num"] = chr_num
	agp_dict.setdefault(sacffold_taq, {})["Chr_start"] = chr_start
	agp_dict.setdefault(sacffold_taq, {})["Chr_end"] = chr_end


with open(argv[2]) as repeat:
	list2 = repeat.readlines()

scaffold_in_chr =[]

for key in agp_dict.keys():
	a = key.split("-")[0]
	scaffold_in_chr.append(a)

for line in list2:
	line = line.strip()
	line = '\t'.join(line.split())
	repeat = line.split('\t')
	scaffoldname = repeat[4].replace('_','')
	div = repeat[1]
	repeat_start = repeat[5]
	repeat_end = repeat[6]
	rep_class = repeat[10]
	for key in agp_dict.keys():
		if scaffoldname == key.split("-")[0] and int(key.split("-")[1]) <= int(repeat_start) <= int(key.split("-")	[2]) and int(key.split("-")[1]) <= int(repeat_end) <= int(key.split("-")[2]):
			if agp_dict[key]["Fangxiang"] == '+':
				new_start = int(repeat[5]) - int(key.split("-")[1]) + int(agp_dict[key]["Chr_start"])
				new_end = int(new_start) + int(repeat[6]) - int(repeat[5])
				print (agp_dict[key]["Chr_num"] + '\t' +  str(new_start) + '\t' + str(new_end) + '\t' + str(div) + '\t' + str(rep_class))
			elif agp_dict[key]["Fangxiang"] == '-':
				new_end = int(agp_dict[key]["Chr_end"]) - int(repeat[5]) + int(key.split("-")[1])
				new_start = new_end - int(repeat[6]) + int(repeat[5])
				print (agp_dict[key]["Chr_num"] + '\t' +  str(new_start) + '\t' + str(new_end) + '\t' + str(div) + '\t' + str(rep_class))




			