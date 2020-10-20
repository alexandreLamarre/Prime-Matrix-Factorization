from helpers import *
import numpy as np

if __name__ == "__main__":
    allMatrices = createAllBinaryMatrix(4)
    reshapeMatrices(allMatrices)
    primeMatrices = findPrimeMatrices(allMatrices)

    for k in range(len(primeMatrices)):
        print(primeMatrices[k])
        print("\n")
