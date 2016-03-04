
import linecache, numpy as np, sys

np_gene_dictionary = {}


def write_to_file(NP_GENE_DICTIONARY, FILE_NUMBER):

	""" Writes the gene dictionary to file.
	"""

	f1 = open('../../../Master_files/simulation/simulation_' + str(FILE_NUMBER), 'w')

	f1.write("!Sample_title\tJurkat\tIM-9\tRaji\tTHP-1\n");

	for key, value in sorted(NP_GENE_DICTIONARY.items()):

		string = str(key) + "\t" + str(value[0]) + "\t" + str(value[1]) + "\t" + str(value[2]) + "\t" + str(value[3]) + "\n";
		f1.write(string)


def write_combined_cell_lines(NP_GENE_DICTIONARY, FILENAME):

	""" Write the gene dictionary with only data from cell lines combined to file.
	"""

	f1 = open('../../../Master_files/simulation/' + FILENAME, 'w')
	
	f1.write("!Sample_title\tJurkat\tIM-9\tRaji\tTHP-1\n");
	gene_array = []

	for key, value in sorted(NP_GENE_DICTIONARY.items()):
		gene_array.append([key, value[0], value[1], value[2], value[3]])

	gene_array.sort()

	for i in range(len(gene_array)):
		f1.write(gene_array[i][0]+"\t"+str(gene_array[i][1])+"\t"+str(gene_array[i][2])+"\t"+str(gene_array[i][3])+"\t"+str(gene_array[i][4])+"\n")

	f1.close()


def write_separate_cell_lines(NP_GENE_DICTIONARY):

	""" Writes the gene dictionary to file.
	"""

	f1 = open('../../../Master_files/simulation/separate_cell_lines', 'w')

	f1.write("!Sample_title\tJurkat\tJurkat\tJurkat\tIM-9\tIM-9\tIM-9\tRaji\tRaji\tRaji\tTHP-1\tTHP-1\tTHP-1\n");

	for key, value in sorted(NP_GENE_DICTIONARY.items()):

		string = str(key) + "\t" + str(value[0]) + "\t" + str(value[1]) + "\t" + str(value[2]) + "\t" + str(value[3]) + "\t" + str(value[4]) + "\t" + str(value[5]) + "\t" + str(value[6]) + "\t" + str(value[7]) + "\t" + str(value[8]) + "\t" + str(value[9]) + "\t" + str(value[10]) + "\t" + str(value[11]) + "\n";
		f1.write(string)


def write_separate_mixtures(NP_GENE_DICTIONARY, MIX):

	""" Writes the gene dictionary to file.
	"""

	f1 = open('../../../Master_files/simulation/separate_mixtures_' + MIX, 'w')

	f1.write("!Sample_title\tMix " + MIX + "\tMix " + MIX + "\tMix " + MIX + "\n");

	for key, value in sorted(NP_GENE_DICTIONARY.items()):

		string = str(key) + "\t" + str(value[0]) + "\t" + str(value[1]) + "\t" + str(value[2]) + "\n";
		f1.write(string)


def write_combined_mixtures(NP_GENE_DICTIONARY, FILENAME, MIX):

	""" Writes the gene dictionary to file.
	"""

	f1 = open('../../../Master_files/simulation/' + FILENAME + MIX, 'w')

	f1.write("!Sample_title\tMix " + MIX + "\n");
	gene_array = []

	for key, value in sorted(NP_GENE_DICTIONARY.items()):
		gene_array.append([key, (value[0] + value[1] + value[2]) / 3.0])

	gene_array.sort()

	for i in range(len(gene_array)):
		f1.write(gene_array[i][0]+"\t"+str(gene_array[i][1])+"\n")


def write_separate_cell_lines_tumor(NP_GENE_DICTIONARY, FILENAME):

	""" Write the gene dictionary with only data from cell lines combined to file.
	"""

	f1 = open('../../../Master_files/simulation/' + FILENAME, 'w')
	
	f1.write("!Sample_title\tJurkat\tJurkat\tJurkat\tIM-9\tIM-9\tIM-9\tRaji\tRaji\tRaji\tTHP-1\tTHP-1\tTHP-1\tTumor\tTumor\n");
	gene_array = []

	for key, value in sorted(NP_GENE_DICTIONARY.items()):
		gene_array.append([key, value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], value[9], value[10], value[11], value[12], value[13]])

	gene_array.sort()

	for i in range(len(gene_array)):
		f1.write(gene_array[i][0]+"\t"+str(gene_array[i][1])+"\t"+str(gene_array[i][2])+"\t"+str(gene_array[i][3])+"\t"+str(gene_array[i][4])+"\t"+str(gene_array[i][5])+"\t"+str(gene_array[i][6])+"\t"+str(gene_array[i][7])+"\t"+str(gene_array[i][8])+"\t"+str(gene_array[i][9])+"\t"+str(gene_array[i][10])+"\t"+str(gene_array[i][11])+"\t"+str(gene_array[i][12])+"\t"+str(gene_array[i][13])+"\t"+str(gene_array[i][14])+"\n")

	f1.close()


def write_combined_mixtures_tumor(NP_GENE_DICTIONARY, FILENAME, TUMOR_CONTENT):

	""" Write the gene dictionary with only data from cell lines combined to file.
	"""

	f1 = open('../../../Master_files/simulation/' + FILENAME + str(TUMOR_CONTENT), 'w')
	
	f1.write("!Sample_title\tMIX A ("+str(100-TUMOR_CONTENT)+"%)\tMIX B ("+str(100-TUMOR_CONTENT)+"%)\tMIX C ("+str(100-TUMOR_CONTENT)+"%)\tMIX D ("+str(100-TUMOR_CONTENT)+"%)\tTUMOR ("+str(TUMOR_CONTENT)+"%)\n");
	gene_array = []

	for key, value in sorted(NP_GENE_DICTIONARY.items()):
		gene_array.append([key, value[0], value[1], value[2], value[3], value[4]])

	gene_array.sort()

	for i in range(len(gene_array)):
		f1.write(gene_array[i][0]+"\t"+str(gene_array[i][1])+"\t"+str(gene_array[i][2])+"\t"+str(gene_array[i][3])+"\t"+str(gene_array[i][4])+"\t"+str(gene_array[i][5])+"\n")

	f1.close()