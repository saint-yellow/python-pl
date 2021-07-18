# 剑指Offer Problem Nr. 42: 连续子数组的最大和

from typing import List


class Solution:
    def maxSubArray(self, numbers: List[int]) -> int:
        return self.__method2(numbers)

    # 基于动态规划的解法，具备常数级空间复杂度
    def __method1(self, numbers: List[int]) -> int:
        pre, ans = 0, numbers[0]
        for n in numbers:
            pre = max(pre + n, n)
            ans = max(ans, pre)
        return ans

    # 基于动态规划的解法，具备线性级空间复杂度
    def __method2(self, numbers: List[int]) -> int:
        if len(numbers) == 1:
            return numbers[0]
        f = [numbers[0]]
        for i in range(1, len(numbers)):
            f.append(max(f[i - 1] + numbers[i], numbers[i]))
        return max(f)
