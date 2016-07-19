
options(max.print=20)
options(warn=-1)

args = commandArgs()

cell_lines <- read.table(args[6], sep="\t", header=T)
mix <- read.table(args[7], sep="\t", header=T)

result = lsfit(cell_lines[2:ncol(cell_lines)], mix[2:ncol(mix)], intercept = TRUE)

write.table(result$coefficients, file=args[8], sep="\t")
