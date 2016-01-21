
import readline, numpy as np, rpy2.robjects as robjects

from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage

#from rpy2.robjects.packages import importr

# test = robjects.r('''
# 	EnsembleToHGNC<-function(EnsembleIDs, organism="hsapiens_gene_ensembl"){

# 	  require(biomaRt);
# 	  ensemble<-useMart("ensembl");
# 	  hsp<-useDataset(mart=ensemble,dataset=organism);
# 	  ids<-getBM(filters= "ensembl_gene_id",
# 	              attributes= c("ensembl_gene_id","hgnc_id", "hgnc_symbol","description"),
# 	              values= EnsembleIDs, mart= hsp);
# 	  return(ids);
# 	}
# 	''')

string = '''
	EnsembleToHGNC<-function(organism="hsapiens_gene_ensembl"){

	  require(biomaRt);
	  EnsembleIDs <- read.table("http://dpaste.com/26KQJ76.txt")
	  ensemble<-useMart("ensembl");
	  hsp<-useDataset(mart=ensemble,dataset=organism);
	  ids<-getBM(filters= "ensembl_gene_id",
	              attributes= c("ensembl_gene_id","hgnc_id", "hgnc_symbol","description"),
	              values= EnsembleIDs, mart= hsp);
	  return(ids);
	}
	'''

# powerpack = SignatureTranslatedAnonymousPackage(string, "powerpack")

# print(powerpack.EnsembleToHGNC())

# test = robjects.r('''
# 	library(biomaRt)
# 	dat<-read.table("http://dpaste.com/3JY819Y.txt")
# 	probes<-as.vector(as.matrix(dat))
# 	human = useMart("ensembl", dataset = "mmusculus_gene_ensembl")
# 	g = getBM( id = probes, type = "affy_mg_u74av2", mart = human)
# 	show(g)
# 	''')

# string = '''
# 	EnsembleToHGNC<-function(organism="mmusculus_gene_ensembl"){

# 	  require(biomaRt);
# 	  EnsembleIDs <- read.table("http://dpaste.com/3JY819Y.txt")
# 	  ensemble<-useMart("ensembl");
# 	  hsp<-useDataset(mart=ensemble,dataset=organism);
# 	  ids<-getBM(filters= "ensembl_gene_id",
#               attributes= c("ensembl_gene_id","mgi_id", "mgi_symbol","mgi_description"),
#               values= EnsembleIDs, mart= hsp);
# 	  return(ids);
# 	}
# 	'''

# powerpack = SignatureTranslatedAnonymousPackage(string, "powerpack")

# print(powerpack.EnsembleToHGNC())

# asd = robjects.r('''
#         f <- function(r, verbose=FALSE) {
#             if (verbose) {
#                 cat("I am calling f().\n")
#             }
#             2 * pi * r
#         }
#         f(3)
#         ''')

# print (asd)

f_read = open('../../../Master_files/output/testfile_1_1', 'r')
f_write = open('../../../Master_files/output/testfile_1_1_geneid', 'w')
i = True

for line in f_read:

	if (i):
		i = False
		continue

	splitted_line = line.split('\t')
	f_write.write(splitted_line[0] + '\n')
