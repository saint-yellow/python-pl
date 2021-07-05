# LeetCode problem #34: 反转字符串

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        return self.__method1(s)

    def __method1(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
