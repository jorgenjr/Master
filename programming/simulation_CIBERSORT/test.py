
import random, numpy as np

f = random.uniform(0.0, 0.99999)
q = 11.6
N = np.random.normal(0,f*q)
noise = 2 ** N

print(noise)

# f = open('../../../Master_files/external/GSE11103.txt', 'r')

# for line in f:
# 	print(line)