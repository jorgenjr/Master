
library(CellMix)
library(GEOquery)


options(max.print=300)

Jurkat <- read.table("/home/jorgen/Projects/Master_files/analyze_result/Jurkat", sep="\t", header=T)
MIXA <- read.table("/home/jorgen/Projects/Master_files/analyze_result/mix_A", sep="\t", header=T)

Jurkatm <- as.matrix(read.table("/home/jorgen/Projects/Master_files/analyze_result/Jurkat", sep="\t"))
MIXAm <- as.matrix(read.table("/home/jorgen/Projects/Master_files/analyze_result/mix_A", sep="\t"))

#XJA = lsfit(Jurkat[2:4], MIXA[2:4])

#print(XJA)

#gse <- ExpressionMix("GSE19830")

#gse11103 <- getGEO("GSE11103")

#print(gse)
#print("1***************")
#print(gse11103)
#print("2***************")

#mix <- mixedSamples(gse11103)
#print(mix)
#print("3***************")
#sig <- basis(mix)
#print(sig)

res <- ged(MIXA[2:4], Jurkat[2:4], "lsfit", verbose = TRUE)






