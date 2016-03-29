
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--INPUT", help="Input")
parser.add_argument("-c", "--COMPARISON", help="Comparison file")
parser.add_argument("-f", "--FILENAME", help="Filename")

args = parser.parse_args()


def remove(INPUT, COMPARISON, FILENAME):

	f1 = open('../../../Master_files/external/' + INPUT, 'r')
	f2 = open('../../../Master_files/external/' + COMPARISON, 'r')
	f3 = open('../../../Master_files/external/' + FILENAME, 'w')

	header = True
	signature = []

	for line in f2:
		signature.append(line)

	for line in f1:

		if header == True:
			f3.write(line)
			header = False
			continue

		for i in range(len(signature)):

			s_line1 = line.split("\t")
			s_line2 = signature[i].split("\t")
			
			if s_line1[0] == s_line2[0]:
				f3.write(line)

	f1.close()
	f2.close()
	f3.close()


remove(args.INPUT, args.COMPARISON, args.FILENAME)