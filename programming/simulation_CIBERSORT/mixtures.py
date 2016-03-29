
import numpy as np, linecache

def combine_cell_line(INPUT, GENE_DICTIONARY):

	""" Reads the GSE11103_series_matrix.txt and gathers the cell lines containing:
	- Jurkat
	- IM-9
	- Raji
	- THP-1

	It then calculates the average of each cell and stores it in a dictionary
	"""

	header = True
	f = open('../../../Master_files/external/' + INPUT, 'r')

	for line in f:

		if header == True:
			header = False
			continue

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


def separate_mixtures(INPUT, GENE_DICTIONARY, MIX):

	""" Reads the GSE11103_series_matrix.txt and gathers the mixtures:
	- Mix A
	- Mix B
	- Mix C
	- Mix D

	It then calculates the average of each cell and stores it in a dictionary
	"""

	M1 = 0; M2 = 0; M3 = 0

	if (MIX == 'A'):
		M1 = 30; M2 = 31; M3 = 32
	elif (MIX == 'B'):
		M1 = 33; M2 = 34; M3 = 35
	elif (MIX == 'C'):
		M1 = 36; M2 = 37; M3 = 38
	elif (MIX == 'D'):
		M1 = 39; M2 = 40; M3 = 41

	header = True
	f = open('../../../Master_files/external/' + INPUT, 'r')

	for line in f:

		if header == True:
			header = False
			continue

		line_list = np.array(line.split('\t'))

		# GENES: Column index 0
		gene_ref = line_list[0].split('"')[1]

		GENE_DICTIONARY[gene_ref] = np.array([line_list[M1], line_list[M2], line_list[M3]])

	return GENE_DICTIONARY


def all_separate_mixtures(INPUT_FILE, GENE_DICTIONARY, INPUT):

	""" Reads the GSE11103_series_matrix.txt and gathers the mixtures:
	- Mix A
	- Mix B
	- Mix C
	- Mix D

	It then calculates the average of each cell and stores it in a dictionary
	"""

	header = True
	f = open('../../../Master_files/external/' + INPUT_FILE, 'r')

	for line in f:

		if header == True:
			header = False
			continue
		
		line_list = np.array(line.split('\t'))

		# GENES: Column index 0
		gene_ref = line_list[0].replace("\"", "")#split('"')[1]
		# print("'" + gene_ref + "'")
		values = []

		for i in range(INPUT[1], INPUT[2]+1):
			values.append(float(line_list[i]))

		if gene_ref in GENE_DICTIONARY:
			GENE_DICTIONARY[gene_ref] = np.array([GENE_DICTIONARY[gene_ref], values])
		else:
			GENE_DICTIONARY[gene_ref] = np.array(values)
	# print(len(GENE_DICTIONARY))
	return GENE_DICTIONARY


def combined_mixtures(INPUT, GENE_DICTIONARY, MIX):

	""" Reads the GSE11103_series_matrix.txt and gathers the mixtures:
	- Mix A
	- Mix B
	- Mix C
	- Mix D

	It then calculates the average of each cell and stores it in a dictionary
	"""

	M1 = 0; M2 = 0; M3 = 0

	if (MIX == 'A'):
		M1 = 30; M2 = 31; M3 = 32
	elif (MIX == 'B'):
		M1 = 33; M2 = 34; M3 = 35
	elif (MIX == 'C'):
		M1 = 36; M2 = 37; M3 = 38
	elif (MIX == 'D'):
		M1 = 39; M2 = 40; M3 = 41

	header = True
	f = open('../../../Master_files/external/' + INPUT, 'r')

	for line in f:

		if header == True:
			header = False
			continue

		line_list = np.array(line.split('\t'))

		# GENES: Column index 0
		gene_ref = line_list[0].split('"')[1]
		gene_value = (float(line_list[M1]) + float(line_list[M2]) + float(line_list[M3])) / 3.0

		GENE_DICTIONARY[gene_ref] = np.array([gene_value])

	return GENE_DICTIONARY


def separate_cell_line(INPUT_FILE, GENE_DICTIONARY, INPUT):

	""" Reads the GSE11103_series_matrix.txt and gathers the cell lines containing:
	- Jurkat
	- IM-9
	- Raji
	- THP-1
	"""

	header = True
	f = open('../../../Master_files/external/' + INPUT_FILE, 'r')

	for line in f:

		if header == True:
			header = False
			continue

		line_list = np.array(line.split('\t'))

		# GENES: Column index 0
		gene_ref = line_list[0].split('"')[1]
		values = []

		for i in range(INPUT[1], INPUT[2]+1):
			values.append(float(line_list[i]))

		if gene_ref in GENE_DICTIONARY:
			GENE_DICTIONARY[gene_ref] = np.array([GENE_DICTIONARY[gene_ref], values])
		else:
			GENE_DICTIONARY[gene_ref] = np.array(values)

	return GENE_DICTIONARY


def combine_tumor(INPUT1, INPUT2, GENE_DICTIONARY):

	""" Reads the GSE10650 files (GSM269529.txt and GSM269530.txt) and gathers tumors cells.
	It then calculates the average and appends the gene values to the gene dictionary containing
	gene values for the cell lines (Jurkat, IM-9, Raji, THP-1).
	"""

	tumor_dictionary = {}
	header = True
	f1 = open('../../../Master_files/external/' + INPUT1, 'r')
	f2 = open('../../../Master_files/external/' + INPUT2, 'r')

	for line in f1:

		if header == True:
			header = False
			continue

		line_list = np.array(line.split('\t'))
		tumor_dictionary[line_list[0]] = np.array(float(line_list[1]))

	header = True

	for line in f2:

		if header == True:
			header = False
			continue

		line_list = np.array(line.split('\t'))
		
		if line_list[0] in tumor_dictionary:
			tumor_dictionary[line_list[0]] = np.array((tumor_dictionary[line_list[0]] + float(line_list[1])) / 2.0)
		else:
			tumor_dictionary[line_list[0]] = np.array(float(line_list[1]))

	for key, value in sorted(tumor_dictionary.items()):

		if key in GENE_DICTIONARY:
			GENE_DICTIONARY[key] = np.append(GENE_DICTIONARY[key], tumor_dictionary[key])

	return GENE_DICTIONARY


def separate_tumor(INPUT_FILE, TUMOR_DICTIONARY, INPUT):

	""" Reads the GSE10650 files (GSM269529.txt and GSM269530.txt) and gathers tumors cells.
	It then calculates the average and appends the gene values to the gene dictionary containing
	gene values for the cell lines (Jurkat, IM-9, Raji, THP-1).
	"""

	header = True
	f = open('../../../Master_files/external/' + INPUT_FILE)

	for line in f:

		if header == True:
			header = False
			continue
		
		line_list = np.array(line.split('\t'))
		values = []

		for i in range(INPUT[1], INPUT[2]+1):
			values.append(float(line_list[i]))
		
		if line_list[0] in TUMOR_DICTIONARY:
			TUMOR_DICTIONARY[line_list[0]] = np.array([TUMOR_DICTIONARY[line_list[0]], values])
		else:
			TUMOR_DICTIONARY[line_list[0]] = np.array(values)

	return TUMOR_DICTIONARY


def from_dictionary_to_matrix(GENE_DICTIONARY):

	""" Convert the dictionary containing genes to a matrix
	"""

	value_length = 0

	for key, value in GENE_DICTIONARY.items():

		value_length = len(value)
		break;
	
	np_matrix_combined = np.zeros(shape=(len(GENE_DICTIONARY), value_length))
	insert = 0

	for key, value in sorted(GENE_DICTIONARY.items()):
		
		value_list = []

		for i in range(len(value)):
			value_list.append(value[i])
		
		np_matrix_combined[insert] = np.array(value_list)
		insert += 1

	return np_matrix_combined


def from_matrix_to_dictionary(COMBINED, GENE_DICTIONARY):

	""" Convert the matrix containing genes to a dictionary
	"""

	index = 0

	for key, value in sorted(GENE_DICTIONARY.items()):
		
		GENE_DICTIONARY[key] = COMBINED[index]
		index += 1

	return GENE_DICTIONARY