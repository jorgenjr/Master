
import readline, sys, quantile_normalisation, noise, file_handler, mixtures

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
	Files: folder_name/Master_files/[input|output]/

	E.g.: python simulation.py -i GSM269529.txt -o GSM269529_NEW.txt
	"""

	i = False
	o = False

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

# NOT COMPATIBLE WITH NEW SETUP!
#file_handler.read_files(INPUT);

np_gene_dictionary = mixtures.combine_cell_line(BEGIN2, END2, FILECOLS2, INPUT[2], np_gene_dictionary);
np_gene_dictionary = mixtures.combine_tumor(BEGIN1, END1, FILECOLS1, INPUT[0], INPUT[1], np_gene_dictionary);

cell_line_values_matrix, tumor_values_matrix = mixtures.from_dictionary_to_matrix(np_gene_dictionary);

norm_matrix_cell_line = quantile_normalisation.algo(cell_line_values_matrix);
norm_matrix_tumor = quantile_normalisation.algo(tumor_values_matrix);

noise_cell_line = noise.add_noise(norm_matrix_cell_line);
noise_tumor = noise.add_noise(norm_matrix_tumor);

np_gene_dictionary = mixtures.from_matrix_to_dictionary(noise_cell_line, noise_tumor, np_gene_dictionary);


############
# OLD CODE #
############

#norm_matrix = quantile_normalisation.algo(BEGIN1, END1, INPUT);
#norm_matrix_noise = noise.add_noise(BEGIN1, END1, norm_matrix);

#file_handler.write_to_file(BEGIN1, END1, norm_matrix_noise, INPUT, OUTPUT);

# OUT OF WORK
#quantile_normalisation_package(BEGIN1, END1);