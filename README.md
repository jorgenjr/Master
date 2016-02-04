# Master thesis

## CIBERSORT

### Description

Replicating [CIBERSORT](http://www.nature.com/nmeth/journal/v12/n5/abs/nmeth.3337.html) simulation of tumors with added noise. Written in Python.

### Run

For running this script, you need to have the following folder setup ("Master" is the origin git folder):

1. folder_name/Master/programming/simulation_CIBERSORT/simulation.py
2. folder_name/Master_files/simulation/
3. folder_name/Master_files/diff_exp/
4. folder_name/Master_files/convert/

This is due to large input (and output) files, which are too big for the 100 MB limit with a free GitHub account.

Execute:
```
simulation_CIBERSORT$ python simulation.py -i GSM269529.txt GSM269530.txt GSE11103_series_matrix.txt -o [output.file ...]
```

## Convert

### Description

Running the simulation of tumors based on CIBERSORTs implementation results in gene ids being represented as Affy IDs (HGU133 plus 2.0), instead of HUGO IDs (CIBERSORT requires HUGO as gene ID).

### Run

First run from_gsm_to_geneid.py to take your resulting cell lines from the CIBERSORT simulation to only save the gene IDs.

Execute:
```
convert_geneID$ python from_gsm_to_geneid.py
```
Open convert.R in Rstudio and run it. To change the input/output file, you need to change it in the code.

If you need to replace Affy IDs with HUGO IDs, run replace.py. It will replace all the Affy IDs from your original cell lines with HUGO IDs. If there are several genes with same ID, they will be added together, then a average score will be calculated.

Execute:
```
convert_geneID$ python replace.py
```
The output will be two files: simulation_hugo and simulation_hugo_unique:

The first one has translated Affy IDs to HUGO, removed unreadable Affy IDs and contains duplicates of genes.

The second one, however, does not contain duplicates and will end up with a number of genes ~20.000.

## Compare

### Description

After converting Affy IDs to HUGO IDs, you need to compare the new HUGO IDs to the ones provided in LM22 (a signature genes file created by the authors of the CIBERSORT algorithm). Running this script will create an output file where the number of matches, unique matches, and every HUGO gene from comparing your file against LM22 will be written.

### Run

To change the input files for comparing, you need to change it in the code.

Execute:
```
convert_geneID$ python compare.py
```
