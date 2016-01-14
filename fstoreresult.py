import numpy as np


def fstoreresult(r):

    results_gen = []
    results_load_lambda = []
    results_branch = []

    for i in range(35):
        inter = [(r['gen'][i, 0]), (r['gen'][i, 1])]
        results_gen.append(inter)
    results_gen = np.asarray(results_gen, dtype=np.float64)

    for j in range(40):
        inter1 = [(r['bus'][j, 0]), (r['bus'][j, 2]), (r['bus'][j, 13])]
        results_load_lambda.append(inter1)
    results_load_lambda = np.asarray(results_load_lambda, dtype=np.float64)

    for k in range(len(r['branch'])):
        inter2 = [(r['branch'][k, 0]), (r['branch'][k, 1]), (r['branch'][k, 13])]
        results_branch.append(inter2)
    results_branch = np.asarray(results_branch, dtype=np.float64)

    return results_gen, results_load_lambda, results_branch

