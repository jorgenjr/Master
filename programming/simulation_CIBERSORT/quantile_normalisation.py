
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


def algo(GENE_VALUES_MATRIX):

	""" Quantile normalization for mean value between to .CEL files.
	Calculate vectors, create matrix based on vectors and normalize the matrix with quantile normalisation.
	"""
	print("3: ", GENE_VALUES_MATRIX[0])
	preprocessCore = importr('preprocessCore')
	vector = robjects.FloatVector([ element for column in GENE_VALUES_MATRIX for element in column ])
	print("4: ", vector[0])
	print("4: ", vector[1])
	matrix = robjects.r['matrix'](vector, ncol = len(GENE_VALUES_MATRIX[0]), byrow=False)
	print("5: ", matrix[0])
	print("5: ", matrix[1])
	R_normalized_matrix = preprocessCore.normalize_quantiles(matrix)
	print("6: ", R_normalized_matrix[0])
	print("6: ", R_normalized_matrix[1])
	normalized_matrix = np.array(R_normalized_matrix)
	print("7: ", normalized_matrix[0])
	print("7: ", normalized_matrix[1])
	return normalized_matrix