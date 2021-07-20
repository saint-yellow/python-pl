from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = self.__reverse(x)
        return x == y

    def __method1(self, x: int) -> bool:
        if x < 0:
            return False
        y = self.__reverse(x)
        return x == y

    def __reverse(self, x: int) -> int:
        numbers = self.__decompose(x)
        length = len(numbers)
        result = 0
        for i in range(length):
            result += numbers[i] * (10 ** (length - 1 - i)) * (10 ** (-i))
        return int(result)

    def __decompose(self, x: int) -> List[int]:
        """
        123 -> [3, 20, 100]\n
        -123 -> [-3, -20, -100]
        """
        c = 0
        n = 1
        l = []
        while c != x:
            e = x % (10 ** n) - c
            l.append(e)
            c += e
            n += 1
        return l

    def __method2(self, x: int) -> int:
        str1 = str(x)
        return True if str1 == str1[::-1] else False
