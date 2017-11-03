# !/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# http://blog.pluskid.org/?p=57
# Vector Quantization 。这项技术广泛地用在信号处理以及数据压缩等领域。事实上，在 JPEG 和 MPEG-4 等多媒体压缩格式里都有 VQ 这一步。
# Vector Quantization 这个名字听起来有些玄乎，其实它本身并没有这么高深。大家都知道，模拟信号是连续的值，而计算机只能处理离散的数字信号，
# 在将模拟信号转换为数字信号的时候，我们可以用区间内的某一个值去代替着一个区间，比如，[0, 1) 上的所有值变为 0 ，[1, 2) 上的所有值变成 1 ，如此类推。
# 其这就是一个 VQ 的过程。一个比较正式一点的定义是：VQ 是将一个向量空间中的点用其中的一个有限子集来进行编码的过程。
# 实际做法就是：将每个像素点当作一个数据，跑一下 K-means ，得到 k 个 centroids ，然后用这些 centroids 的像素值来代替对应的 cluster 里的所有点的像素值。
# 对于彩色图片来说，也可以用同样的方法来做，例如 RGB 三色的图片，每一个像素被当作是一个 3 维向量空间中的点。

def restore_image(cb, cluster, shape):
    row, col, dummy = shape
    image = np.empty((row, col, 3))
    index = 0
    for r in range(row):
        for c in range(col):
            image[r, c] = cb[cluster[index]]
            index += 1
    return image


def show_scatter(a):
    N = 10
    print '原始数据：\n', a
    density, edges = np.histogramdd(a, bins=[N, N, N], range=[(0, 1), (0, 1), (0, 1)])
    density /= density.sum()
    x = y = z = np.arange(N)
    d = np.meshgrid(x, y, z)

    fig = plt.figure(1, facecolor='w')
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(d[1], d[0], d[2], c='r', s=100 * density / density.max(), marker='o', depthshade=True)
    ax.set_xlabel(u'红色分量')
    ax.set_ylabel(u'绿色分量')
    ax.set_zlabel(u'蓝色分量')
    plt.title(u'图像颜色三维频数分布', fontsize=20)

    plt.figure(2, facecolor='w')
    den = density[density > 0]
    print den.shape
    den = np.sort(den)[::-1]
    t = np.arange(len(den))
    plt.plot(t, den, 'r-', t, den, 'go', lw=2)
    plt.title(u'图像颜色频数分布', fontsize=18)
    plt.grid(True)

    plt.show()


if __name__ == '__main__':
    matplotlib.rcParams['font.sans-serif'] = [u'SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False

    num_vq = 50
    im = Image.open('lena.png')  # son.bmp(100)/flower2.png(200)/son.png(60)/lena.png(50)
    image = np.array(im).astype(np.float) / 255
    image = image[:, :, :3]
    image_v = image.reshape((-1, 3))
    show_scatter(image_v)

    N = image_v.shape[0]  # 图像像素总数
    # 选择足够多的样本(如1000个)，计算聚类中心
    idx = np.random.randint(0, N, size=1000)
    image_sample = image_v[idx]
    model = KMeans(num_vq)
    model.fit(image_sample)
    c = model.predict(image_v)  # 聚类结果
    print '聚类结果：\n', c
    print '聚类中心：\n', model.cluster_centers_

    plt.figure(figsize=(15, 8), facecolor='w')
    plt.subplot(121)
    plt.axis('off')
    plt.title(u'原始图片', fontsize=18)
    plt.imshow(image)
    # plt.savefig('1.png')

    plt.subplot(122)
    vq_image = restore_image(model.cluster_centers_, c, image.shape)
    plt.axis('off')
    plt.title(u'矢量量化后图片：%d色' % num_vq, fontsize=20)
    plt.imshow(vq_image)
    # plt.savefig('2.png')

    plt.tight_layout(2)
    plt.show()
