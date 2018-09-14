import numpy as np


vector_rand = np.random.randint(0,21,size=15)
print("Vector with random integers between 0 and 20: ",vector_rand)
print("Most frequent value in the vector list: ",np.argmax(np.bincount(vector_rand)))