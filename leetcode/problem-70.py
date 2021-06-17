class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def method1(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        return self.method1(n-1) + self.method1(n-2)

    