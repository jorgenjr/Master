
options(max.print=20)
options(warn=-1)

args = commandArgs()

CELL_LINES <- read.table(args[6], sep="\t", header=T)
MIX <- read.table(args[7], sep="\t", header=T)

n_CELL = c(CELL_LINES[2], CELL_LINES[3], CELL_LINES[4], CELL_LINES[5])
names(n_CELL) = c("A", "B", "C", "D")
n_MIX = c(MIX[2], MIX[3], MIX[4], MIX[5])
names(n_MIX) = c("A", "B", "C", "D")

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

write.table(mat_w, file=args[8], sep="\t")