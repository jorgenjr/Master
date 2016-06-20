
import matplotlib.pyplot as plt
import numpy as np
import linecache


N = 4

ind = np.arange(N)  # the x locations for the groups
width = 0.25       # the width of the bars
plt.rcParams.update({'font.size': 9})

def autolabel(rects, ax):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.3f' % float(height),
                ha='center', va='bottom')


def plot_result():

	first_line = linecache.getline('../../../Master_files/abbas/deconvoluted_test', 1)
	splitted_line = first_line.split("\t")

	for j in range(len(splitted_line)):

		ABBAS = open('../../../Master_files/abbas/deconvoluted_test', 'r')
		CIBERSORT = open('../../../Master_files/output/CIBERSORT_result_tumor_0', 'r')

		mix_abbas = []
		mix_cibersort = []

		for i, line in enumerate(ABBAS):
			if i > 0:
				mix_abbas.append(float(line.split('\t')[j+1]))

		skip = True

		for i, line in enumerate(CIBERSORT):
			
			splitted_line = line.split("\t")
			
			if splitted_line[0] == "0":
				skip = False

			if skip == False:
				mix_cibersort.append(float(splitted_line[j+1]))

		fig, ax = plt.subplots()

		rects1 = ax.bar(ind, (mix_abbas[0], mix_abbas[1], mix_abbas[2], mix_abbas[3]), width, color='r')
		rects2 = ax.bar(ind + (width), (mix_cibersort[0], mix_cibersort[1], mix_cibersort[2], mix_cibersort[3]), width, color='g')

		ax.set_ylabel('Scores')
		ax.set_ylim([0.0, 1.0])
		ax.set_title('Scores by cell lines')
		ax.set_xticks(ind + width)
		ax.set_xticklabels(('Jurkat', 'IM-9', 'Raji', 'THP-1'))

		ax.legend((rects1[0], rects2[0]), ('Abbas', 'CIBERSORT'))

		autolabel(rects1, ax)
		autolabel(rects2, ax)

		fig.savefig("mix" + str(j) + ".png")
		plt.close(fig)


#plot_result()
#java -Xmx3g -Xms3g -jar CIBERSORT.jar -M ../Master_files/simulation/mixtures_normalized -c ../Master_files/simulation/phenotype_classes -P ../Master_files/simulation/separate_cell_lines_norm > CIBERSORT_referencenorm

def mixture(MIX):

	REAL_JURKAT = 0; REAL_IM9 = 0; REAL_RAJI = 0; REAL_THP1 = 0;
	CIBERSORT_JURKAT = 0; CIBERSORT_IM9 = 0; CIBERSORT_RAJI = 0; CIBERSORT_THP1 = 0;
	ABBAS_JURKAT = 0; ABBAS_IM9 = 0; ABBAS_RAJI = 0; ABBAS_THP1 = 0;
	MIX_LINE = 0;

	if MIX == 'A':
		REAL_JURKAT = 0.25; REAL_IM9 = 0.125; REAL_RAJI = 0.25; REAL_THP1 = 0.375;
		CIB_LINE = 11
		ABBAS_COLUMN = 1
	elif MIX == 'B':
		REAL_JURKAT = 0.05; REAL_IM9 = 0.317; REAL_RAJI = 0.475; REAL_THP1 = 0.158;
		CIB_LINE = 12
		ABBAS_COLUMN = 2
	elif MIX == 'C':
		REAL_JURKAT = 0.01; REAL_IM9 = 0.495; REAL_RAJI = 0.165; REAL_THP1 = 0.33;
		CIB_LINE = 13
		ABBAS_COLUMN = 3
	elif MIX == 'D':
		REAL_JURKAT = 0.002; REAL_IM9 = 0.333; REAL_RAJI = 0.333; REAL_THP1 = 0.333;
		CIB_LINE = 14
		ABBAS_COLUMN = 4

	line = linecache.getline('../../../Master_files/output/CIBERSORT_referencenorm', CIB_LINE)
	CIBERSORT_JURKAT = float(line.split('\t')[1])
	CIBERSORT_IM9 = float(line.split('\t')[2])
	CIBERSORT_RAJI = float(line.split('\t')[3])
	CIBERSORT_THP1 = float(line.split('\t')[4])

	line = linecache.getline('../../../Master_files/abbas/Abbas_notumor', 3)
	ABBAS_JURKAT = float(line.split('\t')[ABBAS_COLUMN])
	line = linecache.getline('../../../Master_files/abbas/Abbas_notumor', 4)
	ABBAS_IM9 = float(line.split('\t')[ABBAS_COLUMN])
	line = linecache.getline('../../../Master_files/abbas/Abbas_notumor', 5)
	ABBAS_RAJI = float(line.split('\t')[ABBAS_COLUMN])
	line = linecache.getline('../../../Master_files/abbas/Abbas_notumor', 6)
	ABBAS_THP1 = float(line.split('\t')[ABBAS_COLUMN])

	if ABBAS_JURKAT < 0.0: ABBAS_JURKAT = 0.0
	if ABBAS_IM9 < 0.0: ABBAS_IM9 = 0.0
	if ABBAS_RAJI < 0.0: ABBAS_RAJI = 0.0
	if ABBAS_THP1 < 0.0: ABBAS_THP1 = 0.0

	temp_array = [ABBAS_JURKAT, ABBAS_IM9, ABBAS_RAJI, ABBAS_THP1]
	norm = [float(i)/sum(temp_array) for i in temp_array]
	ABBAS_JURKAT = norm[0]
	ABBAS_IM9 = norm[1]
	ABBAS_RAJI = norm[2]
	ABBAS_THP1 = norm[3]

	fig, ax = plt.subplots()

	rects1 = ax.bar(ind, (CIBERSORT_JURKAT, CIBERSORT_IM9, CIBERSORT_RAJI, CIBERSORT_THP1), width, color='r')
	rects2 = ax.bar(ind + width, (ABBAS_JURKAT, ABBAS_IM9, ABBAS_RAJI, ABBAS_THP1), width, color='y')
	rects3 = ax.bar(ind + (2*width), (REAL_JURKAT, REAL_IM9, REAL_RAJI, REAL_THP1), width, color='g')

	ax.set_ylabel('Coefficients')
	ax.set_ylim([0.0, 1.0])
	ax.set_title('Scores by cell lines for mixture ' + MIX)
	ax.set_xticks(ind + width)
	ax.set_xticklabels(('Jurkat', 'IM-9', 'Raji', 'THP-1'))

	ax.legend((rects1[0], rects2[0], rects3[0]), ('CIBERSORT', 'LLSR', 'Actual amount'))

	autolabel(rects1, ax)
	autolabel(rects2, ax)
	autolabel(rects3, ax)

	fig.savefig("mix" + MIX + "_referencenorm.png")
	plt.close(fig)


# mixture('A')
# mixture('B')
# mixture('C')
# mixture('D')


def cibersort():
	
	i = 0
	result = []
	while i <= 95:
		liste = []
		j = 0
		while j <= 95:
			correlation = 0.0
			# for k in range(11, 15):
			# 	line = linecache.getline('../../../Master_files/output/CIBERSORT_hugo_LM22_' + str(i) + '_' + str(j), k)
			# 	# TUMOR
			# 	# correlation += float(line.split('\t')[7])
			# 	# NOT TUMOR
			# 	correlation += float(line.split('\t')[6])
			for k in range(8, 12):
				line = linecache.getline('../../../Master_files/output/CIBERSORT_hugo_LM22_' + str(i) + '_' + str(j), k)
				correlation += float(line.split('\t')[24])

			liste.append(correlation / 4.0)
			j += 5
		result.append(liste)
		i += 5
	#result = reversed(result)
	result = [list(x) for x in zip(*result)]

	return result


def abbas():
	
	i = 0
	result = []
	while i <= 95:
		liste = []
		j = 0
		while j <= 95:
			correlationA = 0.0
			correlationB = 0.0
			correlationC = 0.0
			correlationD = 0.0
			# TUMOR
			for k in range(9, 14):
			# NOT TUMOR
			# for k in range(7, 11):
				line = linecache.getline('../../../Master_files/abbas/Abbas_tumor_present_' + str(i) + '_' + str(j), k)
				correlationA += float(line.split('\t')[1])
				correlationB += float(line.split('\t')[2])
				correlationC += float(line.split('\t')[3])
				correlationD += float(line.split('\t')[4])
			# TUMOR
			divide = 5.0
			# NOT TUMOR
			# divide = 4.0
			correlationA = correlationA / divide
			correlationB = correlationB / divide
			correlationC = correlationC / divide
			correlationD = correlationD / divide
			liste.append((correlationA + correlationB + correlationC + correlationD) / 4.0)
			j += 5
		result.append(liste)
		i += 5
	result = [list(x) for x in zip(*result)]

	return result


def llsr():

	f = open('../../../Master_files/abbas/correlation_signature_hugo', 'r')
	correlation = []
	for line in f:
		splitted_line = line.split('\t')[:-1]
		for i in range(len(splitted_line)):
			splitted_line[i] = float(splitted_line[i])
		correlation.append(splitted_line)
	
	result = [list(x) for x in zip(*correlation)]

	return result


def heatmap():

	result = cibersort()
	# result = abbas()
	# result = llsr()
	#print(result)


	reversed_result = []
	for i in reversed(result):
		reversed_result.append(i)

	from matplotlib import pyplot as pltt
	import matplotlib as mpl

	#hist, xedges, yedges = np.histogram2d(x,y)
	#X,Y = np.meshgrid(xedges,yedges)
	#pltt.imshow(hist)

	fig, ax = pltt.subplots()
	ax.set_title('CIBERSORT')
	# ax.set_title('Abbas')
	# ax.set_title('LLSR')
	ax.set_xlabel('Tumor content (%)')
	ax.set_ylabel('Added noise (%)')

	im = pltt.imshow(reversed_result, extent=[0, 100, 0, 100])
	#pltt.gca().invert_yaxis()
	pltt.grid(True)
	# pltt.colorbar()
	norm = mpl.colors.Normalize(vmin=0.0, vmax=1.0)
	im.set_norm(norm)
	pltt.colorbar(im)
	pltt.show()


heatmap()


def dot_line():

	CIBERSORT = []
	ABBAS = []
	RAJI = []

	for spike in range(0, 11, 1):

		A = 11; B = 12; C = 13; D = 14;
		CELL = 3

		line = linecache.getline('../../../Master_files/analyze_result/CIBERSORT_tumor_70_raji_' + str(spike), A)
		print(line)
		CIBERSORT.append(line.split('\t')[CELL])
	#print(CIBERSORT)
	for spike in range(0, 11, 1):

		A = 1; B = 2; C = 3; D = 4;
		Jurkat = 3; IM9 = 4; Raji = 5; THP1 = 6; Tumor = 7;

		Jurkat = linecache.getline('../../../Master_files/analyze_result/Abbas_tumor_70_raji_' + str(spike), Jurkat)
		IM9 = linecache.getline('../../../Master_files/analyze_result/Abbas_tumor_70_raji_' + str(spike), IM9)
		Raji = linecache.getline('../../../Master_files/analyze_result/Abbas_tumor_70_raji_' + str(spike), Raji)
		THP1 = linecache.getline('../../../Master_files/analyze_result/Abbas_tumor_70_raji_' + str(spike), THP1)
		Tumor = linecache.getline('../../../Master_files/analyze_result/Abbas_tumor_70_raji_' + str(spike), Tumor)

		temp_array = [float(Jurkat.split('\t')[A]), float(IM9.split('\t')[A]), float(Raji.split('\t')[A]), float(THP1.split('\t')[A]), float(Tumor.split('\t')[A])]
		#print(temp_array)
		norm = [float(i)/sum(temp_array) for i in temp_array]
		#print(norm)

		#ABBAS.append(Raji.split('\t')[A])
		ABBAS.append(norm[2])
	#print(ABBAS)
	for spike in range(0, 11, 1):

		# Raji
		A = 25; B = 47.5; C = 16.5; D = 33.3;

		MIX_content = A * (0.3 - (spike / 100))
		spike_content = spike * (100/30)
		#RAJI.append((MIX_content+spike_content) / 100)
		RAJI.append((MIX_content+spike)/100)
		print(0.3 - (spike / 100))
		print(MIX_content)
		print(spike_content)
		print(MIX_content+spike_content)
		print((MIX_content+spike)/100)
		print("\n")
	#print(RAJI)

	#raw = [0.07, 0.14, 0.07]
	#norm = [float(i)/sum(raw) for i in raw]
	#print(norm)

	plt.figure(1)
	plt.subplot(221)
	plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], CIBERSORT, marker='o', linestyle='-', color='r', label='CIBERSORT')
	plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ABBAS, marker='o', linestyle='-', color='g', label='LLSR')
	plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], RAJI, marker='o', linestyle='-', color='k', label='Raji')
	axes = plt.gca()
	axes.set_xlim([0, 10])
	axes.set_ylim([0.0, 0.3])
	plt.legend()
	plt.title('Mixture A with Raji spike-in')
	plt.xlabel('Spike in (%)')
	plt.ylabel('Cell line present in mixture')
	plt.show()


def dot_line_GSE26495():

	CIBERSORT_h = []; CIBERSORT_l = []
	ABBAS_h = []; ABBAS_l = []
	HIGH = [0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0.0];
	LOW = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1];

	for spike in range(0, 11, 1):

		A = 11; B = 12; C = 13; D = 14;
		H = 5; L = 6;

		line = linecache.getline('../../../Master_files/analyze_result/CIBERSORT_tumor_70_GSE26495_l' + str(10-spike) + '_h' + str(spike), A)
		CIBERSORT_h.append(line.split('\t')[H])
		CIBERSORT_l.append(line.split('\t')[L])

	for spike in range(0, 11, 1):

		A = 1; B = 2; C = 3; D = 4;
		Jurkat = 3; IM9 = 4; Raji = 5; THP1 = 6; H = 7; L = 8; Tumor = 9; 

		Jurkat = linecache.getline('../../../Master_files/analyze_result/Abbas_tumor_70_GSE26495_l' + str(10-spike) + '_h' + str(spike), Jurkat)
		IM9 = linecache.getline('../../../Master_files/analyze_result/Abbas_tumor_70_GSE26495_l' + str(10-spike) + '_h' + str(spike), IM9)
		Raji = linecache.getline('../../../Master_files/analyze_result/Abbas_tumor_70_GSE26495_l' + str(10-spike) + '_h' + str(spike), Raji)
		THP1 = linecache.getline('../../../Master_files/analyze_result/Abbas_tumor_70_GSE26495_l' + str(10-spike) + '_h' + str(spike), THP1)
		TH = linecache.getline('../../../Master_files/analyze_result/Abbas_tumor_70_GSE26495_l' + str(10-spike) + '_h' + str(spike), H)
		TL = linecache.getline('../../../Master_files/analyze_result/Abbas_tumor_70_GSE26495_l' + str(10-spike) + '_h' + str(spike), L)
		Tumor = linecache.getline('../../../Master_files/analyze_result/Abbas_tumor_70_GSE26495_l' + str(10-spike) + '_h' + str(spike), Tumor)
		
		Jurkat = float(Jurkat.split('\t')[A])
		IM9 = float(IM9.split('\t')[A])
		Raji = float(Raji.split('\t')[A])
		THP1 = float(THP1.split('\t')[A])
		TH = float(TH.split('\t')[A])
		TL = float(TL.split('\t')[A])
		Tumor = float(Tumor.split('\t')[A])

		if Jurkat < 0.0: Jurkat = 0.0
		if IM9 < 0.0: IM9 = 0.0
		if Raji < 0.0: Raji = 0.0
		if THP1 < 0.0: THP1 = 0.0
		if TH < 0.0: TH = 0.0
		if TL < 0.0: TL = 0.0
		if Tumor < 0.0: Tumor = 0.0

		temp_array = [Jurkat, IM9, Raji, THP1, TH, TL, Tumor]
		norm = [float(i)/sum(temp_array) for i in temp_array]

		ABBAS_h.append(norm[4])
		ABBAS_l.append(norm[5])

	reversed_HIGH = []
	reversed_LOW = []
	reversed_CIBERSORT_h = []
	reversed_CIBERSORT_l = []
	reversed_ABBAS_h = []
	reversed_ABBAS_l = []
	for i in reversed(HIGH):
		reversed_HIGH.append(i)
	for i in reversed(LOW):
		reversed_LOW.append(i)
	for i in reversed(CIBERSORT_h):
		reversed_CIBERSORT_h.append(i)
	for i in reversed(CIBERSORT_l):
		reversed_CIBERSORT_l.append(i)
	for i in reversed(ABBAS_h):
		reversed_ABBAS_h.append(i)
	for i in reversed(ABBAS_l):
		reversed_ABBAS_l.append(i)

	plt.figure(1)
	plt.subplot(221)
	plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], reversed_CIBERSORT_h, marker='o', linestyle='-', color='r', label='CIBERSORT high')
	plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], reversed_CIBERSORT_l, marker='o', linestyle='-', color='b', label='CIBERSORT low')
	plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], reversed_ABBAS_h, marker='o', linestyle='-', color='g', label='LLSR high')
	plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], reversed_ABBAS_l, marker='o', linestyle='-', color='c', label='LLSR low')
	plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], reversed_HIGH, marker='o', linestyle='-', color='k', label='PD-1 high')
	plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], reversed_LOW, marker='o', linestyle='-', color='y', label='PD-1 low')
	#plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3], linestyle='-', color='m', label="Total mixture")
	axes = plt.gca()
	axes.set_xlim([0, 10])
	axes.set_ylim([0.0, 0.3])
	plt.legend()
	plt.title('Mixture A with PD-1 high and PD-1 low spike-in (70% tumor)')
	plt.xlabel('Spike in (%)')
	plt.ylabel('Cell line present in mixture')
	plt.show()


def new_dot_line_GSE26495():

	CIBERSORT_h = []; CIBERSORT_l = []
	ABBAS_h = []; ABBAS_l = []
	HIGH = [0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0.0];
	LOW = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1];
	MIX = "D"

	for spike in range(0, 11, 1):

		A = 11; B = 12; C = 13; D = 14;
		H = 5; L = 6;

		line = linecache.getline('../../../Master_files/analyze_result/CIBERSORT_new_norm'+MIX+'_tumor_0_GSE26495_h' + str(10 - spike) + '_l' + str(spike), A)
		CIBERSORT_h.append(line.split('\t')[H])
		CIBERSORT_l.append(line.split('\t')[L])
	# print(CIBERSORT_h)
	#print(CIBERSORT_l)
	for spike in range(0, 11, 1):

		A = 1; B = 2; C = 3; D = 4;
		Jurkat = 3; IM9 = 4; Raji = 5; THP1 = 6; H = 7;# L = 8;# Tumor = 9; 

		Jurkat = linecache.getline('../../../Master_files/analyze_result/Abbas_new_norm'+MIX+'_tumor_0_GSE26495_h' + str(10 - spike) + '_l' + str(spike), Jurkat)
		IM9 = linecache.getline('../../../Master_files/analyze_result/Abbas_new_norm'+MIX+'_tumor_0_GSE26495_h' + str(10 - spike) + '_l' + str(spike), IM9)
		Raji = linecache.getline('../../../Master_files/analyze_result/Abbas_new_norm'+MIX+'_tumor_0_GSE26495_h' + str(10 - spike) + '_l' + str(spike), Raji)
		THP1 = linecache.getline('../../../Master_files/analyze_result/Abbas_new_norm'+MIX+'_tumor_0_GSE26495_h' + str(10 - spike) + '_l' + str(spike), THP1)
		TH = linecache.getline('../../../Master_files/analyze_result/Abbas_new_norm'+MIX+'_tumor_0_GSE26495_h' + str(10 - spike) + '_l' + str(spike), H)
		TL = linecache.getline('../../../Master_files/analyze_result/Abbas_new_norm'+MIX+'_tumor_0_GSE26495_h' + str(10 - spike) + '_l' + str(spike), L)
		#Tumor = linecache.getline('../../../Master_files/analyze_result/Abbas_tumor_70_GSE26495_h' + str(10 - spike) + '_l' + str(spike), Tumor)

		Jurkat = float(Jurkat.split('\t')[A])
		IM9 = float(IM9.split('\t')[A])
		Raji = float(Raji.split('\t')[A])
		THP1 = float(THP1.split('\t')[A])
		TH = float(TH.split('\t')[A])
		TL = float(TL.split('\t')[A])
		#Tumor = float(Tumor.split('\t')[A])

		if Jurkat < 0.0: Jurkat = 0.0
		if IM9 < 0.0: IM9 = 0.0
		if Raji < 0.0: Raji = 0.0
		if THP1 < 0.0: THP1 = 0.0
		if TH < 0.0: TH = 0.0
		if TL < 0.0: TL = 0.0
		#if Tumor < 0.0: Tumor = 0.0

		temp_array = [Jurkat, IM9, Raji, THP1, TH, TL]#, Tumor]
		#print(temp_array)
		norm = [float(i)/sum(temp_array) for i in temp_array]
		#print(norm)

		#ABBAS.append(Raji.split('\t')[A])
		ABBAS_h.append(norm[4])
		ABBAS_l.append(norm[5])
	# print(ABBAS_h)
	#print(ABBAS_l)

	plt.figure(1)
	plt.subplot(221)
	plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], CIBERSORT_h, marker='o', linestyle='-', color='r', label='CIBERSORT high')
	plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], CIBERSORT_l, marker='o', linestyle='-', color='b', label='CIBERSORT low')
	plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ABBAS_h, marker='o', linestyle='-', color='g', label='LLSR high')
	plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ABBAS_l, marker='o', linestyle='-', color='c', label='LLSR low')
	plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], HIGH, marker='o', linestyle='-', color='k', label='T high')
	plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], LOW, marker='o', linestyle='-', color='y', label='T low')
	#plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3], linestyle='-', color='m', label="Total mixture")
	axes = plt.gca()
	axes.set_xlim([0, 10])
	axes.set_ylim([0.0, 0.3])
	plt.legend()
	plt.title('Mixture '+MIX+' with T-high and T-low spike-in')
	plt.xlabel('Spike in (%)')
	plt.ylabel('Cell line present in mixture')
	plt.show()


# dot_line()
# dot_line_GSE26495()
# new_dot_line_GSE26495()