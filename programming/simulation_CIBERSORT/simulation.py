
import readline, sys, quantile_normalisation, noise, file_handler, mixtures, tumor, copy

INPUT = []
OUTPUT = []
np_gene_dictionary = {}

# Variables for GSE10650

BEGIN1 = 4
END1 = 54679
EOF1 = 54683
FILECOLS1 = 2

# Variables for GSE11103

BEGIN2 = 64
END2 = 54739
EOF2 = 54740
FILECOLS2 = 42


def read_args():

	""" Reading the arguments sent by the user from the terminal.
	-i flag must be followed by input file(s)
	-o flag must be followed by output file(s)

	The given files must be placed outside the "Master" folder:
	Code: folder_name/Master/programming/simulation_CIBERSORT/simulation.py
	Files: folder_name/Master_files/simulation/

	E.g.: python simulation.py -i GSM269529.txt -o GSM269529_NEW.txt
	"""

	i = False
	o = False

	if len(sys.argv) == 1:
		print('\n[ERROR] Wrong sys.argv format! Run:\n\npython simulation.py -i [input.file input.file ...] -o [output.file output.file]\n')
		sys.exit()

	for x in range(1, len(sys.argv)):
		
		if sys.argv[x] == '-i':
			i = True
			o = False
			
		elif sys.argv[x] == '-o':
			i = False
			o = True
			
		elif i == True:
			INPUT.append(sys.argv[x])
			
		elif o == True:
			OUTPUT.append(sys.argv[x])
			
		else:
			print('\n[ERROR] Wrong sys.argv format! Run:\n\npython simulation.py -i [input.file input.file ...] -o [output.file output.file]\n')
			sys.exit()


read_args();

np_gene_dictionary = mixtures.combine_cell_line(BEGIN2, END2, FILECOLS2, INPUT[2], np_gene_dictionary)

np_gene_dictionary_copy = copy.deepcopy(np_gene_dictionary)

np_gene_dictionary_not_combined = mixtures.separate_cell_line(BEGIN2, END2, FILECOLS2, INPUT[2], np_gene_dictionary_copy)

file_handler.write_combined_cell_lines(np_gene_dictionary)

np_gene_dictionary_with_tumor = mixtures.combine_tumor(BEGIN1, END1, FILECOLS1, INPUT[0], INPUT[1], np_gene_dictionary)

##################################
# GENERATE REFERENCE SAMPLE FILE #
##################################

separate_values_matrix = mixtures.from_dictionary_to_matrix(np_gene_dictionary_not_combined);

norm_matrix_separate = quantile_normalisation.algo(separate_values_matrix);

np_gene_dictionary_clean = mixtures.from_matrix_to_dictionary(norm_matrix_separate, np_gene_dictionary_not_combined)

file_handler.write_separate_cell_lines(np_gene_dictionary_clean)

###########################################
# QUANTILE TUMOR AND CELL LINE SEPARATELY #
###########################################

# cell_line_values_matrix, tumor_values_matrix = mixtures.from_dictionary_to_matrix(np_gene_dictionary);

# norm_matrix_cell_line = quantile_normalisation.algo(cell_line_values_matrix);
# norm_matrix_tumor = quantile_normalisation.algo(tumor_values_matrix);

# np_gene_dictionary = mixtures.from_matrix_to_dictionary(norm_matrix_cell_line, norm_matrix_tumor, np_gene_dictionary);

#########################################
# QUANTILE TUMOR AND CELL LINE TOGETHER #
#########################################

# combined_values_matrix = mixtures.from_dictionary_to_matrix(np_gene_dictionary_with_tumor);

# norm_matrix_combined = quantile_normalisation.algo(combined_values_matrix);

# np_gene_dictionary_with_tumor = mixtures.from_matrix_to_dictionary(norm_matrix_combined, np_gene_dictionary_with_tumor);

# tumor.random_tumor_content(np_gene_dictionary_with_tumor);