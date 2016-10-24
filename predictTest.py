# !/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from hmmlearn import hmm
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.metrics.pairwise import pairwise_distances_argmin


def expand(a, b):
    d = (b - a) * 0.05
    return a-d, b+d

if __name__ == "__main__":
    #0日期 1开盘 2最高 3最低 4收盘 5成交量 6成交额
    x = np.loadtxt('18.SH600000.txt', delimiter='\t', skiprows=2, usecols=(4, 5, 6, 2, 3))
    