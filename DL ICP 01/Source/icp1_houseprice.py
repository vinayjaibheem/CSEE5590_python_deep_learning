from keras import losses
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


dataset = pd.read_csv("housing.csv", header=None).values

X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,0:13], dataset[:,13],test_size=0.20, random_state=87)
np.random.seed(155)
model = Sequential() # create model
model.add(Dense(30, input_dim=13, activation='relu')) # hidden layer
model.add(Dense(10, activation='relu')) # hidden layer
model.add(Dense(1, activation='tanh')) # output layer
model.compile(loss='mean_squared_error', optimizer='adagrad')
model_fit = model.fit(X_train, Y_train, epochs=100, verbose=0,initial_epoch=0)
print(model.summary())
print(model.evaluate(X_test, Y_test, verbose=0))
#print(losses.mean_squared_error(X_test,Y_test))