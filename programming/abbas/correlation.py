
import numpy as np
import sys

from scipy import stats


signature = [];

def signature_genes():

	f3 = open('../../../Master_files/simulation/phenotype_classes.separate_cell_lines_norm.bm.K999.0.txt', 'r')
	header = True
	for line in f3:
		if header == True:
			header = False; continue
		signature.append(line.split('\t')[:-1])
	f3.close()


def find_signature_genes(TUMOR, NOISE):

	f1 = open('../../../Master_files/abbas/LLSR_log_'+str(TUMOR)+'_'+str(NOISE), 'r')
	f2 = open('../../../Master_files/simulation/mixtures_log_tumor_'+str(TUMOR)+'_'+str(NOISE), 'r')
	global signature
	estimated = []; original = []; header = True;

	for line in f1:
		if header == True:
			header = False; continue
		splitted_line = line.split('\t')[1:]
		for i in range(len(splitted_line)):
			splitted_line[i] = splitted_line[i].replace("\"", "")
		estimated.append(splitted_line)
	header = True
	for line in f2:
		if header == True:
			header = False; continue
		original.append(line.split('\t'))

	new_estimated = []; new_original = [];

	for i in range(len(signature)):
		for j in range(len(estimated)):
			if signature[i][0] == estimated[j][0]:
				new_estimated.append(estimated[j])
			if signature[i][0] == original[j][0]:
				new_original.append(original[j])
	
	for i in range(len(new_estimated)):
		new_estimated[i] = [float(new_estimated[i][1]), float(new_estimated[i][2]), float(new_estimated[i][3]), float(new_estimated[i][4])]
		new_original[i] = [float(new_original[i][1]), float(new_original[i][2]), float(new_original[i][3]), float(new_original[i][4])]

	corr1 = stats.pearsonr(column(new_estimated,0), column(new_original, 0))
	corr2 = stats.pearsonr(column(new_estimated,1), column(new_original, 1))
	corr3 = stats.pearsonr(column(new_estimated,2), column(new_original, 2))
	corr4 = stats.pearsonr(column(new_estimated,3), column(new_original, 3))

	f1.close(); f2.close();

	return str((corr1[0]+corr2[0]+corr3[0]+corr4[0]) / 4.0)


def all_genes(TUMOR, NOISE):

	f1 = open('../../../Master_files/abbas/LLSR_tumor_present_'+str(TUMOR)+'_'+str(NOISE), 'r')
	f2 = open('../../../Master_files/simulation/mixtures_normalized_tumor_'+str(TUMOR)+'_'+str(NOISE), 'r')
	global signature
	estimated = []; original = []; cells = []; header = True;

	for line in f1:
		if header == True:
			header = False; continue
		splitted_line = line.split('\t')[1:]
		for i in range(len(splitted_line)):
			splitted_line[i] = splitted_line[i].replace("\"", "")
		estimated.append(splitted_line)
	header = True
	for line in f2:
		if header == True:
			header = False; continue
		original.append(line.split('\t'))
	
	for i in range(len(estimated)):
		estimated[i] = [float(estimated[i][1]), float(estimated[i][2]), float(estimated[i][3]), float(estimated[i][4])]
		original[i] = [float(original[i][1]), float(original[i][2]), float(original[i][3]), float(original[i][4])]

	corr1 = stats.pearsonr(column(estimated,0), column(original, 0))
	corr2 = stats.pearsonr(column(estimated,1), column(original, 1))
	corr3 = stats.pearsonr(column(estimated,2), column(original, 2))
	corr4 = stats.pearsonr(column(estimated,3), column(original, 3))

	f1.close(); f2.close();

	return str((corr1[0]+corr2[0]+corr3[0]+corr4[0]) / 4.0)


def column(matrix, i):
    return [row[i] for row in matrix]

f4 = open('../../../Master_files/abbas/correlation_lognormal', 'w')
signature_genes()
counter = 0
for i in range(0, 100, 5):
	for j in range(0, 100, 5):
		corr = find_signature_genes(i, j)
		# corr = all_genes(i, j)
		f4.write(corr+'\t')
		counter += 1
		print("Done with " + str(counter) + " files.")
	f4.write('\n')

f4.close();