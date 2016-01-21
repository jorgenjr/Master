
require(biomaRt);

organism="hsapiens_gene_ensembl"

EnsembleIDs <- read.table("../../../Master_files/output/testfile_1_1_geneid")

ensemble<-useMart("ensembl");

hsp<-useDataset(mart=ensemble,dataset=organism);

# ids<-getBM(filters= "ensembl_gene_id",
#            attributes= c("ensembl_gene_id","hgnc_id", "hgnc_symbol","description"),
#            values= EnsembleIDs, mart= hsp);

ids <- getBM(filters = "affy_hg_u133_plus_2",
             attributes = c("affy_hg_u133_plus_2", "hgnc_symbol"),
             values = EnsembleIDs, mart = hsp);

options(max.print=20)
print(ids)

#write.table(ids, file="hugo.txt", sep='\t')