
#library(limma)
#library(edgeR)

options(max.print=20)

Jurkat <- read.table("/home/jorgen/Projects/Master_files/analyze_result/Jurkat", sep="\t", header=T)
IM9 <- read.table("/home/jorgen/Projects/Master_files/analyze_result/IM-9", sep="\t", header=T)
Raji <- read.table("/home/jorgen/Projects/Master_files/analyze_result/Raji", sep="\t", header=T)
THP1 <- read.table("/home/jorgen/Projects/Master_files/analyze_result/THP-1", sep="\t", header=T)
MIXA <- read.table("/home/jorgen/Projects/Master_files/analyze_result/mix_A", sep="\t", header=T)
MIXB <- read.table("/home/jorgen/Projects/Master_files/analyze_result/mix_B", sep="\t", header=T)
MIXC <- read.table("/home/jorgen/Projects/Master_files/analyze_result/mix_C", sep="\t", header=T)
MIXD <- read.table("/home/jorgen/Projects/Master_files/analyze_result/mix_D", sep="\t", header=T)

Jurkat_s <- read.table("/home/jorgen/Projects/Master_files/analyze_result/Jurkat_small", sep="\t", header=T)
MIXA_s <- read.table("/home/jorgen/Projects/Master_files/analyze_result/mix_A_small", sep="\t", header=T)

nrow <- function(x) dim(x)[1]
ncol <- function(x) dim(x)[2]

#for(i in 1:nrow(countdata)) {
#  for(j in 1:ncol(countdata)) {
#    print(countdata[i,j])
#  }
#}

XJA = lsfit(Jurkat[2:4], MIXA[2:4])
XIA = lsfit(IM9[2:4], MIXA[2:4])
XRA = lsfit(Raji[2:4], MIXA[2:4])
XTA = lsfit(THP1[2:4], MIXA[2:4])

XJB = lsfit(Jurkat[2:4], MIXB[2:4])
XIB = lsfit(IM9[2:4], MIXB[2:4])
XRB = lsfit(Raji[2:4], MIXB[2:4])
XTB = lsfit(THP1[2:4], MIXB[2:4])

XJC = lsfit(Jurkat[2:4], MIXC[2:4])
XIC = lsfit(IM9[2:4], MIXC[2:4])
XRC = lsfit(Raji[2:4], MIXC[2:4])
XTC = lsfit(THP1[2:4], MIXC[2:4])

XJD = lsfit(Jurkat[2:4], MIXD[2:4])
XID = lsfit(IM9[2:4], MIXD[2:4])
XRD = lsfit(Raji[2:4], MIXD[2:4])
XTD = lsfit(THP1[2:4], MIXD[2:4])



