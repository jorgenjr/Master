
options(max.print=20)
options(warn=-1)

args = commandArgs()

CELL_LINES <- read.table(args[6], sep="\t", header=T)
MIX <- read.table(args[7], sep="\t", header=T)

TESTS = lsfit(CELL_LINES[2:ncol(CELL_LINES)], MIX[2:ncol(MIX)], intercept = TRUE)

#correlation = cor(CELL_LINES[2:ncol(CELL_LINES)], MIX[2:ncol(MIX)], method="pearson")

write.table(TESTS$coefficients, file=args[8], sep="\t")
# write.table(correlation, file=args[8], sep="\t", append=TRUE, col.names=TRUE)