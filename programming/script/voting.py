
import config
import linecache
import numpy
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ITERATION", help="Iteration", nargs='*')

args = parser.parse_args()


def rules_coef(ACTUAL, ESTIMATED):
	
	if (ESTIMATED > ACTUAL - config.THRESHOLD_COEF and ESTIMATED < ACTUAL + config.THRESHOLD_COEF):
		return 1
	return 0


def rules_pearson(ESTIMATED):

	if (ESTIMATED >= config.THRESHOLD_PEARSON):
		return 1
	return 0


def rules_pvalue(ESTIMATED):

	if (ESTIMATED <= config.THRESHOLD_PVALUE):
		return 1
	return 0


def write_to_file(RESULTS):

	f = open(config.PATH + 'Master_files/output/voting_' + args.ITERATION[0] + '_' + args.ITERATION[1], 'w')
	f.write(RESULTS)
	f.close()


def vote_separate(CIBERSORT_result, LLSR_result):

	string_result = "\n"
	string_result += "*** VOTING PARAMETERS ***\n"
	string_result += "Option: " + config.VOTE_OPTIONS[config.VOTE] + "\n"
	string_result += "Variable: " + config.VOTE_VARIABLE[config.VOTE_V] + "\n"
	
	if config.VOTE_VARIABLE[config.VOTE_V] == "coef":
		string_result += "Threshold: " + str(config.THRESHOLD_COEF) + "\n"
	elif config.VOTE_VARIABLE[config.VOTE_V] == "p-value":
		string_result += "Threshold: " + str(config.THRESHOLD_PVALUE) + "\n"
	elif config.VOTE_VARIABLE[config.VOTE_V] == "pearson":
		string_result += "Threshold: " + str(config.THRESHOLD_PEARSON) + "\n"
	
	string_result += "\n"
	string_result += "*** CIBERSORT ***\n"

	for i in range(len(CIBERSORT_result)):

		string_result += "Mix " + str(i+1) + ": [ "

		for j in range(len(CIBERSORT_result[i])):

			if (j+1) == len(CIBERSORT_result[i]):
				string_result += str(CIBERSORT_result[i][j])
			else:
				string_result += str(CIBERSORT_result[i][j]) + ", " 

		string_result += " ]\n"
	
	string_result += "\n"
	string_result += "*** LLSR ***\n"
	
	for i in range(len(LLSR_result)):

		string_result += "Mix " + str(i+1) + ": [ "

		for j in range(len(LLSR_result[i])):

			if (j+1) == len(LLSR_result[i]):
				string_result += str(LLSR_result[i][j])
			else:
				string_result += str(LLSR_result[i][j]) + ", "

		string_result += " ]\n"

	result = []

	for i in range(len(CIBERSORT_result)):

		mix_result = []

		for j in range(len(CIBERSORT_result[i])):

			if (CIBERSORT_result[i][j] == 1):
				mix_result.append(1)
			elif (LLSR_result[i][j] == 1):
				mix_result.append(1)
			else:
				mix_result.append(0)

		result.append(mix_result)

	string_result += "\n"
	string_result += "*** UNION ***\n"

	for i in range(len(result)):

		string_result += "Mix " + str(i+1) + ": [ "

		for j in range(len(result[i])):

			if (j+1) == len(result[i]):
				string_result += str(result[i][j])
			else:
				string_result += str(result[i][j]) + ", "

		string_result += " ]\n"

	write_to_file(string_result)


def vote_combined(CIBERSORT_result, LLSR_result):

	string_result = "\n"
	string_result += "*** VOTING PARAMETERS ***\n"
	string_result += "Option: " + config.VOTE_OPTIONS[config.VOTE] + "\n"
	string_result += "Variable: " + config.VOTE_VARIABLE[config.VOTE_V] + "\n"
	
	if config.VOTE_VARIABLE[config.VOTE_V] == "coef":
		string_result += "Threshold: " + str(config.THRESHOLD_COEF) + "\n"
	elif config.VOTE_VARIABLE[config.VOTE_V] == "p-value":
		string_result += "Threshold: " + str(config.THRESHOLD_PVALUE) + "\n"
	elif config.VOTE_VARIABLE[config.VOTE_V] == "pearson":
		string_result += "Threshold: " + str(config.THRESHOLD_PEARSON) + "\n"
	
	string_result += "\n"
	string_result += "*** CIBERSORT ***\n"

	for i in range(len(CIBERSORT_result)):

		string_result += "Mix " + str(i+1) + ": [ "

		for j in range(len(CIBERSORT_result[i])):

			if (j+1) == len(CIBERSORT_result[i]):
				string_result += str(CIBERSORT_result[i][j])
			else:
				string_result += str(CIBERSORT_result[i][j]) + ", "

		string_result += " ]\n"
	
	string_result += "\n"
	string_result += "*** LLSR ***\n"
	
	for i in range(len(LLSR_result)):

		string_result += "Mix " + str(i+1) + ": [ "

		for j in range(len(LLSR_result[i])):

			if (j+1) == len(LLSR_result[i]):
				string_result += str(LLSR_result[i][j])
			else:
				string_result += str(LLSR_result[i][j]) + ", "

		string_result += " ]\n"

	result = []

	for i in range(len(CIBERSORT_result)):

		mix_result = []

		for j in range(len(CIBERSORT_result[i])):

			if (CIBERSORT_result[i][j] == 1 and LLSR_result[i][j] == 1):
				mix_result.append(1)
			else:
				mix_result.append(0)

		result.append(mix_result)

	string_result += "\n"
	string_result += "*** UNANIMOUS ***\n"

	for i in range(len(result)):

		string_result += "Mix " + str(i+1) + ": [ "

		for j in range(len(result[i])):

			if (j+1) == len(result[i]):
				string_result += str(result[i][j])
			else:
				string_result += str(result[i][j]) + ", "

		string_result += " ]\n"

	write_to_file(string_result)


def prepare_vote(CIBERSORT_mixes, LLSR_mixes):

	CIBERSORT_result = []
	LLSR_result = []

	for i in range(len(config.ACTUAL_AMOUNT)):

		c_mix = []
		l_mix = []

		for j in range(len(config.ACTUAL_AMOUNT[i])):

			c_mix.append(rules_coef(config.ACTUAL_AMOUNT[i][j], CIBERSORT_mixes[i][j]))
			l_mix.append(rules_coef(config.ACTUAL_AMOUNT[i][j], LLSR_mixes[i][j]))

		CIBERSORT_result.append(c_mix)
		LLSR_result.append(l_mix)

	if (config.VOTE_OPTIONS[config.VOTE] == 'union'):
		vote_separate(CIBERSORT_result, LLSR_result)
	elif (config.VOTE_OPTIONS[config.VOTE] == 'unanimous'):
		vote_combined(CIBERSORT_result, LLSR_result)
	else:
		print("[ ERROR ] - Wrong variable value for either 'VOTE_OPTIONS' or 'VOTE' in config.py\n")


def get_coef():

	CIBERSORT_mixes = []
	LLSR_mixes = []

	for i in range(config.CIBERSORT_FIRST_MIX, config.CIBERSORT_LAST_MIX + 1):
		
		line = linecache.getline(config.CIBERSORT_OUTPUT + args.ITERATION[0] + '_' + args.ITERATION[1], i)
		splitted_line = line.split('\t')
		line_to_append = []

		for j in range(config.CIBERSORT_FIRST_CELL, config.CIBERSORT_LAST_CELL + 1):
			line_to_append.append(float(splitted_line[j]))

		CIBERSORT_mixes.append(line_to_append)

	for i in range(config.ABBAS_FIRST_CELL, config.ABBAS_LAST_CELL + 1):

		line = linecache.getline(config.ABBAS_OUTPUT + args.ITERATION[0] + '_' + args.ITERATION[1], i)
		splitted_line = line.split('\t')
		line_to_append = []

		for j in range(config.ABBAS_FIRST_MIX, config.ABBAS_LAST_MIX + 1):
			line_to_append.append(float(splitted_line[j]))

		LLSR_mixes.append(line_to_append)

	LLSR_temp = numpy.asarray(LLSR_mixes).T.tolist()
	temp_array = []

	for j in range(len(LLSR_temp)):
		
		for k in range(len(LLSR_temp)):
			if LLSR_temp[j][k] < 0.0:
				LLSR_temp[j][k] = 0.0

		try:
			LLSR_mixes[j] = [float(i)/sum(LLSR_temp[j]) for i in LLSR_temp[j]]
		except ZeroDivisionError as e:
			print(e)

	prepare_vote(CIBERSORT_mixes, LLSR_mixes)


def get_pearson():

	CIBERSORT_mixes = []

	for i in range(config.CIBERSORT_FIRST_MIX, config.CIBERSORT_LAST_MIX + 1):
		
		line = linecache.getline(config.PATH + config.CIBERSORT_OUTPUT, i)
		splitted_line = line.split('\t')

		CIBERSORT_mixes.append(rules_pearson(float(splitted_line[config.CIBERSORT_PEARSON])))

	print("")
	print("*** PEARSON CIBERSORT ***")
	print(CIBERSORT_mixes)


def get_pvalue():

	CIBERSORT_mixes = []

	for i in range(config.CIBERSORT_FIRST_MIX, config.CIBERSORT_LAST_MIX + 1):
		
		line = linecache.getline(config.PATH + config.CIBERSORT_OUTPUT, i)
		splitted_line = line.split('\t')

		CIBERSORT_mixes.append(rules_pvalue(float(splitted_line[config.CIBERSORT_PVALUE])))

	print("")
	print("*** P-VALUE CIBERSORT ***")
	print(CIBERSORT_mixes)


if (config.VOTE_VARIABLE[config.VOTE_V] == 'coef'):
	get_coef()
elif (config.VOTE_VARIABLE[config.VOTE_V] == 'pearson'):
	get_pearson()
elif (config.VOTE_VARIABLE[config.VOTE_V] == 'p-value'):
	get_pvalue()
else:
	print("[ ERROR ] - Wrong variable value for either 'VOTE_VARIABLE' or 'VOTE_V' in config.py\n")