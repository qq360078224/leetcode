from collections import Counter

class Solution:

    '''
    1. Counter()法
    - 对字符串进行Counter后, 看value != 0 的元素个数是否大于1 
    '''
    def canPermutePalindrome(self, s: str) -> bool:
        dict = Counter(s)
        res = 0
        for (_, value) in dict.items():
            if value % 1 != 0:
                res += 1
        return res <= 1
