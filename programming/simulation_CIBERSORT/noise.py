
import numpy as np
import random
import math

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

	""" Adding controlled amount to a normalized matrix.
	Formula for noise is defined by the authors of the CIBERSORT paper.
	"""

	append_noise_to_values = []

	for j in range(len(normalized_matrix)):

		f = interval / 100.0
		q = 11.6
		N = np.random.normal(0, f*q)
		noise = 2 ** N
		append_noise_to_values.append(normalized_matrix[j] + noise)

	return np.array(append_noise_to_values);


def add_log_noise_controlled(normalized_matrix, interval):

	""" Adding controlled amount to a normalized matrix.
	Formula for noise is defined by the authors of the CIBERSORT paper,
	this function uses log-normal distribution instead of normal distribution.
	"""

	append_noise_to_values = []

	for j in range(len(normalized_matrix)):

		while (True):

			try:
				f = interval / 100.0
				q = 11.6
				N = np.random.lognormal(0, f*q)
				noise = 2 ** N

				if noise < 99999999.0:
					append_noise_to_values.append(normalized_matrix[j] + noise)
					break
				else:
					append_noise_to_values.append(normalized_matrix[j] + 99999999.0)
					break

			except OverflowError as e:
				continue

	return np.array(append_noise_to_values);