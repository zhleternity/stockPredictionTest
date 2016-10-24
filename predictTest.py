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
    close_price = x[:, 0]
    volumn = x[:, 1]
    amount = x[:, 2]
    #  每天的最高价与最低价的差
    amplitude_price = x[:, 3] - x[:, 4]
    #  涨跌值
    diff_price = np.diff(close_price)
    #  成交量
    volumn = volumn[1:]
    #  成交额
    amount = amount[1:]
    #  每日振幅
    amplitude_price = amplitude_price[1:]
    #  观测值
    sample = np.column_stack(diff_price, volumn, amount, amplitude_price)
    n = 5
    model = hmm.GaussianHMM(n_components=n, covariance_type='full')
    model.fit(sample)
    y = model.predict_proba(sample)
    np.set_printoptions(suppress=True)
    print y

    t = np.arange(len(diff_price))
    





















