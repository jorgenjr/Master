
require(biomaRt);

organism="hsapiens_gene_ensembl"

EnsembleIDs <- read.table("/home/jorgen/Projects/Master_files/convert/testfile_1_1_geneid")

ensemble<-useMart("ensembl");

hsp<-useDataset(mart=ensemble,dataset=organism);

ids <- getBM(filters = "affy_hg_u133_plus_2",
             attributes = c("affy_hg_u133_plus_2", "hgnc_symbol"),
             values = EnsembleIDs, mart = hsp);

options(max.print=20)

write.table(ids, file="/home/jorgen/Projects/Master_files/diff_exp/hugo", sep='\t')