#!/usr/bin/python

from sys import argv

with open(argv[1]) as agp:
	list1 = agp.readlines()

agp_dict={}

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

with open(argv[2]) as oldgff:
	list2 = oldgff.readlines()

scaffold_in_chr =[]

for key in agp_dict.keys():
	a = key.split("-")[0]
	scaffold_in_chr.append(a)

for line in list2:
	line = line.strip()
	gff_list = line.split('\t')
	scaffoldname = gff_list[0].replace('_','')
	genestart = gff_list[3]
	geneend = gff_list[4]
	for key in agp_dict.keys():
		if scaffoldname == key.split("-")[0] and int(key.split("-")[1]) <= int(genestart) <= int(key.split("-")[2]) and int(key.split("-")[1]) <= int(geneend) <= int(key.split("-")[2]):
			if agp_dict[key]["Fangxiang"] == '+':
				new_start = int(gff_list[3]) - int(key.split("-")[1]) + int(agp_dict[key]["Chr_start"])
				new_end = int(new_start) + int(gff_list[4]) - int(gff_list[3])
				print (agp_dict[key]["Chr_num"] + '\tEVM\t' + gff_list[2] + '\t' +  str(new_start) + '\t' + str(new_end) + '\t.\t' + gff_list[6] + '\t.\t' + gff_list[-1])
			elif agp_dict[key]["Fangxiang"] == '-':
				new_end = int(agp_dict[key]["Chr_end"]) - int(gff_list[3]) + int(key.split("-")[1])
				new_start = new_end - int(gff_list[4]) + int(gff_list[3])
				if gff_list[6] == '+':
					print (agp_dict[key]["Chr_num"] + '\tEVM\t' + gff_list[2] + '\t' +  str(new_start) + '\t' + str(new_end) + '\t.\t' + '-' + '\t.\t' + gff_list[-1])
				else:
					print (agp_dict[key]["Chr_num"] + '\tEVM\t' + gff_list[2] + '\t' +  str(new_start) + '\t' + str(new_end) + '\t.\t' + '+' + '\t.\t' + gff_list[-1])
	if scaffoldname not in scaffold_in_chr:
		print (str(line))



"""
for line in list2:
	line = line.strip()
	if not line[0] == '#':
		gff_list = line.split('\t')
		scaffold1 = gff_list[0]
		if scaffold1 in agp_dict.keys():
			if agp_dict[scaffold1]["Fangxiang"] == '+':
				new_start = int(gff_list[3]) + int(agp_dict[scaffold1]["Chr_start"]) - 1
				new_end = int(new_start) + int(gff_list[4]) - int(gff_list[3])
				print (agp_dict[scaffold1]["Chr_num"] + '\tmaker\t' + gff_list[2] + '\t' +  str(new_start) + '\t' + str(new_end) + '\t.\t' + gff_list[6] + '\t.\t' + gff_list[-1])
			elif agp_dict[scaffold1]["Fangxiang"] == '-':
				new_end = int(agp_dict[scaffold1]["Chr_end"]) - int(gff_list[3]) + 1
				new_start = new_end - int(gff_list[4]) + int(gff_list[3])
				if gff_list[6] == '+':
					print (agp_dict[scaffold1]["Chr_num"] + '\tmaker\t' + gff_list[2] + '\t' +  str(new_start) + '\t' + str(new_end) + '\t.\t' + '-' + '\t.\t' + gff_list[-1])
				else:
					print (agp_dict[scaffold1]["Chr_num"] + '\tmaker\t' + gff_list[2] + '\t' +  str(new_start) + '\t' + str(new_end) + '\t.\t' + '+' + '\t.\t' + gff_list[-1])
"""