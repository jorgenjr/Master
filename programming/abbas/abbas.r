
options(max.print=20)
options(warn=-1)

args = commandArgs()

CELL_LINES <- read.table(args[6], sep="\t", header=T)
TESTMIX <- read.table(args[7], sep="\t", header=T)

TESTS = lsfit(CELL_LINES[2:ncol(CELL_LINES)], TESTMIX[2:ncol(TESTMIX)], intercept = FALSE)

correlation = cor(CELL_LINES[2:ncol(CELL_LINES)], TESTMIX[2:ncol(TESTMIX)], method="pearson")

write.table(TESTS$coefficients, file=args[8], sep="\t")
write.table(correlation, file=args[8], sep="\t", append=TRUE, col.names=TRUE)