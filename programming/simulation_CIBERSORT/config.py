
##############
# SIMULATION #
##############

OUTPUT = "../../../Master_files/simulation/"
REFERENCE = "separate_custom_test"
REFERENCE_TUMOR = "separate_cell_lines_tumor_norm"
COMBINED_CELLS = "combined_cell_lines_test"
COMBINED_CELLS_TUMOR = "combined_cell_lines_tumor"
MIXTURE = "mixtures_test"
MIXTURES = "mixtures_tumor_test_"
PATH_SIMULATION = "../../../Master_files/simulation/"
PATH_EXTERNAL = "../../../Master_files/external/"


# 6 5 5 5 5 4 5 5 5 7 7 6 7 6 4 5 4 4 10 4 5 7 9 4 5 4 5 5 4 4 5 4 7 6 7 7 7 7
# java -Xmx3g -Xms3g -jar /home/jorgen/Projects/CIBERSORT/CIBERSORT.jar -M /home/jorgen/Projects/Master_files/simulation/mixtures_tumor_0_0 -c /home/jorgen/Projects/Master_files/simulation/phenotype_classes_LM40 -P /home/jorgen/Projects/Master_files/simulation/separate_custom_LM > /home/jorgen/Projects/Master_files/simulation/mixtures_lm40
# java -Xmx3g -Xms3g -jar /home/jorgen/Projects/CIBERSORT/CIBERSORT.jar -M /home/jorgen/Projects/Master_files/convert/GSE22153_affy.txt -c /home/jorgen/Projects/Master_files/simulation/phenotype_classes_LM40 -P /home/jorgen/Projects/Master_files/simulation/separate_custom_LM > /home/jorgen/Projects/Master_files/simulation/mixtures_lm40
# java -Xmx3g -Xms3g -jar /home/jorgen/Projects/CIBERSORT/CIBERSORT.jar -M /home/jorgen/Projects/Master_files/external/normdata.txt -B /home/jorgen/Projects/Master_files/simulation/phenotype_classes_LM40.separate_custom_LM.bm.K999.0.txt > /home/jorgen/Projects/Master_files/simulation/prostate_cancer_lm40