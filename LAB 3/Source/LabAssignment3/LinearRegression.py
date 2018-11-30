from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
from keras.datasets import mnist
from keras.utils import np_utils
from keras.callbacks import TensorBoard
import tensorflow as tf
import matplotlib as plt
batch_size = 40
nb_classes = 10
nb_epoch = 20


(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
Y_Train = np_utils.to_categorical(y_train, nb_classes)
Y_Test = np_utils.to_categorical(y_test, nb_classes)

# Linear regression model
model = Sequential()
model.add(Dense(output_dim=10, input_shape=(784,), init='normal', activation='sigmoid'))
model.compile(optimizer='SGD', loss='mean_absolute_error')
model.summary()


# Train
tensorboard = TensorBoard(log_dir="logs/{}",histogram_freq=0, write_graph=True, write_images=True)
model.fit(X_train, Y_Train, nb_epoch=nb_epoch, batch_size=batch_size,callbacks=[tensorboard])


# Evaluate
evaluation = model.evaluate(X_test, Y_Test, verbose=1)
print(evaluation)