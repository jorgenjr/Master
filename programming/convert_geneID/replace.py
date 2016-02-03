
import copy, time

f_hugo = open('../../../Master_files/diff_exp/hugo', 'r')
f_simulation = open('../../../Master_files/simulation/testfile_1_1', 'r')
f_simulation_hugo = open('../../../Master_files/convert/simulation_hugo', 'w')
f_simulation_hugo_unique = open('../../../Master_files/convert/simulation_hugo_unique', 'w')
header = True
affy_to_hugo = {}
unique_hugo_genes = []

for line in f_hugo:

	if (header == True):
		header = False
		continue

	splitted_line = line.split('\t')
	affy = splitted_line[1].split('\"')
	hugo = splitted_line[2].split('\"')
	
	if hugo[1] and not hugo[1].isspace():
		affy_to_hugo[affy[1]] = hugo[1]

f_hugo.close()
header = True

for line in f_simulation:

	if (header == True):
		f_simulation_hugo.write(line)
		f_simulation_hugo_unique.write(line)
		header = False
		continue

	splitted_line = line.split('\t')

	try:
		geneid = affy_to_hugo[splitted_line[0]]
		f_simulation_hugo.write(geneid + '\t' + splitted_line[1] + '\t' + splitted_line[2] + '\t' + splitted_line[3] + '\t' + splitted_line[4]);

		if len(unique_hugo_genes) == 0:
			unique_hugo_genes.append([geneid, [float(splitted_line[1]), float(splitted_line[2]), float(splitted_line[3]), float(splitted_line[4][:-1])], 1]);
			continue;

		found = False;

		for i in range(len(unique_hugo_genes)):
			
			if unique_hugo_genes[i][0] == geneid:
				unique_hugo_genes[i][1] = [unique_hugo_genes[i][1][0] + float(splitted_line[1]), unique_hugo_genes[i][1][1] + float(splitted_line[2]), unique_hugo_genes[i][1][2] + float(splitted_line[3]), unique_hugo_genes[i][1][3] + float(splitted_line[4])]
				unique_hugo_genes[i][2] = unique_hugo_genes[i][2] + 1;
				found = True;
				break;
			

		if (found == False):
			unique_hugo_genes.append([geneid, [float(splitted_line[1]), float(splitted_line[2]), float(splitted_line[3]), float(splitted_line[4][:-1])], 1]);

	except KeyError:
		# print("Error!")
		pass

for i in range(len(unique_hugo_genes)):
	if (unique_hugo_genes[i][2] > 1):
		unique_hugo_genes[i][1] = [unique_hugo_genes[i][1][0] / float(unique_hugo_genes[i][2]), unique_hugo_genes[i][1][1] / float(unique_hugo_genes[i][2]), unique_hugo_genes[i][1][2] / float(unique_hugo_genes[i][2]), unique_hugo_genes[i][1][3] / float(unique_hugo_genes[i][2])]

for i in range(len(unique_hugo_genes)):
	f_simulation_hugo_unique.write(unique_hugo_genes[i][0] + '\t' + str(unique_hugo_genes[i][1][0]) + '\t' + str(unique_hugo_genes[i][1][1]) + '\t' + str(unique_hugo_genes[i][1][2]) + '\t' + str(unique_hugo_genes[i][1][3]) + '\n')

f_simulation.close()
f_simulation_hugo.close()
f_simulation_hugo_unique.close()