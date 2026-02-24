import numpy as np

def load_data():
    x_train = np.load("../data/processed/x_train.npy")
    x_test = np.load("../data/processed/x_test.npy")
    return x_train, x_test