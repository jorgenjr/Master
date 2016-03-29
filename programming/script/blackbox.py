
import readline, os, sys, timeit, argparse

#from subprocess import call
import subprocess

PATH = "/home/jorgen/Projects/";
#PATH = "/usit/abel/u1/jorgenjr/Projects/"
START_TUMOR = 0
STOP_TUMOR = 100
STEP_TUMOR = 5
START_NOISE = 0
STOP_NOISE = 100
STEP_NOISE = 5
REFERENCE_FILE = PATH + "Master_files/convert/reference_hugo_unique"
PHENOTYPE_CLASSES_FILE = PATH + "Master_files/simulation/phenotype_classes"

FLAGS = []
MIXTURES = []
TUMORS = []
CELL_LINES = []
OUTPUT = ""


parser = argparse.ArgumentParser()
parser.add_argument("-m", "--MIXTURES", help="Mixtures", nargs='*')
parser.add_argument("-t", "--TUMORS", help="Tumors", nargs='*')
parser.add_argument("-c", "--CELL_LINES", help="Cell lines", nargs='*')
parser.add_argument("-o", "--OUTPUT", help="Output")

args = parser.parse_args()

print(args.MIXTURES)
print(args.TUMORS)
print(args.CELL_LINES)
print(args.OUTPUT)

# def read_args():

# 	""" Reading the arguments sent by the user from the terminal.
# 	-i flag must be followed by input file(s)
# 	-o flag must be followed by output file(s)

# 	The given files must be placed outside the "Master" folder:
# 	Code: folder_name/Master/programming/simulation_CIBERSORT/simulation.py
# 	Files: folder_name/Master_files/simulation/

# 	E.g.: python blackbox.py -m GSE11103.txt -t GSM269529.txt GSM269530.txt
# 	"""

# 	if len(sys.argv) == 1:
# 		print('\n[ERROR] Wrong sys.argv format! Too few arguments. Example run:\n\npython blackbox.py -m [mixture.file mixture.file ...] -t [tumor.file tumor.file]\n')
# 		sys.exit()

# 	m = False; t = False; c = False; o = False;

# 	for x in range(1, len(sys.argv)):
		
# 		# CELL LINE
# 		if sys.argv[x] == '-c':
# 			FLAGS.append("C")
# 			m = False; t = False; c = True; o = False;
# 			continue
# 		# MIXTURE
# 		elif sys.argv[x] == '-m':
# 			FLAGS.append("M")
# 			m = True; t = False; c = False; o = False;
# 			continue
# 		# SIGNATURE
# 		elif sys.argv[x] == '-r':
# 			FLAGS.append("R")
# 			continue
# 		# TUMOR
# 		elif sys.argv[x] == '-t':
# 			FLAGS.append("T")
# 			m = False; t = True; c = False; o = False;
# 			continue

# 		elif sys.argv[x] == '-o':
# 			FLAGS.append("O")
# 			m = False; t = True; c = False; o = True;
# 			continue

# 		if m == True:
# 			MIXTURES.append(sys.argv[x])
# 			continue

# 		elif t == True:
# 			TUMORS.append(sys.argv[x])
# 			continue

# 		elif c == True:
# 			CELL_LINES.append(sys.argv[x])
# 			continue

# 		elif o == True:
# 			global OUTPUT
# 			OUTPUT = sys.argv[x]

# 		print('\n[ERROR] Wrong sys.argv format! Run:\n\npython blackbox.py -m [mixture.file mixture.file ...] -t [tumor.file tumor.file]\n')
# 		sys.exit()


def arguments():

	cmd = "-i " + str(START_TUMOR) + " " + str(STOP_TUMOR) + " " + str(STEP_TUMOR) + " " + str(START_NOISE) + " " + str(STOP_NOISE) + " " + str(STEP_NOISE) + " ";

	if args.MIXTURES != None and len(args.MIXTURES) > 0:
		cmd += "-m"
		for i in range(len(args.MIXTURES)):
			cmd += " " + args.MIXTURES[i]
		cmd += " "

	if args.TUMORS != None and len(args.TUMORS) > 0:
		cmd += "-t"
		for i in range(len(args.TUMORS)):
			cmd += " " + args.TUMORS[i]
		cmd += " "

	if args.CELL_LINES != None and len(args.CELL_LINES) > 0:
		cmd += "-c"
		for i in range(len(args.CELL_LINES)):
			cmd += " " + args.CELL_LINES[i]
		cmd += " "

	return cmd


# def execute():

# 	start_total = timeit.default_timer()

# 	print("Executing simulation script ... ")
# 	cmd = "python3 " + PATH + "Master/programming/simulation_CIBERSORT/simulation.py " + arguments() + " -o " + OUTPUT
# 	start = timeit.default_timer()
# 	os.system(cmd)
# 	stop = timeit.default_timer()
# 	print("Time spent: %.2f seconds" % (stop - start)) 


# 	print("Simulation completed! Converting Affy to HUGO ... ")
# 	cmd = "python3 " + PATH + "Master/programming/convert_geneID/replace.py -t -i " + str(START_TUMOR) + " " + str(STOP_TUMOR) + " " + str(STEP_TUMOR) + " " + str(START_NOISE) + " " + str(STOP_NOISE) + " " + str(STEP_NOISE) + " -o " + OUTPUT;
# 	start = timeit.default_timer()
# 	os.system(cmd)
# 	stop = timeit.default_timer()
# 	print("Time spent: %.2f seconds" % (stop - start))

# 	print("Conversion completed! Executing CIBERSORT ... ")
# 	files_done = 0
# 	start = timeit.default_timer()
# 	for tumor_content in range(START_TUMOR, STOP_TUMOR, STEP_TUMOR):
# 		for noise_content in range(START_NOISE, STOP_NOISE, STEP_NOISE):
# 			cmd = "java -Xmx3g -Xms3g -jar " + PATH + "CIBERSORT/CIBERSORT.jar -M " + PATH + "Master_files/convert/simulation_hugo_unique_tumor_" + str(tumor_content) + "_" + str(noise_content) + " -P " + REFERENCE_FILE + " -c " + PHENOTYPE_CLASSES_FILE + " > " + PATH + "Master_files/output/CIBERSORT_result_tumor_" + str(tumor_content) + "_" + str(noise_content)
# 			os.system(cmd)
# 			files_done += 1
# 			print("--- CIBERSORT is done with " + str(files_done) + " files.")
# 	stop = timeit.default_timer()
# 	print("Time spent: %.2f seconds" % (stop - start))

# 	print("CIBERSORT completed! Exexuting Abbas ... ")
# 	files_done = 0
# 	start = timeit.default_timer()
# 	for tumor_content in range(START_TUMOR, STOP_TUMOR, STEP_TUMOR):
# 		for noise_content in range(START_NOISE, STOP_NOISE, STEP_NOISE):
# 			cmd = "Rscript " + PATH + "Master/programming/abbas/abbas.r " + PATH + "Master_files/simulation/combined_cell_lines_tumor " + PATH + "Master_files/simulation/mixtures_with_tumor_" + str(tumor_content) + "_" + str(noise_content) + " " + PATH + "Master_files/abbas/Abbas_result_tumor_" + str(tumor_content) + "_" + str(noise_content)
# 			#os.system(cmd)
# 			files_done += 1
# 			print("--- Abbas is done with " + str(files_done) + " files.")
# 	stop = timeit.default_timer()
# 	print("Time spent: %.2f seconds" % (stop - start))

# 	print("Abbas completed! Plotting results ... ")
# 	cmd = "python " + PATH + "Master/programming/analyze_result/plot.py"
# 	start = timeit.default_timer()
# 	#os.system(cmd)
# 	stop = timeit.default_timer()
# 	print("Time spent: %.2f seconds" % (stop - start))

# 	stop_total = timeit.default_timer()
# 	print("Total time spent: %.2f seconds" % (stop_total - start_total))


def execute_args():

	start_total = timeit.default_timer()

	print("Executing simulation script ... ")
	cmd = "python3 " + PATH + "Master/programming/simulation_CIBERSORT/simulation.py " + arguments() + " -o " + args.OUTPUT
	start = timeit.default_timer()
	os.system(cmd)
	stop = timeit.default_timer()
	print("Time spent: %.2f seconds" % (stop - start)) 


	print("Simulation completed! Converting Affy to HUGO ... ")
	cmd = "python3 " + PATH + "Master/programming/convert_geneID/replace.py -t -i " + str(START_TUMOR) + " " + str(STOP_TUMOR) + " " + str(STEP_TUMOR) + " " + str(START_NOISE) + " " + str(STOP_NOISE) + " " + str(STEP_NOISE) + " -o " + args.OUTPUT;
	start = timeit.default_timer()
	#os.system(cmd)
	stop = timeit.default_timer()
	print("Time spent: %.2f seconds" % (stop - start))

	print("Conversion completed! Executing CIBERSORT ... ")
	files_done = 0
	start = timeit.default_timer()
	for tumor_content in range(START_TUMOR, STOP_TUMOR, STEP_TUMOR):
		for noise_content in range(START_NOISE, STOP_NOISE, STEP_NOISE):
			cmd = "java -Xmx3g -Xms3g -jar " + PATH + "CIBERSORT/CIBERSORT.jar -M " + PATH + "Master_files/simulation/HUGO_tumor_" + str(tumor_content) + "_" + str(noise_content) + " -P " + REFERENCE_FILE + " -c " + PHENOTYPE_CLASSES_FILE + " > " + PATH + "Master_files/output/CIBERSORT_HUGOfirst_tumor_" + str(tumor_content) + "_" + str(noise_content)
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
			cmd = "Rscript " + PATH + "Master/programming/abbas/abbas.r " + PATH + "Master_files/abbas/abbas_signature " + PATH + "Master_files/simulation/HUGO_signaturegenes_" + str(tumor_content) + "_" + str(noise_content) + " " + PATH + "Master_files/abbas/Abbas_HUGO_" + str(tumor_content) + "_" + str(noise_content)
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

#read_args()
#execute()
execute_args()