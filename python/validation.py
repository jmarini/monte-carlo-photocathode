#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def read_output_files(folder):
    pe = pd.read_csv(os.path.join(folder, 'photoexcited_particles.csv'),
                     sep=' ', names=['id', 'x', 'y', 'Ei'], header=0)
    pe['x'] *= 1e9
    pe['y'] *= 1e9

    em = pd.read_csv(os.path.join(folder, 'emitted.csv'),
                     sep=' ', names=['id', 'time', 'Ef'], header=0)
    em['time'] *= 1e12

    return em.merge(pe, on='id').copy()




if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} <folder>'.format(sys.argv[0]))
        sys.exit()

    df = read_output_files(sys.argv[1])


    fig, ax  = plt.subplots(figsize=(14, 10))
    df.hist('x', bins=100, ax=ax)

    ax.set_xlabel('x [nm]', fontsize=18)
    ax.set_ylabel('Counts', fontsize=18)
    ax.tick_params(axis='both', which='major', labelsize=14)
    ax.set_title('Emitted Particles', fontsize=22)


    plt.show()

