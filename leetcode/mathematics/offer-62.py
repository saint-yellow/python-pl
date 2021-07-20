# 剑指Offer Problem Nr. 62: 圆圈中最后剩下的数字 (约瑟夫环问题)

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return self.__method2(n, m)

    def __method1(self, n: int, m: int) -> int:
        people = [i for i in range(n)]

        die = 0
        while n > 1:
            die = (die + m - 1) % n
            del people[die]
            n -= 1

        return people[0]

    def __method2(self, n: int, m: int) -> int:
        die = 0
        for i in range(2, n+1):
            die = (die + m) % i
        return die


if __name__ == '__main__':
    s = Solution()
    print(s.lastRemaining(10, 17))
