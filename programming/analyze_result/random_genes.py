
import readline
import linecache
import numpy as np
import rpy2.robjects as robjects
import time

from random import randint
from rpy2.robjects.packages import importr


def random_genes():

	f1 = open('../../../Master_files/external/GSE11103_HUGO.txt', 'r')
	f2 = open('../../../Master_files/convert/phenotype_classes.reference_hugo_unique.bm.K999.0.txt', 'r')
	f3 = open('../../../Master_files/external/random_signature_genesQ', 'w')

	GSE = []; old_signature = []; new_signature = []; header = True; prev_numbers = [];

	for line in f1:
		if header == True:
			header = False; continue
		GSE.append(line.split('\t'))

	for line in f2:
		if header == True:
			header = False; continue
		old_signature.append(line.split('\t'))
	
	num_genes = 221

	for i in range(num_genes):
		random_gene_found = False; gene = None
		while random_gene_found == False:
			random = randint(0, len(GSE))
			if random in prev_numbers:
				continue
			gene_array = GSE[random]
			old = False
			for j in range(len(old_signature)):
				if gene_array[0] == old_signature[j][0]:
					old = True
			prev_numbers.append(random)
			if old == False:
				new_signature.append(gene_array)
				random_gene_found = True

	Jurkat = []; IM9 = []; Raji = []; THP1 = [];
	new_signature.sort()
	for i in range(len(new_signature)):
		Jurkat.append([float(new_signature[i][18]), float(new_signature[i][19]), float(new_signature[i][20])])
		IM9.append([float(new_signature[i][21]), float(new_signature[i][22]), float(new_signature[i][23])])
		Raji.append([float(new_signature[i][24]), float(new_signature[i][25]), float(new_signature[i][26])])
		THP1.append([float(new_signature[i][27]), float(new_signature[i][28]), float(new_signature[i][29])])

	Jurkat = algo(Jurkat); IM9 = algo(IM9); Raji = algo(Raji); THP1 = algo(THP1)

	for i in range(len(new_signature)):
		new_signature[i] = [new_signature[i][0], (Jurkat[i][0]+Jurkat[i][1]+Jurkat[i][2])/3.0, (IM9[i][0]+IM9[i][1]+IM9[i][2])/3.0, (Raji[i][0]+Raji[i][1]+Raji[i][2])/3.0, (THP1[i][0]+THP1[i][1]+THP1[i][2])/3.0]
	
	f3.write('Gene symbol\tJurkat\tIM-9\tRaji\tTHP-1\n')
	for i in range(len(new_signature)):
		f3.write(new_signature[i][0]+'\t'+str(new_signature[i][1])+'\t'+str(new_signature[i][2])+'\t'+str(new_signature[i][3])+'\t'+str(new_signature[i][4])+'\n')


def algo(GENE_VALUES_MATRIX):
	""" Quantile normalization for mean value between to .CEL files.
	Calculate vectors, create matrix based on vectors and normalize the matrix with quantile normalisation.
	"""
	
	preprocessCore = importr('preprocessCore')
	vector = robjects.FloatVector([ element for column in GENE_VALUES_MATRIX for element in column ])
	matrix = robjects.r['matrix'](vector, ncol = len(GENE_VALUES_MATRIX[0]), byrow=False)
	R_normalized_matrix = preprocessCore.normalize_quantiles(matrix)

	test_norm_matrix = []
	
	for i in range(0,len(R_normalized_matrix),len(GENE_VALUES_MATRIX[0])):
		
		gene_matrix = []
		
		for j in range(i,i+len(GENE_VALUES_MATRIX[0])):			
			gene_matrix.append(R_normalized_matrix[j])

		test_norm_matrix.append(gene_matrix)
		i += len(GENE_VALUES_MATRIX[0])

	normalized_matrix = np.array(test_norm_matrix)

	return normalized_matrix


random_genes()