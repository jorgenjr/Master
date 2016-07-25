
import numpy as np


def algo(GENE_VALUES_MATRIX):

	""" An array with samples in the columns and probes across the rows

	import numpy as np
	"""

	A = GENE_VALUES_MATRIX

	AA = np.zeros_like(A)

	I = np.argsort(A,axis=0)

	AA[I,np.arange(A.shape[1])] = np.mean(A[I,np.arange(A.shape[1])],axis=1)[:,np.newaxis]

	return AA


def quantile_normalize_separately(CELL_LINES_MATRIX):

	""" Quantile normalize every cell line separately.
	"""

	np_cell_lines_matrix = []

	for i in range(len(CELL_LINES_MATRIX)):
		
		np_cell_lines_matrix.append([])
		np_cell_lines_matrix[i] = np.zeros(shape=(len(CELL_LINES_MATRIX[i]), len(CELL_LINES_MATRIX[i][0])))
		
		for j in range(len(CELL_LINES_MATRIX[i])):
			np_cell_lines_matrix[i][j] = CELL_LINES_MATRIX[i][j]

	for i in range(len(CELL_LINES_MATRIX)):
		CELL_LINES_MATRIX[i] = algo(np_cell_lines_matrix[i])

	return CELL_LINES_MATRIX