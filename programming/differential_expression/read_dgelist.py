
import time

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

f = open('dgelist', 'r')
skip = True

for line in f:
	splitted = line.split(' ')
	splitted[-1] = splitted[-1][0:-1]
	new_line = []
	for index in splitted:
		if index != '':
			new_line.append(index)

	if len(new_line) != 5:
		if skip == True:
			skip == False
			continue
		
		print (new_line)

	for num in new_line:
		if RepresentsInt(num) == False:
			print (new_line)

	# print (new_line)