
import linecache, numpy as np, sys

np_gene_dictionary = {}

# Variables for GSE10650

BEGIN1 = 4
END1 = 54679
EOF1 = 54683
FILECOLS1 = 2
GENE = 0
VALUE = 1

# Variables for GSE11103

BEGIN2 = 64
END2 = 54739
EOF2 = 54740
FILECOLS2 = 42

def read_file(START, STOP, INDEX, COLS):

	""" Reads the data from the specific file.
	Format for the dictionary is: { 'gene1' : [value1, value2, ... ], 'gene2' : [ ... ], ... }
	
	If the gene is not already in the dictionary, it will be added with a numpy array as value.
	If the gene already is in the dictionary, the value from the specific file is appended to the numpy array.
	"""

	for x in range(START, STOP):

		line = linecache.getline('../../../Master_files/input/' + INPUT[INDEX], x)
		line_list = np.array(line.split('\t'))
		gene_ref = ""

		if COLS == FILECOLS1:
			gene_ref = line_list[GENE]
		elif COLS == FILECOLS2:
			gene_ref = line_list[GENE].split('"')[1]

		for j in range(1, COLS):
			if gene_ref in np_gene_dictionary:
				np_gene_dictionary[gene_ref] = np.append(np_gene_dictionary[gene_ref], np.array(float(line_list[j])))
			else:
				np_gene_dictionary[gene_ref] = np.array(float(line_list[j]))


def read_files(INPUT):

	""" Reads the input files. Splitted up in two parts as GSM and GSE have different formats.
	"""

	for i in range(len(INPUT)):

		if INPUT[i] == 'GSM269529.txt' or INPUT[i] == 'GSM269530.txt':
			read_file(BEGIN1, END1, i, FILECOLS1)
		elif INPUT[i] == 'GSE11103_series_matrix.txt':
			read_file(BEGIN2, END2, i, FILECOLS2)

	print(np_gene_dictionary)


def write_to_file(BEGIN, END, normalized_matrix, INPUT, OUTPUT):

	""" Creating new files with the quantile normalized matrix with added noise.
	Everything from the original data is copied except the MEAN value, which is from the normalized matrix.
	"""

	f1 = open('../../../Master_files/input/' + INPUT[0], 'r')
	f2 = open('../../../Master_files/input/' + INPUT[1], 'r')
	f1_new = open('../../../Master_files/output/' + OUTPUT[0], 'w')
	f2_new = open('../../../Master_files/output/' + OUTPUT[1], 'w')

	insert = 0

	for x in range(0, END):

		if x < BEGIN:

			f1_new.write(linecache.getline('../../../Master_files/input/' + INPUT[0], x))
			f2_new.write(linecache.getline('../../../Master_files/input/' + INPUT[1], x))

		elif x < END:

			line1 = linecache.getline('../../../Master_files/input/' + INPUT[0], x)
			line2 = linecache.getline('../../../Master_files/input/' + INPUT[1], x)

			list1 = np.array(line1.split('\t'))
			list2 = np.array(line2.split('\t'))

			list1 = [list1[GENE], normalized_matrix[x-BEGIN][0]]
			list2 = [list1[GENE], normalized_matrix[x-BEGIN][1]]

			f1_new.write('\t'.join(str(s) for s in list1) + '\n')
			f2_new.write('\t'.join(str(s) for s in list2) + '\n')

		else:
			print (linecache.getline('../../../Master_files/input/' + INPUT[0], x))
			print (linecache.getline('../../../Master_files/input/' + INPUT[1], x))
		
		insert += 1