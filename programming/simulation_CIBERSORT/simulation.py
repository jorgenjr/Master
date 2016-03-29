
import readline, sys, numpy as np, quantile_normalisation, noise, file_handler, mixtures, tumor, copy, argparse

FLAGS = []
MIXTURES = []
MIXTURES_INPUT = []
TUMORS = []
TUMORS_INPUT = []
CELL_LINES = []
CELL_LINES_INPUT = []
ITERATION = []
OUTPUT = "../../../Master_files/simulation/"

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--MIXTURES", help="Mixtures", nargs='*')
parser.add_argument("-t", "--TUMORS", help="Tumors", nargs='*')
parser.add_argument("-c", "--CELL_LINES", help="Cell lines", nargs='*')
parser.add_argument("-r", "--REFERENCE", help="Reference", nargs='*')
parser.add_argument("-o", "--OUTPUT", help="Output")
parser.add_argument("-i", "--ITERATION", help="Iteration", nargs='*')

args = parser.parse_args()

print(args.MIXTURES)
print(args.TUMORS)
print(args.CELL_LINES)
print(args.REFERENCE)
print(args.OUTPUT)
print(args.ITERATION)


# def read_args():

# 	""" Reading the arguments sent by the user from the terminal.
# 	-c flag must be followed by cell line file(s)
# 	-m flag must be followed by mixture file(s)
# 	-r flag must be followed by reference file(s)
# 	-t flag must be followed by tumor file(s)

# 	The given files must be placed outside the "Master" folder:
# 	Code: folder_name/Master/programming/simulation_CIBERSORT/simulation.py
# 	Files: folder_name/Master_files/external/

# 	E.g.: python simulation.py -t GSM269529.txt GSM269530.txt -m GSE11103.txt
# 	"""

# 	if len(sys.argv) == 1:
# 		print('\n[ERROR] Wrong sys.argv format! Too few arguments. Run:\n\npython simulation.py -i [input.file input.file ...] -o [output.file output.file]\n')
# 		sys.exit()

# 	m = False; t = False; c = False; i = False; o = False;

# 	for x in range(1, len(sys.argv)):
		
# 		# CELL LINE
# 		if sys.argv[x] == '-c':
# 			FLAGS.append("C")
# 			m = False; t = False; c = True; i = False; o = False;
# 			continue
# 		# MIXTURE
# 		elif sys.argv[x] == '-m':
# 			FLAGS.append("M")
# 			m = True; t = False; c = False; i = False; o = False;
# 			continue
# 		# SIGNATURE
# 		elif sys.argv[x] == '-r':
# 			FLAGS.append("R")
# 		# TUMOR
# 		elif sys.argv[x] == '-t':
# 			FLAGS.append("T")
# 			m = False; t = True; c = False; i = False; o = False;
# 			continue
# 		# ITERATION
# 		elif sys.argv[x] == '-i':
# 			FLAGS.append("I")
# 			m = False; t = False; c = False; i = True; o = False;
# 			continue

# 		elif sys.argv[x] == '-o':
# 			FLAGS.append("O")
# 			m = False; t = False; c = False; i = True; o = True;
# 			continue

# 		if m == True:
# 			MIXTURES.append(sys.argv[x])
# 			continue

# 		elif t == True:
# 			TUMORS.append(sys.argv[x])
# 			continue

# 		elif c == True:
# 			CELL_LINES.append(sys.argv[x])
# 			continue

# 		elif i == True:
# 			ITERATION.append(int(sys.argv[x]))
# 			continue

# 		elif o == True:
# 			global OUTPUT
# 			OUTPUT = sys.argv[x]
# 			continue
			
# 		print('\n[ERROR] Wrong sys.argv format! E.g. run:\n\npython simulation.py -t [tumor.file tumor.file ...] -m [mixture.file mixture.file]\n')
# 		sys.exit()


def read_stdin():

	""" Reads in from keyboard. This is needed to know which part of the input files that are
	supposed to be read by the program.
	"""

	print("")

	if args.MIXTURES != None and len(args.MIXTURES) > 0:

		print("*** MIXTURES ***")

		for i in range(len(args.MIXTURES)):

			no_mixtures = int(input("How many distinct mixtures in " + args.MIXTURES[i] + "? "))
			start = int(input("From which column does the first mixture begin (0 is first column)? "))
			stop = int(input("To which column does the last mixture end? "))
			replicates = int(input("Number of replicates per mixture (type 1 if only one mixture)? "))
			
			MIXTURES_INPUT.append([no_mixtures, start, stop, replicates])

	print("")

	if args.TUMORS != None and len(args.TUMORS) > 0:

		print("*** TUMORS ***")

		for i in range(len(args.TUMORS)):

			no_tumors = int(input("How many tumor cell lines in " + args.TUMORS[i] + "? "))
			start = int(input("From which column does the first tumor cell line begin (0 is first column)? "))
			stop = int(input("To which column does the last tumor cell line end? "))
			replicates = int(input("Number of replicates per tumor cell line (type 1 if only one cell line)? "))
			
			TUMORS_INPUT.append([no_tumors, start, stop, replicates])

	print("")

	if args.CELL_LINES != None and len(args.CELL_LINES) > 0:

		print("*** CELL LINES ***")

		for i in range(len(args.CELL_LINES)):

			no_cell_lines = int(input("How many cell lines in " + args.CELL_LINES[i] + "? "))
			start = int(input("From which column does the first cell line begin (0 is first column)? "))
			stop = int(input("To which column does the last cell line end? "))
			replicates = int(input("Number of replicates per cell line (type 1 if only one cell line)? "))
			
			CELL_LINES_INPUT.append([no_cell_lines, start, stop, replicates])

	print("")


def execute():

	""" This is the function that initiates the whole simulation. There are different possibilities
	for simulation:

	1. Generate a reference file (used for signature matrix in CIBERSORT) using immune cell lines
		and tumor cell lines.
	2. Generate a simulation file with spiked in tumor. This should be generated by using mixture
		files and tumor files.
	3. ???
	"""

	np_gene_dictionary = {}

	if args.CELL_LINES != None and len(args.CELL_LINES) > 0:

		if args.REFERENCE != None and len(args.REFERENCE) > 0:

			# TODO: FIX THIS
			np_gene_dictionary = mixtures.separate_cell_line(args.CELL_LINES[0], np_gene_dictionary, CELL_LINES_INPUT[0])
			# IF TUMOR
			#np_gene_dictionary_tumor = mixtures.separate_tumor(args.TUMORS[0], args.TUMORS[1], np_gene_dictionary)
			# IF TUMOR
			#separate_values_matrix = mixtures.from_dictionary_to_matrix(np_gene_dictionary_tumor)
			# IF NOT TUMOR
			separate_values_matrix = mixtures.from_dictionary_to_matrix(np_gene_dictionary)

			Jurkat = []; IM9 = []; Raji = []; THP1 = [];# tumor_list = [];
			
			for i in range(len(separate_values_matrix)):
				
				Jurkat.append([separate_values_matrix[i][0], separate_values_matrix[i][1], separate_values_matrix[i][2]])
				IM9.append([separate_values_matrix[i][3], separate_values_matrix[i][4], separate_values_matrix[i][5]])
				Raji.append([separate_values_matrix[i][6], separate_values_matrix[i][7], separate_values_matrix[i][8]])
				THP1.append([separate_values_matrix[i][9], separate_values_matrix[i][10], separate_values_matrix[i][11]])
				#tumor_list.append([separate_values_matrix[i][12], separate_values_matrix[i][13]])

			Jurkat_normalized = quantile_normalisation.algo(Jurkat)
			IM9_normalized = quantile_normalisation.algo(IM9)
			Raji_normalized = quantile_normalisation.algo(Raji)
			THP1_normalized = quantile_normalisation.algo(THP1)
			#tumor_normalized = quantile_normalisation.algo(tumor_list)
			separate_values_matrix_normalised = []

			for i in range(len(Jurkat_normalized)):
				separate_values_matrix_normalised.append([Jurkat_normalized[i][0], Jurkat_normalized[i][1], Jurkat_normalized[i][2], IM9_normalized[i][0], IM9_normalized[i][1], IM9_normalized[i][2], Raji_normalized[i][0], Raji_normalized[i][1], Raji_normalized[i][2], THP1_normalized[i][0], THP1_normalized[i][1], THP1_normalized[i][2]])#, tumor_normalized[i][0], tumor_normalized[i][1]])

			np_gene_dictionary = mixtures.from_matrix_to_dictionary(separate_values_matrix_normalised, np_gene_dictionary)#_tumor)
			# IF TUMOR
			# file_handler.write_separate_cell_lines_tumor(np_gene_dictionary, "separate_cell_lines_tumor")
			# IF NOT TUMOR
			file_handler.write_separate_cell_lines(np_gene_dictionary, "separate_cell_lines")

		elif args.TUMORS != None and len(args.TUMORS) > 0:

			""" Gathers all the cell lines and tumor cell lines from the input files and adds them
				to a dictionary with the probe id as 'key', and a list of all the different values
				as 'value'.
			"""

			np_tumor_dictionary = {}
			np_gene_dictionary_tumor = {}

			for i in range(len(args.CELL_LINES)):
				np_gene_dictionary = mixtures.all_separate_mixtures(args.CELL_LINES[i], np_gene_dictionary, CELL_LINES_INPUT[i])

			for i in range(len(args.TUMORS)):
				np_tumor_dictionary = mixtures.separate_tumor(TUMORS[i], np_tumor_dictionary, TUMORS_INPUT[i])

			for key, value in sorted(np_tumor_dictionary.items()):

				if key in np_gene_dictionary:
					np_gene_dictionary_tumor[key] = np.append(np_gene_dictionary[key], np_tumor_dictionary[key])

			""" After mapping all the input data to their correct probe ID, the dictionary is
				converted to a matrix, and then splitted up to smaller matrices. Each of the small
				matrices indicate a cell line or a tumor cell line.
			"""

			separate_values_matrix = mixtures.from_dictionary_to_matrix(np_gene_dictionary_tumor)
			cell_lines_list = []
			tumor_list = []

			# TODO: ENDRE???
			for j in range(CELL_LINES_INPUT[0][0]):
				cell_lines_list.append([])

			# for j in range(TUMORS_INPUT[0][0]):
			# 	tumor_list.append([])
			
			for i in range(len(separate_values_matrix)):

				for j in range(0, CELL_LINES_INPUT[0][2] - CELL_LINES_INPUT[0][1], CELL_LINES_INPUT[0][3]):

					temp_list = []

					for k in range(j, j+CELL_LINES_INPUT[0][3]):
						temp_list.append(separate_values_matrix[i][k])

					cell_lines_list[int(j/CELL_LINES_INPUT[0][3])].append(temp_list)

				temp_list = []

				for j in range(CELL_LINES_INPUT[0][2] - CELL_LINES_INPUT[0][1] + 1, len(separate_values_matrix[i])):
					temp_list.append(separate_values_matrix[i][j])
				
				tumor_list.append(temp_list)

			""" Quantile normalise each matrix separately (to avoid all the mixtures (plus tumor cell 
				line) to contain the exact same values).
			"""
			
			for i in range(len(cell_lines_list)):
				cell_lines_list[i] = quantile_normalisation.algo(cell_lines_list[i])
			
			#for i in range(len(tumor_list)):
			#	tumor_list = quantile_normalisation.algo(tumor_list)
			tumor_list = quantile_normalisation.algo(tumor_list)

			""" Each cell line containing normalised data is then calculated by average values.
				This would typically be like: (value1 + value2 + value 3) / 3.0
			"""

			combined_values_matrix_normalised = []

			for i in range(len(cell_lines_list[0])):

				average_list = []

				for j in range(len(cell_lines_list)):

					temp_value = 0.0
					
					for k in range(len(cell_lines_list[j][i])):
						temp_value += cell_lines_list[j][i][k]

					average_list.append(temp_value / float(len(cell_lines_list[j][i])))

				temp_value = 0.0

				for j in range(len(tumor_list[i])):
					temp_value += tumor_list[i][j]

				average_list.append(temp_value / float(len(tumor_list[i])))

				combined_values_matrix_normalised.append(average_list)

			#print(combined_values_matrix_normalised[0])

			np_gene_dictionary_tumor = mixtures.from_matrix_to_dictionary(combined_values_matrix_normalised, np_gene_dictionary_tumor)

			file_handler.write_combined_cell_lines_tumor(np_gene_dictionary_tumor, "combined_cell_lines_tumor")

		else:

			# Jurkat, IM-9, Raji, THP-1
			# np_gene_dictionary = mixtures.combine_cell_line(INPUT[2], np_gene_dictionary)

			# separate_values_matrix = mixtures.from_dictionary_to_matrix(np_gene_dictionary)
			
			# norm_matrix_separate = quantile_normalisation.algo(separate_values_matrix)

			# file_handler.write_combined_cell_lines(np_gene_dictionary, "combined_cell_lines")

			""" Gathers all the cell lines and tumor cell lines from the input files and adds them
				to a dictionary with the probe id as 'key', and a list of all the different values
				as 'value'.
			"""

			for i in range(len(args.CELL_LINES)):
				np_gene_dictionary = mixtures.all_separate_mixtures(args.CELL_LINES[i], np_gene_dictionary, CELL_LINES_INPUT[i])


			""" After mapping all the input data to their correct probe ID, the dictionary is
				converted to a matrix, and then splitted up to smaller matrices. Each of the small
				matrices indicate a cell line.
			"""

			separate_values_matrix = mixtures.from_dictionary_to_matrix(np_gene_dictionary)
			cell_lines_list = []

			# TODO: ENDRE???
			for j in range(CELL_LINES_INPUT[0][0]):
				cell_lines_list.append([])

			for i in range(len(separate_values_matrix)):

				for j in range(0, CELL_LINES_INPUT[0][2] - CELL_LINES_INPUT[0][1], CELL_LINES_INPUT[0][3]):

					temp_list = []

					for k in range(j, j+CELL_LINES_INPUT[0][3]):
						temp_list.append(separate_values_matrix[i][k])

					cell_lines_list[int(j/CELL_LINES_INPUT[0][3])].append(temp_list)


			""" Quantile normalise each matrix separately (to avoid all the mixtures to contain the exact same values).
			"""
			
			for i in range(len(cell_lines_list)):
				cell_lines_list[i] = quantile_normalisation.algo(cell_lines_list[i])


			""" Each cell line containing normalised data is then calculated by average values.
				This would typically be like: (value1 + value2 + value 3) / 3.0
			"""

			combined_values_matrix_normalised = []

			for i in range(len(cell_lines_list[0])):

				average_list = []

				for j in range(len(cell_lines_list)):

					temp_value = 0.0
					
					for k in range(len(cell_lines_list[j][i])):
						temp_value += cell_lines_list[j][i][k]

					average_list.append(temp_value / float(len(cell_lines_list[j][i])))

				combined_values_matrix_normalised.append(average_list)

			np_gene_dictionary = mixtures.from_matrix_to_dictionary(combined_values_matrix_normalised, np_gene_dictionary)

			file_handler.write_combined_cell_lines(np_gene_dictionary, "combined_cell_lines_HUGO")

	if args.MIXTURES != None and len(args.MIXTURES) > 0:

		if args.TUMORS != None and len(args.TUMORS) > 0:

			""" Gathers all the mixtures and tumor cell lines from the input files and adds them
				to a dictionary with the probe id as 'key', and a list of all the different values
				as 'value'.
			"""

			np_tumor_dictionary = {}
			np_gene_dictionary_tumor = {}

			for i in range(len(args.MIXTURES)):
				np_gene_dictionary = mixtures.all_separate_mixtures(args.MIXTURES[i], np_gene_dictionary, MIXTURES_INPUT[i])

			for i in range(len(args.TUMORS)):
				np_tumor_dictionary = mixtures.separate_tumor(args.TUMORS[i], np_tumor_dictionary, TUMORS_INPUT[i])

			for key, value in sorted(np_tumor_dictionary.items()):

				if key in np_gene_dictionary:
					np_gene_dictionary_tumor[key] = np.append(np_gene_dictionary[key], np_tumor_dictionary[key])

			""" After mapping all the input data to their correct probe ID, the dictionary is
				converted to a matrix, and then splitted up to smaller matrices. Each of the small
				matrices indicate a mixture or a tumor cell line.
			"""
			#print(np_gene_dictionary_tumor)
			separate_values_matrix = mixtures.from_dictionary_to_matrix(np_gene_dictionary_tumor)
			mixtures_list = []
			tumor_list = []

			# TODO: ENDRE???
			for j in range(MIXTURES_INPUT[0][0]):
				mixtures_list.append([])

			# for j in range(TUMORS_INPUT[0][0]):
			# 	tumor_list.append([])
			#print(len(separate_values_matrix))
			for i in range(len(separate_values_matrix)):

				for j in range(0, MIXTURES_INPUT[0][2] - MIXTURES_INPUT[0][1], MIXTURES_INPUT[0][3]):

					temp_list = []

					for k in range(j, j+MIXTURES_INPUT[0][3]):
						temp_list.append(separate_values_matrix[i][k])

					mixtures_list[int(j/MIXTURES_INPUT[0][3])].append(temp_list)

				temp_list = []

				for j in range(MIXTURES_INPUT[0][2] - MIXTURES_INPUT[0][1] + 1, len(separate_values_matrix[i])):
					temp_list.append(separate_values_matrix[i][j])
				
				tumor_list.append(temp_list)

			""" Calculating the total mRNA in each mixture. Used later in Abbas algorithm.
			"""

			#file_handler.write_probe_values([MIXA, MIXB, MIXC, MIXD], ["MIX A", "MIX B", "MIX C", "MIX D"], "probe_values_mixtures")

			""" Quantile normalise each matrix separately (to avoid all the mixtures (plus tumor cell 
				line) to contain the exact same values).
			"""
			
			for i in range(len(mixtures_list)):
				mixtures_list[i] = quantile_normalisation.algo(mixtures_list[i])
			
			#for i in range(len(tumor_list)):
			#	tumor_list = quantile_normalisation.algo(tumor_list)
			tumor_list = quantile_normalisation.algo(tumor_list)

			""" Each mixture containing normalised data is then calculated by average values.
				This would typically be like: (value1 + value2 + value 3) / 3.0
			"""

			combined_values_matrix_normalised = []

			for i in range(len(mixtures_list[0])):

				average_list = []

				for j in range(len(mixtures_list)):

					temp_value = 0.0
					
					for k in range(len(mixtures_list[j][i])):
						temp_value += mixtures_list[j][i][k]

					average_list.append(temp_value / float(len(mixtures_list[j][i])))

				temp_value = 0.0

				for j in range(len(tumor_list[i])):
					temp_value += tumor_list[i][j]

				average_list.append(temp_value / float(len(tumor_list[i])))

				combined_values_matrix_normalised.append(average_list)

			""" The data is then iterated over 0 to 100 percent tumor content with intervals
				of 5 percent. Each iteration is written to file.
			"""

			start_tumor = int(args.ITERATION[0]); stop_tumor = int(args.ITERATION[1]); step_tumor = int(args.ITERATION[2])
			start_noise = int(args.ITERATION[3]); stop_noise = int(args.ITERATION[4]); step_noise = int(args.ITERATION[5])

			for tumor_content in range(start_tumor, stop_tumor, step_tumor):

				for noise_amount in range(start_noise, stop_noise, step_noise):

					fixed_tumor_matrix = []

					for i in range(len(combined_values_matrix_normalised)):

						temp_list = []

						for k in range(len(combined_values_matrix_normalised[i]) - 1):
							temp_list.append((combined_values_matrix_normalised[i][k] * (1-(tumor_content/100))) + combined_values_matrix_normalised[i][len(combined_values_matrix_normalised[i])-1] * (tumor_content/100))

						#temp_list.append(combined_values_matrix_normalised[i][len(combined_values_matrix_normalised[i])-1] * (tumor_content/100))

						if noise_amount > 0:
							# print("BEFORE: ")
							# print(temp_list)
							temp_list = noise.add_noise_controlled(temp_list, noise_amount)
							# print("AFTER: ")
							# print(temp_list)
							# print("")

						fixed_tumor_matrix.append(temp_list)

					np_gene_dictionary = mixtures.from_matrix_to_dictionary(fixed_tumor_matrix, np_gene_dictionary_tumor)

					#file_handler.write_combined_mixtures_tumor(np_gene_dictionary, OUTPUT + "mixtures_with_tumor_", tumor_content, noise_amount)
					file_handler.write_combined_mixtures_tumor(np_gene_dictionary, OUTPUT + "HUGO_signaturegenes_", tumor_content, noise_amount)

				print("--- Generated simulation file with " + str(tumor_content) + "% tumor content. " + str(int((stop_tumor - tumor_content) / step_tumor)) + " files remaining.")

		else:

			# Mixture A, B, C, and D
			mixes = ["A", "B", "C", "D"]

			for i in range(len(mixes)):

				# Separate
				np_gene_dictionary = mixtures.separate_mixtures(INPUT[2], np_gene_dictionary, mixes[i])
				# Combined
				# np_gene_dictionary = mixtures.combined_mixtures(INPUT[2], np_gene_dictionary, mixes[i])

				separate_values_matrix = mixtures.from_dictionary_to_matrix(np_gene_dictionary)

				norm_matrix_separate = quantile_normalisation.algo(separate_values_matrix)

				np_gene_dictionary = mixtures.from_matrix_to_dictionary(norm_matrix_separate, np_gene_dictionary)

				# SEPARATE
				# file_handler.write_separate_mixtures(np_gene_dictionary, mix)
				# COMBINED
				file_handler.write_combined_mixtures(np_gene_dictionary, "combined_mixtures_", mixes[i])


#read_args();
read_stdin();
execute();


# np_gene_dictionary_copy = copy.deepcopy(np_gene_dictionary)

# np_gene_dictionary_not_combined = mixtures.separate_cell_line(BEGIN2, END2, FILECOLS2, INPUT[2], np_gene_dictionary_copy)

# file_handler.write_combined_cell_lines(np_gene_dictionary)

# np_gene_dictionary_with_tumor = mixtures.combine_tumor(BEGIN1, END1, FILECOLS1, INPUT[0], INPUT[1], np_gene_dictionary)

####################################
# QUANTILE WITHOUT TUMOR AND NOISE #
####################################

# separate_values_matrix = mixtures.from_dictionary_to_matrix(np_gene_dictionary)

# norm_matrix_separate = quantile_normalisation.algo(separate_values_matrix)

# np_gene_dictionary = mixtures.from_matrix_to_dictionary(norm_matrix_separate, np_gene_dictionary)

# # SEPARATE
# # file_handler.write_separate_mixtures(np_gene_dictionary, mix)
# # COMBINED
# file_handler.write_combined_mixtures(np_gene_dictionary, mix)

#########################################
# QUANTILE TUMOR AND CELL LINE TOGETHER #
#########################################

# combined_values_matrix = mixtures.from_dictionary_to_matrix(np_gene_dictionary_with_tumor);

# norm_matrix_combined = quantile_normalisation.algo(combined_values_matrix);

# np_gene_dictionary_with_tumor = mixtures.from_matrix_to_dictionary(norm_matrix_combined, np_gene_dictionary_with_tumor);

# tumor.random_tumor_content(np_gene_dictionary_with_tumor);