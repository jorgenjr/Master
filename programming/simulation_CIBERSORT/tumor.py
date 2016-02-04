
import numpy as np, random, file_handler, noise, copy

def random_tumor_content(NP_GENE_DICTIONARY):

	""" Generates 30 x 30 datasets with random tumor content.
	1. Generate a random tumor content (0 - 100%).
	2. Use that tumor content percentage to generate 30 datasets with different noise values.
	"""

	num_tumor = 1
	num_noise = 1
	iteration = 1

	max_tumor = 1 # Normally 30
	max_noise = 1 # Normally 30

	for i in range(0,max_tumor):

		# ELLER 0 -> 99? Er slik i artikkelen.
		tumor_content = random.randint(0,100)

		for j in range(0,max_noise):
			
			add_tumor_content(NP_GENE_DICTIONARY, tumor_content, str(num_tumor) + "_" + str(num_noise));

			print ("Done with ", round((iteration/(max_tumor*max_noise))*100, 2), "%")

			num_noise += 1;
			iteration += 1;

		num_tumor += 1;
		num_noise = 1;

def add_tumor_content(NP_GENE_DICTIONARY, TUMOR_CONTENT, NUM_FILE):

	""" Adding the tumor content to the cell lines including noise.
	"""

	CELL_LINE_CONTENT = (((100 - TUMOR_CONTENT) * 5) / 4) / 100;
	fixed_tumor_content = (TUMOR_CONTENT * 5) / 100;
	np_matrix_gene = {}
	
	for key, value in NP_GENE_DICTIONARY.items():
		
		noise_value = noise.add_noise([copy.deepcopy(value)])
		
		np_matrix_gene[key] = np.array([(noise_value[0][1] * CELL_LINE_CONTENT) + (noise_value[0][0] * fixed_tumor_content / 4), (noise_value[0][2] * CELL_LINE_CONTENT) + (noise_value[0][0] * fixed_tumor_content / 4), (noise_value[0][3] * CELL_LINE_CONTENT) + (noise_value[0][0] * fixed_tumor_content / 4), (noise_value[0][4] * CELL_LINE_CONTENT) + (noise_value[0][0] * fixed_tumor_content / 4)])

	file_handler.write_to_file(np_matrix_gene, NUM_FILE);

	for key, value in NP_GENE_DICTIONARY.items():
		print("10: ", key, ": ", value)
		break;