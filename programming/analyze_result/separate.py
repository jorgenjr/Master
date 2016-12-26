
import linecache

# Variables for GSE11103

BEGIN = 1
END = 22284
EOF = 22285
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


def separate_mixtures():

	""" Reads the GSE11103_series_matrix.txt and gathers the mixtures:
	- Mix A
	- Mix B
	- Mix C
	- Mix D
	"""

	f = open('../../../Master_files/analyze_result/mixtures', 'w')

	MA_1 = 30; MA_2 = 31; MA_3 = 32
	MB_1 = 33; MB_2 = 34; MB_3 = 35
	MC_1 = 36; MC_2 = 37; MC_3 = 38
	MD_1 = 39; MD_2 = 40; MD_3 = 41

	f.write("!Sample_title\tMIX A\tMIX A\tMIX A\tMIX B\tMIX B\tMIX B\tMIX C\tMIX C\tMIX C\tMIX D\tMIX D\tMIX D\n")

	for x in range(BEGIN, END):

		line = linecache.getline('../../../Master_files/external/GSE11103_series_matrix.txt', x)
		line_list = line.split('\t')

		# GENES: Column index 0
		gene_ref = line_list[0].split('"')[1]

		f.write(gene_ref + '\t' + line_list[MA_1] + '\t' + line_list[MA_2] + '\t' + line_list[MA_3] + '\t' + line_list[MB_1] + '\t' + line_list[MB_2] + '\t' + line_list[MB_3] + '\t' + line_list[MC_1] + '\t' + line_list[MC_2] + '\t' + line_list[MC_3] + '\t' + line_list[MD_1] + '\t' + line_list[MD_2] + '\t' + line_list[MD_3])

	f.close();


def get_relevant_cells():

	fr = open('../../../Master_files/external/GSE22886.txt', 'r')
	fw = open('../../../Master_files/external/GSE22886_new.txt', 'w')

	Tcd8Start = 1
	Tcd8End = 5
	Tcd4ResStart = 19
	Tcd4ResEnd = 22
	Tcd4ActStart = 22
	Tcd4ActEnd = 25
	NKResStart = 25
	NKResEnd = 29
	NKActStart = 29
	NKActEnd = 40
	BnaiveStart = 40
	BnaiveEnd = 47
	BmemoryStart = 47
	BmemoryEnd = 55
	PlasmaStart = 55
	PlasmaEnd = 62
	MonoStart = 62
	MonoEnd = 74
	MacM0Start = 86
	MacM0End = 98
	DenResStart = 98
	DenResEnd = 104
	DenActStart = 104
	DenActEnd = 110
	NeuStart = 110
	NeuEnd = 115

	Header = True

	for line in fr:

		splitted_line = line.split('\t')
		fw.write(splitted_line[0])

		# T cells CD8 GSM565269 GSM565270 GSM565271 GSM565272
		for i in range(Tcd8Start, Tcd8End):
			if Header == True:
				fw.write("\tT cells CD8")
			else:
				fw.write("\t" + splitted_line[i])

		# T cells CD4 memory resting GSM565287 GSM565288 GSM565289
		for i in range(Tcd4ResStart, Tcd4ResEnd):
			if Header == True:
				fw.write("\tT cells CD4 memory resting")
			else:
				fw.write("\t" + splitted_line[i])

		# T cells CD4 memory activated GSM565290 GSM565291 GSM565292
		for i in range(Tcd4ActStart, Tcd4ActEnd):
			if Header == True:
				fw.write("\tT cells CD4 memory actived")
			else:
				fw.write("\t" + splitted_line[i])

		# NK cells resting GSM565293 GSM565294 GSM565295 GSM565296
		for i in range(NKResStart, NKResEnd):
			if Header == True:
				fw.write("\tNK cells resting")
			else:
				fw.write("\t" + splitted_line[i])

		# NK cells activated GSM565297 GSM565298 GSM565299 GSM565300 GSM565301 GSM565302 GSM565303 GSM565304 GSM565305 GSM565306 GSM565307
		for i in range(NKActStart, NKActEnd):
			if Header == True:
				fw.write("\tNK cells activated")
			else:
				fw.write("\t" + splitted_line[i])

		# B cells naïve GSM565308 GSM565309 GSM565310 GSM565311 GSM565312 GSM565313 GSM565314
		for i in range(BnaiveStart, BnaiveEnd):
			if Header == True:
				fw.write("\tB cells naïve")
			else:
				fw.write("\t" + splitted_line[i])

		# B cells memory GSM565315 GSM565316 GSM565317 GSM565318 GSM565319 GSM565320 GSM565321 GSM565322
		for i in range(BmemoryStart, BmemoryEnd):
			if Header == True:
				fw.write("\tB cells memory")
			else:
				fw.write("\t" + splitted_line[i])

		# Plasma cells GSM565323 GSM565324 GSM565325 GSM565326 GSM565327 GSM565328 GSM565329
		for i in range(PlasmaStart, PlasmaEnd):
			if Header == True:
				fw.write("\tPlasma cells")
			else:
				fw.write("\t" + splitted_line[i])

		# Monocytes GSM565330 GSM565331 GSM565332 GSM565333 GSM565334 GSM565335 GSM565336 GSM565337 GSM565338 GSM565339 GSM565340 GSM565341
		for i in range(MonoStart, MonoEnd):
			if Header == True:
				fw.write("\tMonocytes")
			else:
				fw.write("\t" + splitted_line[i])

		# Macrophages M0 GSM565354 GSM565355 GSM565356 GSM565357 GSM565358 GSM565359 GSM565360 GSM565361 GSM565362 GSM565363 GSM565364 GSM565365
		for i in range(MacM0Start, MacM0End):
			if Header == True:
				fw.write("\tMacrophages M0")
			else:
				fw.write("\t" + splitted_line[i])

		# Dendritic cells resting GSM565366 GSM565367 GSM565368 GSM565369 GSM565370 GSM565371
		for i in range(DenResStart, DenResEnd):
			if Header == True:
				fw.write("\tDendritic cells resting")
			else:
				fw.write("\t" + splitted_line[i])

		# Dendritic cells activated GSM565372 GSM565373 GSM565374 GSM565375 GSM565376 GSM565377
		for i in range(DenActStart, DenActEnd):
			if Header == True:
				fw.write("\tDendritic cells activated")
			else:
				fw.write("\t" + splitted_line[i])

		# Neutrophils GSM565378 GSM565379 GSM565380 GSM565381 GSM565382
		for i in range(NeuStart, NeuEnd):
			if Header == True:
				fw.write("\tNeutophils")
			else:
				fw.write("\t" + splitted_line[i])

		if Header == True:
			fw.write("\n")
			Header = False
		# break

	fr.close()
	fw.close()

	fr = open('../../../Master_files/external/GSE4527.txt', 'r')
	fw = open('../../../Master_files/external/GSE4527_new.txt', 'w')

	Treg1 = 2
	Treg2 = 4

	Header = True

	for line in fr:

		splitted_line = line.split('\t')
		fw.write(splitted_line[0])

		# T cells regulatory (Tregs) GSM101519 GSM101521
		if Header == True:
			fw.write("\tT cells regulatory\tT cells regulatory\n")
		else:
			fw.write("\t" + splitted_line[Treg1] + "\t" + splitted_line[Treg2] + "\n")

		if Header == True:
			Header = False

	fr.close()
	fw.close()

	fr = open('../../../Master_files/external/GSE5099.txt', 'r')
	fw = open('../../../Master_files/external/GSE5099_new.txt', 'w')

	M1Start = 10
	M1End = 13
	M2Start = 13
	M2End = 16

	Header = True

	for line in fr:

		splitted_line = line.split('\t')
		fw.write(splitted_line[0])

		# Macrophages M1 GSM115055 GSM115056 GSM115057
		for i in range(M1Start, M1End):
			if Header == True:
				fw.write("\tMacrophages M1")
			else:
				fw.write("\t" + splitted_line[i])

		# Macrophages M2 GSM115058 GSM115059 GSM115060
		for i in range(M2Start, M2End):
			if Header == True:
				fw.write("\tMacrophages M2")
			else:
				fw.write("\t" + splitted_line[Treg1])

		fw.write("\n")

		if Header == True:
			Header = False

	fr.close()
	fw.close()

	fr = open('../../../Master_files/external/GSE26495_new.txt', 'r')
	fw = open('../../../Master_files/external/GSE26495_PD1lowhigh.txt', 'w')

	highStart = 5
	highEnd = 11
	lowStart = 11
	lowEnd = 17

	Header = True

	for line in fr:

		splitted_line = line.split('\t')
		fw.write(splitted_line[0])

		# PD-1 high
		for i in range(highStart, highEnd):
			if Header == True:
				fw.write("\tPD-1 high")
			else:
				fw.write("\t" + splitted_line[i])

		# PD-1 low
		for i in range(lowStart, lowEnd):
			if Header == True:
				fw.write("\tPD-1 low")
			else:
				fw.write("\t" + splitted_line[Treg1])

		fw.write("\n")

		if Header == True:
			Header = False

	fr.close()
	fw.close()


def get_only_probes():

	fr = open('../../../Master_files/external/output_2016-11-01/processeddata/normdata.txt', 'r')
	fw = open('../../../Master_files/external/normdata.txt', 'w')

	for line in fr:

		splitted_line = line.split('\t')
		fw.write(splitted_line[0])

		for i in range(3, len(splitted_line)):

			fw.write('\t' + splitted_line[i])

	fr.close()
	fw.close()


#read_files()
#separate_mixtures()
#get_relevant_cells()
get_only_probes()
