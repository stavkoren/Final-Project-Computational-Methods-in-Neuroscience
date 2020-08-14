import numpy as np




def load_abalone_data():
    data = np.loadtxt("data/abalone_data.txt", dtype=str, delimiter=',')
    np.random.shuffle(data)
    print(data)



load_abalone_data()
