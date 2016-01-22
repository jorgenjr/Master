
import time

f_lm = open('../../../Master_files/input/LM22.txt', 'r')
f_hugo = open('hugo.txt', 'r')

lm = []
hugo = []
match = 0
unique_match = []
skip = True

for line in f_lm:
	
	if (skip):
		skip = False
		continue;

	splitted_line = line.split('\t')
	lm.append(splitted_line[0])
	
skip = True

for line in f_hugo:

	if (skip):
		skip = False
		continue;

	splitted_line = line.split('\t')
	hugo_symbol = splitted_line[2].split('"')
	hugo.append(hugo_symbol[1])
	
	if (hugo_symbol[1] in lm):
		match += 1

		if (hugo_symbol[1] not in unique_match):
			unique_match.append(hugo_symbol[1])
			

unique_match.sort()
f = open('matches.txt', 'w')
f.write("Total matches: " + str(match) + '\n')
f.write("Unique gene matches: " + str(len(unique_match)) + '\n')

for i in range(len(unique_match)):
	f.write(unique_match[i] + "\n")

f.close()
f_lm.close()
f_hugo.close()