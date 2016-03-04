
import matplotlib.pyplot as plt, numpy as np

da = open('../../../Master_files/abbas/deconvoluted_mixA', 'r')
db = open('../../../Master_files/abbas/deconvoluted_mixB', 'r')
dc = open('../../../Master_files/abbas/deconvoluted_mixC', 'r')
dd = open('../../../Master_files/abbas/deconvoluted_mixD', 'r')
dai = open('../../../Master_files/abbas/deconvoluted_mixA_intercept', 'r')
dbi = open('../../../Master_files/abbas/deconvoluted_mixB_intercept', 'r')
dci = open('../../../Master_files/abbas/deconvoluted_mixC_intercept', 'r')
ddi = open('../../../Master_files/abbas/deconvoluted_mixD_intercept', 'r')
sa = open('../../../Master_files/output/combined_mixA.txt', 'r')
sb = open('../../../Master_files/output/combined_mixB.txt', 'r')
sc = open('../../../Master_files/output/combined_mixC.txt', 'r')
sd = open('../../../Master_files/output/combined_mixD.txt', 'r')


N = 4

ind = np.arange(N)  # the x locations for the groups
width = 0.25       # the width of the bars

fig, ax = plt.subplots()

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.4f' % float(height),
                ha='center', va='bottom')

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

# plt.show()

#############
# MIXTURE B #
#############

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

# plt.show()

#############
# MIXTURE C #
#############

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

# plt.show()

#############
# MIXTURE D #
#############

mixD_d = []
mixD_di = []
mixD_s = []

for i, line in enumerate(dd):
	if i > 0:
		mixD_d.append(float(line.split('\t')[1]))

for i, line in enumerate(ddi):
	if i > 1:
		mixD_di.append(float(line.split('\t')[1]))

for i, line in enumerate(sd):
	if i > 0:
		splitted_line = line.split('\t')
		mixD_s.append(float(splitted_line[1]))
		mixD_s.append(float(splitted_line[2]))
		mixD_s.append(float(splitted_line[3]))
		mixD_s.append(float(splitted_line[4]))

rects10 = ax.bar(ind, (mixD_d[0], mixD_d[1], mixD_d[2], mixD_d[3]), width, color='r')
rects11 = ax.bar(ind + width, (mixD_di[0], mixD_di[1], mixD_di[2], mixD_di[3]), width, color='y')
rects12 = ax.bar(ind + (2*width), (mixD_s[0], mixD_s[1], mixD_s[2], mixD_s[3]), width, color='g')

ax.set_ylabel('Scores')
ax.set_ylim([-1.0, 1.0])
ax.set_title('Scores by cell lines')
ax.set_xticks(ind + width)
ax.set_xticklabels(('Jurkat', 'IM-9', 'Raji', 'THP-1'))

ax.legend((rects10[0], rects11[0], rects12[0]), ('Abbas', 'Abbas (intercept)', 'CIBERSORT'))

autolabel(rects10)
autolabel(rects11)
autolabel(rects12)

plt.show()