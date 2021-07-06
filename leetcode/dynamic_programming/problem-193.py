from typing import List


class Solution:
    def rob(self, numbers: List[int]) -> int:
        return self.__method3(numbers)


    def __method1(self, numbers: List[int]) -> int:
        # 没得偷
        if not numbers:
            return 0

        # 只有一家可偷
        n = len(numbers)
        if n == 1:
            return numbers[0]

        dp = [numbers[0], max(numbers[0], numbers[1])]
        for i in range(2, n):
            # 偷： dp[i] = dp[i-2] + numbers[i]
            # 不偷：dp[i] = dp[i-1]
            dp.append(max(dp[i-2]+numbers[i], dp[i-1]))
        return dp[n-1]


    def __method2(self, numbers: List[int]) -> int:
        # 没得偷
        if not numbers:
            return 0

        # 只有一家可偷
        n = len(numbers)
        if n == 1:
            return numbers[0]

        p, q = numbers[0], max(numbers[0], numbers[1])
        for i in range(2, n):
            # 偷： dp[i] = dp[i-2] + numbers[i]
            # 不偷：dp[i] = dp[i-1]
            p, q = q, max(p+numbers[i], q)
        return q

if __name__ == '__main__':
    s = Solution()
    print(s.rob([2,7,9,3,1]))
