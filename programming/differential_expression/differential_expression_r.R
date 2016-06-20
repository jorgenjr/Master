
library(limma)
library(edgeR)
library(globaltest)

options(max.print=200)

#########
# edgeR #
#########

#countdata <- read.table("/home/jorgen/Projects/Master_files/simulation/combined_cell_lines", sep="\t", header=T)
#countdata <- read.table("/home/jorgen/Projects/Master_files/diff_exp/combined_t-high_t-low", sep="\t", header=T)

#rownames(countdata) <- countdata[,1]
#countdata <- countdata[,-1]

#dge <- DGEList(counts=countdata, group=c(1,2))

#dge$common.dispersion <- 0.05
#dge$counts[is.na(dge$counts)] <- 0
#print(D)
#D <- estimateCommonDisp(dge, group=c(1,2))  #, rowsum.filter=0)
#D <- estimateDisp(dge)

#D$counts[is.na(D$counts)] <- 0

#D <- exactTest(D, dispersion=0.05)

#tags <- topTags(D, n=nrow(countdata))

#write.table(tags, file="/home/jorgen/Projects/Master_files/diff_exp/T-high_T-low_4", sep="\t")

#########
# limma #
#########

#countdata <- read.table("/home/jorgen/Projects/Master_files/diff_exp/combined_t-high_t-low", sep="\t", header=T)
#design <- model.matrix(countdata$T.high ~ countdata$T.low)
#countdata <- as.matrix(countdata[,-1])

#print(design)
#print(countdata)
#fit <- lmFit(countdata, design)

#fit <- eBayes(fit)

#topTable(fit, adjust = "fdr")

#write.table(fit, file="/home/jorgen/Projects/Master_files/diff_exp/new_limma_T-high_T-low", sep="\t")

#######
# ??? #
#######

#lcd = read.delim('/home/jorgen/Projects/Master_files/diff_exp/combined_t-high_t-low', row.names=1, as.is=T)
#cds  <- DGEList(lcd, group = c(1,2))
#design = model.matrix(object = ~group)
#f <- glmFit(cds, design)
#lrt <- glmLRT(f, coef=2) # 1: intercept. 2: c(1,2)

#write.table(topTags(lrt, n=1000000), file="/home/jorgen/Projects/Master_files/diff_exp/T-high_T-low_4", sep="\t")


##############
# globaltest #
##############

#countdata <- read.table("/home/jorgen/Projects/Master_files/diff_exp/separate_t-high_t-low", sep="\t", header=T)
countdata <- read.table("/home/jorgen/Projects/Master_files/diff_exp/separate_Jurkat_Raji", sep="\t", header=T)

rownames(countdata) <- countdata[,1]
countdata <- countdata[,-1]

X <- countdata
#for (j in 1:12) X[,j] <- as.numeric(countdata[,j])
for (j in 1:6) X[,j] <- as.numeric(countdata[,j])

Y <- as.matrix(X)
Z <- t(Y)

#v <- rep(0:1, each=6)
v <- rep(0:1, each=3)
z <- gt(v, Z)
print(z)









