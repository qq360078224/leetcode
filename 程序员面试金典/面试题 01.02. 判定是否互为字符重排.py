from collections import Counter

class Solution:

    '''
    1. Counter() 
    - 对字符串进行Counter 后, 如果相等, 表示所有字符和字符个数相等
    '''
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        return Counter(s1) == Counter(s2)


    '''
    2. 数组去重法
    - 我们可以将第二个字符串转为数组, 并对第一个字符串进行遍历, 每遍历一个字符, 就看数组中是否包含当前元素, 如果包含就从数组中删除. 当第一个字符串遍历结束后, 数组为空, 则表示2个字符串可以进行重排
    '''
    def CheckPermutation1(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        list2 = list(s2)
        for item in s1:
            if item in list2:
                list2.remove(item)
        return len(list2) == 0