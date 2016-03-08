
#library(CellMix)
#library(GEOquery)

options(max.print=20)

args = commandArgs()

#CELL_LINES <- read.table("/home/jorgen/Projects/Master_files/simulation/combined_cell_lines", sep="\t", header=T)
CELL_LINES <- read.table(args[6], sep="\t", header=T)
#MIXA <- read.table("/home/jorgen/Projects/Master_files/simulation/combined_mixtures_A", sep="\t", header=T)
#MIXB <- read.table("/home/jorgen/Projects/Master_files/simulation/combined_mixtures_B", sep="\t", header=T)
#MIXC <- read.table("/home/jorgen/Projects/Master_files/simulation/combined_mixtures_C", sep="\t", header=T)
#MIXD <- read.table("/home/jorgen/Projects/Master_files/simulation/combined_mixtures_D", sep="\t", header=T)
#TESTMIX <- read.table("/home/jorgen/Projects/Master_files/simulation/mixtures_with_tumor_0", sep="\t", header=T)
TESTMIX <- read.table(args[7], sep="\t", header=T)

#XA = lsfit(CELL_LINES[2:5], MIXA[2:2], intercept = FALSE)
#XB = lsfit(CELL_LINES[2:5], MIXB[2:2], intercept = FALSE)
#XC = lsfit(CELL_LINES[2:5], MIXC[2:2], intercept = FALSE)
#XD = lsfit(CELL_LINES[2:5], MIXD[2:2], intercept = FALSE)
TESTS = lsfit(CELL_LINES[2:ncol(CELL_LINES)], TESTMIX[2:ncol(TESTMIX)], intercept = FALSE)

#write.table(XA$coefficients, file="/home/jorgen/Projects/Master_files/abbas/deconvoluted_mixA", sep="\t")
#write.table(XB$coefficients, file="/home/jorgen/Projects/Master_files/abbas/deconvoluted_mixB", sep="\t")
#write.table(XC$coefficients, file="/home/jorgen/Projects/Master_files/abbas/deconvoluted_mixC", sep="\t")
#write.table(XD$coefficients, file="/home/jorgen/Projects/Master_files/abbas/deconvoluted_mixD", sep="\t")
write.table(TESTS$coefficients, file="/home/jorgen/Projects/Master_files/abbas/deconvoluted_test", sep="\t")

#XA = lsfit(CELL_LINES[2:5], MIXA[2:2], intercept = TRUE)
#XB = lsfit(CELL_LINES[2:5], MIXB[2:2], intercept = TRUE)
#XC = lsfit(CELL_LINES[2:5], MIXC[2:2], intercept = TRUE)
#XD = lsfit(CELL_LINES[2:5], MIXD[2:2], intercept = TRUE)

#write.table(XA$coefficients, file="/home/jorgen/Projects/Master_files/abbas/deconvoluted_mixA_intercept", sep="\t")
#write.table(XB$coefficients, file="/home/jorgen/Projects/Master_files/abbas/deconvoluted_mixB_intercept", sep="\t")
#write.table(XC$coefficients, file="/home/jorgen/Projects/Master_files/abbas/deconvoluted_mixC_intercept", sep="\t")
#write.table(XD$coefficients, file="/home/jorgen/Projects/Master_files/abbas/deconvoluted_mixD_intercept", sep="\t")

