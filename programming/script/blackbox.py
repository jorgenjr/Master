
import readline, os, sys

from subprocess import call


FLAGS = []
MIXTURES = []
TUMORS = []


def read_args():

	""" Reading the arguments sent by the user from the terminal.
	-i flag must be followed by input file(s)
	-o flag must be followed by output file(s)

	The given files must be placed outside the "Master" folder:
	Code: folder_name/Master/programming/simulation_CIBERSORT/simulation.py
	Files: folder_name/Master_files/simulation/

	E.g.: python simulation.py -i GSM269529.txt -o GSM269529_NEW.txt
	"""

	if len(sys.argv) == 1:
		print('\n[ERROR] Wrong sys.argv format! Too few arguments. Run:\n\npython simulation.py -i [input.file input.file ...] -o [output.file output.file]\n')
		sys.exit()

	m = False; t = False;

	for x in range(1, len(sys.argv)):
		print(sys.argv[x])
		# INPUT
		if sys.argv[x] == '-i':
			print(sys.argv[x])
		# CELL LINE
		elif sys.argv[x] == '-c':
			FLAGS.append("C")
			continue
		# MIXTURE
		elif sys.argv[x] == '-m':
			FLAGS.append("M")
			m = True; t = False;
			continue
		# SIGNATURE
		elif sys.argv[x] == '-r':
			FLAGS.append("R")
			continue
		# TUMOR
		elif sys.argv[x] == '-t':
			FLAGS.append("T")
			m = False; t = True;
			continue

		if m == True:
			MIXTURES.append(sys.argv[x])
			continue

		elif t == True:
			TUMORS.append(sys.argv[x])
			continue

		print('\n[ERROR] Wrong sys.argv format! Run:\n\npython simulation.py -i [input.file input.file ...] -o [output.file output.file]\n')
		sys.exit()




def execute():
	# print (FLAGS)
	# print (MIXTURES)
	# print (TUMORS)

	print("Executing simulation script ... ")
	cmd = "python /home/jorgen/Projects/Master/programming/simulation_CIBERSORT/simulation.py -t GSM269529.txt GSM269530.txt -m GSE11103.txt"
	os.system(cmd)

	print("Simulation completed! Converting Affy to HUGO now ... ")
	cmd = "python /home/jorgen/Projects/Master/programming/convert_geneID/replace.py -t"
	os.system(cmd)

	print("Conversion completed! Executing CIBERSORT ... ")
	cmd = "java -Xmx3g -Xms3g -jar /home/jorgen/Projects/CIBERSORT/CIBERSORT.jar -M /home/jorgen/Projects/Master_files/convert/simulation_hugo_unique_tumor_0 -B /home/jorgen/Projects/Master_files/output/signature_tumor_0.txt > /home/jorgen/Projects/Master_files/output/CIBERSORT_result_tumor_0"
	os.system(cmd)

	print("CIBERSORT completed!")

read_args()
execute()