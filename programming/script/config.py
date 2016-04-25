
##############
# SIMULATION #
##############

PATH = "/home/jorgen/Projects/";
#PATH = "/usit/abel/u1/jorgenjr/Projects/"
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
CIBERSORT_MIXTURES = PATH + "Master_files/simulation/mixtures_normalized_tumor_"
PHENOTYPE_CLASSES_FILE = PATH + "Master_files/simulation/phenotype_classes"
REFERENCE_FILE = PATH + "Master_files/simulation/separate_cell_lines_norm"
SIGNATURE_FILE = PATH + "Master_files/external/random_signature_genesQ"
CIBERSORT_OUTPUT = PATH + "Master_files/output/CIBERSORT_referencenorm_"

########
# LLSR #
########

PATH_LLSR = PATH + "Master/programming/abbas/abbas.r"
COMBINED_CELLS = PATH + "Master_files/simulation/combined_cell_lines"
LLSR_MIXTURES = PATH + "Master_files/simulation/mixtures_normalized_tumor_"
LLSR_OUTPUT = PATH + "Master_files/abbas/Abbas_tumor_"