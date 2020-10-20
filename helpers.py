import numpy as np
from Matrix import Matrix

def findPrimeMatrices(matrices):
    factoredMatrix = {}## dictionary that contains all matrices that can be factored
    for i in range(len(matrices)):
        factoredMatrix[matrices[i]] = True

    for i in range(len(matrices)):
        for j in range(len(matrices)):
            if not matrices[i].is_identity() and not matrices[j].is_identity():
                # print("matrices to multiply")
                # print(matrices[i], matrices[j])
                # print("product:")
                # print(matrices[i]*matrices[j])
                factoredMatrix[matrices[i]*matrices[j]] = False
    prime_matrices = []

    for (k,v) in factoredMatrix.items():
        if(v == True): prime_matrices.append(k)

    return prime_matrices

def reshapeMatrices(matrices):
    for k in range(len(matrices)):
        matrices[k] = np.array(matrices[k])
        matrices[k] = Matrix(matrices[k].reshape(2,2))


def createAllBinaryMatrix(size):
    return generateAllBinaryStrings(size,[None]*size,0, [])


def generateAllBinaryStrings(n, arr, i, res):
    if i == n:
        res.append(arr.copy())
        return
    arr[i] = 0
    generateAllBinaryStrings(n,arr,i+1, res)

    arr[i] = 1
    generateAllBinaryStrings(n,arr, i+1,res)
    return res
