
library(limma)
library(edgeR)

options(max.print=200)

#countdata <- read.table("/home/jorgen/Projects/Master_files/simulation/combined_cell_lines", sep="\t", header=T)
countdata <- read.table("/home/jorgen/Projects/Master_files/diff_exp/combined_t-high_t-low", sep="\t", header=T)

rownames(countdata) <- countdata[,1]
countdata <- countdata[,-1]
print("1")
dge <- DGEList(counts=countdata, group=c(1,2))
print("2")
print(dge)
#dge$common.dispersion <- 0.05
dge$counts[is.na(dge$counts)] <- 0
D <- estimateCommonDisp(dge, rowsum.filter=0)
#D <- estimateDisp(dge)
print("3")
print(D)
D$counts[is.na(D$counts)] <- 0
print("4")
D <- exactTest(D, dispersion=0.05)
print("5")
print(D)
tags <- topTags(D, n=nrow(countdata))
print("6")
write.table(tags, file="/home/jorgen/Projects/Master_files/diff_exp/T-high_T-low", sep="\t")
