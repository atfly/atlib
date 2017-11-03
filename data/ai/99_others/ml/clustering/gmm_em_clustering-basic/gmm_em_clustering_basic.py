# !/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from scipy.stats import multivariate_normal
from sklearn.mixture import GaussianMixture
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import pairwise_distances_argmin

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
# GaussianMixtureModel(GMM)。事实上，GMM和k - means很像，不过GMM是学习出一些概率密度函数来（所以GMM除了用在clustering上之外，
# 还经常被用于densityestimation），简单地说，k - means的结果是每个数据点被assign到其中某一个cluster了，
# 而GMM则给出这些数据点被assign到每个cluster的概率，又称作softassignment。
# 所谓混合高斯模型（GMM）就是指对样本的概率密度分布进行估计，而估计采用的模型（训练模型）是几个高斯模型的加权和（具体是几个要在模型训练前建立好）。
# 每个高斯模型就代表了一个类（一个Cluster）。对样本中的数据分别在几个高斯模型上投影，就会分别得到在各个类上的概率。然后我们可以选取概率最大的类所为判决结果。

#GaussianMixture(n_components=1, covariance_type=’full’, tol=0.001, reg_covar=1e-06, max_iter=100, n_init=1, init_params=’kmeans’, weights_init=None, means_init=None, 
#precisions_init=None, random_state=None, warm_start=False, verbose=0, verbose_interval=10) 
#参数： 
#1. n_components:混合高斯模型个数，默认为1 
#2. covariance_type:协方差类型，包括{‘full’,‘tied’, ‘diag’, ‘spherical’}四种，分别对应完全协方差矩阵（元素都不为零），相同的完全协方差矩阵（HMM会用到），对角协方差矩阵（非对角为零，对角不为零），球面协方差矩阵（非对角为零，对角完全相同，球面特性），默认‘full’ 完全协方差矩阵 
#3. tol：EM迭代停止阈值，默认为1e-3. 
#4. reg_covar:协方差对角非负正则化，保证协方差矩阵均为正，默认为0 
#5. max_iter:最大迭代次数，默认100 
#6. n_init:初始化次数，用于产生最佳初始参数，默认为1 
#7. init_params: {‘kmeans’, ‘random’}, defaults to ‘kmeans’.初始化参数实现方式，默认用kmeans实现，也可以选择随机产生 
#8. weights_init:各组成模型的先验权重，可以自己设，默认按照7产生 
#9. means_init:初始化均值，同8 
#10. precisions_init:初始化精确度（模型个数，特征个数），默认按照7实现 
#11. random_state :随机数发生器 
#12. warm_start :若为True，则fit（）调用会以上一次fit（）的结果作为初始化参数，适合相同问题多次fit的情况，能加速收敛，默认为False。 
#13. verbose :使能迭代信息显示，默认为0，可以为1或者大于1（显示的信息不同） 
#14. verbose_interval :与13挂钩，若使能迭代信息显示，设置多少次迭代后显示信息，默认10次。


if __name__ == '__main__':
    style = 'sklearn'

    np.random.seed(0)
    mu1_fact = (0, 0, 0)
    # 生成对角矩阵
    cov1_fact = np.diag((1, 2, 3))
    data1 = np.random.multivariate_normal(mu1_fact, cov1_fact, 400)
    mu2_fact = (2, 2, 1)
    cov2_fact = np.array(((1, 1, 3), (1, 2, 1), (0, 0, 1)))
    data2 = np.random.multivariate_normal(mu2_fact, cov2_fact, 100)
    data = np.vstack((data1, data2))
    y = np.array([True] * 400 + [False] * 100)

    if style == 'sklearn':

        g = GaussianMixture(n_components=2, covariance_type='full', tol=1e-6, max_iter=1000)
        g.fit(data)
        print u'类别概率:\t', g.weights_[0]
        print u'均值:\n', g.means_, '\n'
        print u'方差:\n', g.covariances_, '\n'
        mu1, mu2 = g.means_
        sigma1, sigma2 = g.covariances_
    else:
        num_iter = 100
        n, d = data.shape
        # 随机指定
        # mu1 = np.random.standard_normal(d)
        # print mu1
        # mu2 = np.random.standard_normal(d)
        # print mu2
        mu1 = data.min(axis=0)
        mu2 = data.max(axis=0)
        sigma1 = np.identity(d)
        sigma2 = np.identity(d)
        pi = 0.5
        # EM
        for i in range(num_iter):
            # E Step
            norm1 = multivariate_normal(mu1, sigma1)
            norm2 = multivariate_normal(mu2, sigma2)
            tau1 = pi * norm1.pdf(data)
            tau2 = (1 - pi) * norm2.pdf(data)
            gamma = tau1 / (tau1 + tau2)

            # M Step
            mu1 = np.dot(gamma, data) / np.sum(gamma)
            mu2 = np.dot((1 - gamma), data) / np.sum((1 - gamma))
            sigma1 = np.dot(gamma * (data - mu1).T, data - mu1) / np.sum(gamma)
            sigma2 = np.dot((1 - gamma) * (data - mu2).T, data - mu2) / np.sum(1 - gamma)
            pi = np.sum(gamma) / n
            print i, ":\t", mu1, mu2
        print u'类别概率:\t', pi
        print u'均值:\t', mu1, mu2
        print u'方差:\n', sigma1, '\n\n', sigma2, '\n'

    # 预测分类
    norm1 = multivariate_normal(mu1, sigma1)
    norm2 = multivariate_normal(mu2, sigma2)
    tau1 = norm1.pdf(data)
    tau2 = norm2.pdf(data)

    fig = plt.figure(figsize=(10, 5), facecolor='w')
    ax = fig.add_subplot(121, projection='3d')
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], c='b', s=30, marker='o', edgecolors='k', depthshade=True)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(u'原始数据', fontsize=15)
    ax = fig.add_subplot(122, projection='3d')
    order = pairwise_distances_argmin([mu1_fact, mu2_fact], [mu1, mu2], metric='euclidean')
    print order
    if order[0] == 0:
        c1 = tau1 > tau2
    else:
        c1 = tau1 < tau2
    c2 = ~c1
    acc = np.mean(y == c1)
    print u'准确率：%.2f%%' % (100 * acc)
    ax.scatter(data[c1, 0], data[c1, 1], data[c1, 2], c='r', s=30, marker='o', edgecolors='k', depthshade=True)
    ax.scatter(data[c2, 0], data[c2, 1], data[c2, 2], c='g', s=30, marker='^', edgecolors='k', depthshade=True)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(u'EM算法分类', fontsize=15)
    plt.suptitle(u'EM算法的实现', fontsize=18)
    plt.subplots_adjust(top=0.90)
    plt.tight_layout()
    plt.show()
