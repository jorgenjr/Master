
f_read = open('../../../Master_files/diff_exp/diff_exp', 'r')
f_write = open('../../../Master_files/convert/diff_exp_clean', 'w')
i = True

for line in f_read:

	if (i):
		i = False
		continue

	splitted_line = line.split('\t')
	affy = splitted_line[0].split('\"')
	f_write.write(affy[1] + '\n')

f_write.close()
