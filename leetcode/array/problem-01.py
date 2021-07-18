from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.method2(numbers, target)

    # 暴力解法
    def method1(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] == numbers[j]:
                    return [i, j]
        return []

    # 基于哈希表的解法
    def method2(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        d = {}
        for i in range(n):
            a = target - numbers[i]
            if numbers[i] in d:
                return [d[numbers[i]], i]
            else:
                d[a] = i
        return []

    # 基于双指针的解法
    def method3(self, numbers: List[int], target: int) -> List[int]:
        # 记住各元素原先的位置（索引）
        tuples = [(index, value) for (index, value) in enumerate(numbers)]
        # 按照元素的值的大小排序
        tuples.sort(key=lambda t: t[1])

        left, right = 0, len(tuples) - 1
        while left < right:
            if tuples[left][1] + tuples[right][1] == target:
                return [tuples[left][0], tuples[right][0]]
            elif tuples[left][1] + tuples[right][1] < target:
                left += 1
            else:
                right -= 1
        return []
