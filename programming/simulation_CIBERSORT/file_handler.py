
import linecache, numpy as np, sys

np_gene_dictionary = {}

# Variables for GSE10650

BEGIN1 = 4
END1 = 54679
EOF1 = 54683
FILECOLS1 = 2
GENE = 0
VALUE = 1

# Variables for GSE11103

BEGIN2 = 64
END2 = 54739
EOF2 = 54740
FILECOLS2 = 42

def read_file(START, STOP, INDEX, COLS):

	""" Reads the data from the specific file.
	Format for the dictionary is: { 'gene1' : [value1, value2, ... ], 'gene2' : [ ... ], ... }
	
	If the gene is not already in the dictionary, it will be added with a numpy array as value.
	If the gene already is in the dictionary, the value from the specific file is appended to the numpy array.
	"""

	for x in range(START, STOP):

		line = linecache.getline('../../../Master_files/simulation/' + INPUT[INDEX], x)
		line_list = np.array(line.split('\t'))
		gene_ref = ""

		if COLS == FILECOLS1:
			gene_ref = line_list[GENE]
		elif COLS == FILECOLS2:
			gene_ref = line_list[GENE].split('"')[1]

		for j in range(1, COLS):
			if gene_ref in np_gene_dictionary:
				np_gene_dictionary[gene_ref] = np.append(np_gene_dictionary[gene_ref], np.array(float(line_list[j])))
			else:
				np_gene_dictionary[gene_ref] = np.array(float(line_list[j]))


def read_files(INPUT):

	""" Reads the input files. Splitted up in two parts as GSM and GSE have different formats.
	"""

	for i in range(len(INPUT)):

		if INPUT[i] == 'GSM269529.txt' or INPUT[i] == 'GSM269530.txt':
			read_file(BEGIN1, END1, i, FILECOLS1)
		elif INPUT[i] == 'GSE11103_series_matrix.txt':
			read_file(BEGIN2, END2, i, FILECOLS2)

	print(np_gene_dictionary)


def write_to_file(NP_GENE_DICTIONARY, FILE_NUMBER):

	""" Writes the gene dictionary to file.
	"""

	f1 = open('../../../Master_files/simulation/testfile_' + str(FILE_NUMBER), 'w')

	f1.write("!Sample_title\tJurkat\tIM-9\tRaji\tTHP-1\n");

	for key, value in NP_GENE_DICTIONARY.items():

		string = str(key) + "\t" + str(value[0]) + "\t" + str(value[1]) + "\t" + str(value[2]) + "\t" + str(value[3]) + "\n";
		f1.write(string)


def write_combined_cell_lines(NP_GENE_DICTIONARY):

	""" Write the gene dictionary with only data from cell lines combined to file.
	"""

	f1 = open('../../../Master_files/simulation/combined_matrix', 'w')
	
	f1.write("!Sample_title\tJurkat\tIM-9\tRaji\tTHP-1\n");

	for key, value in NP_GENE_DICTIONARY.items():
		f1.write(key+"\t"+str(value[0])+"\t"+str(value[1])+"\t"+str(value[2])+"\t"+str(value[3])+"\n")

	f1.close()


def write_separate_cell_lines(NP_GENE_DICTIONARY):

	""" Writes the gene dictionary to file.
	"""

	f1 = open('../../../Master_files/simulation/separate_cell_lines', 'w')

	f1.write("!Sample_title\tJurkat\tJurkat\tJurkat\tIM-9\tIM-9\tIM-9\tRaji\tRaji\tRaji\tTHP-1\tTHP-1\tTHP-1\n");

	for key, value in NP_GENE_DICTIONARY.items():

		string = str(key) + "\t" + str(value[0]) + "\t" + str(value[1]) + "\t" + str(value[2]) + "\t" + str(value[3]) + "\t" + str(value[4]) + "\t" + str(value[5]) + "\t" + str(value[6]) + "\t" + str(value[7]) + "\t" + str(value[8]) + "\t" + str(value[9]) + "\t" + str(value[10]) + "\t" + str(value[11]) + "\n";
		f1.write(string)