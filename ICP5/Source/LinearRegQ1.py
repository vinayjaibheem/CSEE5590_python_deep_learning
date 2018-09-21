import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading Data
data = pd.read_csv('slr04.csv')
print(data.shape)
data.head()

X = data['X'].values
Y = data['Y'].values

mean_x = np.mean(X)
mean_y = np.mean(Y)

# Total number of values
m = len(X)

# Using the formula to calculate b1 and b2
numer = 0
denom = 0
for i in range(m):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
b1 = numer / denom
b0 = mean_y - (b1 * mean_x)

# Print coefficients
print(b1, b0)

max_x = np.max(X) + 100
min_x = np.min(X) - 100

x = np.linspace(min_x, max_x, 1000)
y = b0 + b1 * x

dates = np.reshape(X, (len(X), 1))  # converting to matrix of n X 1
prices = np.reshape(Y, (len(Y), 1))

print(dates.shape)
plt.scatter(dates, prices, color='yellow')
plt.plot(x, y, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
