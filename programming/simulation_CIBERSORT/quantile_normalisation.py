
import readline, linecache, numpy as np, rpy2.robjects as robjects, time

from rpy2.robjects.packages import importr


def algo(GENE_VALUES_MATRIX):

	# """ Quantile normalization for mean value between to .CEL files.
	# Calculate vectors, create matrix based on vectors and normalize the matrix with quantile normalisation.
	# """
	
	# preprocessCore = importr('preprocessCore')
	# vector = robjects.FloatVector([ element for column in GENE_VALUES_MATRIX for element in column ])
	# matrix = robjects.r['matrix'](vector, ncol = len(GENE_VALUES_MATRIX[0]), byrow=False)
	# R_normalized_matrix = preprocessCore.normalize_quantiles(matrix)

	# test_norm_matrix = []
	
	# for i in range(0,len(R_normalized_matrix),len(GENE_VALUES_MATRIX[0])):
		
	# 	gene_matrix = []
		
	# 	for j in range(i,i+len(GENE_VALUES_MATRIX[0])):			
	# 		gene_matrix.append(R_normalized_matrix[j])

	# 	test_norm_matrix.append(gene_matrix)
	# 	i += len(GENE_VALUES_MATRIX[0])

	# normalized_matrix = np.array(test_norm_matrix)

	# return normalized_matrix

	"""

	anarray with samples in the columns and probes across the rows

	import numpy as np

	"""

	A=GENE_VALUES_MATRIX

	AA = np.zeros_like(A)

	I = np.argsort(A,axis=0)

	AA[I,np.arange(A.shape[1])] = np.mean(A[I,np.arange(A.shape[1])],axis=1)[:,np.newaxis]

	return AA