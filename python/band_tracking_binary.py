#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division, unicode_literals

import os
import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import scipy.interpolate
import seaborn as sns
import re


def read_tracking_data(filename):
    dt = np.dtype([('t', np.float32), ('x', np.float32), ('y', np.float32), ('E', np.float32), ('v', np.int32),])
    raw_data = np.fromfile(filename, dtype=dt)
    tr = pd.DataFrame(raw_data.tolist(), columns=raw_data.dtype.names)
    tr['t'] *= 1e12
    tr['x'] *= 1e9
    tr['y'] *= 1e9
    tr.loc[tr.v==9, 'v'] = 1
    tr['Eadj'] = tr.E + [valley_offset[v] for v in tr.v]
    tr['V'] = tr.Eadj + [band_inter(_) for _ in tr.x]
    return tr

def times_scattered(data, Eth):
    all_times = data[data.V >= Eth].t.unique()
    if len(all_times) == 0:
        return 0
    times_scattered = all_times[np.array([len(data[data.t==t]) >= 2 for t in all_times])]
    return len(times_scattered)


def average_distance(data, Eth):
    positions = data[data.V >= Eth].x.unique()
    if len(positions) == 0:
        return (0, 0)
    differences = np.abs(positions[:-1] - positions[1:])
    return (differences.mean(), differences.std())


def plot_energy_band(data, pid, cmap=None, ax=None):
    cmap = cmap or plt.cm.coolwarm
    xy = data[['x', 'V']].as_matrix().reshape(-1, 1, 2)
    segments = np.hstack([xy[:-1], xy[1:]])

    coll = LineCollection(segments, cmap=cmap)
    coll.set_array(data.v - 1.0)

    if ax is None:
        fig, ax = plt.subplots()
    ax.axhline(3.18, c='k', ls='--', lw=1)
    band.plot(x='x', y='V', c='k', ax=ax, xlim=(0, max(50, data.x.max() * 1.1)), legend=False)
    ax.add_collection(coll)
    ax.autoscale_view()
    ax.scatter(data['x'].iloc[[0, -1]].as_matrix(),
               data['V'].iloc[[0, -1]].as_matrix(),
               c=[0.0, 1.0], s=50, cmap=cmap, zorder=10)
    ax.annotate('num_scatter = {}'.format(times_scattered(data, 3.18)), xy=(max(50, data.x.max() * 1.1) * 0.75, 0), fontsize=14)
    ax.annotate((r'$\mu_x$ = ' '{:.3f} nm\n ' r'$\sigma_x$ = ' '{:.3f} nm').format(*average_distance(data, 3.18)), xy=(max(50, data.x.max() * 1.1) * 0.5, -0.3), fontsize=14)
    plt.suptitle(pid)
    plt.savefig('img/{}.png'.format(pid))


    plt.close()
    print('.', end='', flush=True)




print('Reading potential...')
potential = pd.read_csv('potential000.xyz',
                        sep=' ', names=['x', 'y', 'V'], header=0)
band = potential[potential.y==0.1][['x']].copy()
band['V'] = potential[potential.y==0.1].V * -1
band['V'] += np.abs(band.iloc[0].V)
band['x'] *= 1e3

band_inter = scipy.interpolate.interp1d(band.x, band.V, bounds_error=False, fill_value=0.)


valley_offset = np.zeros(10)
valley_offset[2] = 1.34
valley_offset[3] = 2.14


particles = {'pid': [], 'n': [], 'mu': [], 'std': [], 'x': [], 'E': []}


print('Reading tracking data...')
for root, dirs, files in os.walk('.'):
    for file in files:
        if os.path.splitext(file)[-1] != '.bin':
            continue

        m = re.search(r'tracking([0-9]+)\.bin', file)
        if m is None:
            print('Error: {}'.format(file))
            continue
        pid = m.group(1)
        df = read_tracking_data(os.path.join(root, file))
        plot_energy_band(df, pid)
        particles['pid'].append(pid)
        particles['x'].append(df.iloc[0].x)
        particles['E'].append(df.iloc[0].E)
        particles['n'].append(times_scattered(df, 3.18))
        mu, std = average_distance(df, 3.18)
        particles['mu'].append(mu)
        particles['std'].append(std)
print('')

print('Saving csv...')
data = pd.DataFrame(particles)
data.to_csv('out.csv', index=False)

