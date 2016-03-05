
import readline, os, sys, timeit

#from subprocess import call
import subprocess

PATH = "/home/jorgen/Projects/";

FLAGS = []
MIXTURES = []
TUMORS = []


def read_args():

	""" Reading the arguments sent by the user from the terminal.
	-i flag must be followed by input file(s)
	-o flag must be followed by output file(s)

	The given files must be placed outside the "Master" folder:
	Code: folder_name/Master/programming/simulation_CIBERSORT/simulation.py
	Files: folder_name/Master_files/simulation/

	E.g.: python simulation.py -i GSM269529.txt -o GSM269529_NEW.txt
	"""

	if len(sys.argv) == 1:
		print('\n[ERROR] Wrong sys.argv format! Too few arguments. Example run:\n\npython simulation.py -m [mixture.file mixture.file ...] -t [tumor.file tumor.file]\n')
		sys.exit()

	m = False; t = False;

	for x in range(1, len(sys.argv)):
		#print(sys.argv[x])
		# INPUT
		if sys.argv[x] == '-i':
			print(sys.argv[x])
		# CELL LINE
		elif sys.argv[x] == '-c':
			FLAGS.append("C")
			continue
		# MIXTURE
		elif sys.argv[x] == '-m':
			FLAGS.append("M")
			m = True; t = False;
			continue
		# SIGNATURE
		elif sys.argv[x] == '-r':
			FLAGS.append("R")
			continue
		# TUMOR
		elif sys.argv[x] == '-t':
			FLAGS.append("T")
			m = False; t = True;
			continue

		if m == True:
			MIXTURES.append(sys.argv[x])
			continue

		elif t == True:
			TUMORS.append(sys.argv[x])
			continue

		print('\n[ERROR] Wrong sys.argv format! Run:\n\npython simulation.py -i [input.file input.file ...] -o [output.file output.file]\n')
		sys.exit()


def execute():
	# print (FLAGS)
	# print (MIXTURES)
	# print (TUMORS)
	start_total = timeit.default_timer()

	print("Executing simulation script ... ")
	cmd = "python " + PATH + "Master/programming/simulation_CIBERSORT/simulation.py -t GSM269529.txt GSM269530.txt -m GSE11103.txt"
	start = timeit.default_timer()
	os.system(cmd)
	stop = timeit.default_timer()
	print("Time spent: %.2f seconds" % (stop - start)) 


	print("Simulation completed! Converting Affy to HUGO ... ")
	cmd = "python " + PATH + "Master/programming/convert_geneID/replace.py -t"
	start = timeit.default_timer()
	os.system(cmd)
	stop = timeit.default_timer()
	print("Time spent: %.2f seconds" % (stop - start))

	print("Conversion completed! Executing CIBERSORT ... ")
	cmd = "java -Xmx3g -Xms3g -jar " + PATH + "CIBERSORT/CIBERSORT.jar -M " + PATH + "Master_files/convert/simulation_hugo_unique_tumor_0 -B " + PATH + "Master_files/output/signature_tumor_0.txt > " + PATH + "Master_files/output/CIBERSORT_result_tumor_0"
	start = timeit.default_timer()
	os.system(cmd)
	stop = timeit.default_timer()
	print("Time spent: %.2f seconds" % (stop - start))

	print("CIBERSORT completed! Exexuting Abbas ... ")
	cmd = "Rscript " + PATH + "Master/programming/abbas/abbas.r"
	start = timeit.default_timer()
	os.system(cmd)
	stop = timeit.default_timer()
	print("Time spent: %.2f seconds" % (stop - start))

	stop_total = timeit.default_timer()
	print("Total time spent: %.2f seconds" % (stop_total - start_total))

read_args()
execute()