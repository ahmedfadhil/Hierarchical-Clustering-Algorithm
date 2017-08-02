import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use('ggplot')

X = np.array([[1, 2],
              [1.5, 1.8],
              [5, 8],
              [8, 8],
              [1, 0.6],
              [9, 11],
              [8, 2],
              [9, 4],
              [10, 2], ])
# plt.scatter(X[:, 0], X[:, 1], s=150)
# plt.show()

colors = 10 * ['g.', 'r.', 'c.', 'b.', 'k.']


class Mean_shift:
    def __init__(self, radius=4):

        self.radius = radius

    def fit(self, data):
        centroids = {}

        for i in range(len(data)):
            centroids[i] = data[i]
        while True:
            new_centroids = []
            for i in centroids:
                in_bandwidth = []
                centroid = centroids[i]
                for featureset in data:
                    if np.linalg.norm(featureset - centroids < self.radius):
                        in_bandwidth.append(featureset)



















                    # plt.scatter(X[:, 0], X[:, 1], s=150)
                    # plt.show()
