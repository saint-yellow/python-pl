# 剑指Offer Problem Nr. 10-I: 斐波那契数列

SUP = 10**9+7


class Solution:
    def fib(self, n: int) -> int:
        return self.__method2(n)

    def __method1(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0, 1]
        for i in range(2, n+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n] % SUP

    def __method2(self, n: int) -> int:
        if n <= 1:
            return n

        p, q = 0, 1
        for _ in range(2, n+1):
            p, q = q, p+q
        return q % SUP


if __name__ == '__main__':
    s = Solution()
    print(s.fib(5))
