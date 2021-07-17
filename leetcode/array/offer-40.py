# 剑指Offer Problem Nr. 40: 最小的k个数

from typing import List


class Solution:
    def getLeastNumbers(self, array: List[int], k: int) -> List[int]:
        return self.__method1(array, k)

    # 基于排序的解法
    def __method1(self, array: List[int], k: int) -> List[int]:
        array.sort()
        return array[0:k]
