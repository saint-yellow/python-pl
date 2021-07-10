class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.__method2(m, n)

    # 基于动态规划的解法，时间、空间复杂度都是平方级
    def __method1(self, m: int, n: int) -> int:
        if not (m and n):
            return 0

        table = [[1]*n] + [[1]+[0]*(n-1) for _ in range(m-1)]

        for j in range(1, m):
            for i in range(1, n):
                table[j][i] = table[j][i-1] + table[j-1][i]
        print(table)
        return table[m-1][n-1]

    # 基于动态规划的解法，时间、空间复杂度分别是平方级和线性级
    def __method2(self, m: int, n: int) -> int:
        if not (m and n):
            return 0

        dp = [1] * n
        for i in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i-1]
        return dp[n-1]

    # 基于组合数学的解法， 时间、空间复杂度分别是线性级和常数级
    def __method3(self, m: int, n: int) -> int:
        from math import comb
        return comb(m+n-2, n-1)


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))
