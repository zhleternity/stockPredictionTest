# !/usr/bin/python
# -*- coding:utf-8 -*-
#__author__ = 'eternity'

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
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(10, 8), facecolor='w')

    plt.subplot(421)
    plt.plot(t, diff_price, 'r-')
    plt.grid(True)
    plt.title('涨跌幅')

    plt.subplot(422)
    plt.plot(t, volumn, 'g-')
    plt.grid(True)
    plt.title('交易量')

    clrs = plt.cm.terrain(np.linspace(0, 0.8, n))
    plt.subplot(423)
    for i, clr in enumerate(clrs):
        plt.plot(t, y[:, i], '-', color=clr, alpha=0.7)
    plt.title('所有组分')

    for i, clr in enumerate(clrs):
        axes = plt.subplot(4, 2, i+4)
        plt.plot(t, y[:, i], '-', color=clr)
        plt.title('组分%d' % (i+1))
        plt.grid(True)

    plt.subtitle(u'SH600000股票: GaussianHMM分解隐变量', fontsize=18)
    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.show()






















