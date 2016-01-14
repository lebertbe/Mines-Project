from xlwt import Workbook


def fwriteinexcel(xlsname, results_gen, results_load_lambda, results_branch):
    book = Workbook()
    Sheet1 = book.add_sheet('Sheet1')

    Sheet1.write(0, 0, 'Bus')
    Sheet1.write(0, 1, 'Generation (MW)')
    Sheet1.write(0, 2, 'Load (MW)')
    Sheet1.write(0, 3, 'Lambda (€/MWh)')
    Sheet1.write(0, 5, 'From Bus')
    Sheet1.write(0, 6, 'To Bus')
    Sheet1.write(0, 7, 'P (MW)')

    for i in range(len(results_gen)):
        Sheet1.write(i+1, 0, results_gen[i, 0])
        Sheet1.write(i+1, 1, results_gen[i, 1])

    compteur = 0
    for j in range(len(results_load_lambda)):
        if j != 15 and j != 16 and j != 32 and j != 38 and j != 39:
            Sheet1.write(compteur+1, 2, results_load_lambda[j, 1])
            Sheet1.write(compteur+1, 3, results_load_lambda[j, 2])
            compteur += 1

    for k in range(len(results_branch)):
        Sheet1.write(k+1, 5, results_branch[k, 0])
        Sheet1.write(k+1, 6, results_branch[k, 1])
        Sheet1.write(k+1, 7, results_branch[k, 2])

    book.save(xlsname)
