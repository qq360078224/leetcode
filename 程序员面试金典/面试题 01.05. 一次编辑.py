from collections import Counter

class Solution:

    '''
    1.遍历对比
    - 循环对比2个字符串的第i,j个字符
    - 如果不相等就对count+1, 并且移动i或j
    - 直到2个字符串都遍历完成, 如果count < 2 则为一次编辑
    '''
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first) - len(second)) > 1: return False
        if first == second: return True
        l1, l2 = len(first), len(second)
        i, j, count = 0, 0, 0

        while i < l1 and j < l2:
            if first[i] == second[j]:
                i += 1
                j += 1
            else:
                count += 1
                if l2 > l1:
                    j += 1
                elif l2 < l1:
                    i += 1
                else:
                    i += 1
                    j += 1
        return count < 2
       
