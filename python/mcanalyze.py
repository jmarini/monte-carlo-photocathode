#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import zipfile

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} UUID'.format(sys.argv[0]))
        sys.exit()

    uuid = sys.argv[1]
    filename = os.path.join(os.getcwd(), '{}.zip'.format(uuid))
    tmpdir = os.path.join(os.getcwd(), 'tmp')

    if not os.path.exists(tmpdir):
        os.makedirs(tmpdir)

    with zipfile.ZipFile(filename, 'r') as zf:
        zf.extractall(tmpdir)


