#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tcad.tsv', sep='\t')
df['V'] *= -1
df['V'] += abs(df.iloc[0].V)

high = 0.9 * df.V.max()

print('{:.2f} nm'.format(df[df.V >= high].iloc[0].x * 1000))
print('{:.2f} eV'.format(df.V.max()))

df.plot(x='x', y='V', xlim=(0, 0.2))
plt.show()
