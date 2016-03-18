
import readline, os, sys, timeit

#from subprocess import call
import subprocess

PATH = "/home/jorgen/Projects/";
START_TUMOR = 0
STOP_TUMOR = 101
STEP_TUMOR = 5
START_NOISE = 0
STOP_NOISE = 100
STEP_NOISE = 30
REFERENCE_FILE = PATH + "Master_files/convert/reference_hugo_unique_tumor"
PHENOTYPE_CLASSES_FILE = PATH + "Master_files/simulation/phenotype_classes_tumor"

FLAGS = []
MIXTURES = []
TUMORS = []
CELL_LINES = []


def read_args():

	""" Reading the arguments sent by the user from the terminal.
	-i flag must be followed by input file(s)
	-o flag must be followed by output file(s)

	The given files must be placed outside the "Master" folder:
	Code: folder_name/Master/programming/simulation_CIBERSORT/simulation.py
	Files: folder_name/Master_files/simulation/

	E.g.: python blackbox.py -m GSE11103.txt -t GSM269529.txt GSM269530.txt
	"""

	if len(sys.argv) == 1:
		print('\n[ERROR] Wrong sys.argv format! Too few arguments. Example run:\n\npython blackbox.py -m [mixture.file mixture.file ...] -t [tumor.file tumor.file]\n')
		sys.exit()

	m = False; t = False; c = False;

	for x in range(1, len(sys.argv)):
		
		# CELL LINE
		if sys.argv[x] == '-c':
			FLAGS.append("C")
			m = False; t = False; c = True;
			continue
		# MIXTURE
		elif sys.argv[x] == '-m':
			FLAGS.append("M")
			m = True; t = False; c = False;
			continue
		# SIGNATURE
		elif sys.argv[x] == '-r':
			FLAGS.append("R")
			continue
		# TUMOR
		elif sys.argv[x] == '-t':
			FLAGS.append("T")
			m = False; t = True; c = False;
			continue

		if m == True:
			MIXTURES.append(sys.argv[x])
			continue

		elif t == True:
			TUMORS.append(sys.argv[x])
			continue

		elif c == True:
			CELL_LINES.append(sys.argv[x])
			continue

		print('\n[ERROR] Wrong sys.argv format! Run:\n\npython blackbox.py -m [mixture.file mixture.file ...] -t [tumor.file tumor.file]\n')
		sys.exit()


def arguments():

	cmd = ""

	if len(MIXTURES) > 0:
		cmd += "-m"
		for i in range(len(MIXTURES)):
			cmd += " " + MIXTURES[i]
		cmd += " "

	if len(TUMORS) > 0:
		cmd += "-t"
		for i in range(len(TUMORS)):
			cmd += " " + TUMORS[i]
		cmd += " "

	if len(CELL_LINES) > 0:
		cmd += "-c"
		for i in range(len(CELL_LINES)):
			cmd += " " + CELL_LINES[i]
		cmd += " "

	return cmd


def execute():

	start_total = timeit.default_timer()

	print("Executing simulation script ... ")
	cmd = "python " + PATH + "Master/programming/simulation_CIBERSORT/simulation.py " + arguments()
	start = timeit.default_timer()
	#os.system(cmd)
	stop = timeit.default_timer()
	print("Time spent: %.2f seconds" % (stop - start)) 


	print("Simulation completed! Converting Affy to HUGO ... ")
	cmd = "python " + PATH + "Master/programming/convert_geneID/replace.py -t"
	start = timeit.default_timer()
	#os.system(cmd)
	stop = timeit.default_timer()
	print("Time spent: %.2f seconds" % (stop - start))

	print("Conversion completed! Executing CIBERSORT ... ")
	files_done = 0
	start = timeit.default_timer()
	for tumor_content in range(START_TUMOR, STOP_TUMOR, STEP_TUMOR):
		for noise_content in range(START_NOISE, STOP_NOISE, STEP_NOISE):
			cmd = "java -Xmx3g -Xms3g -jar " + PATH + "CIBERSORT/CIBERSORT.jar -M " + PATH + "Master_files/convert/simulation_hugo_unique_tumor_" + str(tumor_content) + "_" + str(noise_content) + " -P " + REFERENCE_FILE + " -c " + PHENOTYPE_CLASSES_FILE + " > " + PATH + "Master_files/output/CIBERSORT_result_tumor_" + str(tumor_content) + "_" + str(noise_content)
			# os.system(cmd)
			files_done += 1
			print("--- CIBERSORT is done with " + str(files_done) + " files.")
	stop = timeit.default_timer()
	print("Time spent: %.2f seconds" % (stop - start))

	print("CIBERSORT completed! Exexuting Abbas ... ")
	files_done = 0
	start = timeit.default_timer()
	for tumor_content in range(START_TUMOR, STOP_TUMOR, STEP_TUMOR):
		for noise_content in range(START_NOISE, STOP_NOISE, STEP_NOISE):
			cmd = "Rscript " + PATH + "Master/programming/abbas/abbas.r " + PATH + "Master_files/simulation/combined_cell_lines_tumor " + PATH + "Master_files/simulation/mixtures_with_tumor_" + str(tumor_content) + "_" + str(noise_content) + " " + PATH + "Master_files/abbas/Abbas_result_tumor_" + str(tumor_content) + "_" + str(noise_content)
			os.system(cmd)
			files_done += 1
			print("--- Abbas is done with " + str(files_done) + " files.")
	stop = timeit.default_timer()
	print("Time spent: %.2f seconds" % (stop - start))

	print("Abbas completed! Plotting results ... ")
	cmd = "python " + PATH + "Master/programming/analyze_result/plot.py"
	start = timeit.default_timer()
	#os.system(cmd)
	stop = timeit.default_timer()
	print("Time spent: %.2f seconds" % (stop - start))

	stop_total = timeit.default_timer()
	print("Total time spent: %.2f seconds" % (stop_total - start_total))

read_args()
execute()