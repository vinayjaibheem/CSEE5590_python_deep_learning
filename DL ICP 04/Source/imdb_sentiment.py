import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Activation, Dense, Embedding, SimpleRNN
from keras import backend as K
#from keras_tqdm import TQDMNotebookCallback
from keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
from keras.callbacks import TensorBoard
from keras.preprocessing.text import Tokenizer

imdb_df = pd.read_csv('./labeledTrainData.tsv', sep = '\t')
pd.set_option('display.max_colwidth', 500)

num_words = 10000
tokenizer = Tokenizer(num_words = num_words)
tokenizer.fit_on_texts( imdb_df.review )
sequences = tokenizer.texts_to_sequences(imdb_df.review)
y = np.array(imdb_df.sentiment)
print(y)
from keras.preprocessing.sequence import pad_sequences

max_review_length = 552

pad = 'pre'

X = pad_sequences(sequences,
                  max_review_length,
                  padding=pad,
                  truncating=pad)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size = 0.2)
input_shape = X_train.shape
K.clear_session()

rnn_model = Sequential()
# We specify the maximum input length to our Embedding layer
# so we can later flatten the embedded inputs

rnn_model.add(Embedding(num_words,
                        8,
                        input_length=max_review_length))

rnn_model.add(SimpleRNN(32))
rnn_model.add(Dense(1))
rnn_model.add(Activation('sigmoid'))
rnn_model.summary()

rnn_model.compile(optimizer="adam",
              loss='binary_crossentropy',
              metrics=['accuracy'])

tensorboard = TensorBoard(log_dir="imdb_rnn_logs",histogram_freq=0, write_graph=True, write_images=True)


rnn_history = rnn_model.fit(X_train,
                            y_train,
                            epochs=5,
                            batch_size=32,
                            validation_split=0.3,
                            callbacks=[tensorboard])
