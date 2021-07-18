# LeetCode Problem Nr. 541: 反转字符串II


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return self.__method1(s, k)

    def __method1(self, s: str, k: int) -> str:
        if not s:
            return ""

        a = list(s)
        for i in range(0, len(a), 2 * k):
            a[i : i + k] = reversed(a[i : i + k])
        return "".join(a)
