
options(max.print=20)
options(warn=-1)

args = commandArgs()

# CELL_LINES <- read.table("/home/jorgen/Projects/Master_files/external/GSE26495_HUGO_quantile_overlap.txt", sep="\t", header=T)
# MIX <- read.table("/home/jorgen/Projects/Master_files/external/GSE22153_HUGO_overlap.txt", sep="\t", header=T)

n_CELL = c(CELL_LINES[2:ncol(CELL_LINES)])

length_c = ncol(CELL_LINES) - 1
names(n_CELL) = c(paste(letters[1:length_c]))

n_MIX = c(MIX[2:ncol(MIX)])

length_m = ncol(MIX) - 1
names(n_MIX) = c(paste(letters[1:length_m]))

A = lm(n_MIX$A ~ n_CELL$A + n_CELL$B + n_CELL$C + n_CELL$D)
B = lm(n_MIX$B ~ n_CELL$A + n_CELL$B + n_CELL$C + n_CELL$D)
C = lm(n_MIX$C ~ n_CELL$A + n_CELL$B + n_CELL$C + n_CELL$D)
D = lm(n_MIX$D ~ n_CELL$A + n_CELL$B + n_CELL$C + n_CELL$D)

fitA = fitted(A)
fitB = fitted(B)
fitC = fitted(C)
fitD = fitted(D)

mat = matrix(c(fitA, fitB, fitC, fitD), nrow=length(fitA), ncol=4)
mat_c = matrix(CELL_LINES$Genes, nrow=nrow(CELL_LINES[1]), ncol=1)
mat_w = matrix(c(mat_c, fitA, fitB, fitC, fitD), nrow=length(fitA), ncol=5)

# write.table(mat_w, file="/home/jorgen/Projects/Master_files/abbas/TEST", sep="\t")







