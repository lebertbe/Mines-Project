from pypower.api import rundcopf
from caseproject import caseproject
from pypower.loadcase import loadcase
from fmap import fmap
from freadexcel import freadexcel
from fstoreresult import fstoreresult
from fwriteinexcel import fwriteinexcel
import os
import numpy as np


# Names of the data folder and output files
foldername = 'Data_été'
filename = 'results_name.txt'
xlsname = 'results_name.xls'
mapname = 'map_name.png'

# Extracting data from xls files and creating 4 ppc matrices
os.chdir(foldername)
ppc = loadcase(caseproject())
bus, gen, branch, gencost = freadexcel()
ppc["bus"] = bus
ppc["branch"] = branch
ppc["gen"] = gen
ppc["gencost"] = gencost

# Running the simulation
r = rundcopf(ppc, fname=filename)

# Storing results
results_gen, results_load_lambda, results_branch = fstoreresult(r)

# Writing results in xls file
# fwriteinexcel(xlsname, results_gen, results_load_lambda, results_branch)

# Creating a map with the results
results_branch_map = []
for i in range(len(branch)):
    inter = [results_branch[i, 0], results_branch[i, 1], results_branch[i, 2], branch[i, 5]]
    results_branch_map.append(inter)
results_branch_map = np.asarray(results_branch_map, dtype=np.float64)
fmap(results_branch_map, results_gen, results_load_lambda, mapname)
