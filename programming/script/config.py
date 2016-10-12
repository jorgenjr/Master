
##############
# SIMULATION #
##############

PATH = "/home/jorgen/Projects/";
START_TUMOR = 0
STOP_TUMOR = 100
STEP_TUMOR = 5
START_NOISE = 0
STOP_NOISE = 100
STEP_NOISE = 5

#############
# CIBERSORT #
#############

PATH_CIBERSORT = PATH + "CIBERSORT/CIBERSORT.jar"
PATH_CIBERSORT_R = PATH + "CIBERSORT/run_CIBERSORT.R"
CIBERSORT_MIXTURES = PATH + "Master_files/simulation/mixtures_tumor_"
PHENOTYPE_CLASSES_FILE = PATH + "Master_files/simulation/phenotype_classes"
REFERENCE_FILE = PATH + "Master_files/simulation/separate_cell_lines_norm"
SIGNATURE_FILE = PATH + "Master_files/external/GSE11103_matrix_classes.GSE11103-GSE10650.AbbasPure.mas5.bm.K999.0.txt"
CIBERSORT_OUTPUT = PATH + "Master_files/output/CIBERSORT_"
CIBERSORT_R_OUTPUT = PATH + "Master_files/output/CIBERSORT_R_"

########
# LLSR #
########

PATH_ABBAS = PATH + "Master/programming/abbas/abbas.r"
PATH_LLSR = PATH + "Master/programming/abbas/llsr.r"
COMBINED_CELLS = PATH + "Master_files/simulation/combined_cell_lines"
LLSR_MIXTURES = PATH + "Master_files/simulation/mixtures_tumor_"
ABBAS_OUTPUT = PATH + "Master_files/abbas/Abbas_"
LLSR_OUTPUT = PATH + "Master_files/abbas/LLSR_"

##########
# VOTING #
##########

CIBERSORT_FIRST_MIX = 2
CIBERSORT_LAST_MIX = 5
CIBERSORT_FIRST_CELL = 1
CIBERSORT_LAST_CELL = 4
CIBERSORT_PVALUE = 5
CIBERSORT_PEARSON = 6
ABBAS_FIRST_CELL = 3
ABBAS_LAST_CELL = 6
ABBAS_FIRST_MIX = 1
ABBAS_LAST_MIX = 4
ACTUAL_AMOUNT = [[0.250, 0.125, 0.250, 0.375],
				 [0.050, 0.317, 0.475, 0.158],
				 [0.010, 0.495, 0.165, 0.330],
				 [0.002, 0.333, 0.333, 0.333]]
VOTE_OPTIONS = ['union', 'intersect']
VOTE = 0
VOTE_VARIABLE = ['p-value', 'pearson', 'coef']
VOTE_V = 2
THRESHOLD_COEF = 0.05
THRESHOLD_PVALUE = 0.05
THRESHOLD_PEARSON = 0.6