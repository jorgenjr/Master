
import linecache, numpy as np, sys, config


def write_combined_cell_lines(NP_GENE_DICTIONARY, FILENAME, CELL_LINES_INPUT):

	""" Write the gene dictionary with only data from cell lines combined to file. IN USE!
	"""

	f = open(config.PATH_SIMULATION + FILENAME, 'w')

	""" Name the header. Each mixtures is called: "MIX_<number_of_mixtures>".
	"""
	header = "Genes"
	cell_no = 1

	for cell_file in range(len(CELL_LINES_INPUT)):

		for mix_line in range(CELL_LINES_INPUT[cell_file][0]):

			header += "\tCELL_"+str(cell_no)
			cell_no += 1

	f.write(header+"\n")

	""" Add every gene expression from cell lines together
	"""
	for key, value in sorted(NP_GENE_DICTIONARY.items()):

		line = str(key)

		for i in range(len(value)):

			line += "\t"+str(value[i])

		f.write(line+"\n")

	f.close()


def write_combined_cell_lines_tumor(NP_GENE_DICTIONARY, FILENAME, CELL_LINES_INPUT, TUMORS_INPUT):

	""" Write the gene dictionary with only data from cell lines combined to file. IN USE!
	"""

	f = open(config.PATH_SIMULATION + FILENAME, 'w')

	""" Name the header. Each mixtures is called: "MIX_<number_of_mixtures>".
	"""
	header = "Genes"
	cell_no = 1

	for cell_file in range(len(CELL_LINES_INPUT)):

		for mix_line in range(CELL_LINES_INPUT[cell_file][0]):

			header += "\tCELL_"+str(cell_no)
			cell_no += 1

	header += "\tTUMOR"

	f.write(header+"\n")

	""" Add every gene expression from cell lines together
	"""
	for key, value in sorted(NP_GENE_DICTIONARY.items()):

		line = str(key)

		for i in range(len(value)):

			line += "\t"+str(value[i])

		f.write(line+"\n")

	f.close()


def write_separate_cell_lines(NP_GENE_DICTIONARY, FILENAME, CELL_LINES_INPUT, TUMORS_INPUT):

	""" Writes the gene dictionary to file. IN USE!
	"""

	f = open(config.PATH_SIMULATION + FILENAME, 'w')

	""" Name the header. Each cell line is called: "CELL_<number_of_cell_line>_<number_of_replicate_for_cell_line>". E.g. Jurkat with 3 replicates could be: "CELL_1_1	CELL_1_2	CELL_1_3".
	"""
	header = "Genes"
	cell_no = 1

	for cell_file in range(len(CELL_LINES_INPUT)):

		for cell_line in range(CELL_LINES_INPUT[cell_file][0]):

			rep = 1

			for replicate in range(CELL_LINES_INPUT[cell_file][3]):

				header += "\tCELL_"+str(cell_no)+"_"+str(rep)
				rep += 1

			cell_no += 1

	tumor_no = 1

	for tumor_file in range(len(TUMORS_INPUT)):

		for tumor_line in range(TUMORS_INPUT[tumor_file][0]):

			rep = 1

			for replicate in range(TUMORS_INPUT[tumor_file][3]):

				header += "\tTUMOR_"+str(tumor_no)+"_"+str(rep)
				rep += 1

			tumor_no += 1

	f.write(header+"\n")

	""" Add every gene expression from cell lines together
	"""
	for key, value in sorted(NP_GENE_DICTIONARY.items()):

		line = str(key)

		for i in range(len(value)):

			line += "\t"+str(value[i])

		f.write(line+"\n")

	f.close()


def write_combined_mixtures(NP_GENE_DICTIONARY, FILENAME, MIXTURES_INPUT):

	""" Writes the gene dictionary to file. IN USE!
	"""

	f = open(config.PATH_SIMULATION + FILENAME, 'w')

	header = "Genes"
	mix_no = 1

	for cell_file in range(len(MIXTURES_INPUT)):

		for cell_line in range(MIXTURES_INPUT[cell_file][0]):

			header += "\tMIX_"+str(mix_no)
			mix_no += 1

	f.write(header+"\n")

	for key, value in sorted(NP_GENE_DICTIONARY.items()):

		line = str(key)

		for i in range(len(value)):

			line += "\t"+str(value[i])

		f.write(line+"\n")

	f.close()


def write_combined_mixtures_tumor(NP_GENE_DICTIONARY, FILENAME, TUMOR_CONTENT, NOISE, MIXTURES_INPUT):

	""" Write the gene dictionary with only data from mixtures combined to file. IN USE!
	"""

	f = open(config.PATH_SIMULATION + FILENAME + str(TUMOR_CONTENT) + "_" + str(NOISE), 'w')

	""" Name the header. Each mixtures is called: "MIX_<number_of_mixtures>".
	"""
	header = "Genes"
	mix_no = 1

	for cell_file in range(len(MIXTURES_INPUT)):

		for mix_line in range(MIXTURES_INPUT[cell_file][0]):

			header += "\tMIX_"+str(mix_no)+" ("+str(TUMOR_CONTENT)+"% TUMOR)"
			mix_no += 1

	f.write(header+"\n")

	""" Add every gene expression from cell lines together
	"""
	for key, value in sorted(NP_GENE_DICTIONARY.items()):

		line = str(key)

		for i in range(len(value)):

			line += "\t"+str(value[i])

		f.write(line+"\n")

	f.close()


def write_probe_values(PROBES, HEADER, FILENAME):

	if len(PROBES) != len(HEADER) and len(HEADER) > 0:

		print()
		sys.exit('\n[ERROR] The lists HEADER and PROBES had not the same length!\n')

	f = open(config.PATH_SIMULATION + FILENAME, 'w')

	write_header = HEADER[0];

	for i in range(1, len(HEADER)):
		write_header += "\t" + HEADER[i];

	f.write(write_header + "\n")

	sum_probes = []

	for i in range(len(PROBES)):

		temp_probes = 0.0

		for j in range(len(PROBES[i])):

			avg_probe = 0.0

			for k in range(len(PROBES[i][j])):
				avg_probe += PROBES[i][j][k]

			temp_probes += (avg_probe / float(len(PROBES[i][j])))
			
		sum_probes.append(temp_probes)

	write_values = str(sum_probes[0])

	for i in range(1, len(sum_probes)):
		write_values += "\t" + str(sum_probes[i])

	f.write(write_values + "\n")

	f.close()