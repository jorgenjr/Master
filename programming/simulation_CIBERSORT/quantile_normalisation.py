
import linecache, numpy as np, rpy2.robjects as robjects
from rpy2.robjects.packages import importr

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

def step_one(BEGIN, END, INPUT):

	np_matrix = np.zeros(shape=(END-BEGIN, 2))
	insert = 0

	for x in range(BEGIN, END):

		line1 = linecache.getline('../../../Master_files/input/' + INPUT[0], x)
		line2 = linecache.getline('../../../Master_files/input/' + INPUT[1], x)
		
		list1 = np.array(line1.split('\t'))
		list2 = np.array(line2.split('\t'))

		np_matrix[insert] = np.array([list1[VALUE], list2[VALUE]])
		
		insert += 1

	return np_matrix


def step_two(np_matrix):

	preprocessCore = importr('preprocessCore')
	vector = robjects.FloatVector([ element for column in np_matrix for element in column ])
	matrix = robjects.r['matrix'](vector, ncol = len(np_matrix[0]), byrow=False)
	R_normalized_matrix = preprocessCore.normalize_quantiles(matrix)
	normalized_matrix = np.array(R_normalized_matrix)

	return normalized_matrix


def algo(BEGIN, END, INPUT):

	""" Quantile normalization for mean value between to .CEL files.
	STEP 1: Read file and add 'mean' to list.
	STEP 2: Calculate vectors, create matrix based on vectors and normalize the matrix with quantile normalisation.
	"""

	np_matrix = step_one(BEGIN, END, INPUT)
	normalized_matrix = step_two(np_matrix)
	
	return normalized_matrix



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