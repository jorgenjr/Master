
import numpy as np
import random

def add_noise(normalized_matrix):

	""" Adding noise to a normalized matrix.
	Formula for noise is defined by the authors of the CIBERSORT paper.
	"""
	
	append_noise_to_values = []
	
	for j in range(len(normalized_matrix[0])):
	
		f = random.uniform(0.0, 0.99999)
		q = 11.6
		N = np.random.normal(0,f*q)
		noise = 2 ** N
		append_noise_to_values.append(normalized_matrix[0][j] + noise)
	
	return np.array(append_noise_to_values);


def add_noise_controlled(normalized_matrix, interval):

	append_noise_to_values = []

	for j in range(len(normalized_matrix)):

		f = interval / 100.0
		q = 11.6
		N = np.random.normal(0, f*q)
		noise = 2 ** N
		append_noise_to_values.append(normalized_matrix[j] + noise)

	return np.array(append_noise_to_values);