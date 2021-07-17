# 剑指Offer Problem Nr. 57-II: 和为s的连续正数序列

from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        return self.__method2(target)

    # 暴力解法
    def __method1(self, target: int) -> List[List[int]]:
        result: List[List[int]] = []
        if target < 3:
            return result

        limit = (target+1) // 2
        sequence = range(1, limit+1)
        for i in range(0, limit+1):
            for j in range(i, target+1):
                if sum(sequence[i:j + 1]) == target:
                    result.append(list(sequence[i:j + 1]))
                    break
                if sum(sequence[i:j + 1]) > target:
                    break

        return result

    # 基于双指针的解法
    def __method2(self, target: int) -> int:
        result: List[List[int]] = []
        left, right = 1, 2
        while left < right:
            total = (left + right) * (right - left + 1) / 2
            if total == target:
                result.append([i for i in range(left, right+1)])
                left += 1
            elif total < target:
                right += 1
            else:
                left += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.findContinuousSequence(20))
