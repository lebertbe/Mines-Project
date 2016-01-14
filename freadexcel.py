from FonctionExtraction import *


def freadexcel():

    bus = importBus()

    gen = importGen()

    branch = importBranch()

    gencost = importGenCost()

    return bus, gen, branch, gencost
