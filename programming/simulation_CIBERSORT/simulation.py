
import readline, sys, quantile_normalisation, noise, file_handler, mixtures, tumor, copy

FLAGS = []
MIXTURES = []
TUMORS = []
CELL_LINES = []
np_gene_dictionary = {}


def read_args():

	""" Reading the arguments sent by the user from the terminal.
	-i flag must be followed by input file(s)
	-o flag must be followed by output file(s)

	The given files must be placed outside the "Master" folder:
	Code: folder_name/Master/programming/simulation_CIBERSORT/simulation.py
	Files: folder_name/Master_files/simulation/

	E.g.: python simulation.py
	"""

	if len(sys.argv) == 1:
		print('\n[ERROR] Wrong sys.argv format! Too few arguments. Run:\n\npython simulation.py -i [input.file input.file ...] -o [output.file output.file]\n')
		sys.exit()

	m = False; t = False; c = False;

	for x in range(1, len(sys.argv)):
		#print(sys.argv[x])
		# INPUT
		if sys.argv[x] == '-i':
			print(sys.argv[x])
		# CELL LINE
		elif sys.argv[x] == '-c':
			FLAGS.append("C")
			m = False; t = True; c = True;
			continue
		# MIXTURE
		elif sys.argv[x] == '-m':
			FLAGS.append("M")
			m = True; t = False; c = False;
			continue
		# SIGNATURE
		elif sys.argv[x] == '-r':
			FLAGS.append("R")
		# TUMOR
		elif sys.argv[x] == '-t':
			FLAGS.append("T")
			m = False; t = True; c = False;
			continue

		if m == True:
			MIXTURES.append(sys.argv[x])
			continue

		elif t == True:
			TUMORS.append(sys.argv[x])
			continue

		elif c == True:
			CELL_LINES.append(sys.argv[x])
			continue
			
		print('\n[ERROR] Wrong sys.argv format! Run:\n\npython simulation.py -i [input.file input.file ...] -o [output.file output.file]\n')
		sys.exit()


read_args();

if len(CELL_LINES) > 0:

	if len(FLAGS) > 1 and FLAGS[1] == "R":

		np_gene_dictionary = mixtures.separate_cell_line(INPUT[2], np_gene_dictionary)

		np_gene_dictionary_tumor = mixtures.separate_tumor(INPUT[0], INPUT[1], np_gene_dictionary)

		separate_values_matrix = mixtures.from_dictionary_to_matrix(np_gene_dictionary_tumor)
		
		Jurkat = []; IM9 = []; Raji = []; THP1 = []; tumor_list = [];
		
		for i in range(len(separate_values_matrix)):
			
			Jurkat.append([separate_values_matrix[i][0], separate_values_matrix[i][1], separate_values_matrix[i][2]])
			IM9.append([separate_values_matrix[i][3], separate_values_matrix[i][4], separate_values_matrix[i][5]])
			Raji.append([separate_values_matrix[i][6], separate_values_matrix[i][7], separate_values_matrix[i][8]])
			THP1.append([separate_values_matrix[i][9], separate_values_matrix[i][10], separate_values_matrix[i][11]])
			tumor_list.append([separate_values_matrix[i][12], separate_values_matrix[i][13]])

		Jurkat_normalized = quantile_normalisation.algo(Jurkat)
		IM9_normalized = quantile_normalisation.algo(IM9)
		Raji_normalized = quantile_normalisation.algo(Raji)
		THP1_normalized = quantile_normalisation.algo(THP1)
		tumor_normalized = quantile_normalisation.algo(tumor_list)
		separate_values_matrix_normalised = []

		for i in range(len(Jurkat_normalized)):
			separate_values_matrix_normalised.append([Jurkat_normalized[i][0], Jurkat_normalized[i][1], Jurkat_normalized[i][2], IM9_normalized[i][0], IM9_normalized[i][1], IM9_normalized[i][2], Raji_normalized[i][0], Raji_normalized[i][1], Raji_normalized[i][2], THP1_normalized[i][0], THP1_normalized[i][1], THP1_normalized[i][2], tumor_normalized[i][0], tumor_normalized[i][1]])

		np_gene_dictionary = mixtures.from_matrix_to_dictionary(separate_values_matrix_normalised, np_gene_dictionary_tumor)

		file_handler.write_separate_cell_lines_tumor(np_gene_dictionary, "combined_cell_lines_tumor")

	else:

		# Jurkat, IM-9, Raji, THP-1
		np_gene_dictionary = mixtures.combine_cell_line(INPUT[2], np_gene_dictionary)

		separate_values_matrix = mixtures.from_dictionary_to_matrix(np_gene_dictionary)
		
		norm_matrix_separate = quantile_normalisation.algo(separate_values_matrix)

		file_handler.write_combined_cell_lines(np_gene_dictionary, "combined_cell_lines")

if len(MIXTURES) > 0:

	if len(TUMORS) > 0:

		np_gene_dictionary = mixtures.all_separate_mixtures(MIXTURES[0], np_gene_dictionary)

		np_gene_dictionary_tumor = mixtures.separate_tumor(TUMORS[0], TUMORS[1], np_gene_dictionary)

		separate_values_matrix = mixtures.from_dictionary_to_matrix(np_gene_dictionary_tumor)

		MIXA = []; MIXB = []; MIXC = []; MIXD = []; tumor_list = [];
		
		for i in range(len(separate_values_matrix)):
			
			MIXA.append([separate_values_matrix[i][0], separate_values_matrix[i][1], separate_values_matrix[i][2]])
			MIXB.append([separate_values_matrix[i][3], separate_values_matrix[i][4], separate_values_matrix[i][5]])
			MIXC.append([separate_values_matrix[i][6], separate_values_matrix[i][7], separate_values_matrix[i][8]])
			MIXD.append([separate_values_matrix[i][9], separate_values_matrix[i][10], separate_values_matrix[i][11]])
			tumor_list.append([separate_values_matrix[i][12], separate_values_matrix[i][13]])

		file_handler.write_probe_values([MIXA, MIXB, MIXC, MIXD], ["MIX A", "MIX B", "MIX C", "MIX D"], "probe_values_mixtures")

		MIXA_normalized = quantile_normalisation.algo(MIXA)
		MIXB_normalized = quantile_normalisation.algo(MIXB)
		MIXC_normalized = quantile_normalisation.algo(MIXC)
		MIXD_normalized = quantile_normalisation.algo(MIXD)
		tumor_normalized = quantile_normalisation.algo(tumor_list)
		combined_values_matrix_normalised = []

		for i in range(len(MIXA_normalized)):
			combined_values_matrix_normalised.append([(MIXA_normalized[i][0] + MIXA_normalized[i][1] + MIXA_normalized[i][2]) / 3.0, (MIXB_normalized[i][0] + MIXB_normalized[i][1] + MIXB_normalized[i][2]) / 3.0, (MIXC_normalized[i][0] + MIXC_normalized[i][1] + MIXC_normalized[i][2]) / 3.0, (MIXD_normalized[i][0] + MIXD_normalized[i][1] + MIXD_normalized[i][2]) / 3.0, (tumor_normalized[i][0] + tumor_normalized[i][1]) / 2.0])
		
		#for j in range(0, 105, 5):
		for j in range(0, 5, 5):

			fixed_tumor_matrix = []

			for i in range(len(combined_values_matrix_normalised)):

				fixed_tumor_matrix.append([combined_values_matrix_normalised[i][0] * (1-(j/100)), combined_values_matrix_normalised[i][1] * (1-(j/100)), combined_values_matrix_normalised[i][2] * (1-(j/100)), combined_values_matrix_normalised[i][3] * (1-(j/100)), combined_values_matrix_normalised[i][4] * (j/100)])

			np_gene_dictionary = mixtures.from_matrix_to_dictionary(fixed_tumor_matrix, np_gene_dictionary_tumor)

			file_handler.write_combined_mixtures_tumor(np_gene_dictionary_tumor, "mixtures_with_tumor_", j)
			#file_handler.write_combined_mixtures_tumor(np_gene_dictionary_tumor, "TESTFILE_", j)

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