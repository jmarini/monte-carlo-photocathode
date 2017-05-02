#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

vo = pd.read_csv('valley_occupation.csv', sep=' ')
vo['time'] *= 1e12
vo['total'] = vo.c1 + vo.c2
vo['G'] = vo.c1 / vo.total
vo['ML'] = vo.c2 / vo.total


fig, ax = plt.subplots(figsize=(8, 8))

vo.plot(x='time', y=['G', 'ML'], ax=ax, lw=3)

ax.set_xlabel('t [ps]', fontsize=18)
plt.setp(ax.get_xticklabels(), fontsize=16)
ax.set_ylabel('Valley Occupation', fontsize=18)
plt.setp(ax.get_yticklabels(), fontsize=16)
ax.set_title('')

plt.legend(fontsize=16)

plt.show()
