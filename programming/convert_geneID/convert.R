
require(biomaRt);

organism="hsapiens_gene_ensembl"
database="illumina_humanwg_6_v2"
# database="affy_hg_u133_plus_2"

# EnsembleIDs <- read.table("/home/jorgen/Projects/Master_files/simulation/combined_cell_lines")
EnsembleIDs <- read.table("/home/jorgen/Projects/Master_files/convert/GSE22153_genes")
print("hello1")
listMarts(host="www.ensembl.org");
print("hello2")
ensemble<-useMart(biomart = "ENSEMBL_MART_ENSEMBL", host = "jul2015.archive.ensembl.org");
print("hello3")
hsp<-useDataset(mart=ensemble,dataset=organism);
# attributes = c(database, "hgnc_symbol"),
print("hello4")
ids <- getBM(filters = database,
             attributes = c(database, "affy_hg_u133_plus_2"),
             values = EnsembleIDs, mart = hsp);

options(max.print=20)

write.table(ids, file="/home/jorgen/Projects/Master_files/simulation/illumina_to_affy", sep='\t')