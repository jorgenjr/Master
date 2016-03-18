
import matplotlib.pyplot as plt, numpy as np, linecache

# da = open('../../../Master_files/abbas/deconvoluted_mixA', 'r')
# db = open('../../../Master_files/abbas/deconvoluted_mixB', 'r')
# dc = open('../../../Master_files/abbas/deconvoluted_mixC', 'r')
# dd = open('../../../Master_files/abbas/deconvoluted_mixD', 'r')
# dai = open('../../../Master_files/abbas/deconvoluted_mixA_intercept', 'r')
# dbi = open('../../../Master_files/abbas/deconvoluted_mixB_intercept', 'r')
# dci = open('../../../Master_files/abbas/deconvoluted_mixC_intercept', 'r')
# ddi = open('../../../Master_files/abbas/deconvoluted_mixD_intercept', 'r')
# sa = open('../../../Master_files/output/combined_mixA.txt', 'r')
# sb = open('../../../Master_files/output/combined_mixB.txt', 'r')
# sc = open('../../../Master_files/output/combined_mixC.txt', 'r')
# sd = open('../../../Master_files/output/combined_mixD.txt', 'r')

# N = 4

# ind = np.arange(N)  # the x locations for the groups
# width = 0.25       # the width of the bars
# plt.rcParams.update({'font.size': 9})

# def autolabel(rects, ax):
#     # attach some text labels
#     for rect in rects:
#         height = rect.get_height()
#         ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
#                 '%.4f' % float(height),
#                 ha='center', va='bottom')


# def plot_result():

# 	first_line = linecache.getline('../../../Master_files/abbas/deconvoluted_test', 1)
# 	splitted_line = first_line.split("\t")

# 	for j in range(len(splitted_line)):

# 		ABBAS = open('../../../Master_files/abbas/deconvoluted_test', 'r')
# 		CIBERSORT = open('../../../Master_files/output/CIBERSORT_result_tumor_0', 'r')

# 		mix_abbas = []
# 		mix_cibersort = []

# 		for i, line in enumerate(ABBAS):
# 			if i > 0:
# 				mix_abbas.append(float(line.split('\t')[j+1]))

# 		skip = True

# 		for i, line in enumerate(CIBERSORT):
			
# 			splitted_line = line.split("\t")
			
# 			if splitted_line[0] == "0":
# 				skip = False

# 			if skip == False:
# 				mix_cibersort.append(float(splitted_line[j+1]))

# 		fig, ax = plt.subplots()

# 		rects1 = ax.bar(ind, (mix_abbas[0], mix_abbas[1], mix_abbas[2], mix_abbas[3]), width, color='r')
# 		rects2 = ax.bar(ind + (width), (mix_cibersort[0], mix_cibersort[1], mix_cibersort[2], mix_cibersort[3]), width, color='g')

# 		ax.set_ylabel('Scores')
# 		ax.set_ylim([0.0, 1.0])
# 		ax.set_title('Scores by cell lines')
# 		ax.set_xticks(ind + width)
# 		ax.set_xticklabels(('Jurkat', 'IM-9', 'Raji', 'THP-1'))

# 		ax.legend((rects1[0], rects2[0]), ('Abbas', 'CIBERSORT'))

# 		autolabel(rects1, ax)
# 		autolabel(rects2, ax)

# 		fig.savefig("mix" + str(j) + ".png")
# 		plt.close(fig)


# plot_result()

#############
# MIXTURE A #
#############

# mixA_d = []
# mixA_di = []
# mixA_s = []

# for i, line in enumerate(da):
# 	if i > 0:
# 		mixA_d.append(float(line.split('\t')[1]))

# for i, line in enumerate(dai):
# 	if i > 1:
# 		mixA_di.append(float(line.split('\t')[1]))

# for i, line in enumerate(sa):
# 	if i > 0:
# 		splitted_line = line.split('\t')
# 		mixA_s.append(float(splitted_line[1]))
# 		mixA_s.append(float(splitted_line[2]))
# 		mixA_s.append(float(splitted_line[3]))
# 		mixA_s.append(float(splitted_line[4]))

# rects1 = ax.bar(ind, (mixA_d[0], mixA_d[1], mixA_d[2], mixA_d[3]), width, color='r')
# rects2 = ax.bar(ind + width, (mixA_di[0], mixA_di[1], mixA_di[2], mixA_di[3]), width, color='y')
# rects3 = ax.bar(ind + (2*width), (mixA_s[0], mixA_s[1], mixA_s[2], mixA_s[3]), width, color='g')

# ax.set_ylabel('Scores')
# ax.set_ylim([0.0, 1.0])
# ax.set_title('Scores by cell lines')
# ax.set_xticks(ind + width)
# ax.set_xticklabels(('Jurkat', 'IM-9', 'Raji', 'THP-1'))

# ax.legend((rects1[0], rects2[0], rects3[0]), ('Abbas', 'Abbas (intercept)', 'CIBERSORT'))

# autolabel(rects1)
# autolabel(rects2)
# autolabel(rects3)

# fig.savefig("mixa.png")
# plt.close(fig)
#plt.show()

#############
# MIXTURE B #
#############

# fig, ax = plt.subplots()

# mixB_d = []
# mixB_di = []
# mixB_s = []

# for i, line in enumerate(db):
# 	if i > 0:
# 		mixB_d.append(float(line.split('\t')[1]))

# for i, line in enumerate(dbi):
# 	if i > 1:
# 		mixB_di.append(float(line.split('\t')[1]))

# for i, line in enumerate(sb):
# 	if i > 0:
# 		splitted_line = line.split('\t')
# 		mixB_s.append(float(splitted_line[1]))
# 		mixB_s.append(float(splitted_line[2]))
# 		mixB_s.append(float(splitted_line[3]))
# 		mixB_s.append(float(splitted_line[4]))

# rects4 = ax.bar(ind, (mixB_d[0], mixB_d[1], mixB_d[2], mixB_d[3]), width, color='r')
# rects5 = ax.bar(ind + width, (mixB_di[0], mixB_di[1], mixB_di[2], mixB_di[3]), width, color='y')
# rects6 = ax.bar(ind + (2*width), (mixB_s[0], mixB_s[1], mixB_s[2], mixB_s[3]), width, color='g')

# ax.set_ylabel('Scores')
# ax.set_ylim([0.0, 1.0])
# ax.set_title('Scores by cell lines')
# ax.set_xticks(ind + width)
# ax.set_xticklabels(('Jurkat', 'IM-9', 'Raji', 'THP-1'))

# ax.legend((rects4[0], rects5[0], rects6[0]), ('Abbas', 'Abbas (intercept)', 'CIBERSORT'))

# autolabel(rects4)
# autolabel(rects5)
# autolabel(rects6)

# fig.savefig("mixb.png")
# plt.close(fig)
#plt.show()

#############
# MIXTURE C #
#############

# fig, ax = plt.subplots()

# mixC_d = []
# mixC_di = []
# mixC_s = []

# for i, line in enumerate(dc):
# 	if i > 0:
# 		mixC_d.append(float(line.split('\t')[1]))

# for i, line in enumerate(dci):
# 	if i > 1:
# 		mixC_di.append(float(line.split('\t')[1]))

# for i, line in enumerate(sc):
# 	if i > 0:
# 		splitted_line = line.split('\t')
# 		mixC_s.append(float(splitted_line[1]))
# 		mixC_s.append(float(splitted_line[2]))
# 		mixC_s.append(float(splitted_line[3]))
# 		mixC_s.append(float(splitted_line[4]))

# rects7 = ax.bar(ind, (mixC_d[0], mixC_d[1], mixC_d[2], mixC_d[3]), width, color='r')
# rects8 = ax.bar(ind + width, (mixC_di[0], mixC_di[1], mixC_di[2], mixC_di[3]), width, color='y')
# rects9 = ax.bar(ind + (2*width), (mixC_s[0], mixC_s[1], mixC_s[2], mixC_s[3]), width, color='g')

# ax.set_ylabel('Scores')
# ax.set_ylim([0.0, 1.0])
# ax.set_title('Scores by cell lines')
# ax.set_xticks(ind + width)
# ax.set_xticklabels(('Jurkat', 'IM-9', 'Raji', 'THP-1'))

# ax.legend((rects7[0], rects8[0], rects9[0]), ('Abbas', 'Abbas (intercept)', 'CIBERSORT'))

# autolabel(rects7)
# autolabel(rects8)
# autolabel(rects9)

# fig.savefig("mixc.png")
# plt.close(fig)
#plt.show()

#############
# MIXTURE D #
#############

# fig, ax = plt.subplots()

# mixD_d = []
# mixD_di = []
# mixD_s = []

# for i, line in enumerate(dd):
# 	if i > 0:
# 		mixD_d.append(float(line.split('\t')[1]))

# for i, line in enumerate(ddi):
# 	if i > 1:
# 		mixD_di.append(float(line.split('\t')[1]))

# for i, line in enumerate(sd):
# 	if i > 0:
# 		splitted_line = line.split('\t')
# 		mixD_s.append(float(splitted_line[1]))
# 		mixD_s.append(float(splitted_line[2]))
# 		mixD_s.append(float(splitted_line[3]))
# 		mixD_s.append(float(splitted_line[4]))

# rects10 = ax.bar(ind, (mixD_d[0], mixD_d[1], mixD_d[2], mixD_d[3]), width, color='r')
# rects11 = ax.bar(ind + width, (mixD_di[0], mixD_di[1], mixD_di[2], mixD_di[3]), width, color='y')
# rects12 = ax.bar(ind + (2*width), (mixD_s[0], mixD_s[1], mixD_s[2], mixD_s[3]), width, color='g')

# ax.set_ylabel('Scores')
# ax.set_ylim([0.0, 1.0])
# ax.set_title('Scores by cell lines')
# ax.set_xticks(ind + width)
# ax.set_xticklabels(('Jurkat', 'IM-9', 'Raji', 'THP-1'))

# ax.legend((rects10[0], rects11[0], rects12[0]), ('Abbas', 'Abbas (intercept)', 'CIBERSORT'))

# autolabel(rects10)
# autolabel(rects11)
# autolabel(rects12)

# fig.savefig("mixd.png")
# plt.close(fig)
#plt.show()



def cibersort():
	
	i = 0
	result = []

	while i <= 100:

		liste = []
		j = 0

		while j <= 90:

			correlation = 0.0

			for k in range(11, 15):

				line = linecache.getline('../../../Master_files/output/CIBERSORT_result_tumor_' + str(i) + '_' + str(j), k)
				correlation += float(line.split('\t')[7])

			liste.append(correlation / 4.0)
			j += 30

		result.append(liste)
		i += 5

	result = reversed(result)
	result = [list(x) for x in zip(*result)]

	return result


def abbas():
	
	i = 0
	result = []

	while i <= 100:

		liste = []
		j = 0

		while j <= 90:

			correlationA = 0.0
			correlationB = 0.0
			correlationC = 0.0
			correlationD = 0.0

			for k in range(8, 13):

				line = linecache.getline('../../../Master_files/abbas/Abbas_result_tumor_' + str(i) + '_' + str(j), k)
				correlationA += float(line.split('\t')[1])
				correlationB += float(line.split('\t')[2])
				correlationC += float(line.split('\t')[3])
				correlationD += float(line.split('\t')[4])

			correlationA = correlationA / 5.0
			correlationB = correlationB / 5.0
			correlationC = correlationC / 5.0
			correlationD = correlationD / 5.0
			liste.append((correlationA + correlationB + correlationC + correlationD) / 4.0)
			j += 30

		result.append(liste)
		i += 5

	result = [list(x) for x in zip(*result)]

	return result

result = cibersort()
# result = abbas()

reversed_result = []
for i in reversed(result):
	reversed_result.append(i)

from matplotlib import pyplot as pltt

#hist, xedges, yedges = np.histogram2d(x,y)
#X,Y = np.meshgrid(xedges,yedges)
#pltt.imshow(hist)
pltt.imshow(reversed_result, extent=[0, 100, 0, 100])
#pltt.gca().invert_yaxis()
pltt.grid(True)
pltt.colorbar(ticks=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
pltt.show()