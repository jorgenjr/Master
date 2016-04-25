
import numpy as np, linecache


def all_separate_mixtures(INPUT_FILE, GENE_DICTIONARY, INPUT):

	""" Reads the GSE11103_series_matrix.txt and gathers the mixtures: IN USE!
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
			GENE_DICTIONARY[gene_ref] = np.append(GENE_DICTIONARY[gene_ref], values)
		else:
			GENE_DICTIONARY[gene_ref] = np.array(values)
	# print(len(GENE_DICTIONARY))
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


def separate_for_normalization(separate_values_matrix, cell_lines_matrix, INPUT, tumor_present, TUMOR_INPUT):

	""" Add each cell line (and its replicates) to a separately matrix.
	1. Loop 1: Iterate through every gene.
	2. Loop 2 & 3: For each line (a specific gene): iterate over the number of cell lines all together from all the files. E.g. 4 cell lines from GSE11103 and 2 cell lines from GSE26495 means a total of 6 iteration all together for loop 2 & 3.
	3. Loop 4: Gather the replicates of a specific cell line and add it to its matrix.
	4. If tumor is present, then it will all be added to one matrix.
	"""
	
	for line in range(len(separate_values_matrix)):
		
		cell_line = 0
		previous_i = 0

		for cell_file in range(len(INPUT)):

			for i in range(INPUT[cell_file][0]):
				
				list_of_one_cell_line = []
				
				for j in range(INPUT[cell_file][3]):
					
					list_of_one_cell_line.append(separate_values_matrix[line][cell_line])
					cell_line += 1

				cell_lines_matrix[previous_i+i].append(list_of_one_cell_line)

			previous_i += INPUT[cell_file][0]

		if tumor_present == True:

			list_of_tumor_lines = []

			for cell_file in range(len(TUMOR_INPUT)):

				for i in range(TUMOR_INPUT[cell_file][0]):

					for j in range(TUMOR_INPUT[cell_file][3]):

						list_of_tumor_lines.append(separate_values_matrix[line][cell_line])
						cell_line += 1

			cell_lines_matrix[previous_i+i].append(list_of_tumor_lines)

	return cell_lines_matrix


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