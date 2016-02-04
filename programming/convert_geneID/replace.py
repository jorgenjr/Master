
import copy, time

def read_hugo():

	""" Reads hugo, and adds Affy ID and HUGO ID to dictionary
	"""

	f_hugo = open('../../../Master_files/diff_exp/hugo', 'r')
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

def replace_affy_with_hugo(affy_to_hugo):

	""" Replaces Affy IDs with HUGO IDs in the original simulation file.
	1. Reads the original simulation file containing Affy IDs.
	2. Converts every Affy IDs to HUGO ID, dismissed unreadable Affy IDs.
	3. Writes the simulation data to a new file with HUGO IDs instead.
	4. Finds unique hugo genes (removes duplicates)
	"""

	f_simulation = open('../../../Master_files/simulation/testfile_1_1', 'r')
	f_simulation_hugo = open('../../../Master_files/convert/simulation_hugo', 'w')
	header = True
	unique_hugo_genes = []

	for line in f_simulation:

		if (header == True):
			f_simulation_hugo.write(line)
			f_simulation_hugo_unique.write(line)
			header = False
			continue

		splitted_line = line.split('\t')

		try:
			geneid = affy_to_hugo[splitted_line[0]]
			f_simulation_hugo.write(geneid + '\t' + splitted_line[1] + '\t' + splitted_line[2] + '\t' + splitted_line[3] + '\t' + splitted_line[4]);

			unique_hugo_genes = find_unique_hugo_genes(unique_hugo_genes, geneid, splitted_line)
			
		except KeyError:
			# print("Error!")
			pass

	f_simulation.close()
	f_simulation_hugo.close()

	return unique_hugo_genes

def find_unique_hugo_genes(unique_hugo_genes, geneid, splitted_line):

	""" Adds unique hugo genes to list. If duplicates is found:
	1. Adds together the gene values
	2. Increment the number of duplicates found.
	"""

	if len(unique_hugo_genes) == 0:
		unique_hugo_genes.append([geneid, [float(splitted_line[1]), float(splitted_line[2]), float(splitted_line[3]), float(splitted_line[4][:-1])], 1]);
		
		return unique_hugo_genes

	found = False;

	for i in range(len(unique_hugo_genes)):
		
		if unique_hugo_genes[i][0] == geneid:
			unique_hugo_genes[i][1] = [unique_hugo_genes[i][1][0] + float(splitted_line[1]), unique_hugo_genes[i][1][1] + float(splitted_line[2]), unique_hugo_genes[i][1][2] + float(splitted_line[3]), unique_hugo_genes[i][1][3] + float(splitted_line[4])]
			unique_hugo_genes[i][2] = unique_hugo_genes[i][2] + 1;
			found = True;
			break;
		

	if (found == False):
		unique_hugo_genes.append([geneid, [float(splitted_line[1]), float(splitted_line[2]), float(splitted_line[3]), float(splitted_line[4][:-1])], 1]);

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
			unique_hugo_genes[i][1] = [unique_hugo_genes[i][1][0] / float(unique_hugo_genes[i][2]), unique_hugo_genes[i][1][1] / float(unique_hugo_genes[i][2]), unique_hugo_genes[i][1][2] / float(unique_hugo_genes[i][2]), unique_hugo_genes[i][1][3] / float(unique_hugo_genes[i][2])]

	unique_hugo_genes.sort();

	return unique_hugo_genes

def write_unique_hugo_genes(unique_hugo_genes_average):

	""" Writes the list of unique hugo genes (and values) to file.
	"""

	for i in range(len(unique_hugo_genes)):
		f_simulation_hugo_unique.write(unique_hugo_genes[i][0] + '\t' + str(unique_hugo_genes[i][1][0]) + '\t' + str(unique_hugo_genes[i][1][1]) + '\t' + str(unique_hugo_genes[i][1][2]) + '\t' + str(unique_hugo_genes[i][1][3]) + '\n')

f_simulation_hugo_unique = open('../../../Master_files/convert/simulation_hugo_unique', 'w')

affy_to_hugo = read_hugo()
unique_hugo_genes = replace_affy_with_hugo(affy_to_hugo)
unique_hugo_genes_average = calc_average(unique_hugo_genes)
write_unique_hugo_genes(unique_hugo_genes_average)

f_simulation_hugo_unique.close()