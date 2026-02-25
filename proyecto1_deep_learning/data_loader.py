import numpy as np

def load_data():
    x_train = np.load("../data/processed/x_train.npy")
    x_test = np.load("../data/processed/x_test.npy")
    return x_train, x_test

#this works if you run yout jupyter command at the level of "/Proyecto1_deep_learning" 
def load_data_2():
    x_train = np.load("./data/processed/x_train.npy")
    x_test = np.load("./data/processed/x_test.npy")
    return x_train, x_test

