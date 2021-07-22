# LeetCode Problem Nr. 10-II: 青蛙跳台阶问题

SUP = 10 ** 9 + 7


class Solution:
    def numWays(self, n: int) -> int:
        return self.__method1(n)

    def __method1(self, n: int) -> int:
        if n <= 1:
            return 1

        p, q = 1, 1
        i = 2
        while i <= n:
            p, q = q, p + q
            i += 1
        return q % SUP


if __name__ == "__main__":
    s = Solution()
    print(s.numWays(7))
