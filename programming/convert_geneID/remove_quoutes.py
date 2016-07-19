


def remove_quotes():

	f_r = open('../../../Master_files/external/GSE26495.txt', 'r')
	f_w = open('../../../Master_files/external/GSE26495_new.txt', 'w')

	for line in f_r:
		splitted_line = line.split('\t')

		for i in range(len(splitted_line)):
			splitted_line[i] = splitted_line[i].replace("\"", "")
			
			if i != len(splitted_line) - 1:
				f_w.write(splitted_line[i] + '\t')
			else:
				f_w.write(splitted_line[i])

	f_r.close()
	f_w.close()


remove_quotes()