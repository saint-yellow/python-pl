from typing import List


class Solution:
    def findErrorNums(self, numbers: List[int]) -> List[int]:
        return self.__method1(numbers)

    # 基于排序的解法
    def __method1(self, numbers: List[int]) -> List[int]:
        numbers.sort()
        n = len(numbers)

        # 找出缺失的数字
        missedNumber = 0
        for i in range(1, n+1):
            if i not in numbers:
                missedNumber = i

        # 找出重复的数字
        repeatedNumber = 0
        for i in range(n-1):
            if numbers[i] == numbers[i+1]:
                repeatedNumber = numbers[i]
        return [repeatedNumber, missedNumber]

    # 基于哈希表的解法
    def __method2(self, numbers: List[int]) -> int:
        result = [0, 0]
        mapping = {}
        for n in numbers:
            mapping.update({n: mapping.get(n, 0) + 1})
        for i in range(1, len(numbers)+1):
            if mapping.get(i, 0) == 0:
                result[1] = i
            if mapping.get(i, 0) == 2:
                result[0] = i
        return result

    # 基于位运算的解法
    def __method3(self, numbers: List[int]) -> int:
        pass


            
