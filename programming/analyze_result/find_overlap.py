



def find_overlap():

	f_1 = open('../../../Master_files/external/GSE22153_HUGO.txt', 'r')
	f_2 = open('../../../Master_files/convert/GSE26495_HUGO_combined.txt', 'r')
	f_3 = open('../../../Master_files/external/GSE22153_HUGO_LLSR_overlap.txt', 'w')
	f_4 = open('../../../Master_files/convert/GSE26495_HUGO_combined_LLSR_overlap.txt', 'w')

	GSE22153 = []
	GSE26495 = []
	header = True

	for line in f_1:

		if header == True:
			f_3.write(line)
			header = False
			continue

		temp_array = []
		splitted_line = line.split('\t')

		for i in range(len(splitted_line)):
			temp_array.append(splitted_line[i])

		GSE22153.append(temp_array)

	header = True

	for line in f_2:

		if header == True:
			f_4.write(line)
			header = False
			continue

		temp_array = []
		splitted_line = line.split('\t')

		for i in range(len(splitted_line)):
			temp_array.append(splitted_line[i])

		GSE26495.append(temp_array)

	print("*** GSE22153 ***")
	index = 0

	for i in range(len(GSE22153)):
		found = False
		for j in range(len(GSE26495)):
			if GSE22153[i][0] == GSE26495[j][0]:
				found = True
				break

		if found == False:
			index += 1
		else:
			for k in range(len(GSE22153[i])):
				f_3.write(GSE22153[i][k])
				if k != len(GSE22153[i]) - 1:
					f_3.write('\t')

	print(index)
	print("")
	print("*** GSE26495 ***")
	index = 0

	for i in range(len(GSE26495)):
		found = False
		for j in range(len(GSE22153)):
			if GSE26495[i][0] == GSE22153[j][0]:
				found = True
				break

		if found == False:
			index += 1
		else:
			for k in range(len(GSE26495[i])):
				f_4.write(GSE26495[i][k])
				if k != len(GSE26495[i]) - 1:
					f_4.write('\t')

	print(index)

	f_1.close()
	f_2.close()
	f_3.close()
	f_4.close()


find_overlap()