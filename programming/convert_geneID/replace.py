
import copy, time

f_hugo = open('../../../Master_files/convert/hugo.txt', 'r')
f_simulation = open('../../../Master_files/simulation/testfile_1_1', 'r')
f_simulation_hugo = open('../../../Master_files/convert/simulation_hugo', 'w')
i = True
affy_to_hugo = {}

for line in f_hugo:

	if (i):
		i = False
		continue

	splitted_line = line.split('\t')
	affy = splitted_line[1].split('\"')
	hugo = splitted_line[2].split('\"')
	
	if hugo[1] and not hugo[1].isspace():
		affy_to_hugo[affy[1]] = hugo[1]

f_hugo.close()
i = True

for line in f_simulation:

	if (i):
		f_simulation_hugo.write(line)
		i = False
		continue

	splitted_line = line.split('\t')

	try:
		geneid = affy_to_hugo[splitted_line[0]]
		f_simulation_hugo.write(geneid + '\t' +
			splitted_line[1] + '\t' + splitted_line[2] + '\t' + 
			splitted_line[3] + '\t' + splitted_line[4]);
	except KeyError:
		print("Error!")
		pass

f_simulation.close()