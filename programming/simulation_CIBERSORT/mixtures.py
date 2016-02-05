
import numpy as np, linecache

def combine_cell_line(BEGIN, END, FILECOLS, INPUT, GENE_DICTIONARY):

	""" Reads the GSE11103_series_matrix.txt and gathers the cell lines containing:
	- Jurkat
	- IM-9
	- Raji
	- THP-1

	It then calculates the average of each cell and stores it in a dictionary
	"""

	for x in range(BEGIN, END):

		line = linecache.getline('../../../Master_files/simulation/' + INPUT, x)
		line_list = np.array(line.split('\t'))

		Jurkat = 0.0
		IM9 = 0.0
		Raji = 0.0
		THP1 = 0.0

		# GENES: Column index 0
		gene_ref = line_list[0].split('"')[1]

		# JURKAT: GSM279589, GSM279590, GSM279591
		for i in range(18, 21):
			Jurkat += float(line_list[i])

		# IM-9: GSM279592, GSM279593, GSM279594
		for i in range(21, 24):
			IM9 += float(line_list[i])

		# RAJI: GSM279595, GSM279596, GSM279597
		for i in range(24, 27):
			Raji += float(line_list[i])

		# THP-1: GSM279598, GSM279599, GSM279600
		for i in range(27, 30):
			THP1 += float(line_list[i])

		GENE_DICTIONARY[gene_ref] = np.array([(Jurkat / 3.0), (IM9 / 3.0), (Raji / 3.0), (THP1 / 3.0)])

	return GENE_DICTIONARY


def combine_tumor(BEGIN, END, FILECOLS, INPUT1, INPUT2, GENE_DICTIONARY):

	""" Reads the GSE10650 files (GSM269529.txt and GSM269530.txt) and gathers tumors cells.
	It then calculates the average and appends the gene values to the gene dictionary containing
	gene values for the cell lines (Jurkat, IM-9, Raji, THP-1).
	"""

	tumor_dictionary = {}

	for x in range(BEGIN, END):

		line = linecache.getline('../../../Master_files/simulation/' + INPUT1, x)
		line_list = np.array(line.split('\t'))
		tumor_dictionary[line_list[0]] = np.array(float(line_list[1]))

	for x in range(BEGIN, END):

		line = linecache.getline('../../../Master_files/simulation/' + INPUT2, x)
		line_list = np.array(line.split('\t'))
		
		if line_list[0] in tumor_dictionary:
			tumor_dictionary[line_list[0]] = np.array((tumor_dictionary[line_list[0]] + float(line_list[1])) / 2.0)
		else:
			tumor_dictionary[line_list[0]] = np.array(float(line_list[1]))

	for key, value in tumor_dictionary.items():

		if key in GENE_DICTIONARY:
			GENE_DICTIONARY[key] = np.append(GENE_DICTIONARY[key], tumor_dictionary[key])

	return GENE_DICTIONARY


def from_dictionary_to_matrix(GENE_DICTIONARY):

	""" Convert the dictionary containing genes to a matrix
	"""

	value_length = 0

	for key, value in GENE_DICTIONARY.items():
		value_length = len(value)
		break;

	np_matrix_combined = np.zeros(shape=(len(GENE_DICTIONARY), value_length))
	insert = 0

	for key, value in GENE_DICTIONARY.items():

		value_list = []

		for i in range(len(value)):
			value_list.append(value[i])
		
		np_matrix_combined[insert] = np.array(value_list)
		#np_matrix_combined[insert] = np.array([value[0], value[1], value[2], value[3], value[4]])
		insert += 1

	return np_matrix_combined


def from_matrix_to_dictionary(COMBINED, GENE_DICTIONARY):

	""" Convert the matrix containing genes to a dictionary
	"""

	index = 0

	for key, value in GENE_DICTIONARY.items():
		
		GENE_DICTIONARY[key] = COMBINED[index]
		index += 1

	return GENE_DICTIONARY