# coding=utf-8
import numpy as np
import sklearn.cluster as skc
from sklearn import metrics
import matplotlib.pyplot as plt

mac2id = dict()

onlinetimes = []
f = open('D:\\workspace\\FileForder\\聚类\\sufOnline.txt', encoding='utf-8')
for line in f:
    # 机器mac地址
    mac = line.split(',')[2]
    onlinetime = int(line.split(',')[6])
    starttime = int(line.split(',')[4].split(' ')[1].split(':')[0])
    if mac not in mac2id:
        mac2id[mac] = len(onlinetimes)
        onlinetimes.append((starttime, onlinetime))
    else:
        onlinetimes[mac2id[mac]] = [(starttime, onlinetime)]
real_X = np.array(onlinetimes).reshape((-1, 2))

X = real_X[:, 0:1]

# eps两个样本被看做邻居节点的最大距离,min_samples簇的样本数
db = skc.DBSCAN(eps=0.01, min_samples=20).fit(X)
labels = db.labels_

print('Labels:')
print(labels)
raito = len(labels[labels[:] == -1]) / len(labels)
print('Noise raito:', format(raito, '.2%'))

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels))

for i in range(n_clusters_):
    print('Cluster ', i, ':')
    print(list(X[labels == i].flatten()))

plt.hist(X, 24)
plt.show()