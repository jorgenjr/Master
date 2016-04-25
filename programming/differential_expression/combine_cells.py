


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
	

combine()