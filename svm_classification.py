import numpy as np

def load_abalone_data():
    data = np.loadtxt("data/abalone_data.txt", dtype=str, delimiter=',')
    print(data)


load_abalone_data()
