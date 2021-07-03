from typing import List


class Solution:
    def containsDuplicate(self, numbers: List[int]) -> bool:
        return self.method1(numbers)


    # 基于哈希表的解法
    def method1(self, numbers: List[int]) -> bool:
        d = {}
        for n in numbers:
            if n in d:
                return True
            else:
                d[n] = 1
        return False

    # 基于排序和双指针的解法
    def method2(self, numbers: List[int]) -> bool:
        length = len(numbers)
        if length == 1:
            return False

        numbers = sorted(numbers)
        i, j = 0, 1
        while j < length:
            if numbers[i] == numbers[j]:
                return True
            i += 1
            j += 1
        return False

