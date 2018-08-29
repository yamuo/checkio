import numpy as np

def checkio(matrix):
    ret = "False"
    input_len = len(matrix)
    add = input_len - 3
    arr2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

    for i in range(add):
        list = matrix[:4,:4]

        arr.transpose()
        print(list)
                
    return ret

print(checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]))
