from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, metrics

diabetes_datasets = datasets.load_diabetes()
x = diabetes_datasets.data
y = diabetes_datasets.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)

y_pred = knn.predict(x_test)

print(metrics.accuracy_score(y_test, y_pred))

k_range = range(1, 50)
scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    scores.append(metrics.accuracy_score(y_test, y_pred))

import matplotlib.pyplot as plt

plt.plot(k_range, scores)
plt.xlabel("Value of k")
plt.ylabel("Testing accuracy")
plt.show()