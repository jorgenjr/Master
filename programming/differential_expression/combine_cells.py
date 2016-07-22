


def combine():

	f = open('../../../Master_files/external/GSE26495.txt', 'r')

	all_cells = []
	t_cells = []
	combined = []
	header = True
	index = 0

	for line in f:

		if header == True:
			header = False
			continue

		all_cells.append(line.split('\t'))

	f.close()
	
	for i in range(len(all_cells)):

		liste = [all_cells[i][0].replace("\"", ""), all_cells[i][5], all_cells[i][6], all_cells[i][7], all_cells[i][8], all_cells[i][9], all_cells[i][10], all_cells[i][11], all_cells[i][12], all_cells[i][13], all_cells[i][14], all_cells[i][15], all_cells[i][16][:-1]]
		t_cells.append(liste)

	for i in range(len(t_cells)):

		t_high = (float(t_cells[i][1]) + float(t_cells[i][2]) + float(t_cells[i][3]) + float(t_cells[i][4]) + float(t_cells[i][5]) + float(t_cells[i][6])) / 6.0
		t_low = (float(t_cells[i][7]) + float(t_cells[i][8]) + float(t_cells[i][9]) + float(t_cells[i][10]) + float(t_cells[i][11]) + float(t_cells[i][12])) / 6.0
		combined.append([t_cells[i][0], t_high, t_low])

	f = open('../../../Master_files/diff_exp/combined_t-high_t-low', 'w')
	f.write("Genes\tT high\tT low\n")

	for i in range(len(combined)):

		f.write(combined[i][0] + "\t" + str(combined[i][1]) + "\t" + str(combined[i][2]) + "\n")

	f.close()

	f = open('../../../Master_files/diff_exp/separate_t-high_t-low', 'w')
	f.write("Genes\thigh1\thigh2\thigh3\thigh4\thigh5\thigh6\tlow1\tlow2\tlow3\tlow4\tlow5\tlow6\n")

	for i in range(len(combined)):

		f.write(t_cells[i][0] + "\t" + t_cells[i][1] + "\t" + t_cells[i][2] + "\t" + t_cells[i][3] + "\t" + t_cells[i][4] + "\t" + t_cells[i][5] + "\t" + t_cells[i][6] + "\t" + t_cells[i][7] + "\t" + t_cells[i][8] + "\t" + t_cells[i][9] + "\t" + t_cells[i][10] + "\t" + t_cells[i][11] + "\t" + t_cells[i][12] + "\n")

	f.close()


def GSE11103():

	f = open('../../../Master_files/external/GSE11103.txt', 'r')

	all_cells = []
	t_cells = []
	combined = []
	header = True
	index = 0

	for line in f:

		if header == True:
			header = False
			continue

		all_cells.append(line.split('\t'))

	f.close()
	
	for i in range(len(all_cells)):

		liste = [all_cells[i][0].replace("\"", ""), all_cells[i][18], all_cells[i][19], all_cells[i][20], all_cells[i][24], all_cells[i][25], all_cells[i][26]]
		t_cells.append(liste)

	f = open('../../../Master_files/diff_exp/separate_Jurkat_Raji', 'w')
	f.write("Genes\tJurkat1\tJurkat2\tJurkat3\tRaji1\tRaji2\tRaji3\n")

	for i in range(len(t_cells)):

		f.write(t_cells[i][0] + "\t" + t_cells[i][1] + "\t" + t_cells[i][2] + "\t" + t_cells[i][3] + "\t" + t_cells[i][4] + "\t" + t_cells[i][5] + "\t" + t_cells[i][6] + "\n")

	f.close()


def GSE26495():

	f = open('../../../Master_files/external/GSE26495.txt', 'r')

	all_cells = []
	t_cells = []
	combined = []
	header = True
	index = 0

	for line in f:

		if header == True:
			header = False
			continue

		all_cells.append(line.split('\t'))

	f.close()
	
	for i in range(len(all_cells)):

		liste = [all_cells[i][0].replace("\"", ""), all_cells[i][1], all_cells[i][2], all_cells[i][3], all_cells[i][4], all_cells[i][5], all_cells[i][6], all_cells[i][7], all_cells[i][8], all_cells[i][9], all_cells[i][10], all_cells[i][11], all_cells[i][12], all_cells[i][13], all_cells[i][14], all_cells[i][15], all_cells[i][16][:-1]]
		t_cells.append(liste)

	for i in range(len(t_cells)):

		naive = (float(t_cells[i][1]) + float(t_cells[i][2]) + float(t_cells[i][3]) + float(t_cells[i][4])) / 4.0
		t_high = (float(t_cells[i][5]) + float(t_cells[i][6]) + float(t_cells[i][7]) + float(t_cells[i][8]) + float(t_cells[i][9]) + float(t_cells[i][10])) / 6.0
		t_low = (float(t_cells[i][11]) + float(t_cells[i][12]) + float(t_cells[i][13]) + float(t_cells[i][14]) + float(t_cells[i][15]) + float(t_cells[i][16])) / 6.0
		combined.append([t_cells[i][0], naive, t_high, t_low])

	f = open('../../../Master_files/simulation/combined_gse26495', 'w')
	f.write("Genes\tNaive\tT high\tT low\n")

	for i in range(len(combined)):

		f.write(combined[i][0] + "\t" + str(combined[i][1]) + "\t" + str(combined[i][2]) + "\t" + str(combined[i][2]) + "\n")

	f.close()

	# f = open('../../../Master_files/diff_exp/separate_t-high_t-low', 'w')
	# f.write("Genes\thigh1\thigh2\thigh3\thigh4\thigh5\thigh6\tlow1\tlow2\tlow3\tlow4\tlow5\tlow6\n")

	# for i in range(len(combined)):

	# 	f.write(t_cells[i][0] + "\t" + t_cells[i][1] + "\t" + t_cells[i][2] + "\t" + t_cells[i][3] + "\t" + t_cells[i][4] + "\t" + t_cells[i][5] + "\t" + t_cells[i][6] + "\t" + t_cells[i][7] + "\t" + t_cells[i][8] + "\t" + t_cells[i][9] + "\t" + t_cells[i][10] + "\t" + t_cells[i][11] + "\t" + t_cells[i][12] + "\n")

	# f.close()
	

#combine()
#GSE11103()
GSE26495()