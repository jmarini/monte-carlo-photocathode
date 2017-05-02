#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

dt = np.dtype([('ts', np.int32), ('x', np.float32), ('energy', np.float32), ('valley', np.int32),])

def read_file(filename):
    raw_data = np.fromfile(filename, dtype=dt)
    return pd.DataFrame(raw_data.tolist(), columns=raw_data.dtype.names)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        df = read_file('tracking001000.bin')
    else:
        df = read_file(sys.argv[1])
    print(df.describe())
