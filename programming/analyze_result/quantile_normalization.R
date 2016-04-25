

#install if necessary
#source('http://bioconductor.org/biocLite.R')
#biocLite('preprocessCore')
#load package
library(preprocessCore)

exprs <- as.matrix(read.table('/home/jorgen/Projects/Master_files/analyze_result/Q_TEST_BEFORE', header=TRUE, sep = "\t", row.names = 1, as.is=TRUE))

Q_exprs = normalize.quantiles(exprs)
print(Q_exprs)
write.table(Q_exprs, file='/home/jorgen/Projects/Master_files/analyze_result/Q_TEST_AFTER_R', sep="\t")