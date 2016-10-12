
require(biomaRt);

organism="hsapiens_gene_ensembl"
database="illumina_humanwg_6_v2"
# database="affy_hg_u133_plus_2"

# EnsembleIDs <- read.table("/home/jorgen/Projects/Master_files/simulation/combined_cell_lines")
EnsembleIDs <- read.table("/home/jorgen/Projects/Master_files/convert/GSE22153_genes")

ensemble<-useMart("ensembl");

hsp<-useDataset(mart=ensemble,dataset=organism);

ids <- getBM(filters = database,
             attributes = c(database, "hgnc_symbol"),
             values = EnsembleIDs, mart = hsp);

options(max.print=20)

write.table(ids, file="/home/jorgen/Projects/Master_files/simulation/illumina_to_hugo", sep='\t')