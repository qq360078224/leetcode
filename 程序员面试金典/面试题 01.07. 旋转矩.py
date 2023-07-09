from collections import Counter
from typing import List, NoReturn
import copy

class Solution:

    '''
    1. copy法<多申请空间>
    - 将原数组进行copy, 然后进行遍历, 将每一行的数据赋值给新数组的每一列
    '''
    def rotate1(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        #result = [[0 for i in range(n)] for j in range(n)]
        result = copy.deepcopy(matrix)
        for i in range(n):
            for j in range(n):
                matrix[j][n-i-1] = result[i][j]

    '''
    2. 两次对折法<原地翻转>
    - 将原数组先沿对角线 (左上-右下) 斜向翻转
    - 对翻转后的数组在沿垂直中线左右翻转
    '''
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
