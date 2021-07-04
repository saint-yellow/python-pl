class Solution:
    def climbStairs(self, n: int) -> int:
        return self.method3(n)

    # 超时
    def method1(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        return self.method1(n-1) + self.method1(n-2)

    def method2(self, n: int) -> int:
        if n in (0, 1, 2):
            return n
        
        dp = [0, 1, 2]
        for i in range(3, n+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[-1]

    def method3(self, n: int) -> int:
        p, q, r = 0, 0, 1
        for _ in range(1, n+1):
            p = q
            q = r
            r = p+q
        return r

    