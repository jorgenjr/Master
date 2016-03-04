
#library(CellMix)
#library(GEOquery)

options(max.print=20)

CELL_LINES <- read.table("/home/jorgen/Projects/Master_files/simulation/combined_cell_lines", sep="\t", header=T)
MIXA <- read.table("/home/jorgen/Projects/Master_files/simulation/combined_mixtures_A", sep="\t", header=T)
MIXB <- read.table("/home/jorgen/Projects/Master_files/simulation/combined_mixtures_B", sep="\t", header=T)
MIXC <- read.table("/home/jorgen/Projects/Master_files/simulation/combined_mixtures_C", sep="\t", header=T)
MIXD <- read.table("/home/jorgen/Projects/Master_files/simulation/combined_mixtures_D", sep="\t", header=T)

XA = lsfit(CELL_LINES[2:5], MIXA[2:2], intercept = FALSE)
XB = lsfit(CELL_LINES[2:5], MIXB[2:2], intercept = FALSE)
XC = lsfit(CELL_LINES[2:5], MIXC[2:2], intercept = FALSE)
XD = lsfit(CELL_LINES[2:5], MIXD[2:2], intercept = FALSE)

write.table(XA$coefficients, file="/home/jorgen/Projects/Master_files/abbas/deconvoluted_mixA", sep="\t")
write.table(XB$coefficients, file="/home/jorgen/Projects/Master_files/abbas/deconvoluted_mixB", sep="\t")
write.table(XC$coefficients, file="/home/jorgen/Projects/Master_files/abbas/deconvoluted_mixC", sep="\t")
write.table(XD$coefficients, file="/home/jorgen/Projects/Master_files/abbas/deconvoluted_mixD", sep="\t")

XA = lsfit(CELL_LINES[2:5], MIXA[2:2], intercept = TRUE)
XB = lsfit(CELL_LINES[2:5], MIXB[2:2], intercept = TRUE)
XC = lsfit(CELL_LINES[2:5], MIXC[2:2], intercept = TRUE)
XD = lsfit(CELL_LINES[2:5], MIXD[2:2], intercept = TRUE)

write.table(XA$coefficients, file="/home/jorgen/Projects/Master_files/abbas/deconvoluted_mixA_intercept", sep="\t")
write.table(XB$coefficients, file="/home/jorgen/Projects/Master_files/abbas/deconvoluted_mixB_intercept", sep="\t")
write.table(XC$coefficients, file="/home/jorgen/Projects/Master_files/abbas/deconvoluted_mixC_intercept", sep="\t")
write.table(XD$coefficients, file="/home/jorgen/Projects/Master_files/abbas/deconvoluted_mixD_intercept", sep="\t")

