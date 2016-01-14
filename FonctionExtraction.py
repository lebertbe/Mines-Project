import xlrd
import numpy as np


def importBus():
    wb = xlrd.open_workbook('Demand.xlsx')
    sh = wb.sheet_by_name(u'Sheet1')
    resultFinal=[]
    compteur = 0
    for rownum in range(sh.nrows):
        inter1 = sh.row_values(rownum)
        if compteur > 0:
            nomBus = inter1[0]
            typeCons = 2
            if compteur == 1:
                typeCons = 3
            if inter1[1] != "":
                Pmax = inter1[1]
            else:
                Pmax = 0
            Qmax = 0
            Gs = 0
            Bs = 0
            area = 1
            Vm = 1
            Va = 0
            baseKV = 380
            zone = 1
            Vmax = 1.05
            Vmin = 0.95
            inter = [nomBus, typeCons, Pmax, Qmax, Gs, Bs, area, Vm, Va, baseKV, zone, Vmax, Vmin]
            resultFinal.append(inter)
        compteur += 1
    resultFinal = np.asarray(resultFinal, dtype=np.float64)
    return resultFinal


def importGenCost():
    wb = xlrd.open_workbook('Capacity_cost.xlsx')
    sh = wb.sheet_by_name(u'Sheet1')
    resultFinal=[]
    compteur = 0
    for rownum in range(sh.nrows):
        LigneExcel = sh.row_values(rownum)
        if compteur > 0:
            model = 1
            startup = 0
            shutdown = 0
            N = 10
            # Each "CapacityN" reprensents the capacity (MW) of one type of technology
            # and is equal to : max installed capacity * capacity factor
            # "CostN" is in €/h [= MW*(€/MWh)]
            # There is one generator per bus. It is the sum of different generators
            # from the cheapest technology (in €/MWh) to the most expensive
            # Costs and Capacities are summed up with the last technology
            Capacity1 = LigneExcel[2]*LigneExcel[3]
            Cost1 = LigneExcel[2]*LigneExcel[3]*LigneExcel[4]
            Capacity2 = LigneExcel[5]*LigneExcel[6]
            Cost2 = LigneExcel[5]*LigneExcel[6]*LigneExcel[7]
            Capacity3 = LigneExcel[8]*LigneExcel[9]
            Cost3 = LigneExcel[8]*LigneExcel[9]*LigneExcel[10]
            Capacity4 = LigneExcel[11]*LigneExcel[12]
            Cost4 = LigneExcel[11]*LigneExcel[12]*LigneExcel[13]
            Capacity5 = LigneExcel[14]*LigneExcel[15]
            Cost5 = LigneExcel[14]*LigneExcel[15]*LigneExcel[16]
            Capacity6 = LigneExcel[17]*LigneExcel[18]
            Cost6 = LigneExcel[19]*LigneExcel[17]*LigneExcel[18]
            Capacity7 = LigneExcel[20]*LigneExcel[21]
            Cost7 = LigneExcel[22]*LigneExcel[20]*LigneExcel[21]
            Capacity8 = LigneExcel[23]*LigneExcel[24]
            Cost8 = LigneExcel[25]*LigneExcel[23]*LigneExcel[24]
            Capacity9 = LigneExcel[26]*LigneExcel[27]
            Cost9 = LigneExcel[28]*LigneExcel[26]*LigneExcel[27]

            Cost = [Cost1, Cost2, Cost3, Cost4, Cost5, Cost6, Cost7, Cost8, Cost9]
            Capacity = [Capacity1, Capacity2, Capacity3, Capacity4, Capacity5, Capacity6, Capacity7, Capacity8, Capacity9]

            p = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            c = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            p[0] = Capacity[0]
            c[0] = Cost[0]
            for x in range(8):
                p[x+1] = p[x] + Capacity[x+1]
                c[x+1] = c[x] + Cost[x+1]

            inter = [model, startup, shutdown, N, 0, 0, p[0], c[0], p[1], c[1], p[2], c[2], p[3], c[3], p[4], c[4], p[5], c[5], p[6], c[6], p[7], c[7], p[8], c[8]]

            resultFinal.append(inter)
        compteur += 1
    resultFinal = np.asarray(resultFinal, dtype=np.float64)
    return resultFinal


def importGen():
    wb = xlrd.open_workbook('Capacity_cost.xlsx')
    sh = wb.sheet_by_name(u'Sheet1')
    resultFinal  = []
    compteur = 0
    for rownum in range(sh.nrows):
        inter1 = sh.row_values(rownum)
        if compteur > 0:
            nomBus = inter1[0]
            if inter1[1] != "":
                Pg = inter1[1]
            else:
                Pg = 0
            Qg = 0
            Qmax = 0
            Qmin = 0
            Vg = 1
            mBase = 100
            status = 1
            Pmax = Pg
            Pmin = 0
            Pc1 = 0
            Pc2 = 0
            Qc1min = 0
            Qc1max = 0
            Qc2min = 0
            Qc2max = 0
            ramp_agc = 0
            ramp_10 = 0
            ramp_30 = 0
            ramp_q = 0
            apf = 0
            inter = [nomBus, Pg, Qg, Qmax, Qmin, Vg, mBase, status, Pmax, Pmin, Pc1, Pc2, Qc1min, Qc1max, Qc2min, Qc2max, ramp_agc, ramp_10, ramp_30, ramp_q, apf]
            if Pg >- 1:
                resultFinal.append(inter)
        compteur += 1
    resultFinal = np.asarray(resultFinal)
    return resultFinal
    

def importBranch():
    wb = xlrd.open_workbook('Branch.xlsx')
    sh = wb.sheet_by_name(u'Sheet1')
    resultFinal = []
    compteur = 0
    for rownum in range(sh.nrows):
        inter1 = sh.row_values(rownum)
        if compteur > 0:
            Bus1 = int(inter1[0])
            Bus2 = int(inter1[1])
            r = inter1[2]
            x = inter1[3]
            b = 0.1
            rateA = inter1[4]
            rateB = inter1[4]
            rateC = inter1[4]
            ratio = 0
            angle = 0
            status = 1
            angmin = -360
            angmax = 360

            inter = [Bus1, Bus2, r, x, b, rateA, rateB, rateC, ratio, angle, status, angmin, angmax]
            resultFinal.append(inter)
        compteur += 1
    resultFinal = np.asarray(resultFinal)
    return resultFinal
