# Master thesis

## DeconSim

### Description

DeconSim is a bioinformatics workflow to deconvolve highly similar cell types from tumor. It automates the whole process of running simulation script, CIBERSORT and LLSR. It is facilitated to have more deconvolution algorithms added to it, thus some minor adjustments may occur.

### Run

You have the opportunity to run with three different flags: -m (mixtures), -c (cell lines) and -t (tumors). For running CIBERSORT and LLSR for checking whether they can recognize tumor content in mixtures, simply use the -m and -t flag. If you want to create a reference file for CIBERSORT (which uses the reference file and a phenotype classes file to create a signature matrix), 'simulation.py' must be run separately (more information below). In order to run the script for your preference, you will need to edit settings in 'config.py' which is located in the same folder as 'deconsim.py'.

In the config file there are several variables that need to be given values before running:

1. PATH: Path to the project, e.g.: "/home/user/Projects/";
2. START_TUMOR: At what percentage of tumor content you want to start at, e.g.: 0
3. STOP_TUMOR: At what percentage of tumor content you want to be maximum (if 100, have it just above, e.g. 101. Depends on on the value of STEP_TUMOR), e.g.: 101
4. STEP_TUMOR: The amount of percentage which is increased for each dataset, e.g.: 5
5. START_NOISE: At what percentage of noise content you want to start at, e.g.: 0
6. STOP_NOISE: At what percentage of noise content you want to be maximum (if 90, have it just above, e.g. 91. Depends on on the value of STEP_TUMOR), e.g.: 91
7. STEP_NOISE: The amount of percentage which is increased for each dataset, e.g.: 30
8. PATH_CIBERSORT: Path to the folder where 'CIBERSORT.jar' is located, e.g.: PATH + "CIBERSORT/CIBERSORT.jar"
9. PATH_CIBERSORT_R: Path to the folder where 'run_CIBERSORT.R' is located. It is a script which executes the R version of CIBERSORT. E.g.: Path + "CIBERSORT/run_CIBERSORT.R"
10. CIBERSORT_MIXTURES: Mixture files used for CIBERSORT. This would normally be the mixture file generated by the simulation script where tumor and noise are iterated from 0 to 95. The name of the mixture files can be changed in the config file in the simulation_CIBERSORT folder. Example of value: PATH + "Master_files/simulation/mixtures_normalized_tumor_"
11. PHENOTYPE_CLASSES_FILE: A file which is needed to generate a signature matrix for CIBERSORT. This file tells CIBERSORT which cell lines in the reference file which are to be compared to each other or ignored. See example files or read more at cibersort.stanford.edu. Example of value: PATH + "Master_files/simulation/phenotype_classes"
11. REFERENCE_FILE: A file which consists of pure cell lines (at least one replicate for each cell line), it is used by CIBERSORT to create a signature matrix together with the phenotype classes file. E.g.: PATH + "Master_files/simulation/separate_cell_lines_norm"
12. SIGNATURE_FILE: If you already have a signature genes file. It is used by CIBERSORT. E.g.: PATH + "Master_files/external/random_signature_genesQ"
13. CIBERSORT_OUTPUT: The name of the output result from CIBERSORT, e.g.: PATH + "Master_files/output/CIBERSORT_referencenorm_"
14. CIBERSORT_R_OUTPUT: The name of the output result from the R version of CIBERSORT, e.g.: PATH + "Master_files/output/CIBERSORT_R_real_log_"
15. PATH_ABBAS: Path to the folder where Abbas file is located, e.g.: PATH + "Master/programming/abbas/abbas.r"
16. PATH_LLSR: Path to the folder where LLSR file is located, e.g.: PATH + "Master/programming/abbas/llsr.r"
17. COMBINED_CELLS: A file which consists of pure cell lines (no replicates), it is used by LLSR to calculate the coefficients. Example of value: PATH + "Master_files/simulation/combined_cell_lines"
18. LLSR_MIXTURES: Mixture files used for LLSR. This would normally be the mixture file genereated by the simulation script where tumor and noise are iterated from 0 to 95. The name of the mixture files can be changed in the config file in the simulation_CIBERSORT folder. CIBERSORT and LLSR must be run with the same mixture files to be able to compare the results. Example of value: PATH + "Master_files/simulation/mixtures_normalized_tumor_"
19. ABBAS_OUTPUT: The name of the output result from Abbas, e.g.: PATH + "Master_files/abbas/Abbas_tumor_"
20. LLSR_OUTPUT: The name of the output result from LLSR, e.g.: PATH + "Master_files/abbas/Abbas_tumor_"
21. CIBERSORT_FIRST_MIX: Indicates the index of the first mix in the CIBERSORT output, used by the voting script. E.g.: 2
22. CIBERSORT_LAST_MIX: Indicates the index of the last mix in the CIBERSORT output, used by the voting script. E.g.: 5
23. CIBERSORT_FIRST_CELL: Indicates the index of the first cell in the CIBERSORT output, used by the voting script. E.g.: 1
24. CIBERSORT_LAST_CELL: Indicates the index of the last cell in the CIBERSORT output, used by the voting script. E.g.: 4
25. CIBERSORT_PVALUE: Indicates the index of the P-value in the CIBERSORT output, used by the voting script. E:g.: 5
26. CIBERSORT_PEARSON: Indicates the index of the Pearson correlation in the CIBERSORT output, used by the voting script. E.g.: 6
27. ABBAS_FIRST_CELL: Indicates the index of the first cell in the Abbas output, used by the voting script. E.g.: 3
28. ABBAS_LAST_CELL: Indicates the index of the last cell in the Abbas output, used by the voting script. E.g.: 6
29. ABBAS_FIRST_MIX: Indicates the index of the first mix in the Abbas output, used by the voting script. E.g.: 1
30. ABBAS_LAST_MIX: Indicates the index of the last mix in the Abbas output, used by the voting script. E.g.: 4
31. ACTUAL_AMOUNT: An array which shows the actual coefficients in a data set, in this case GSE11103. E.g.:
[[0.250, 0.125, 0.250, 0.375],
 [0.050, 0.317, 0.475, 0.158],
 [0.010, 0.495, 0.165, 0.330],
 [0.002, 0.333, 0.333, 0.333]]
32. VOTE_OPTIONS: The two different ways of voting: union and intersection. SHOULD NOT BE CHANGED.
33. VOTE: Indicates the index of the possible choices for voting options (VOTE_OPTIONS), e.g.: 0
34. VOTE_VARIABLE: The three different voting parameters: P-value, Pearson correlation and coefficients. SHOULD NOT BE CHANGED.
35. VOTE_V: Indicates the index of the possible choices for voting parameters (VOTE_VARIABLE), e.g.: 2
36. THRESHOLD_COEF: A threshold value for coefficients, e.g.: 0.05
37. THRESHOLD_PVALUE: A threshold value for P-values, e.g.: 0.05
38. THRESHOLD_PEARSON: A threshold value for Pearson correlation, e.g.: 0.6

E.g. execute:
```
script$ python deconsim.py -m GSE11103.txt -t GSM269529.txt GSM269530.txt
```

### Disclaimer

In order to run this framework optimally, please note:

1. The simulation script will ask for which columns in the matrices (mixture files, tumor files, etc.) you want to use, and every file must contain equal set of replicates. E.g.: In file A, you CANNOT use column 1 and 2 for cell X and column 3, 4, 5 and 6 for cell Y. Instead: In file A, you can use column 1, 2 and 3 for cell X, column 4, 5 and 6 for cell Y etc., meaning that each cell (or mixture) must be equal within a file.
2. Allow execution of R scripts by using chmod.

## Simulation (CIBERSORT)

### Description

If you want to run the simulation script separately (not from deconsim.py). This is a script which is interpreted and replicated from the text [CIBERSORT](http://www.nature.com/nmeth/journal/v12/n5/abs/nmeth.3337.html) simulation of tumors with added noise. Written in Python.

### Run

Available flags are -t (tumors), -m (mixtures), -c (cell lines), -r (reference) and -i (iteration).

If you are running -m, it is required that you use -i as well. The syntax is: -i \[start tumor percent\] \[end tumor percent\] \[step tumor percent\] \[start noise percent\] \[end noise percent\] \[step noise percent\] and an example would be: -i 0 100 5 0 100 5

Execute (almost the same as deconsim.py):
```
simulation_CIBERSORT$ python simulation.py -t GSM269529.txt GSM269530.txt -m GSE11103.txt -i 0 100 5 0 100 5
```
or
```
simulation_CIBERSORT$ python simulation.py -t GSM269529.txt GSM269530.txt -c GSE11103.txt -r true
```

## Convert

### Description

Running the simulation of tumors based on CIBERSORTs implementation results in gene ids being represented as Affy IDs (HGU133 plus 2.0), instead of HUGO IDs. This is a standalone part of the thesis and not a part of 'DeconSim'. Please read the 'Disclaimer' before converting Affy IDs to HUGO IDs.

### Run

First run convert.R to map Affy IDs to HUGO genes.

Open convert.R in Rstudio and run it. To change the input/output file, you need to change it in the source code.

replace.py will replace all the Affy IDs from your original cell lines with HUGO IDs. If there are several genes with same ID, they will be added together, then an average score will be calculated.

Execute:
```
convert_geneID$ python replace.py
```
To change the input/output file, you need to change it in the source code. The output will be a file which will end up with a number of genes ~20.000.

### Disclaimer

A few things to remember before converting Affy to HUGO:

1. There are about ~5.000 probes in Affy which does not map to a HUGO gene symbol and is therefore thrown.
2. ~10.000 HUGO genes (of ~20.000) have two or more Affy probes mapped to it. This means that the total score of the probes mapped to a HUGO gene is divided by the number of probes, and this score is kept (i.e. an average score).

Regarding the notes above, there are important "information" which are removed or missed by converting Affy to HUGO and one should not convert the Affy to HUGO in order to preserve the original signals/data.

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