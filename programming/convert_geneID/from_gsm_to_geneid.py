
def from_gsm_to_geneid():

	""" Opens a GSM file, retrieves the gene IDs, and writes the IDs to a new file.
	"""

	f_read = open('../../../Master_files/simulation/testfile_1_1', 'r')
	f_write = open('../../../Master_files/convert/affy', 'w')
	header = True
	gene_ids = []

	for line in f_read:

		if (header == True):
			header = False
			continue

		splitted_line = line.split('\t')
		gene_ids.append(splitted_line[0])	

	gene_ids.sort()

	for i in range(len(gene_ids)):

		f_write.write(gene_ids[i] + '\n')

	f_write.close()

from_gsm_to_geneid()