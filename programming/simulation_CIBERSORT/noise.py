
import numpy as np, random

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
	
	#write_to_file(BEGIN, END, normalized_matrix)
	return normalized_matrix;