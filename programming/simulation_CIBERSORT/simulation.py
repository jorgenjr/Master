
import linecache, numpy as np, operator, itertools, readline, rpy2.robjects as robjects, random, time, sys
from rpy2.robjects.packages import importr

INPUT = []
OUTPUT = []

# Variables for GSE10650

BEGIN1 = 4
END1 = 54679
GENE = 0
VALUE = 1

# Variables for GSE11103

FILECOLS = 41
BEGIN2 = 64
END2 = 54739
EOF2 = 54740


def read_args():

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


def quantile_normalisation_package(BEGIN, END):

	""" Quantile normalization for mean value between to .CEL files.
	STEP 1: Read file and add 'mean' to list.
	STEP 2: Calculate vectors, create matrix based on vectors and normalize the matrix with quantile normalisation.
	"""

	preprocessCore = importr('preprocessCore')

	np_matrix = np.zeros(shape=(END-BEGIN, 2))

	insert = 0

	# STEP 1

	for x in range(BEGIN, END):

		line1 = linecache.getline('../../../Master_files/input/' + INPUT[0], x)
		line2 = linecache.getline('../../../Master_files/input/' + INPUT[1], x)
		
		list1 = np.array(line1.split('\t'))
		list2 = np.array(line2.split('\t'))

		np_matrix[insert] = np.array([list1[VALUE], list2[VALUE]])
		
		insert += 1

	# STEP 2
	
	vector = robjects.FloatVector([ element for column in np_matrix for element in column ])
	matrix = robjects.r['matrix'](vector, ncol = len(np_matrix[0]), byrow=False)
	R_normalized_matrix = preprocessCore.normalize_quantiles(matrix)
	normalized_matrix = np.array(R_normalized_matrix)
	
	add_noise(BEGIN, END, normalized_matrix)


def add_noise(BEGIN, END, normalized_matrix):

	""" Adding noise to a normalized matrix.
	Formula for noise is defined by the authors of the CIBERSORT paper.
	"""

	for i in range(len(normalized_matrix)):
		for j in range(len(normalized_matrix[i])):

			f = random.uniform(0.0, 0.99999)
			q = 11.6
			N = np.random.normal(0,f*q)
			noise = 2 ** N
			normalized_matrix[i][j] += noise
	
	write_to_file(BEGIN, END, normalized_matrix)


def write_to_file(BEGIN, END, normalized_matrix):

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



read_args();
quantile_normalisation_package(BEGIN1, END1);


# def quantile_normalization():

# 	""" Quantile normalization for mean value between to .CEL files.
# 	STEP 1: Read file and add 'mean' to list.
# 	STEP 2: Sort hence to 'mean', but keep the original index as well: [original index , sorted index based on mean ].
# 	STEP 3: Calculate 'mean' using the sorted index in arrays: A[0] + B[0] / 2.0 = mean.
# 	STEP 4: Add the new 'mean' to the original array which is sorted hence to the original index.
# 	"""

# 	np_dictionary1 = np.zeros(shape=(END-BEGIN,2))
# 	np_dictionary2 = np.zeros(shape=(END-BEGIN,2))

# 	insert = 0

# 	# STEP 1

# 	for x in range(BEGIN, END):
# 		line1 = linecache.getline('files/input/' + INPUT[0], x)
# 		line2 = linecache.getline('files/input/' + INPUT[1], x)
		
# 		list1 = np.array(line1.split('\t'), dtype=float)
# 		list2 = np.array(line2.split('\t'), dtype=float)

# 		np_dictionary1[insert] = np.array([insert, list1[MEAN]])
# 		np_dictionary2[insert] = np.array([insert, list2[MEAN]])

# 		insert += 1

# 	print (np_dictionary1)
# 	print (np_dictionary2)

# 	# STEP 2

# 	np_sorted_dictionary1 = np.argsort(np_dictionary1, axis=0)
# 	np_sorted_dictionary2 = np.argsort(np_dictionary2, axis=0)

# 	# STEP 3

# 	np_combined = np.zeros(shape=(END-BEGIN,2))

# 	for x in range(0, END-BEGIN):
# 		np_combined[x] = [x, (np_dictionary1[np_sorted_dictionary1[x][1]][1] + np_dictionary2[np_sorted_dictionary2[x][1]][1]) / 2.0]

# 	# STEP 4

# 	np_array1 = np.zeros(END-BEGIN)
# 	np_array2 = np.zeros(END-BEGIN)

# 	for x in range(0, END-BEGIN):
# 		np_array1[np_sorted_dictionary1[x][1]] = np_combined[x][1]
# 		np_array2[np_sorted_dictionary2[x][1]] = np_combined[x][1]

# 	print (np_array1)
# 	print (np_array2)	


#quantile_normalization();