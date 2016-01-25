
import readline, numpy as np, rpy2.robjects as robjects, csv, collections, rpy2.robjects.numpy2ri, time, sys

from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage

rpy2.robjects.numpy2ri.activate()

def read_count_file():

	f = open("../../../Master_files/simulation/testfile_1_1", "r")
	header = []
	reads = 0
	counts = collections.defaultdict(dict)
	total_counts = [0.0, 0.0, 0.0, 0.0]

	for lines in f:
		
		line = lines.split("\t")

		if reads == 0:
			header = line[1:]
		else:
			gene_id = line[0]
			gene_counts = [float(x) for x in line[1:]]

			for ci, condition in enumerate(header):
				counts[condition][gene_id] = gene_counts[ci]
				total_counts[ci] += gene_counts[ci]

		reads += 1

	return counts, total_counts

def get_conditions_and_genes(work_counts, total_counts):

	conditions = list(work_counts.keys())
	conditions.sort()
	all_genes = []
	
	for c in conditions:
		all_genes.extend(work_counts[c].keys())
		all_genes = list(set(all_genes))
		all_genes.sort()

	return conditions, all_genes

def edger_matrices(work_counts, total_counts):
	
	conditions, all_genes = get_conditions_and_genes(work_counts, total_counts)
	assert len(total_counts) == 4
	groups = [1, 2, 3, 4]
	data = []
	final_genes = []

	for g in all_genes:
		cur_row = [int(work_counts[c][g]) for c in conditions]
		
		if sum(cur_row) > 0:
			data.append(cur_row)
			final_genes.append(g)
	print(final_genes)			
	return (np.array(data), np.array(groups), np.array(total_counts), conditions, final_genes)

def run_edger(data, groups, sizes, genes):
    """Call edgeR in R and organize the resulting differential expressed genes.
    """
    robjects.r('''
        library(edgeR)
    ''')

    # find the version we are running -- check for edgeR exactTest function
    try:
        robjects.r["exactTest"]
        is_13_plus = True
    except LookupError:
        is_13_plus = False

    params = {'group' : groups, 'lib.size' : sizes}
    dgelist = robjects.r.DGEList(data, **params)
    
    # 1.3+ version has a different method of calling and retrieving p values
    if is_13_plus:
        # perform Poisson adjustment and assignment as recommended in the manual
        robjects.globalenv['dP'] = dgelist
        print(dgelist)
        # robjects.r('''
        #     msP <- de4DGE(dP, doPoisson = TRUE)
        #     dP$pseudo.alt <- msP$pseudo
        #     dP$common.dispersion <- 1e-06
        #     dP$conc <- msP$conc
        #     dP$common.lib.size <- msP$M
        # ''')
        robjects.r('''
            msP <- estimateCommonDisp(dP) #, rowsum.filter=0
            dP$pseudo.alt <- msP$pseudo
            dP$common.dispersion <- 1e-06
            dP$conc <- msP$conc
            dP$common.lib.size <- msP$M
            dP$counts[is.na(dP$counts)] <- 0
            # options(max.print=100000)
        ''')
        
        dgelist = robjects.globalenv['dP']

        de = robjects.r.exactTest(dgelist)
        tags = robjects.r.topTags(de, n=len(genes))
        tag_table = tags[0]
        indexes = [int(t) - 1 for t in tag_table.rownames()]
        # can retrieve either raw or adjusted p-values
        #pvals = list(tags.r['p.value'][0])
        pvals = list(tag_table.r['adj.p.val'][0])
    # older 1.2 version of edgeR
    else:
        ms = robjects.r.deDGE(dgelist, doPoisson=True)
        tags = robjects.r.topTags(ms, pair=groups, n=len(genes))
        indexes = [int(t) - 1 for t in tags.rownames()]
        # can retrieve either raw or adjusted p-values
        #pvals = list(tags.r['P.Value'][0])
        pvals = list(tags.r['adj.P.Val'][0])
    assert len(indexes) == len(pvals)
    pvals_w_index = zip(indexes, pvals)
    pvals_w_index.sort()
    assert len(pvals_w_index) == len(indexes)
    return [p for i,p in pvals_w_index]

def remove_NAs(dgelist):

	string = str(dgelist[0])
	string_list = string.split('\n')
	new_dgelist = []
	i = 0

	for i in range(len(string_list)):
		
		splitted = string_list[i].split(' ')
		new_line = []

		for index in splitted:
			if index != '':
				new_line.append(index)

		j = 0

		for j in range(len(new_line)):
			# print (new_line)
			if len(new_line) == 4:
				continue

			try: 
				int(new_line[j])
			except ValueError:
				print (new_line)
				new_line[j] = '0'

		new_dgelist.append(new_line)

	return new_dgelist

counts, total_counts = read_count_file()
data, groups, sizes, conditions, genes = edger_matrices(counts, total_counts)
probs = run_edger(data, groups, sizes, genes)