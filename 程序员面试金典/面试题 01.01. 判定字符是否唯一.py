class Solution:

    '''
    1. 位运算
    - 对于每个字符, 我们可以使用 ASCII码作为数组的idx, dict的key等.
    - 在一个数组中, 如果idxN没有元素, 那么我们将遍历的字符放进数组中
    - 如果idxN已有的元素与当前遍历的字符相等, 那么这个字符就是重复字符. 否则直到字符串遍历完成, 得出没有重复字符.
    - 因为这个题目我们不需要知道具体字符是什么, 所以就可以借助位运算来做. 将1左移"ASCII位"后得到一个类似于数组的int, 通过 & 操作与之前的结果进行对比判断字符是否相等, 通过 | 操作对不相等的元素进行"放进数组" 操作]
    '''
    def isUnique(self, astr: str) -> bool:
        mask = 0
        for item in astr:
            position = ord(item) - ord('a')
            if mask & (1 << position) != 0:
                return False
            else:
                mask |= (1 << position)
        return True

    '''
    2. set()法 
    - 题目本质是判断是否含有重复元素, 我们可以使用set, dict这种数据结构进行判断; 同时也可以借助一些系统内置函数减少代码量
    '''
    def isUnique1(self, astr: str) -> bool:
        allSet = set()
        for item in astr:
            if item in allSet:
                return False
            else:
                allSet.add(item)
        return True