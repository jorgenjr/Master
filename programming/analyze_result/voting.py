
import config


def vote_separate():

	f_cibersort = open(config.CIBERSORT_OUTPUT + '0_0', 'r')
	f_llsr = open(config.ABBAS_OUTPUT + '0_0', 'r')

	for line in f_cibersort:
		print(line)

vote_separate()