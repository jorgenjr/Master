
import numpy as np
import linecache
import quantile_normalisation
import file_handler
import sys
import config


def all_separate_mixtures(INPUT_FILE, GENE_DICTIONARY, INPUT, header = True):

	""" Reads a mixture file and gathers the mixtures in a dictionary
	"""

	f = open(config.PATH_EXTERNAL + INPUT_FILE, 'r')

	for line in f:

		if header:
			header = False
			continue
		
		line_list = np.array(line.split('\t'))
		gene_ref = line_list[0].replace("\"", "")
		values = []

		for i in range(len(INPUT)):

			index = INPUT[i][1]

			for j in range(INPUT[i][2]):
				values.append(line_list[index+j])

		if gene_ref in GENE_DICTIONARY:
			GENE_DICTIONARY[gene_ref] = np.append(GENE_DICTIONARY[gene_ref], values)
		else:
			GENE_DICTIONARY[gene_ref] = np.array(values)

	return GENE_DICTIONARY


def separate_for_normalization(SEPARATE_VALUES_MATRIX, CELL_LINES_MATRIX, INPUT, TUMOR_PRESENT, TUMOR_INPUT):

	""" Add each cell line (and its replicates) to a separately matrix.
	1. Loop 1: Iterate through every gene.
	2. Loop 2 & 3: For each line (a specific gene): iterate over the number of cell lines all together from all the files. E.g. 4 cell lines from GSE11103 and 2 cell lines from GSE26495 means a total of 6 iteration all together for loop 2 & 3.
	3. Loop 4: Gather the replicates of a specific cell line and add it to its matrix.
	4. If tumor is present, then it will all be added to one matrix.
	"""

	for line in range(len(SEPARATE_VALUES_MATRIX)):
		
		cell_line = 0
		previous_i = 0

		for cell_file in range(len(INPUT)):
			for i in range(len(INPUT[cell_file])):
				
				list_of_one_cell_line = []
				replicate_range = cell_line + INPUT[cell_file][i][2]
				
				for j in range(cell_line, replicate_range):
					list_of_one_cell_line.append(SEPARATE_VALUES_MATRIX[line][cell_line])
					cell_line += 1

				CELL_LINES_MATRIX[previous_i+i].append(list_of_one_cell_line)

			previous_i += len(INPUT[cell_file])		

		if TUMOR_PRESENT == True:

			list_of_tumor_lines = []

			for cell_file in range(len(TUMOR_INPUT)):
				for i in range(len(TUMOR_INPUT[cell_file])):

					replicate_range = cell_line + TUMOR_INPUT[cell_file][i][2]

					for j in range(cell_line, replicate_range):
						list_of_tumor_lines.append(SEPARATE_VALUES_MATRIX[line][cell_line])
						cell_line += 1

			CELL_LINES_MATRIX[previous_i+i].append(list_of_tumor_lines)

	return CELL_LINES_MATRIX


def get_relevant_information(NP_GENE_DICTIONARY, TUMOR_PRESENT, FILES, FILES_INPUT, TUMORS, TUMORS_INPUT):

	""" Iterate through all the input files and every relevant information in that file.
	"""

	for i in range(len(FILES)):
		NP_GENE_DICTIONARY = all_separate_mixtures(FILES[i], NP_GENE_DICTIONARY, FILES_INPUT[i])

	if TUMOR_PRESENT == True:
		for i in range(len(TUMORS)):
			NP_GENE_DICTIONARY = all_separate_mixtures(TUMORS[i], NP_GENE_DICTIONARY, TUMORS_INPUT[i])

	return NP_GENE_DICTIONARY


def get_separated_for_normalization(SEPARATE_VALUES_MATRIX, TUMOR_PRESENT, FILES_INPUT, TUMORS_INPUT):

	""" For quantile normalization, each unique mixture/cell line must be normalized separately. Need first to initialize a matrix for each mixture/cell line.
	"""

	cell_lines_matrix = []

	for i in range(len(FILES_INPUT)):
		for j in range(len(FILES_INPUT[i])):
			cell_lines_matrix.append([])
	
	if TUMOR_PRESENT == True:
		cell_lines_matrix.append([])

	if TUMOR_PRESENT == True:
		cell_lines_matrix = separate_for_normalization(SEPARATE_VALUES_MATRIX, cell_lines_matrix, FILES_INPUT, TUMOR_PRESENT, TUMORS_INPUT)
	else:
		cell_lines_matrix = separate_for_normalization(SEPARATE_VALUES_MATRIX, cell_lines_matrix, FILES_INPUT, TUMOR_PRESENT, None)

	return cell_lines_matrix


def combine_separated_normalized_data(CELL_LINES_MATRIX, SEPARATE_VALUES_MATRIX):

	""" Gather all the normalized gene values (from each mixture/cell line) back together to a matrix containing everyone.
	Each mixture/cell line is combined by calculated the average score.

	Quantile normalize the whole matrix before return.
	"""

	all_cell_lines_combined = np.zeros(shape=(len(CELL_LINES_MATRIX[0]), len(CELL_LINES_MATRIX)))
	
	for i in range(len(SEPARATE_VALUES_MATRIX)):
		for cell_line in range(len(CELL_LINES_MATRIX)):

			avg = 0.0

			for replicate in range(len(CELL_LINES_MATRIX[cell_line][i])):
				avg += CELL_LINES_MATRIX[cell_line][i][replicate]

			all_cell_lines_combined[i][cell_line] = avg / float(len(CELL_LINES_MATRIX[cell_line][i]))

	return quantile_normalisation.algo(all_cell_lines_combined)


def gather_separated_normalized_data(SEPARATE_VALUES_MATRIX, CELL_LINES_MATRIX):

	""" Gather all the normalized gene values (from each cell line) back together to a matrix containing everyone.
	"""

	for i in range(len(SEPARATE_VALUES_MATRIX)):

		all_cell_lines = []

		for cell_line in range(len(CELL_LINES_MATRIX)):
			for replicate in range(len(CELL_LINES_MATRIX[cell_line][i])):
				all_cell_lines.append(CELL_LINES_MATRIX[cell_line][i][replicate])

		SEPARATE_VALUES_MATRIX[i] = all_cell_lines

	return SEPARATE_VALUES_MATRIX


def save_separate_matrix(NP_GENE_DICTIONARY, SEPARATE_VALUES_MATRIX, TUMOR_PRESENT, FILENAME, FILENAME_TUMOR, FILES_INPUT, TUMORS_INPUT):

	""" Save the matrix of separated values to file.
	"""

	# mixtures.save_separate_matrix(np_gene_dictionary, separate_values_matrix, tumor_present, config.REFERENCE, config.REFERENCE_TUMOR, CELL_LINES_INPUT, TUMORS_INPUT)
	NP_GENE_DICTIONARY = from_matrix_to_dictionary(SEPARATE_VALUES_MATRIX, NP_GENE_DICTIONARY)
	
	if TUMOR_PRESENT == False:
		file_handler.write_separate_cell_lines(NP_GENE_DICTIONARY, FILENAME, FILES_INPUT, [])
	else:
		file_handler.write_separate_cell_lines(NP_GENE_DICTIONARY, FILENAME_TUMOR, FILES_INPUT, TUMORS_INPUT)


def save_combined_matrix(NP_GENE_DICTIONARY, COMBINED_VALUES_MATRIX, TUMOR_PRESENT, FILENAME, FILENAME_TUMOR, FILES_INPUT, TUMORS_INPUT):

	""" Save the matrix of combined values to file.
	"""

	NP_GENE_DICTIONARY = from_matrix_to_dictionary(COMBINED_VALUES_MATRIX, NP_GENE_DICTIONARY)
	
	if TUMOR_PRESENT == False:
		file_handler.write_combined_cell_lines(NP_GENE_DICTIONARY, FILENAME, FILES_INPUT, [])
	else:
		file_handler.write_combined_cell_lines(NP_GENE_DICTIONARY, FILENAME_TUMOR, FILES_INPUT, TUMORS_INPUT)


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