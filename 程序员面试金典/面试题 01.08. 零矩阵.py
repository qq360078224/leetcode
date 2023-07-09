from collections import Counter
from typing import List, NoReturn
import copy


class Solution:

    """
    1. 额外数组记录
    - 申请额外的数组, 第一次遍历: 记录某一列或某一行是否有0
    - 第二次遍历: 如果记录的这一列或这一行有0, 则当前节点修改为0
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row, col = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = 1

        for i in range(m):
            for j in range(n):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0

    """
    2. 使用数组的第一行和第一列记录
    - 先判断数组第一行和第一列是否有0, 为后边处理第一列做准备
    - 第一次遍历: 记录某一列或某一行是否有0
    - 第二次遍历: 如果记录的这一列或这一行有0, 则当前节点修改为0
    - 最后根据之前记录的第一行,第一列是否为0, 单独处理第一行和第一列
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        i0 = any(matrix[i][0] == 0 for i in range(n))
        j0 = any(v == 0 for v in matrix[0])

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        for i in range(n):
            if i0:
                matrix[i][0] = 0

        for i in range(m):
            if j0:
                matrix[0][i] = 0
