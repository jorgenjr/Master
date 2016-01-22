
f_read = open('../../../Master_files/output/testfile_1_1', 'r')
f_write = open('../../../Master_files/output/testfile_1_1_geneid', 'w')
i = True

for line in f_read:

	if (i):
		i = False
		continue

	splitted_line = line.split('\t')
	f_write.write(splitted_line[0] + '\n')

f_write.close()
