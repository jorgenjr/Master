
import readline
import os
import sys
import timeit
import argparse
import config


FLAGS = []
MIXTURES = []
TUMORS = []
CELL_LINES = []


parser = argparse.ArgumentParser()
parser.add_argument("-m", "--MIXTURES", help="Mixtures", nargs='*')
parser.add_argument("-t", "--TUMORS", help="Tumors", nargs='*')
parser.add_argument("-c", "--CELL_LINES", help="Cell lines", nargs='*')

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
	# cmd = "python3 " + config.PATH + "Master/programming/simulation_CIBERSORT/simulation.py " + arguments()
	# start = timeit.default_timer()
	# os.system(cmd)
	# stop = timeit.default_timer()
	# print("Time spent: %.2f seconds" % (stop - start)) 

	# print("Simulation completed! Converting Affy to HUGO ... ")
	# cmd = "python3 " + config.PATH + "Master/programming/convert_geneID/replace.py -t true -i " + str(config.START_TUMOR) + " " + str(config.STOP_TUMOR) + " " + str(config.STEP_TUMOR) + " " + str(config.START_NOISE) + " " + str(config.STOP_NOISE) + " " + str(config.STEP_NOISE)
	# start = timeit.default_timer()
	# os.system(cmd)
	# stop = timeit.default_timer()
	# print("Time spent: %.2f seconds" % (stop - start))

	print("Conversion completed! Executing CIBERSORT ... ")
	files_done = 0
	start = timeit.default_timer()
	for tumor_content in range(config.START_TUMOR, config.STOP_TUMOR, config.STEP_TUMOR):
		for noise_content in range(config.START_NOISE, config.STOP_NOISE, config.STEP_NOISE):
			# cmd = "java -Xmx3g -Xms3g -jar " + config.PATH_CIBERSORT + " -M " + config.CIBERSORT_MIXTURES + str(tumor_content) + "_" + str(noise_content) + " -c " + config.PHENOTYPE_CLASSES_FILE + " -P " + config.REFERENCE_FILE + " > " + config.CIBERSORT_OUTPUT + str(tumor_content) + "_" + str(noise_content)
			cmd = "Rscript " + config.PATH_CIBERSORT_R + " " + config.PATH + "Master_files/external/GSE11103_matrix_classes.GSE11103-GSE10650.AbbasPure.mas5.bm.K999.0.txt " + config.CIBERSORT_MIXTURES + str(tumor_content) + "_" + str(noise_content) + " " + config.CIBERSORT_R_OUTPUT + str(tumor_content) + "_" + str(noise_content)
			os.system(cmd)
			files_done += 1
			print("--- CIBERSORT is done with " + str(files_done) + " files.")
	stop = timeit.default_timer()
	print("Time spent: %.2f seconds" % (stop - start))

	# print("CIBERSORT completed! Exexuting LLSR ... ")
	# files_done = 0
	# start = timeit.default_timer()
	# for tumor_content in range(config.START_TUMOR, config.STOP_TUMOR, config.STEP_TUMOR):
	# 	for noise_content in range(config.START_NOISE, config.STOP_NOISE, config.STEP_NOISE):
	# 		# cmd = "Rscript " + config.PATH_ABBAS + " " + config.COMBINED_CELLS + " " + config.LLSR_MIXTURES + str(tumor_content) + "_" + str(noise_content) + " " + config.ABBAS_OUTPUT + str(tumor_content) + "_" + str(noise_content)
	# 		cmd = "Rscript " + config.PATH_LLSR + " " + config.COMBINED_CELLS + " " + config.LLSR_MIXTURES + str(tumor_content) + "_" + str(noise_content) + " " + config.LLSR_OUTPUT + str(tumor_content) + "_" + str(noise_content)
	# 		os.system(cmd)
	# 		files_done += 1
	# 		print("--- LLSR is done with " + str(files_done) + " files.")
	# stop = timeit.default_timer()
	# print("Time spent: %.2f seconds" % (stop - start))

	print("LLSR completed! Voting ... ")
	files_done = 0
	start = timeit.default_timer()
	for tumor_content in range(config.START_TUMOR, config.STOP_TUMOR, config.STEP_TUMOR):
		for noise_content in range(config.START_NOISE, config.STOP_NOISE, config.STEP_NOISE):
			cmd = "python3 " + config.PATH + "Master/programming/script/voting.py -i " + str(tumor_content) + " " + str(noise_content)
			os.system(cmd)
			files_done += 1
			print("--- Voting is done with " + str(files_done) + " files.")
	stop = timeit.default_timer()
	print("Time spent: %.2f seconds" % (stop - start))

	print("Voting completed!")

	stop_total = timeit.default_timer()
	print("Total time spent: %.2f seconds" % (stop_total - start_total))


execute_args()