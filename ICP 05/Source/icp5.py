
import matplotlib.pyplot as plt

import numpy as np
from sklearn.cluster import KMeans
X = np.array([[1,1],
     [1.5,2.0],
     [3.0,4.0],
     [5.0,7.0],
     [3.5,5.0],
     [4.5,5.0],
     ])

kmeans = KMeans(n_clusters=2).fit(X)
print(kmeans.cluster_centers_)
print(kmeans.labels_)
plt.scatter(X[:,0],X[:,1], label='True Position')
plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap='viridis')
plt.show()