from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Dropout, Embedding, Flatten, LSTM, SpatialDropout1D, SimpleRNN
from keras.layers.convolutional import Conv1D
from keras.constraints import maxnorm
from keras.layers.convolutional import MaxPooling1D
from keras.callbacks import ModelCheckpoint
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#Loading dataset
tweets = pd.read_csv('Tweets.csv', sep=',')
tweets.head(2)
data = tweets[['text','airline_sentiment']]
#formatting data
data = data[data.airline_sentiment != "neutral"]
data['text'] = data['text'].apply(lambda x: x.lower())
data['text'] = data['text'].apply((lambda x: re.sub('[^a-zA-z0-9\s]','',x)))
max_features = 2000
tokenizer = Tokenizer(num_words=max_features, split=' ')
tokenizer.fit_on_texts(data['text'].values) #tokenizing
X = tokenizer.texts_to_sequences(data['text'].values)
X = pad_sequences(X)
embed_dim = 128
lstm_out = 196
Y = pd.get_dummies(data['airline_sentiment']).values
#splitting testing and training data
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.25, random_state = 42)
#selecting data for training and validation
X_val = X_train[:500]
Y_val = Y_train[:500]
partial_X_train = X_train[500:]
partial_Y_train = Y_train[500:]
batch_size = 512
num_classes = Y_test.shape[1]
#creating model
model = Sequential()
model.add(Embedding(max_features, embed_dim, input_length=X_train.shape[1]))
model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=2))
model.add(Conv1D(filters=64, kernel_size=3, padding='same', activation='relu'))
model.add(Flatten())
model.add(Dense(2, activation='softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics = ['accuracy']) #compiling model
print(model.summary())
#fitting into model
history = model.fit(partial_X_train,
                    partial_Y_train,
                    epochs = 20,
                    batch_size=batch_size,
                    validation_data=(X_val, Y_val))

#plotting traning and validation loss
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss) + 1)
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
plt.clf()
#plotting training and validation accuracy
acc = history.history['acc']
val_acc = history.history['val_acc']
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()