# 剑指Offer Problem Nr. 58-II: 左旋转字符串


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return self.__method1(s, n)

    def __method1(self, s: str, n: int) -> str:
        words = list(s)
        left = 0
        right = n - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        left = n
        right = len(s) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        left = 0
        right = len(s) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return "".join(words)

    def __method2(self, s: str, n: int) -> str:
        return s[n:] + s[:n]
