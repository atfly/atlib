# !/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn.mixture import GaussianMixture, BayesianGaussianMixture
import scipy as sp
import matplotlib as mpl
import matplotlib.colors
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


def expand(a, b, rate=0.05):
    d = (b - a) * rate
    return a-d, b+d


matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

#Dirichlet Process Gaussian Mixture Models
if __name__ == '__main__':
    np.random.seed(0)
    cov1 = np.diag((1, 2))
    N1 = 500
    N2 = 300
    N = N1 + N2
    #多元正态分布
    x1 = np.random.multivariate_normal(mean=(3, 2), cov=cov1, size=N1)
    m = np.array(((1, 1), (1, 3)))
    x1 = x1.dot(m)
    x2 = np.random.multivariate_normal(mean=(-1, 10), cov=cov1, size=N2)
    x = np.vstack((x1, x2))
    y = np.array([0]*N1 + [1]*N2)
    n_components = 3

    # 绘图使用
    colors = '#A0FFA0', '#2090E0', '#FF8080'
    cm = mpl.colors.ListedColormap(colors)
    x1_min, x1_max = x[:, 0].min(), x[:, 0].max()
    x2_min, x2_max = x[:, 1].min(), x[:, 1].max()
    x1_min, x1_max = expand(x1_min, x1_max)
    x2_min, x2_max = expand(x2_min, x2_max)
    x1, x2 = np.mgrid[x1_min:x1_max:500j, x2_min:x2_max:500j]
    grid_test = np.stack((x1.flat, x2.flat), axis=1)

    plt.figure(figsize=(6, 6), facecolor='w')
    plt.suptitle(u'GMM/DPGMM比较', fontsize=15)

    ax = plt.subplot(211)
    gmm = GaussianMixture(n_components=n_components, covariance_type='full', random_state=0)
    gmm.fit(x)
    centers = gmm.means_
    covs = gmm.covariances_
    print u'GMM均值 = \n', centers
    print u'GMM方差 = \n', covs
    y_hat = gmm.predict(x)

    grid_hat = gmm.predict(grid_test)
    grid_hat = grid_hat.reshape(x1.shape)
    plt.pcolormesh(x1, x2, grid_hat, cmap=cm)
    plt.scatter(x[:, 0], x[:, 1], s=20, c=y, cmap=cm, marker='o', edgecolors='#202020')

    clrs = list('rgbmy')
    for i, (center, cov) in enumerate(zip(centers, covs)):
        value, vector = sp.linalg.eigh(cov)
        width, height = value[0], value[1]
        v = vector[0] / sp.linalg.norm(vector[0])
        angle = 180* np.arctan(v[1] / v[0]) / np.pi
        e = Ellipse(xy=center, width=width, height=height,
                    angle=angle, color=clrs[i], alpha=0.5, clip_box = ax.bbox)
        ax.add_artist(e)

    ax1_min, ax1_max, ax2_min, ax2_max = plt.axis()
    plt.xlim((x1_min, x1_max))
    plt.ylim((x2_min, x2_max))
    plt.title('GMM', fontsize=15)
    plt.grid(b=True, ls=':', color='#606060')

    # DPGMM
    dpgmm = BayesianGaussianMixture(n_components=n_components, covariance_type='full', max_iter=1000, n_init=5,
                                    weight_concentration_prior_type='dirichlet_process', weight_concentration_prior=0.1)
    dpgmm.fit(x)
    centers = dpgmm.means_
    covs = dpgmm.covariances_
    print u'DPGMM均值 = \n', centers
    print u'DPGMM方差 = \n', covs
    y_hat = dpgmm.predict(x)
    print y_hat

    ax = plt.subplot(212)
    grid_hat = dpgmm.predict(grid_test)
    grid_hat = grid_hat.reshape(x1.shape)
    plt.pcolormesh(x1, x2, grid_hat, cmap=cm)
    plt.scatter(x[:, 0], x[:, 1], s=20, c=y, cmap=cm, marker='o', edgecolors='#202020')

    for i, cc in enumerate(zip(centers, covs)):
        if i not in y_hat:
            continue
        center, cov = cc
        value, vector = sp.linalg.eigh(cov)
        width, height = value[0], value[1]
        v = vector[0] / sp.linalg.norm(vector[0])
        angle = 180* np.arctan(v[1] / v[0]) / np.pi
        e = Ellipse(xy=center, width=width, height=height,
                    angle=angle, color='m', alpha=0.5, clip_box = ax.bbox)
        ax.add_artist(e)
    plt.xlim((x1_min, x1_max))
    plt.ylim((x2_min, x2_max))
    plt.title('DPGMM', fontsize=15)
    plt.grid(b=True, ls=':', color='#606060')
    plt.tight_layout(2, rect=(0, 0, 1, 0.95))
    plt.show()
