
import linecache

# Variables for GSE11103

BEGIN = 64
END = 54739
EOF = 54740
FILECOLS = 42


def read_files():

	""" Reads the GSE11103_series_matrix.txt and gathers the mixtures and cell lines:
	- Mix A
	- Mix B
	- Mix C
	- Mix D
	- Jurkat
	- IM-9
	- Raji
	- THP-1
	"""

	f_j = open('../../../Master_files/analyze_result/Jurkat', 'w')
	f_i = open('../../../Master_files/analyze_result/IM-9', 'w')
	f_r = open('../../../Master_files/analyze_result/Raji', 'w')
	f_t = open('../../../Master_files/analyze_result/THP-1', 'w')
	f_a = open('../../../Master_files/analyze_result/mix_A', 'w')
	f_b = open('../../../Master_files/analyze_result/mix_B', 'w')
	f_c = open('../../../Master_files/analyze_result/mix_C', 'w')
	f_d = open('../../../Master_files/analyze_result/mix_D', 'w')

	CJ_1 = 18; CJ_2 = 19; CJ_3 = 20
	CI_1 = 21; CI_2 = 22; CI_3 = 23
	CR_1 = 24; CR_2 = 25; CR_3 = 26
	CT_1 = 27; CT_2 = 28; CT_3 = 29
	MA_1 = 30; MA_2 = 31; MA_3 = 32
	MB_1 = 33; MB_2 = 34; MB_3 = 35
	MC_1 = 36; MC_2 = 37; MC_3 = 38
	MD_1 = 39; MD_2 = 40; MD_3 = 41

	f_j.write("!Sample_title\tJurkat\tJurkat\tJurkat\n")
	f_i.write("!Sample_title\tIM-9\tIM-9\tIM-9\n")
	f_r.write("!Sample_title\tRaji\tRaji\tRaji\n")
	f_t.write("!Sample_title\tTHP-1\tTHP-1\tTHP-1\n")	
	f_a.write("!Sample_title\tMIX A\tMIX A\tMIX A\n")
	f_b.write("!Sample_title\tMIX B\tMIX B\tMIX B\n")
	f_c.write("!Sample_title\tMIX C\tMIX C\tMIX C\n")
	f_d.write("!Sample_title\tMIX D\tMIX D\tMIX D\n")

	for x in range(BEGIN, END):

		line = linecache.getline('../../../Master_files/external/GSE11103_series_matrix.txt', x)
		line_list = line.split('\t')

		# GENES: Column index 0
		gene_ref = line_list[0].split('"')[1]

		f_j.write(gene_ref + '\t' + line_list[CJ_1] + '\t' + line_list[CJ_2] + '\t' + line_list[CJ_3] + '\n')
		f_i.write(gene_ref + '\t' + line_list[CI_1] + '\t' + line_list[CI_2] + '\t' + line_list[CI_3] + '\n')
		f_r.write(gene_ref + '\t' + line_list[CR_1] + '\t' + line_list[CR_2] + '\t' + line_list[CR_3] + '\n')
		f_t.write(gene_ref + '\t' + line_list[CT_1] + '\t' + line_list[CT_2] + '\t' + line_list[CT_3] + '\n')
		f_a.write(gene_ref + '\t' + line_list[MA_1] + '\t' + line_list[MA_2] + '\t' + line_list[MA_3] + '\n')
		f_b.write(gene_ref + '\t' + line_list[MB_1] + '\t' + line_list[MB_2] + '\t' + line_list[MB_3] + '\n')
		f_c.write(gene_ref + '\t' + line_list[MC_1] + '\t' + line_list[MC_2] + '\t' + line_list[MC_3] + '\n')
		f_d.write(gene_ref + '\t' + line_list[MD_1] + '\t' + line_list[MD_2] + '\t' + line_list[MD_3])

	f_j.close(); f_i.close(); f_r.close(); f_t.close()	
	f_a.close(); f_b.close(); f_c.close(); f_d.close()

read_files()