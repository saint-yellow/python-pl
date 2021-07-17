# 剑指Offer Problem Nr. 39: 数组中出现次数超过一半的数字

from typing import Dict, List


class Solution:
    def majorityElement(self, numbers: List[int]) -> int:
        return self.__method1(numbers)

    # 基于哈希表的解法
    def __method1(self, numbers: List[int]) -> int:
        d: Dict[int, int] = {}
        half = (len(numbers) + 1) // 2
        for n in numbers:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
            if d[n] >= half:
                return n
        return None

    # 基于Boyer-Moore投票算法的解法
    def __method2(self, numbers: List[int]) -> int:
        count = 0
        candidate: int = None

        for n in numbers:
            if count == 0:
                candidate = n
            count += (1 if n == candidate else -1)
        return candidate
