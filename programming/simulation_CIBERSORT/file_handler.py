
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


def write_to_file(NP_GENE_DICTIONARY, FILE_NUMBER):

	""" Writes the gene dictionary to file.
	"""

	f1 = open('../../../Master_files/simulation/simulation_' + str(FILE_NUMBER), 'w')

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


def write_separate_mixtures(NP_GENE_DICTIONARY, MIX):

	""" Writes the gene dictionary to file.
	"""

	f1 = open('../../../Master_files/simulation/separate_mixtures_' + MIX, 'w')

	f1.write("!Sample_title\tMix " + MIX + "\tMix " + MIX + "\tMix " + MIX + "\n");

	for key, value in NP_GENE_DICTIONARY.items():

		string = str(key) + "\t" + str(value[0]) + "\t" + str(value[1]) + "\t" + str(value[2]) + "\n";
		f1.write(string)


def write_combined_mixtures(NP_GENE_DICTIONARY, MIX):

	""" Writes the gene dictionary to file.
	"""

	f1 = open('../../../Master_files/simulation/combined_mixtures_' + MIX, 'w')

	f1.write("!Sample_title\tMix " + MIX + "\n");

	for key, value in NP_GENE_DICTIONARY.items():

		string = str(key) + "\t" + str(value[0]) + "\n";
		f1.write(string)