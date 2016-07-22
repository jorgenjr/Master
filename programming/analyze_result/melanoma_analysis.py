
import linecache



def cibersort():

	f = open('../../../Master_files/analyze_result/Melanoma_result_text.txt', 'r')
	header = True

	for line in f:

		if header == True:
			print(line[:-1])
			header = False
			continue

		splitted_line = line.split('\t')
		
		if splitted_line[2] == '-':
			continue

		if int(splitted_line[2]) >= 100:
			print(line[:-1])


def llsr():

	first_line = linecache.getline('../../../Master_files/abbas/Abbas_melanoma', 3)
	second_line = linecache.getline('../../../Master_files/abbas/Abbas_melanoma', 4)
	third_line = linecache.getline('../../../Master_files/abbas/Abbas_melanoma', 5)

	coef = [first_line[:-1].split('\t')[1:], second_line[:-1].split('\t')[1:], third_line[:-1].split('\t')[1:]]
	
	for i in range(len(coef)):
		for j in range(len(coef[i])):
			coef[i][j] = float(coef[i][j])
			if coef[i][j] < 0.0:
				coef[i][j] = 0.0

	result = [list(x) for x in zip(*coef)]

	for i in range(len(result)):
		result[i] = [float(l)/sum(result[i]) for l in result[i]]

	f = open('../../../Master_files/abbas/Abbas_melanoma_fixed', 'w')

	for i in range(len(result)):
		f.write(str(result[i][0]) + '\t' + str(result[i][1]) + '\t' + str(result[i][2]) + '\n')

	f.close()


def new_llsr():

	f = open('../../../Master_files/abbas/Abbas_melanoma_analysis', 'r')
	header = True

	for line in f:

		if header == True:
			print(line[:-1])
			header = False
			continue

		splitted_line = line.split('\t')
		
		if splitted_line[2] == '-':
			continue

		if int(splitted_line[2]) >= 100:
			print(line[:-1])


# cibersort()
# llsr()
new_llsr()