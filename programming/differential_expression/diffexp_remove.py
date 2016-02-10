
def write_only_geneid():

	""" Reads the data produced from 'differential_expression_r.R' and writes
	only the gene IDs to file.
	"""

	f_read = open('../../../Master_files/diff_exp/diff_exp', 'r')
	f_write = open('../../../Master_files/diff_exp/diff_exp_clean', 'w')
	header = True

	for line in f_read:

		if (header == True):
			header = False
			continue

		splitted_line = line.split('\t')
		affy = splitted_line[0].split('\"')
		f_write.write(affy[1] + '\n')

	f_write.close()

write_only_geneid()