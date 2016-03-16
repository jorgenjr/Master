
options(max.print=20)

args = commandArgs()

CELL_LINES <- read.table(args[6], sep="\t", header=T)
TESTMIX <- read.table(args[7], sep="\t", header=T)

TESTS = lsfit(CELL_LINES[2:ncol(CELL_LINES)], TESTMIX[2:ncol(TESTMIX)], intercept = FALSE)

correlation = cor(TESTS$coefficients, method="pearson")

print(TESTS)
print("****************")
print(correlation)

write.table(TESTS$coefficients, file=args[8], sep="\t")