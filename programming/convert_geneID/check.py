


f_r = open('../../../Master_files/convert/reference_PD-1_HUGO', 'r')
f_m = open('../../../Master_files/convert/mixtures_hugo_tumor_0_0', 'r')

ref = []
mix = []

for line in f_r:
	splitted_line = line.split('\t')

	if (len(splitted_line) != 13):
		print(splitted_line)

	ref.append(splitted_line)

for line in f_m:
	splitted_line = line.split('\t')

	if len(splitted_line) != 5:
		print(splitted_line)

	mix.append(splitted_line)

header = True

for i in range(len(ref)):

	if header == True:
		header = False
		continue
		
	if ref[i][0] != mix[i][0]:
		print(ref[i][0], mix[i][0])