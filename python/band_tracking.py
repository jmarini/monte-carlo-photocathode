#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division, unicode_literals

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import scipy.interpolate
import seaborn as sns


print('Reading photoexcited particles...')
pe = pd.read_csv('photoexcited_particles.csv',
                 sep=' ', names=['id', 'x', 'y', 'Ei'], header=0)
pe['x'] *= 1e9
pe['y'] *= 1e9

print('Reading emitted particles...')
em = pd.read_csv('emitted.csv',
                 sep=' ', names=['id', 'time', 'Ef'], header=0)
em['time'] *= 1e12

df = em.merge(pe, on='id')

x_min = df.x.min()

print('Reading potential...')
potential = pd.read_csv('potential000.xyz',
                        sep=' ', names=['x', 'y', 'V'], header=0)
band = potential[potential.y==0.1][['x']].copy()
band['V'] = potential[potential.y==0.1].V * -1
band['V'] += np.abs(band.iloc[0].V)
band['x'] *= 1e3

valley_offset = np.zeros(10)
valley_offset[2] = 1.34
valley_offset[3] = 2.14

print('Reading tracking data...')
tr = pd.read_csv('tracking.csv',
                 sep=' ', names=['id', 'time', 'x', 'y', 'E', 'valley'], header=0)
tr.loc[tr.valley==9, 'valley'] = 1
tr['x'] *= 1e9
tr['y'] *= 1e9
tr['time'] *= 1e12
tr['Eadj'] = tr.E + [valley_offset[v] for v in tr.valley]

pids = tr.id.unique()
print('{} particles'.format(len(pids)))

band_inter = scipy.interpolate.interp1d(band.x, band.V, bounds_error=False, fill_value=0.)

def plot_energy_band(data, pid, cmap=None, ax=None):
    cmap = cmap or plt.cm.coolwarm
    df = data[data.id==pid][['x']].copy()
    df['V'] = data[data.id==pid].Eadj + [band_inter(_) for _ in df.x]
    xy = df.as_matrix().reshape(-1, 1, 2)
    segments = np.hstack([xy[:-1], xy[1:]])

    coll = LineCollection(segments, cmap=cmap)
    coll.set_array(data[data.id==pid].valley - 1.0)

    if ax is None:
        fig, ax = plt.subplots()
    ax.axhline(3.18, c='k', ls='--', lw=1)
    ax.axvline(x_min, c='k', ls='--', lw=1)
    band.plot(x='x', y='V', c='k', ax=ax, xlim=(0, max(50, df.x.max() * 1.1)), legend=False)
    ax.add_collection(coll)
    ax.autoscale_view()
    ax.scatter(df['x'].iloc[[0, -1]].as_matrix(),
               df['V'].iloc[[0, -1]].as_matrix(),
               c=[0.0, 1.0], s=50, cmap=cmap, zorder=10)
    plt.suptitle(pid)
    plt.savefig('img/{}.png'.format(pid))
    plt.close()
    print('.', end='', flush=True)

for pid in pids:
    plot_energy_band(tr, pid)
print('')
