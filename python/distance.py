#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division

import pandas as pd
import matplotlib.pyplot as plt


def process(plot=False):
    pe = pd.read_csv('photoexcited_particles.csv', sep=' ', names=['id', 'x', 'y', 'Ei'], header=0)
    pe['x'] *= 1e9
    pe['y'] *= 1e9
    # pe.plot(x='x', y='y', kind='scatter', xlim=(0, 300), ylim=(0, 220))
    # plt.show()

    em = pd.read_csv('emitted.csv', sep=' ', names=['id', 'time', 'Ef'], header=0)

    df = em.merge(pe, on='id')

    df.plot(x='x', y='Ef', kind='scatter', xlim=(0, 300), ylim=(0, 3))
    if plot:
        plt.show()
    return df

if __name__ == '__main__':
    process(plot=True)


# qe = []
# for i in range(0, 301, 300 // 100):
#     dpe = pe[(pe.x >= i) & (pe.x < i + dn)]
#     dem = em.merge(dpe, on='id')
#     num_pe = len(dpe)
#     num_em = len(dem)
#     if num_pe:
#         qe.append(100. * num_em / num_pe)
#     else:
#         qe.append(0.)
