
library(limma)
library(edgeR)

options(max.print=200)

countdata <- read.table("../../../Master_files/output/testfile_1_1", sep="\t", header=T)

rownames(countdata) <- countdata[,1]
countdata <- countdata[,-1]

dge <- DGEList(counts=countdata, group=c(1,2,3,4))

D <- estimateCommonDisp(dge, rowsum.filter=0)

is.na(D$counts)

D <- exactTest(D, dispersion=0.05)

tags <- topTags(D, n=nrow(countdata))

write.table(tags, file="diff_exp.txt", sep="\t")
