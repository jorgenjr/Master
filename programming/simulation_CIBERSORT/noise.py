
import numpy as np, random

def add_noise(normalized_matrix):

	""" Adding noise to a normalized matrix.
	Formula for noise is defined by the authors of the CIBERSORT paper.
	"""
	# print("normalized_matrix: ", len(normalized_matrix))
	# for i in range(len(normalized_matrix)):
	# 	for j in range(len(normalized_matrix[i])):

	# 		f = random.uniform(0.0, 0.99999)
	# 		q = 11.6
	# 		N = np.random.normal(0,f*q)
	# 		noise = 2 ** N
	# 		normalized_matrix[i][j] += noise
	
	# return normalized_matrix;

	# Because the length of normalized_matrix is always 1?
	append_noise_to_values = []
	
	for j in range(len(normalized_matrix[0])):

		f = random.uniform(0.0, 0.99999)
		q = 11.6
		N = np.random.normal(0,f*q)
		noise = 2 ** N
		append_noise_to_values.append(normalized_matrix[0][j] + noise)
	
	return np.array(append_noise_to_values);