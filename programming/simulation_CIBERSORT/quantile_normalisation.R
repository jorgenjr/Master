
require(preprocessCore)

exprs <- as.matrix(read.table('/home/jorgen/Projects/Master/programming/simulation_CIBERSORT/combined_matrix', header=TRUE, sep = "\t",
                              row.names = 1,
                              as.is=TRUE))

new_exprs = normalize.quantiles(exprs,copy=TRUE)
options(max.print=20000000)
print(new_exprs)
print(exprs)