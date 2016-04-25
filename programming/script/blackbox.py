
import readline, os, sys, timeit, argparse, config

#from subprocess import call
import subprocess

# PATH = "/home/jorgen/Projects/";
# #PATH = "/usit/abel/u1/jorgenjr/Projects/"
# START_TUMOR = 0
# STOP_TUMOR = 100
# STEP_TUMOR = 5
# START_NOISE = 0
# STOP_NOISE = 100
# STEP_NOISE = 5
# REFERENCE_FILE = PATH + "Master_files/simulation/separate_cell_lines"
# PHENOTYPE_CLASSES_FILE = PATH + "Master_files/simulation/phenotype_classes"
# SIGNATURE_FILE = PATH + "Master_files/external/random_signature_genesQ"

FLAGS = []
MIXTURES = []
TUMORS = []
CELL_LINES = []
OUTPUT = ""


parser = argparse.ArgumentParser()
parser.add_argument("-m", "--MIXTURES", help="Mixtures", nargs='*')
parser.add_argument("-t", "--TUMORS", help="Tumors", nargs='*')
parser.add_argument("-c", "--CELL_LINES", help="Cell lines", nargs='*')
#parser.add_argument("-o", "--OUTPUT", help="Output")

args = parser.parse_args()


def arguments():

	cmd = "-i " + str(config.START_TUMOR) + " " + str(config.STOP_TUMOR) + " " + str(config.STEP_TUMOR) + " " + str(config.START_NOISE) + " " + str(config.STOP_NOISE) + " " + str(config.STEP_NOISE) + " ";

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


def execute_args():

	start_total = timeit.default_timer()

	# print("Executing simulation script ... ")
	# cmd = "python3 " + config.PATH + "Master/programming/simulation_CIBERSORT/simulation.py " + arguments() + " -o " + args.OUTPUT
	# start = timeit.default_timer()
	# os.system(cmd)
	# stop = timeit.default_timer()
	# print("Time spent: %.2f seconds" % (stop - start)) 


	# print("Simulation completed! Converting Affy to HUGO ... ")
	# cmd = "python3 " + config.PATH + "Master/programming/convert_geneID/replace.py -t -i " + str(config.START_TUMOR) + " " + str(config.STOP_TUMOR) + " " + str(config.STEP_TUMOR) + " " + str(config.START_NOISE) + " " + str(config.STOP_NOISE) + " " + str(config.STEP_NOISE) + " -o " + args.OUTPUT;
	# start = timeit.default_timer()
	# os.system(cmd)
	# stop = timeit.default_timer()
	# print("Time spent: %.2f seconds" % (stop - start))

	print("Conversion completed! Executing CIBERSORT ... ")
	files_done = 0
	start = timeit.default_timer()
	for tumor_content in range(config.START_TUMOR, config.STOP_TUMOR, config.STEP_TUMOR):
		for noise_content in range(config.START_NOISE, config.STOP_NOISE, config.STEP_NOISE):
			cmd = "java -Xmx3g -Xms3g -jar " + config.PATH_CIBERSORT + " -M " + config.CIBERSORT_MIXTURES + str(tumor_content) + "_" + str(noise_content) + " -c " + config.PHENOTYPE_CLASSES_FILE + " -P " + config.REFERENCE_FILE + " > " + config.CIBERSORT_OUTPUT + str(tumor_content) + "_" + str(noise_content)
			os.system(cmd)
			files_done += 1
			print("--- CIBERSORT is done with " + str(files_done) + " files.")
	stop = timeit.default_timer()
	print("Time spent: %.2f seconds" % (stop - start))

	# print("CIBERSORT completed! Exexuting Abbas ... ")
	# files_done = 0
	# start = timeit.default_timer()
	# for tumor_content in range(config.START_TUMOR, config.STOP_TUMOR, config.STEP_TUMOR):
	# 	for noise_content in range(config.START_NOISE, config.STOP_NOISE, config.STEP_NOISE):
	# 		cmd = "Rscript " + config.PATH_LLSR + " " + config.COMBINED_CELLS + " " + config.LLSR_MIXTURES + str(tumor_content) + "_" + str(noise_content) + " " + config.LLSR_OUTPUT + str(tumor_content) + "_" + str(noise_content)
	# 		# cmd = "Rscript " + PATH + "Master/programming/abbas/llsr.r " + PATH + "Master_files/simulation/combined_cell_lines " + PATH + "Master_files/simulation/mixtures_normalized_tumor_" + str(tumor_content) + "_" + str(noise_content) + " " + PATH + "Master_files/abbas/LLSR_tumor_" + str(tumor_content) + "_" + str(noise_content)
	# 		os.system(cmd)
	# 		files_done += 1
	# 		print("--- Abbas is done with " + str(files_done) + " files.")
	# stop = timeit.default_timer()
	# print("Time spent: %.2f seconds" % (stop - start))

	# print("Abbas completed! Plotting results ... ")
	# cmd = "python " + PATH + "Master/programming/analyze_result/plot.py"
	# start = timeit.default_timer()
	# os.system(cmd)
	# stop = timeit.default_timer()
	# print("Time spent: %.2f seconds" % (stop - start))

	stop_total = timeit.default_timer()
	print("Total time spent: %.2f seconds" % (stop_total - start_total))


execute_args()