#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division, unicode_literals

import pandas as pd
import numpy as np
import scipy.interpolate

df = pd.read_csv('export.csv')
del df['Nd X']
del df['Potential X']
del df['eDensity X']
del df['hDensity X']
del df['eFieldX X']
del df['eFieldY X']

df = df.rename(columns={
    'Na X': 'x',
    'Na Y': 'Na',
    'Nd Y': 'Nd',
    'Potential Y': 'V',
    'eDensity Y': 'n',
    'hDensity Y': 'p',
    'eFieldX Y': 'Ex',
    'eFieldY Y': 'Ey',
})
sign = np.sign(df.x.mean())
df.x = df.x.abs()
df = df[df.x >= 0.1]
df.x -= 0.1
df.n *= 1e6
df.p *= 1e6
df.Na *= 1e6
df.Nd *= 1e6
df.Ex *= 1e2
df.Ey *= sign * 1e2

df2 = pd.DataFrame({'x': np.arange(0, 0.5, 0.0025)})
# x and y are flipped between sentaurus and tcad
for col in ['Na', 'Nd', 'V', 'n', 'p', 'Ey', 'Ex']:
    interpolate = scipy.interpolate.interp1d(df.x, df[col], bounds_error=False)
    df2[col] = interpolate(df2.x)

df2.to_csv('tcad.tsv', sep='\t')
