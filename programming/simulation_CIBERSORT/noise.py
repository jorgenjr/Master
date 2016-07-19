
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

	append_noise_to_values = []

	for j in range(len(normalized_matrix)):

		f = interval / 100.0
		q = 11.6
		N = np.random.normal(0, f*q)
		noise = 2 ** N
		append_noise_to_values.append(normalized_matrix[j] + noise)

	return np.array(append_noise_to_values);


def add_log_noise_controlled(normalized_matrix, interval):

	append_noise_to_values = []

	for j in range(len(normalized_matrix)):

		while (True):

			try:
				f = interval / 100.0
				q = 11.6
				N = np.random.normal(0, f*q)
				noise = 2 ** N
				append_noise_to_values.append(normalized_matrix[j] + noise)
				break
			except OverflowError as e:
				print(e)

	return np.array(append_noise_to_values);


def new_noise():

	f = open('../../../Master_files/simulation/mixtures_newman_replication_tumor_0_0', 'r')

	A = []; B = []; C = []; D = [];
	header = True

	for line in f:
		if header == True:
			header = False
			continue
		splitted_line = line.split('\t')
		A.append(float(splitted_line[1])); B.append(float(splitted_line[2])); C.append(float(splitted_line[3])); D.append(float(splitted_line[4]));

	np_A = np.mean(A); np_B = np.mean(B); np_C = np.mean(C); np_D = np.mean(D);
	mean = (np_A+np_B+np_C+np_D)/4.0
	print("MEAN: ", mean)
	np_A = np.std(A); np_B = np.std(B); np_C = np.std(C); np_D = np.std(D);
	std = (np_A+np_B+np_C+np_D)/4.0
	print("STD: ", std)
	z = 500

	noise = (1/(std*(math.sqrt(2*math.pi))))*math.exp(-(((z-mean)**2)/(2*mean**2)))
	print("NOISE: ", noise)
	dist = np.random.normal(mean, std, 1000)
	#print(dist)
	print("DIST NORMAL: ", dist[0]*0.01)
	log = np.random.lognormal(mean, np.log2(std), 10)
	print("LOG: ", log)
	print("LOG2 STD: ", np.log2(std))

	print(A[0])
	f = 100 / 100.0
	q = 11.6
	N = np.random.normal(0, f*q)
	noise = 2 ** N
	print(noise)

	for i in range(0,10):
		while (True):
			try:
				NN = np.random.lognormal(0, f*q)
				nnoise = 2 ** NN
				print(nnoise)
				break
			except OverflowError as e:
				print(e)

# new_noise()