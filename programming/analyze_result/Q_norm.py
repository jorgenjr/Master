
import numpy as np


def quantile(GENE_VALUES_MATRIX):

	""" An array with samples in the columns and probes across the rows

	import numpy as np
	"""

	A = GENE_VALUES_MATRIX

	AA = np.zeros_like(A)

	I = np.argsort(A,axis=0)

	AA[I,np.arange(A.shape[1])] = np.mean(A[I,np.arange(A.shape[1])],axis=1)[:,np.newaxis]

	return AA


def Q_norm():

	f_r = open('../../../Master_files/external/GSE26495.txt', 'r')

	naive = []
	high = []
	low = []
	matrix = []

	header = True

	for line in f_r:

		splitted_line = line.split('\t')
		matrix.append(splitted_line)

		if header == True:
			header = False
			continue

		temp_n = []
		temp_h = []
		temp_l = []

		for i in range(1, len(splitted_line)):

			if i <= 4:
				temp_n.append(float(splitted_line[i]))
			elif i <= 10:
				temp_h.append(float(splitted_line[i]))
			else:
				temp_l.append(float(splitted_line[i]))

		naive.append(temp_n)
		high.append(temp_h)
		low.append(temp_l)

	np_naive = np.zeros(shape=(len(naive), len(naive[0])))
	np_high = np.zeros(shape=(len(high), len(high[0])))
	np_low = np.zeros(shape=(len(low), len(low[0])))

	for i in range(len(naive)):

		np_naive[i] = naive[i]
		np_high[i] = high[i]
		np_low[i] = low[i]

	np_naive = quantile(np_naive)
	np_high = quantile(np_high)
	np_low = quantile(np_low)

	np_all = np.zeros(shape=(len(naive), 16))

	for i in range(len(naive)):

		temp_list = [	np_naive[i][0], np_naive[i][1], np_naive[i][2], np_naive[i][3], 
						np_high[i][0], np_high[i][1], np_high[i][2], np_high[i][3], np_high[i][4], np_high[i][5],
						np_low[i][0], np_low[i][1], np_low[i][2], np_low[i][3], np_low[i][4], np_low[i][5]]
		np_all[i] = np.array(temp_list)

	np_all = quantile(np_all)

	f_w = open('../../../Master_files/external/GSE26495_quantile.txt', 'w')
	header = True

	if header == True:
		f_w.write(str(matrix[0][0]) + '\t' + str(matrix[0][1]) + '\t' + str(matrix[0][2]) + '\t' + str(matrix[0][3]) + '\t' + str(matrix[0][4]) + '\t' + str(matrix[0][5]) + '\t' + str(matrix[0][6]) + '\t' + str(matrix[0][7]) + '\t' + str(matrix[0][8]) + '\t' + str(matrix[0][9]) + '\t' + str(matrix[0][10]) + '\t' + str(matrix[0][11]) + '\t' + str(matrix[0][12]) + '\t' + str(matrix[0][13]) + '\t' + str(matrix[0][14]) + '\t' + str(matrix[0][15]) + '\t' + str(matrix[0][16])) 

	for i in range(len(np_all)):

		f_w.write(str(matrix[i+1][0]) + '\t' + str(np_all[i][0]) + '\t' + str(np_all[i][1]) + '\t' + str(np_all[i][2]) + '\t' + str(np_all[i][3]) + '\t' + str(np_all[i][4]) + '\t' + str(np_all[i][5]) + '\t' + str(np_all[i][6]) + '\t' + str(np_all[i][7]) + '\t' + str(np_all[i][8]) + '\t' + str(np_all[i][9]) + '\t' + str(np_all[i][10]) + '\t' + str(np_all[i][11]) + '\t' + str(np_all[i][12]) + '\t' + str(np_all[i][13]) + '\t' + str(np_all[i][14]) + '\t' + str(np_all[i][15]) + '\n')

	f_r.close()
	f_w.close()


Q_norm()