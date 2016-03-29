# Master thesis

## Black box

### Description

The black box is a script which automates the whole process of running simulation script, CIBERSORT and Abbas.

### Run

You have the opportunity to run with three different flags: -m (mixtures), -c (cell lines) and -t (tumors). For running CIBERSORT and Abbas for checking whether they can recognize tumor content in mixtures, simply use the -m and -t flag. If you want to create a reference file for CIBERSORT (which uses the reference file to create a signature matrix), use -c and -t flags.

In the source code there are several variables that need to be given values before running:

1. PATH: Path to the project, e.g.: "/home/jorgen/Projects/";
2. START_TUMOR: At what percentage of tumor content you want to start at, e.g.: 0
3. STOP_TUMOR: At what percentage of tumor content you want to be maximum (if 100, have it just above, e.g. 101. Depends on on the value of STEP_TUMOR), e.g.: 101
4. STEP_TUMOR: The amount of percentage which is increased for each dataset, e.g.: 5
5. START_NOISE: At what percentage of noise content you want to start at, e.g.: 0
6. STOP_NOISE: At what percentage of noise content you want to be maximum (if 90, have it just above, e.g. 91. Depends on on the value of STEP_TUMOR), e.g.: 91
7. STEP_NOISE: The amount of percentage which is increased for each dataset, e.g.: 30
8. REFERENCE_FILE: Path to where your reference file is located. A reference file is a file that contains cell lines which are to be used for creating the signature matrix in CIBERSORT, e.g.: PATH + "Master_files/convert/reference_hugo_unique_tumor"
9. PHENOTYPE_CLASSES_FILE: Path to where you phenotype classes file is located. A phenotype classes file is a file that contains which cell lines are to be compared to each other. It is needed for creating the signature matrix in CIBERSORT combined with the reference file. E.g. location: PATH + "Master_files/simulation/phenotype_classes_tumor"

E.g. execute:
```
script$ python blackbox.py -m GSE11103.txt -t GSM269529.txt GSM269530.txt
```

## CIBERSORT (simulation)

### Description

If you want to run the simulation script separately (not from blackbox.py). Replicating [CIBERSORT](http://www.nature.com/nmeth/journal/v12/n5/abs/nmeth.3337.html) simulation of tumors with added noise. Written in Python.

### Run

For running this script, you need to have the following folder setup ("Master" is the origin git folder):

1. folder_name/Master/programming/simulation_CIBERSORT/simulation.py
2. folder_name/Master_files/simulation/
3. folder_name/Master_files/diff_exp/
4. folder_name/Master_files/convert/
5. folder_name/Master_files/external/

This is due to large input (and output) files, which are too big for the 100 MB limit with a free GitHub account.

Available flags are -t (tumors), -m (mixtures), -c (cell lines) and -r (reference)

Execute (almost the same as blackbox.py):
```
simulation_CIBERSORT$ python simulation.py -t GSM269529.txt GSM269530.txt -m GSE11103.txt
```
or
```
simulation_CIBERSORT$ python simulation.py -t GSM269529.txt GSM269530.txt -c GSE11103.txt -r
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
The result is written to "matches"

## CIBERSORT (algorithm)

### Description

Request to download CIBERSORT executable .jar file from cibersort.stanford.edu and read their documentation on how to run the algorithm.

## Abbas (algorithm)

### Description

An algorithm which uses 'least square fit' to deconvolute cells from mixtures.

### Run

Example of execute with random files (from command line):
```
Rscript path/to/abbas/abbas.r path/to/cell_lines/combined_cell_lines_tumor path/to/mixture/mixtures_with_tumor_15_30 path/to/desired/output/folder/Abbas_result_tumor_15_30
```
It is required that you run it with three arguments. The first must be cell lines, the second mixture(s) and the last is where you want the output to be written.