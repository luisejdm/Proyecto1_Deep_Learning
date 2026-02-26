import numpy as np

def load_data():
    x_train = np.load("../data/processed/x_train.npy")
    x_test = np.load("../data/processed/x_test.npy")
    return x_train, x_test

#this works if you run yout jupyter command at the level of "/Proyecto1_deep_learning" 
def load_data_2():
    try:
        x_train = np.load("../data/processed/x_train.npy")
        x_test = np.load("../data/processed/x_test.npy")
        return x_train, x_test
    except Exception as e:
        x_train = np.load("./data/processed/x_train.npy")
        x_test = np.load("./data/processed/x_test.npy")
    return x_train, x_test


# np.save("./data/processed/x_train_128.npy", x_train.astype("uint8"))
# np.save("./data/processed/x_test_128.npy", x_test.astype("uint8"))
# print("saved dataset in ../data/processed/")
def load_data_3():
    try:
        x_train = np.load("../data/processed/x_train_128.npy")
        x_test = np.load("../data/processed/x_test_128.npy")
        return x_train, x_test
    except Exception as e:
        x_train = np.load("./data/processed/x_train_128.npy")
        x_test = np.load("./data/processed/x_test_128.npy")
    return x_train, x_test

def load_data_full():
    try:
        x_train = np.load("../data/processed/x_train_full.npy")
        x_test = np.load("../data/processed/x_test_full.npy")
        return x_train, x_test
    except Exception as e:
        x_train = np.load("./data/processed/x_train_full.npy")
        x_test = np.load("./data/processed/x_test_full.npy")
    return x_train, x_test