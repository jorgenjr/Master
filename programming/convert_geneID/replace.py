
import copy
import numpy as np
import readline
import sys
import argparse

OUTPUT_PATH = "../../../Master_files"

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--MIXTURES", help="Mixtures", nargs='*')
parser.add_argument("-t", "--TUMORS", help="Tumors", nargs='*')
parser.add_argument("-c", "--CELL_LINES", help="Cell lines", nargs='*')
parser.add_argument("-r", "--REFERENCE", help="Reference", nargs='*')
parser.add_argument("-i", "--ITERATION_LIST", help="Iteration list", nargs='*')

args = parser.parse_args()


def read_hugo():

	""" Reads hugo, and adds Affy ID and HUGO ID to dictionary
	"""

	f_hugo = open(OUTPUT_PATH + '/simulation/affy_to_hugo', 'r')
	header = True
	affy_to_hugo = {}
	empty = 0

	for line in f_hugo:

		if (header == True):
			header = False
			continue

		splitted_line = line.split('\t')
		affy = splitted_line[1].split('\"')
		hugo = splitted_line[2].split('\"')
		
		if hugo[1] and not hugo[1].isspace():
			affy_to_hugo[affy[1]] = hugo[1]
		else:
			empty += 1

	# print("Number of AFFY IDs not mapped to HUGO: " + str(empty))
	f_hugo.close()

	return affy_to_hugo

def replace_affy_with_hugo(affy_to_hugo, filename):

	""" Replaces Affy IDs with HUGO IDs in the original simulation file.
	1. Reads the original simulation file containing Affy IDs.
	2. Converts every Affy IDs to HUGO ID, dismissed unreadable Affy IDs.
	3. Writes the simulation data to a new file with HUGO IDs instead.
	4. Finds unique hugo genes (removes duplicates)
	"""

	f_simulation = open(OUTPUT_PATH + filename, 'r')
	header = True
	unique_hugo_genes = []

	for line in f_simulation:

		if (header == True):
			f_simulation_hugo_unique.write(line)
			header = False
			continue

		splitted_line = line.split('\t')
		splitted_line[0] = splitted_line[0].replace("\"", "")
		try:
			unique_hugo_genes = find_unique_hugo_genes(unique_hugo_genes, affy_to_hugo[splitted_line[0]], splitted_line)
		except KeyError:
			#print("Error!")
			pass

	f_simulation.close()
	
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
		
	if found == False:

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
	
	duplicates = 0

	for i in range(len(unique_hugo_genes)):

		if (unique_hugo_genes[i][2] > 1):
			
			duplicates += 1
			list_of_genes = []
			
			for j in range(len(unique_hugo_genes[i][1])):
				list_of_genes.append(unique_hugo_genes[i][1][j] / float(unique_hugo_genes[i][2]))
			
			unique_hugo_genes[i][1] = list_of_genes

	# print("The number of duplicates (two or more probsesets mapped to one HUGO symbol): " + str(duplicates))
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


affy_to_hugo = read_hugo()

if args.CELL_LINES != None and len(args.CELL_LINES) > 0:

	f_simulation_hugo_unique = open(OUTPUT_PATH + '/convert/combined_cell_lines_hugo', 'w')

	unique_hugo_genes = replace_affy_with_hugo(affy_to_hugo, "/simulation/combined_cell_lines")
	unique_hugo_genes_average = calc_average(unique_hugo_genes)
	write_unique_hugo_genes(unique_hugo_genes_average)

	f_simulation_hugo_unique.close()

elif args.MIXTURES != None and len(args.MIXTURES) > 0:

	mixes = ["A", "B", "C", "D"]

	for i in range(len(mixes)):

		f_simulation_hugo_unique = open(OUTPUT_PATH + '/convert/mixtures_normalized_tumor_HUGO_' + mixes[i], 'w')
		# f_simulation_hugo_unique = open('../../../Master_files/convert/reference_hugo_unique', 'w')

		unique_hugo_genes = replace_affy_with_hugo(affy_to_hugo, "/simulation/combined_mixtures_" + mixes[i])
		unique_hugo_genes_average = calc_average(unique_hugo_genes)
		write_unique_hugo_genes(unique_hugo_genes_average)

		f_simulation_hugo_unique.close()

elif args.REFERENCE != None and len(args.REFERENCE) > 0:

	f_simulation_hugo_unique = open(OUTPUT_PATH + '/convert/separate_cell_lines_norm_hugo', 'w')
	
	unique_hugo_genes = replace_affy_with_hugo(affy_to_hugo, '/simulation/separate_cell_lines_norm')
	unique_hugo_genes_average = calc_average(unique_hugo_genes)
	write_unique_hugo_genes(unique_hugo_genes_average)

	f_simulation_hugo_unique.close()

elif args.TUMORS != None and len(args.TUMORS) > 0:

	start_tumor = int(args.ITERATION_LIST[0]); stop_tumor = int(args.ITERATION_LIST[1]); step_tumor = int(args.ITERATION_LIST[2])
	start_noise = int(args.ITERATION_LIST[3]); stop_noise = int(args.ITERATION_LIST[4]); step_noise = int(args.ITERATION_LIST[5])

	for tumor_content in range(start_tumor, stop_tumor, step_tumor):

		for noise_content in range(start_noise, stop_noise, step_noise):

			f_simulation_hugo_unique = open(OUTPUT_PATH + '/convert/mixtures_hugo_tumor_' + str(tumor_content) + '_' + str(noise_content), 'w')

			unique_hugo_genes = replace_affy_with_hugo(affy_to_hugo, "/simulation/mixtures_normalized_tumor_" + str(tumor_content) + '_' + str(noise_content))
			unique_hugo_genes_average = calc_average(unique_hugo_genes)
			write_unique_hugo_genes(unique_hugo_genes_average)

			f_simulation_hugo_unique.close()

		print("--- Converted file with " + str(tumor_content) + "% tumor content. " + str(int((stop_tumor - tumor_content) / step_tumor)) + " files remaining.")

else:
	
	f_simulation_hugo_unique = open(OUTPUT_PATH + '/external/GSE26495_HUGO_quantile.txt', 'w')

	unique_hugo_genes = replace_affy_with_hugo(affy_to_hugo, '/external/GSE26495_quantile.txt')
	unique_hugo_genes_average = calc_average(unique_hugo_genes)
	write_unique_hugo_genes(unique_hugo_genes_average)

	f_simulation_hugo_unique.close()