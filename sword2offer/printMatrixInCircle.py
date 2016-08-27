# encoding: utf-8

def printMatrixInCircle(matrix):

    flag = 0
    for item in matrix:
        if item != []:
            flag = 1

    if flag == 0:
        return

    if len(matrix) == 1:
        for x in matrix[0]:
            print x
        return



    # 上
    for x in matrix[0][:-1]:
        print x,
    # 左
    for x in [item[-1] for item in matrix][:-1]:
        print x,

    # 下
    for x in matrix[-1][::-1][:-1]:
        print x,

    # 右
    for x in [item[0] for item in matrix][::-1][:-1]:
        print x,

    printMatrixInCircle([item[1:-1] for item in matrix[1:-1]])



if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    printMatrixInCircle(matrix)