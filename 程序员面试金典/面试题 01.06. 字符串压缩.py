from collections import Counter

class Solution:

    '''
    1. 遍历法
    - 对字符串进行遍历
    - 如果当前字符与之前遍历字符相同, 使count+1, 
    - 如果不同, 则进行字符串拼接, 并且重置 tempC和count
    - 最后遍历结束后, 对最后一次得到的tempC和count 拼接
    - 注意题目要求, 对比result和原字符串的长度
    '''
    def compressString(self, S: str) -> str:
        if len(S) <= 0: return S
        result = ""
        tempC = S[0]
        count = 0

        for item in S:
            if item == tempC:
                count += 1
            else:
                result += f"{tempC}{count}"
                tempC = item
                count = 1
        result += f"{item}{count}"
        return S if len(S) <= len(result) else result
