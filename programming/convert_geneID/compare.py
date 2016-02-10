
import time

def get_gene_from_lm22():

	""" Reads LM22.txt and retrieves the gene ID from it.
	"""

	f_lm = open('../../../Master_files/external/LM22.txt', 'r')
	skip = True
	lm = []

	for line in f_lm:
		
		if (skip == True):
			skip = False
			continue;

		splitted_line = line.split('\t')
		lm.append(splitted_line[0])
		
	f_lm.close()

	return lm


def get_gene_from_diff_exp():

	""" Reads diff_exp_hugo and retrieves the gene ID from it.
	"""

	f_diff_exp_hugo = open('../../../Master_files/diff_exp/diff_exp_hugo', 'r')
	skip = True
	diff_exp_hugo = []

	for line in f_diff_exp_hugo:
		
		if (skip == True):
			skip = False
			continue;

		splitted_line = line.split('\t')
		hugo_symbol = splitted_line[0].split('"')
		diff_exp_hugo.append(hugo_symbol[1])
		
	f_diff_exp_hugo.close()

	return diff_exp_hugo


def compare_against_lm22(hugo_genes):

	""" Reads hugo, retrieves gene ID from it, and compares it to genes from LM22.
	If a match, then the variable 'match' is incremented.
	If a match, but not found earlier, then added to 'unique_match' list.
	"""

	#f_hugo = open('../../../Master_files/simulation/affy_to_hugo', 'r')
	f_hugo = open('../../../Master_files/output/signature.txt', 'r')
	skip = True
	match = 0
	unique_match = []

	for line in f_hugo:

		if (skip == True):
			skip = False
			continue;

		splitted_line = line.split('\t')
		
		# FOR AFFY_TO_HUGO:
		#hugo_symbol_list = splitted_line[2].split('"')
		#hugo_symbol = hugo_symbol_list[1]
		
		# FOR SIGNATURE:
		hugo_symbol = splitted_line[0]

		if (hugo_symbol in hugo_genes):
			match += 1

			if (hugo_symbol not in unique_match):
				unique_match.append(hugo_symbol)
			

	unique_match.sort()
	f_hugo.close()
	
	return match, unique_match

def write_matches_to_file(match, unique_match):

	""" Write total matches, total unique matches, and all unique genes to file.
	"""

	f_matches = open('../../../Master_files/convert/matches', 'w')

	f_matches.write("Total matches: " + str(match) + '\n')
	f_matches.write("Unique gene matches: " + str(len(unique_match)) + '\n')

	for i in range(len(unique_match)):
		f_matches.write(unique_match[i] + "\n")

	f_matches.close()

# lm = get_gene_from_lm22()
diff_exp = get_gene_from_diff_exp()
match, unique_match = compare_against_lm22(diff_exp)
write_matches_to_file(match, unique_match)