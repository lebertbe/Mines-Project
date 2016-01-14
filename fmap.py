try:
    import matplotlib.pyplot as plt
except:
    raise
import numpy as np
import networkx as nx
from scipy.misc import imread


def fmap(results_branch_map, results_gen, results_load_lambda, mapname):

    G = nx.house_graph()

    # explicitly set positions
    pos = {1: (14.370117, 47.418176),
        2: (4.614258, 50.699357),
        3: (8.041992, 46.820110),
        4: (15.424805, 49.856874),
        5: (13.051758, 52.447082),
        6: (7.690430, 50.754993),
        7: (10.415039, 51.799557),
        8: (9.494063, 48.693917),
        9: (9.448242, 55.940997),
        10: (11.645508, 55.245727),
        11: (26.264136, 59.256457),
        12: (-3.823242, 40.066862),
        13: (26.039473, 62.645926),
        14: (2.768555, 47.179757),
        15: (-1.274414, 52.820469),
        16: (22.368164, 38.845412),
        17: (19.116211, 47.060143),
        18: (10.678711, 44.923325),
        19: (11.381836, 43.855656),
        20: (12.788086, 42.185115),
        21: (16.127930, 40.201253),
        22: (14.721680, 37.393436),
        23: (9.272461, 39.999566),
        24: (23.842208, 55.646382),
        25: (5.998535, 49.705536),
        26: (25.512130, 57.227828),
        27: (5.493164, 51.962320),
        28: (10.854492, 61.157371),
        29: (7.514648, 59.100786),
        30: (10.327148, 63.988811),
        31: (16.215820, 68.312733),
        32: (7.426758, 61.536660),
        33: (19.665527, 52.277120),
        34: (-8.217773, 39.729721),
        35: (20.170898, 67.010288),
        36: (17.182617, 64.674052),
        37: (15.073242, 60.471659),
        38: (14.018555, 57.104429),
        39: (14.699707, 45.991873),
        40: (19.489746, 48.787565)}

    # Calcul of the difference between generation and load
    diff = []
    compteur = 0
    for j in range(len(results_load_lambda)):
        if j != 15 and j != 16 and j != 32 and j != 38 and j != 39:
            inter = results_gen[compteur, 1] - results_load_lambda[j, 1]
            diff.append(inter)
            compteur += 1
    diff = np.asarray(diff, dtype=np.float64)

    # Colors for Exporting and Importing buses
    compteur = 0
    for j in range(len(results_load_lambda)):
        if j != 15 and j != 16 and j != 32 and j != 38 and j != 39:
            if diff[compteur] > 0:
                nx.draw_networkx_nodes(G, pos, node_size=30, nodelist=[j+1], node_color='g')
            else:
                nx.draw_networkx_nodes(G, pos, node_size=30, nodelist=[j+1], node_color='r')
            compteur += 1
        else:
            nx.draw_networkx_nodes(G, pos, node_size=30, nodelist=[j+1], node_color='w')

    # Colors and width for branches (depending on the capacity used)
    for i in results_branch_map:
        u = [i[0], i[1]]
        ptrans = i[2]
        pmax = i[3]
        tau = abs(float(ptrans)/float(pmax))
        if tau > 0.8:
            nx.draw_networkx_edges(G, pos,
                                   edgelist=[u], width=1.5, alpha=0.8, edge_color='r')
        elif 0.5 < tau < 0.8:
            nx.draw_networkx_edges(G, pos,
                                   edgelist=[u], width=1.5, alpha=0.8, edge_color='k')
        elif 0.25 < tau < 0.5:
            nx.draw_networkx_edges(G, pos,
                                   edgelist=[u], width=1, alpha=0.8, edge_color='b')
        else:
            nx.draw_networkx_edges(G, pos,
                                   edgelist=[u], width=1, alpha=0.8, edge_color='g')

    # Names of the buses
    labels = {}
    labels[1] = r'$AT$'
    labels[2] = r'$BE$'
    labels[3] = r'$CH$'
    labels[4] = r'$CZ$'
    labels[5] = r'$DE$'
    labels[6] = r'$DE$'
    labels[7] = r'$DE$'
    labels[8] = r'$DE$'
    labels[9] = r'$DK$'
    labels[10] = r'$DK$'
    labels[11] = r'$EE$'
    labels[12] = r'$ES$'
    labels[13] = r'$FI$'
    labels[14] = r'$FR$'
    labels[15] = r'$GB$'
    labels[16] = r'$GR$'
    labels[17] = r'$HU$'
    labels[18] = r'$IT$'
    labels[19] = r'$IT$'
    labels[20] = r'$IT$'
    labels[21] = r'$IT$'
    labels[22] = r'$IT$'
    labels[23] = r'$IT$'
    labels[24] = r'$LT$'
    labels[25] = r'$LU$'
    labels[26] = r'$LV$'
    labels[27] = r'$NL$'
    labels[28] = r'$NO$'
    labels[29] = r'$NO$'
    labels[30] = r'$NO$'
    labels[31] = r'$NO$'
    labels[32] = r'$NO$'
    labels[33] = r'$PL$'
    labels[34] = r'$PT$'
    labels[35] = r'$SE$'
    labels[36] = r'$SE$'
    labels[37] = r'$SE$'
    labels[38] = r'$SE$'
    labels[39] = r'$SI$'
    labels[40] = r'$SK$'

    # Put labels on each buses
    # nx.draw_networkx_labels(G, pos, labels, font_size=5)

    # Background European map
    map_background = imread('map_europe.png')
    plt.imshow(map_background, zorder=0, extent=[-25.5, 42, 30.5, 75])

    plt.axis('off')
    plt.savefig(mapname, dpi=1000)  # save as png
    plt.show()  # display
