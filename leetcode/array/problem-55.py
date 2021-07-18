from typing import List


class Solution:
    def canJump(self, numbers: List[int]) -> bool:
        return self.__method1(numbers)

    # 基于贪心策略的解法
    def __method1(self, numbers: List[int]) -> bool:
        cover, final = 0, len(numbers) - 1
        if final == 0:
            return True
        i = 0
        while i <= cover:
            cover = max(i + numbers[i], cover)
            if cover >= final:
                return True
            i += 1
        return False

    # 基于动态规划的解法
    def __method2(self, numbers: List[int]) -> bool:
        pass
