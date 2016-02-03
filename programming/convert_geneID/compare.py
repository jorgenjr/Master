
import time

f_lm = open('../../../Master_files/convert/LM22.txt', 'r')
f_hugo = open('../../../Master_files/diff_exp/hugo', 'r')
f_matches = open('matches', 'w')

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

f_matches.write("Total matches: " + str(match) + '\n')
f_matches.write("Unique gene matches: " + str(len(unique_match)) + '\n')

for i in range(len(unique_match)):
	f_matches.write(unique_match[i] + "\n")

f_matches.close()
f_lm.close()
f_hugo.close()