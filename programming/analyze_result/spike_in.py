
import readline
import linecache
import numpy as np
import time
import sys


def spike_in():

	# READ DATA
	# genes, mixA, mixB, mixC, mixD, cell_line = read_mixture()
	genes, mixA, mixB, mixC, mixD, t_high, t_low = read_mixture_GSE26495()
	tumor = read_tumor()
	
	# Q-NORM
	mixA_norm = quantile_normalization(mixA)
	mixB_norm = quantile_normalization(mixB)
	mixC_norm = quantile_normalization(mixC)
	mixD_norm = quantile_normalization(mixD)
	tumor_norm = quantile_normalization(tumor)
	# cell_line_norm = quantile_normalize(cell_line)
	t_high_norm = quantile_normalization(t_high)
	t_low_norm = quantile_normalization(t_low)

	# SPIKE IN 70% TUMOR AND 0% -> 10% CELL LINE
	final_mixture = []

	for spike in range(0, 11, 1):

		# f = open('../../../Master_files/analyze_result/mixture_tumor_70_Raji_' + str(spike), 'w')
		f = open('../../../Master_files/analyze_result/new_mixture_tumor_0_GSE26495_h' + str(10-spike), 'w')
		f.write("Genes\tMIX A\tMIX B\tMIX C\tMIX D\n")
		# print(spike/100)
		# print((10-spike)/100)
		# print(len(tumor_norm))
		for i in range(len(tumor_norm)):

			a = (mixA_norm[i][0] + mixA_norm[i][1] + mixA_norm[i][2]) / 3.0
			b = (mixB_norm[i][0] + mixB_norm[i][1] + mixB_norm[i][2]) / 3.0
			c = (mixC_norm[i][0] + mixC_norm[i][1] + mixC_norm[i][2]) / 3.0
			d = (mixD_norm[i][0] + mixD_norm[i][1] + mixD_norm[i][2]) / 3.0
			t = (tumor_norm[i][0] + tumor_norm[i][1]) / 2.0
			# cl = (cell_line_norm[i][0] + cell_line_norm[i][1] + cell_line_norm[i][2]) / 3.0
			th = (t_high_norm[i][0] + t_high_norm[i][1] + t_high_norm[i][2] + t_high_norm[i][3] + t_high_norm[i][4] + t_high_norm[i][5]) / 6.0
			tl = (t_low_norm[i][0] + t_low_norm[i][1] + t_low_norm[i][2] + t_low_norm[i][3] + t_low_norm[i][4] + t_low_norm[i][5]) / 6.0
			
			# a = (a * (0.3 - (spike / 100))) + (t * 0.7) + (cl * (spike / 100))
			# b = (b * (0.3 - (spike / 100))) + (t * 0.7) + (cl * (spike / 100))
			# c = (c * (0.3 - (spike / 100))) + (t * 0.7) + (cl * (spike / 100))
			# d = (d * (0.3 - (spike / 100))) + (t * 0.7) + (cl * (spike / 100))
			# a = (a * 0.2 + t * 0.7 + (th * ((10 - spike) / 100)) + (tl * (spike / 100)))
			# b = (b * 0.2 + t * 0.7 + (th * ((10 - spike) / 100)) + (tl * (spike / 100)))
			# c = (c * 0.2 + t * 0.7 + (th * ((10 - spike) / 100)) + (tl * (spike / 100)))
			# d = (d * 0.2 + t * 0.7 + (th * ((10 - spike) / 100)) + (tl * (spike / 100)))
			a = (a * (1.0 - ((10 - spike) / 100)) + (th * ((10 - spike) / 100)))
			b = (b * (1.0 - ((10 - spike) / 100)) + (th * ((10 - spike) / 100)))
			c = (c * (1.0 - ((10 - spike) / 100)) + (th * ((10 - spike) / 100)))
			d = (d * (1.0 - ((10 - spike) / 100)) + (th * ((10 - spike) / 100)))

			# print((th * (spike / 30)))
			# print((tl * (spike / 100)))
			# print((th * (10 - spike) / 100))
			# print((10 - spike) / 100)
			# print(spike / 100)
			# print(th * (10 - spike) / 100)
			# print(tl * (spike / 100))

			f.write(genes[i]+'\t'+str(a)+'\t'+str(b)+'\t'+str(c)+'\t'+str(d)+'\n')


def new_spike_in():

	# READ DATA
	genes, mixA, mixB, mixC, mixD, t_high, t_low = read_mixture_GSE26495()
	# genes, mixA, mixB, mixC, mixD, raji = read_mixture()
	tumor = read_tumor()
	
	# Q-NORM
	mixA_norm = quantile_normalization(mixA)
	mixB_norm = quantile_normalization(mixB)
	mixC_norm = quantile_normalization(mixC)
	mixD_norm = quantile_normalization(mixD)
	# raji_norm = quantile_normalization(raji)
	tumor_norm = quantile_normalization(tumor)
	t_high_norm = quantile_normalization(t_high)
	t_low_norm = quantile_normalization(t_low)
	
	np_a = np.zeros((len(mixA_norm), 1))
	np_b = np.zeros((len(mixB_norm), 1))
	np_c = np.zeros((len(mixC_norm), 1))
	np_d = np.zeros((len(mixD_norm), 1))
	# np_r = np.zeros((len(raji_norm), 1))
	np_t = np.zeros((len(tumor_norm), 1))
	np_h = np.zeros((len(t_high), 1))
	np_l = np.zeros((len(t_low), 1))

	for i in range(len(tumor_norm)):
		np_a[i] = (mixA_norm[i][0] + mixA_norm[i][1] + mixA_norm[i][2]) / 3.0
		np_b[i] = (mixB_norm[i][0] + mixB_norm[i][1] + mixB_norm[i][2]) / 3.0
		np_c[i] = (mixC_norm[i][0] + mixC_norm[i][1] + mixC_norm[i][2]) / 3.0
		np_d[i] = (mixD_norm[i][0] + mixD_norm[i][1] + mixD_norm[i][2]) / 3.0
		# np_r[i] = (raji_norm[i][0] + raji_norm[i][1] + raji_norm[i][2]) / 3.0
		np_t[i] = (tumor_norm[i][0] + tumor_norm[i][1]) / 2.0
		np_h[i] = (t_high[i][0] + t_high[i][1] + t_high[i][2] + t_high[i][3] + t_high[i][4] + t_high[i][5]) / 6.0
		np_l[i] = (t_low[i][0] + t_low[i][1] + t_low[i][2] + t_low[i][3] + t_low[i][4] + t_low[i][5]) / 6.0

	# A_norm = np.concatenate((np_a, np_t, np_r), axis=1)
	# B_norm = np.concatenate((np_b, np_t, np_r), axis=1)
	# C_norm = np.concatenate((np_c, np_t, np_r), axis=1)
	# D_norm = np.concatenate((np_d, np_t, np_r), axis=1)
	# A_norm = np.concatenate((np_a, np_t, np_l), axis=1)
	# B_norm = np.concatenate((np_b, np_t, np_l), axis=1)
	# C_norm = np.concatenate((np_c, np_t, np_l), axis=1)
	# D_norm = np.concatenate((np_d, np_t, np_l), axis=1)
	A_norm = np.concatenate((np_a, np_t, np_l, np_h), axis=1)
	B_norm = np.concatenate((np_b, np_t, np_l, np_h), axis=1)
	C_norm = np.concatenate((np_c, np_t, np_l, np_h), axis=1)
	D_norm = np.concatenate((np_d, np_t, np_l, np_h), axis=1)

	A_norm = quantile_normalization(A_norm)
	B_norm = quantile_normalization(B_norm)
	C_norm = quantile_normalization(C_norm)
	D_norm = quantile_normalization(D_norm)

	# SPIKE IN 70% TUMOR AND 0% -> 10% CELL LINE
	final_mixture = []

	for spike in range(0, 11, 1):

		# fA = open('../../../Master_files/analyze_result/new_norm_mixtureA_tumor_0_GSE26495_h' + str(10-spike) + '_l' + str(spike), 'w')
		# fB = open('../../../Master_files/analyze_result/new_norm_mixtureB_tumor_0_GSE26495_h' + str(10-spike) + '_l' + str(spike), 'w')
		# fC = open('../../../Master_files/analyze_result/new_norm_mixtureC_tumor_0_GSE26495_h' + str(10-spike) + '_l' + str(spike), 'w')
		# fD = open('../../../Master_files/analyze_result/new_norm_mixtureD_tumor_0_GSE26495_h' + str(10-spike) + '_l' + str(spike), 'w')
		f = open('../../../Master_files/analyze_result/mixture_tumor_70_GSE26495_l' + str(spike) + '_h' + str(10-spike), 'w')
		
		f.write("Genes\tMIX A\tMIX B\tMIX C\tMIX D\n")

		for i in range(len(tumor_norm)):

			# a = (A_norm[i][0] * (0.3 - (spike / 100)) + (A_norm[i][1] * 0.7) + (A_norm[i][2] * (spike / 100)))
			# b = (B_norm[i][0] * (0.3 - (spike / 100)) + (B_norm[i][1] * 0.7) + (B_norm[i][2] * (spike / 100)))
			# c = (C_norm[i][0] * (0.3 - (spike / 100)) + (C_norm[i][1] * 0.7) + (C_norm[i][2] * (spike / 100)))
			# d = (D_norm[i][0] * (0.3 - (spike / 100)) + (D_norm[i][1] * 0.7) + (D_norm[i][2] * (spike / 100)))
			# a = (A_norm[i][0] * (1 - (spike / 100)) + (A_norm[i][1] * 0) + (A_norm[i][2] * (spike / 100)))
			# b = (B_norm[i][0] * (1 - (spike / 100)) + (B_norm[i][1] * 0) + (B_norm[i][2] * (spike / 100)))
			# c = (C_norm[i][0] * (1 - (spike / 100)) + (C_norm[i][1] * 0) + (C_norm[i][2] * (spike / 100)))
			# d = (D_norm[i][0] * (1 - (spike / 100)) + (D_norm[i][1] * 0) + (D_norm[i][2] * (spike / 100)))
			a = (A_norm[i][0] * 0.2 + A_norm[i][1] * 0.7 + A_norm[i][2] * (spike / 100) + A_norm[i][3] * ((10 - spike) / 100))
			b = (B_norm[i][0] * 0.2 + B_norm[i][1] * 0.7 + B_norm[i][2] * (spike / 100) + B_norm[i][3] * ((10 - spike) / 100))
			c = (C_norm[i][0] * 0.2 + C_norm[i][1] * 0.7 + C_norm[i][2] * (spike / 100) + C_norm[i][3] * ((10 - spike) / 100))
			d = (D_norm[i][0] * 0.2 + D_norm[i][1] * 0.7 + D_norm[i][2] * (spike / 100) + D_norm[i][3] * ((10 - spike) / 100))


			f.write(genes[i]+'\t'+str(a)+'\t'+str(b)+'\t'+str(c)+'\t'+str(d)+'\n')
			# fA.write(genes[i]+'\t'+str(a)+'\n')
			# fB.write(genes[i]+'\t'+str(b)+'\n')
			# fC.write(genes[i]+'\t'+str(c)+'\n')
			# fD.write(genes[i]+'\t'+str(d)+'\n')

		f.close()
		# fA.close(); fB.close(); fC.close(); fD.close();


def read_mixture():

	mix = open('../../../Master_files/external/GSE11103.txt', 'r')
	genes = []; mixA = []; mixB = []; mixC = []; mixD = []; cell_line = []
	
	Jurkat1 = 18; Jurkat2 = 19; Jurkat3 = 20
	IM1 = 21; IM2 = 22; IM3 = 23
	Raji1 = 24; Raji2 = 25; Raji3 = 26
	THP1 = 27; THP2 = 28; THP3 = 29
	MA1 = 30; MA2 = 31; MA3 = 32
	MB1 = 33; MB2 = 34; MB3 = 35
	MC1 = 36; MC2 = 37; MC3 = 38
	MD1 = 39; MD2 = 40; MD3 = 41

	header = True

	for line in mix:

		if header == True:
			header = False
			continue

		splitted_line = line.split('\t')
		genes.append(splitted_line[0].replace("\"", ""))
		mixA.append([float(splitted_line[MA1]), float(splitted_line[MA2]), float(splitted_line[MA3])])
		mixB.append([float(splitted_line[MB1]), float(splitted_line[MB2]), float(splitted_line[MB3])])
		mixC.append([float(splitted_line[MC1]), float(splitted_line[MC2]), float(splitted_line[MC3])])
		mixD.append([float(splitted_line[MD1]), float(splitted_line[MD2]), float(splitted_line[MD3])])
		cell_line.append([float(splitted_line[Raji1]), float(splitted_line[Raji2]), float(splitted_line[Raji3])])

	np_a = np.zeros((len(mixA), 3))
	np_b = np.zeros((len(mixB), 3))
	np_c = np.zeros((len(mixC), 3))
	np_d = np.zeros((len(mixD), 3))
	np_r = np.zeros((len(cell_line), 3))

	for i in range(len(mixA)):

		np_a[i] = mixA[i]
		np_b[i] = mixB[i]
		np_c[i] = mixC[i]
		np_d[i] = mixD[i]
		np_r[i] = cell_line[i]

	return genes, np_a, np_b, np_c, np_d, np_r


def read_mixture_GSE26495():

	mix = open('../../../Master_files/external/GSE11103.txt', 'r')
	genes = []; mixA = []; mixB = []; mixC = []; mixD = []
	
	MA1 = 30; MA2 = 31; MA3 = 32
	MB1 = 33; MB2 = 34; MB3 = 35
	MC1 = 36; MC2 = 37; MC3 = 38
	MD1 = 39; MD2 = 40; MD3 = 41

	header = True

	for line in mix:

		if header == True:
			header = False
			continue

		splitted_line = line.split('\t')
		genes.append(splitted_line[0].replace("\"", ""))
		mixA.append([float(splitted_line[MA1]), float(splitted_line[MA2]), float(splitted_line[MA3])])
		mixB.append([float(splitted_line[MB1]), float(splitted_line[MB2]), float(splitted_line[MB3])])
		mixC.append([float(splitted_line[MC1]), float(splitted_line[MC2]), float(splitted_line[MC3])])
		mixD.append([float(splitted_line[MD1]), float(splitted_line[MD2]), float(splitted_line[MD3])])

	np_a = np.zeros((len(mixA), 3))
	np_b = np.zeros((len(mixB), 3))
	np_c = np.zeros((len(mixC), 3))
	np_d = np.zeros((len(mixD), 3))

	for i in range(len(mixA)):

		np_a[i] = mixA[i]
		np_b[i] = mixB[i]
		np_c[i] = mixC[i]
		np_d[i] = mixD[i]

	cell_lines = open('../../../Master_files/external/GSE26495.txt', 'r')
	high = []; low = [];

	H1 = 5; H2 = 6; H3 = 7; H4 = 8; H5 = 9; H6 = 10;
	L1 = 11; L2 = 12; L3 = 13; L4 = 14; L5 = 15; L6 = 16;

	header = True

	for line in cell_lines:

		if header == True:
			header = False
			continue

		splitted_line = line.split('\t')
		high.append([float(splitted_line[H1]), float(splitted_line[H2]), float(splitted_line[H3]), float(splitted_line[H4]), float(splitted_line[H5]), float(splitted_line[H6])])
		low.append([float(splitted_line[L1]), float(splitted_line[L2]), float(splitted_line[L3]), float(splitted_line[L4]), float(splitted_line[L5]), float(splitted_line[L6])])

	np_h = np.zeros((len(high), 6))
	np_l = np.zeros((len(low), 6))

	for i in range(len(high)):

		np_h[i] = high[i]
		np_l[i] = low[i]

	#return genes, mixA, mixB, mixC, mixD, high, low
	return genes, np_a, np_b, np_c, np_d, np_h, np_l


def read_tumor():
	
	tumor1 = open('../../../Master_files/external/GSM269529.txt', 'r')
	tumor2 = open('../../../Master_files/external/GSM269530.txt', 'r')
	tumor_dictionary = {}
	header = True

	for line in tumor1:

		if header == True:
			header = False
			continue
		
		line_list = np.array(line.split('\t'))
		
		if line_list[0] in tumor_dictionary:
			tumor_dictionary[line_list[0]] = np.array([tumor_dictionary[line_list[0]], line_list[1]])
		else:
			tumor_dictionary[line_list[0]] = np.array(line_list[1])

	header = True

	for line in tumor2:

		if header == True:
			header = False
			continue
		
		line_list = np.array(line.split('\t'))
		
		if line_list[0] in tumor_dictionary:
			tumor_dictionary[line_list[0]] = np.array([tumor_dictionary[line_list[0]], line_list[1]])
		else:
			tumor_dictionary[line_list[0]] = np.array(line_list[1])

	value_length = 0

	for key, value in tumor_dictionary.items():

		value_length = len(value)
		break;
	
	np_matrix_combined = np.zeros(shape=(len(tumor_dictionary), value_length))
	insert = 0

	for key, value in sorted(tumor_dictionary.items()):
		
		value_list = []

		for i in range(len(value)):
			value_list.append(value[i])
		
		np_matrix_combined[insert] = np.array(value_list)
		insert += 1

	return np_matrix_combined


def quantile_normalization(anarray):

	"""

	anarray with samples in the columns and probes across the rows

	import numpy as np

	"""

	A=anarray

	AA = np.zeros_like(A)

	I = np.argsort(A,axis=0)

	AA[I,np.arange(A.shape[1])] = np.mean(A[I,np.arange(A.shape[1])],axis=1)[:,np.newaxis]

	return AA


# spike_in()
new_spike_in()