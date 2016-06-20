



f_r = open('../../../Master_files/external/GSE22153.txt', 'r')
f_w = open('../../../Master_files/convert/GSE22153_genes', 'w')

header = True

for line in f_r:

	if header == True:
		header = False
		continue

	splitted_line = line.split('\t')
	f_w.write(splitted_line[0].replace("\"", "") + '\n')

f_r.close()
f_w.close()