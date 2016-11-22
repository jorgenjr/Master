



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


def find_overlap_custom_LM():

	f_1 = open('../../../Master_files/external/GSE22886_new.txt', 'r')
	f_2 = open('../../../Master_files/external/GSE4527_new.txt', 'r')
	f_3 = open('../../../Master_files/external/GSE5099_new.txt', 'r')
	f_4 = open('../../../Master_files/external/GSE22886_overlap.txt', 'w')
	f_5 = open('../../../Master_files/external/GSE4527_overlap.txt', 'w')
	f_6 = open('../../../Master_files/external/GSE5099_overlap.txt', 'w')
	f_7 = open('../../../Master_files/external/GSE26495_PD1lowhigh.txt', 'r')
	f_8 = open('../../../Master_files/external/GSE26495_PD1lowhigh_overlap.txt', 'w')	

	GSE22886 = []
	GSE4527 = []
	GSE5099 = []
	GSE26495 = []
	header = True

	for line in f_1:

		if header == True:
			f_4.write(line)
			header = False
			continue

		temp_array = []
		splitted_line = line.split('\t')
		splitted_line[0] = splitted_line[0].split("\"")[1]

		for i in range(len(splitted_line)):
			temp_array.append(splitted_line[i])

		GSE22886.append(temp_array)

	header = True

	for line in f_2:

		if header == True:
			f_5.write(line)
			header = False
			continue

		temp_array = []
		splitted_line = line.split('\t')
		splitted_line[0] = splitted_line[0].split("\"")[1]

		for i in range(len(splitted_line)):
			temp_array.append(splitted_line[i])

		GSE4527.append(temp_array)

	header = True

	for line in f_3:

		if header == True:
			f_6.write(line)
			header = False
			continue

		temp_array = []
		splitted_line = line.split('\t')
		splitted_line[0] = splitted_line[0].split("\"")[1]

		for i in range(len(splitted_line)):
			temp_array.append(splitted_line[i])

		GSE5099.append(temp_array)

	header = True

	for line in f_7:

		if header == True:
			f_8.write(line)
			header = False
			continue

		temp_array = []
		splitted_line = line.split('\t')

		for i in range(len(splitted_line)):
			temp_array.append(splitted_line[i])

		GSE26495.append(temp_array)

	print("*** GSE22886 ***")
	index = 0

	for i in range(len(GSE22886)):
		
		found1 = []
		found2 = []
		found3 = []

		for j in range(len(GSE4527)):
			if GSE22886[i][0] == GSE4527[j][0]:
				found1 = GSE4527[j]
				break

		for j in range(len(GSE5099)):
			if GSE22886[i][0] == GSE5099[j][0]:
				found2 = GSE5099[j]
				break

		for j in range(len(GSE26495)):
			if GSE22886[i][0] == GSE26495[j][0]:
				found3 = GSE26495[j]
				break

		if len(found1) == 0 or len(found2) == 0 or len(found3) == 0:
			index += 1
		else:
			for k in range(len(GSE22886[i])):
				f_4.write(GSE22886[i][k])
				if k != len(GSE22886[i]) - 1:
					f_4.write('\t')
			for k in range(len(GSE4527[i])):
				f_5.write(GSE4527[i][k])
				if k != len(GSE4527[i]) - 1:
					f_5.write('\t')
			for k in range(len(GSE5099[i])):
				f_6.write(GSE5099[i][k])
				if k != len(GSE5099[i]) - 1:
					f_6.write('\t')
			for k in range(len(GSE26495[i])):
				f_8.write(GSE26495[i][k])
				if k != len(GSE26495[i]) - 1:
					f_8.write('\t')

	print(index)
	
	f_1.close()
	f_2.close()
	f_3.close()
	f_4.close()
	f_5.close()
	f_6.close()
	f_7.close()
	f_8.close()


# find_overlap()
find_overlap_custom_LM()