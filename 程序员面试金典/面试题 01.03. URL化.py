
class Solution:

    '''
    1. 遍历法 
    '''
    def replaceSpaces(self, S: str, length: int) -> str:
        res = ""
        for idx in range(length):
            res += (S[idx] if S[idx] != ' ' else "%20")
        return res
