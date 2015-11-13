# Master thesis

## CIBERSORT

### Description

Replicating [CIBERSORT](http://www.nature.com/nmeth/journal/v12/n5/abs/nmeth.3337.html) simulation of tumors with added noise. Written in Python.

### Run

For running this script, you need to have the following folder setup ("Master" is the origin git folder):

1. folder_name/Master/programming/simulation_CIBERSORT/simulation.py
2. folder_name/Master_files/input/
3. folder_name/Master_files/output/

This is due to large input (and output) files, which are too big for the 100 MB limit with a free GitHub account.

Execute:
simulation_CIBERSORT$ python simulation.py -i [input.file input.file ... ] -o [output.file output.file ...]
