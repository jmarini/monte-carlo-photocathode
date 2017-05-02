#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
import seaborn as sns

pe = pd.read_csv('photoexcited_particles.csv', sep=' ', names=['id', 'x', 'y', 'Ei'], header=0)
pe['x'] *= 1e9
pe['y'] *= 1e9

em = pd.read_csv('emitted.csv', sep=' ', names=['id', 'time', 'Ef'], header=0)
em['time'] *= 1e12

df = em.merge(pe, on='id')

particles = pd.read_csv('particles.csv', sep=' ', names=['timestep', 'time', 'n'], header=0)
particles['time'] *= 1e12


potential = pd.read_csv('potential000.xyz', sep=' ', names=['x', 'y', 'V'], header=0)
band = potential[potential.y==0.1][['x']].copy()
band['V'] = potential[potential.y==0.1].V * -1
band['V'] += np.abs(band.iloc[0].V)
band['x'] *= 1e3

band_around = scipy.interpolate.interp1d(band.x, band.V, bounds_error=False, fill_value=0.)


qe = len(em) / len(pe) * 100.
max_qe = (1.0 - len(pe[pe.x < df.x.min()]) / len(pe)) * 100.
qe_adj = len(em) / len(pe[pe.x >= df.x.min()]) * 100.
x_min = df.x.min()

fig, ax  = plt.subplots(figsize=(10, 8))
ax2 = ax.twinx()

df.hist('x', bins=100, ax=ax)
band.plot('x', 'V', ax=ax2, c='k', grid=False, legend=False, ylim=(-1, 5), xlim=(0, 250), lw=2)

ax.axvline(df.x.min(), c='k', ls='--', lw=1)
ax2.axhline(band.iloc[0].V + 3.18, lw=2)
# ax2.axhline(band_around(df.x.min()) + (5 - 3.393), ls='--')

ax.set_xlabel(r'x [$\mu m$]', fontsize=18)
plt.setp(ax.get_xticklabels(), fontsize=16)
ax.set_ylabel('Emitted Particle Count', fontsize=18)
plt.setp(ax.get_yticklabels(), fontsize=16)
ax2.set_ylabel('E [eV]', fontsize=18)
plt.setp(ax2.get_yticklabels(), fontsize=16)
ax.set_title('')

ax2.annotate('Y = {:.2f}%'.format(qe), xy=(155, 4.6), fontsize=16)
ax2.annotate('Yadj = {:.2f}%'.format(qe_adj), xy=(155, 4.3), fontsize=16)
ax2.annotate('Ymax = {:.2f}%'.format(max_qe), xy=(155, 4.0), fontsize=16)
ax2.annotate('xmin = {:.2f} nm'.format(x_min), xy=(155, 3.7), fontsize=16)

plt.show()
