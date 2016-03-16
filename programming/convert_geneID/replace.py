
import copy, numpy as np, readline, sys

FLAGS = []

def read_args():

	""" Reading the arguments sent by the user from the terminal.
	-i flag must be followed by input file(s)
	-o flag must be followed by output file(s)

	The given files must be placed outside the "Master" folder:
	Code: folder_name/Master/programming/simulation_CIBERSORT/simulation.py
	Files: folder_name/Master_files/simulation/

	E.g.: python simulation.py -i GSM269529.txt -o GSM269529_NEW.txt
	"""

	if len(sys.argv) == 1:
		print('\n[ERROR] Wrong sys.argv format! Run:\n\npython simulation.py -i [input.file input.file ...] -o [output.file output.file]\n')
		sys.exit()

	for x in range(1, len(sys.argv)):
		
		if sys.argv[x] == '-c':
			FLAGS.append("C")

		elif sys.argv[x] == '-m':
			FLAGS.append("M")

		elif sys.argv[x] == '-r':
			FLAGS.append("R")

		elif sys.argv[x] == '-t':
			FLAGS.append("T")

		else:
			print('\n[ERROR] Wrong sys.argv format! Run:\n\npython simulation.py -i [input.file input.file ...] -o [output.file output.file]\n')
			sys.exit()


def read_hugo():

	""" Reads hugo, and adds Affy ID and HUGO ID to dictionary
	"""

	f_hugo = open('../../../Master_files/simulation/affy_to_hugo', 'r')
	header = True
	affy_to_hugo = {}

	for line in f_hugo:

		if (header == True):
			header = False
			continue

		splitted_line = line.split('\t')
		affy = splitted_line[1].split('\"')
		hugo = splitted_line[2].split('\"')
		
		if hugo[1] and not hugo[1].isspace():
			affy_to_hugo[affy[1]] = hugo[1]

	f_hugo.close()

	return affy_to_hugo

def replace_affy_with_hugo(affy_to_hugo, filename):

	""" Replaces Affy IDs with HUGO IDs in the original simulation file.
	1. Reads the original simulation file containing Affy IDs.
	2. Converts every Affy IDs to HUGO ID, dismissed unreadable Affy IDs.
	3. Writes the simulation data to a new file with HUGO IDs instead.
	4. Finds unique hugo genes (removes duplicates)
	"""

	f_simulation = open('../../../Master_files/simulation/' + filename, 'r')
	# f_simulation_hugo = open('../../../Master_files/convert/simulation_hugo_combined_' + mix, 'w')
	# f_simulation_hugo = open('../../../Master_files/convert/reference_hugo', 'w')
	header = True
	unique_hugo_genes = []

	for line in f_simulation:

		if (header == True):
			# f_simulation_hugo.write(line)
			f_simulation_hugo_unique.write(line)
			header = False
			continue

		splitted_line = line.split('\t')

		try:
			line_to_write = affy_to_hugo[splitted_line[0]]

			# Skip gene ID
			for i in range(1, len(splitted_line)):
				line_to_write += "\t" + splitted_line[i]

			# f_simulation_hugo.write(line_to_write);

			unique_hugo_genes = find_unique_hugo_genes(unique_hugo_genes, affy_to_hugo[splitted_line[0]], splitted_line)
			
		except KeyError:
			# print("Error!")
			pass

	f_simulation.close()
	# f_simulation_hugo.close()
	
	return unique_hugo_genes

def find_unique_hugo_genes(unique_hugo_genes, geneid, splitted_line):

	""" Adds unique hugo genes to list. If duplicates is found:
	1. Adds together the gene values
	2. Increment the number of duplicates found.
	"""

	if len(unique_hugo_genes) == 0:

		list_of_genes = []

		for i in range(1, len(splitted_line)):

			if i == len(splitted_line) - 1:
				list_of_genes.append(float(splitted_line[i][:-1]))
			else:
				list_of_genes.append(float(splitted_line[i]))

		unique_hugo_genes.append([geneid, list_of_genes, 1]);
		
		return unique_hugo_genes

	found = False;

	for i in range(len(unique_hugo_genes)):

		if unique_hugo_genes[i][0] == geneid:

			list_of_genes = []

			for j in range(1, len(splitted_line)):
			
				if i == len(splitted_line) - 1:
					list_of_genes.append(float(splitted_line[j][:-1]))
				else:	
					list_of_genes.append(float(splitted_line[j]))

			unique_hugo_genes[i][1] = list_of_genes
			unique_hugo_genes[i][2] = unique_hugo_genes[i][2] + 1;
			found = True;
			break;
		
	if (found == False):

		list_of_genes = []

		for i in range(1, len(splitted_line)):

			if i == len(splitted_line) - 1:
				list_of_genes.append(float(splitted_line[i][:-1]))
			else:	
				list_of_genes.append(float(splitted_line[i]))

		unique_hugo_genes.append([geneid, list_of_genes, 1])

	return unique_hugo_genes

def calc_average(unique_hugo_genes):

	""" Loops through 'unique_hugo_genes' and calculates the average gene value.
	If current index has occurrence == 1; continue.
	If current index has occurrence > 1; calculate average by dividing the
	gene value by the number of occurrence.
	Sorts by gene ID.
	"""
	
	for i in range(len(unique_hugo_genes)):

		if (unique_hugo_genes[i][2] > 1):
			
			list_of_genes = []
			
			for j in range(len(unique_hugo_genes[i][1])):
				list_of_genes.append(unique_hugo_genes[i][1][j] / float(unique_hugo_genes[i][2]))
			
			unique_hugo_genes[i][1] = list_of_genes

	unique_hugo_genes.sort();

	return unique_hugo_genes

def write_unique_hugo_genes(unique_hugo_genes_average):

	""" Writes the list of unique hugo genes (and values) to file.
	"""

	for i in range(len(unique_hugo_genes)):

		line_to_write = unique_hugo_genes[i][0]

		for j in range(len(unique_hugo_genes[i][1])):
			line_to_write += "\t" + str(unique_hugo_genes[i][1][j])

		line_to_write += "\n"

		f_simulation_hugo_unique.write(line_to_write)


read_args();

if FLAGS[0] == "C":

	f_simulation_hugo_unique = open('../../../Master_files/convert/simulation_hugo_combined_cell_lines', 'w')

	affy_to_hugo = read_hugo()
	unique_hugo_genes = replace_affy_with_hugo(affy_to_hugo, "combined_cell_lines")
	unique_hugo_genes_average = calc_average(unique_hugo_genes)
	write_unique_hugo_genes(unique_hugo_genes_average)

	f_simulation_hugo_unique.close()

if FLAGS[0] == "M":

	mixes = ["A", "B", "C", "D"]

	for i in range(len(mixes)):

		f_simulation_hugo_unique = open('../../../Master_files/convert/simulation_hugo_unique_combined_' + mixes[i], 'w')
		# f_simulation_hugo_unique = open('../../../Master_files/convert/reference_hugo_unique', 'w')

		affy_to_hugo = read_hugo()
		unique_hugo_genes = replace_affy_with_hugo(affy_to_hugo, "combined_mixtures_" + mixes[i])
		unique_hugo_genes_average = calc_average(unique_hugo_genes)
		write_unique_hugo_genes(unique_hugo_genes_average)

		f_simulation_hugo_unique.close()

if FLAGS[0] == "R":

	f_simulation_hugo_unique = open('../../../Master_files/convert/reference_hugo_unique_tumor', 'w')

	affy_to_hugo = read_hugo()
	unique_hugo_genes = replace_affy_with_hugo(affy_to_hugo, "combined_cell_lines_tumor")
	unique_hugo_genes_average = calc_average(unique_hugo_genes)
	write_unique_hugo_genes(unique_hugo_genes_average)

	f_simulation_hugo_unique.close()

if FLAGS[0] == "T":
	
	affy_to_hugo = read_hugo()

	start = 0; stop = 101; step = 5;

	for tumor_content in range(start, stop, step):

		for noise_content in range(0, 100, 30):

			f_simulation_hugo_unique = open('../../../Master_files/convert/simulation_hugo_unique_tumor_' + str(tumor_content) + "_" + str(noise_content), 'w')

			unique_hugo_genes = replace_affy_with_hugo(affy_to_hugo, "mixtures_with_tumor_" + str(tumor_content) + "_" + str(noise_content))
			unique_hugo_genes_average = calc_average(unique_hugo_genes)
			write_unique_hugo_genes(unique_hugo_genes_average)

			f_simulation_hugo_unique.close()

		print("--- Converted file with " + str(tumor_content) + "% tumor content. " + str(int((stop - tumor_content) / step)) + " files remaining.")