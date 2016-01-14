from pypower.api import rundcopf
from pypower.caseproject import caseproject
from pypower.loadcase import loadcase
from freadexcel import freadexcel
from fstoreresult import fstoreresult
from fupdate import fupdate
from fwriteinexcel import fwriteinexcel

ppc = loadcase(caseproject())

# On va chercher les 4 matrices statiques et les variables demand
bus, gen, branch, gencost = freadexcel()
ppc["branch"] = branch
ppc["gen"] = gen
ppc["gencost"] = gencost

# for loop (0 to 8759)
for i in range(8760):
    # On update la matrice bus avec les variables demand
    bus = fupdate()
    ppc["bus"] = bus
    # On lance la simulation
    r = rundcopf(ppc)
    # On stocke les résultats à chaque itération
    results_1, results_2, results_3 = fstoreresult(r)

# On écrit les résultats des 8760 simulations dans un fichier Excel
fwriteinexcel(results_1, results_2, results_3)
