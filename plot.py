from matplotlib import pyplot as plt
import numpy as np


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


if __name__ == "__main__":
    x = np.linspace(0, 8, 50) + np.abs(np.random.randn((50))) * 0.3
    plt.plot(sigmoid(x))
    plt.show()

