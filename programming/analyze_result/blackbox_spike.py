
import os

PATH = "/home/jorgen/Projects/";
# REFERENCE_FILE = PATH + "Master_files/simulation/separate_cell_lines_tumor"
# PHENOTYPE_CLASSES_FILE = PATH + "Master_files/simulation/phenotype_classes_tumor"
REFERENCE_FILE = PATH + "Master_files/simulation/separate_GSE26495_cell_lines"
PHENOTYPE_CLASSES_FILE = PATH + "Master_files/simulation/phenotype_classes_GSE26495"
COMBINED_CELL_LINES = PATH + "Master_files/simulation/combined_GSE26495_cell_lines"

def execute():

	print("Executing CIBERSORT ... ")
	files_done = 0
	for spike in range(0, 11, 1):
		cmd = "java -Xmx3g -Xms3g -jar " + PATH + "CIBERSORT/CIBERSORT.jar -M " + PATH + "Master_files/analyze_result/new_norm_mixtureD_tumor_0_GSE26495_h" + str(10 - spike) + "_l" + str(spike) + " -P " + REFERENCE_FILE + " -c " + PHENOTYPE_CLASSES_FILE + " > " + PATH + "Master_files/analyze_result/CIBERSORT_new_normD_tumor_0_GSE26495_h" + str(10 - spike) + "_l" + str(spike)
		os.system(cmd)
		files_done += 1
		print("--- CIBERSORT is done with " + str(files_done) + " files.")

	print("CIBERSORT completed! Exexuting lsfit ... ")
	files_done = 0
	for spike in range(0, 11, 1):
		cmd = "Rscript " + PATH + "Master/programming/abbas/abbas.r " + COMBINED_CELL_LINES + " " + PATH + "Master_files/analyze_result/new_norm_mixtureD_tumor_0_GSE26495_h" + str(10 - spike) + "_l" + str(spike) + " " + PATH + "Master_files/analyze_result/Abbas_new_normD_tumor_0_GSE26495_h" + str(10 - spike) + "_l" + str(spike)
		os.system(cmd)
		files_done += 1
		print("--- lsfit is done with " + str(files_done) + " files.")

	# print("lsfit completed! Exexuting LLSR ... ")
	# files_done = 0
	# for spike in range(0, 11, 1):
	# 	cmd = "Rscript " + PATH + "Master/programming/abbas/llsr.r " + COMBINED_CELL_LINES + " " + PATH + "Master_files/analyze_result/mixture_tumor_70_Raji_" + str(spike) + " " + PATH + "Master_files/analyze_result/LLSR_tumor_70_Raji_" + str(spike)
	# 	os.system(cmd)
	# 	files_done += 1
	# 	print("--- LLSR is done with " + str(files_done) + " files.")


execute()