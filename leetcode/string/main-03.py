# LeetCode Problem Nr. 3: 无重复字符的字符串

from typing import List


class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        return self.__method2(string)

    # 基于双指针的解法 (个人的劣解)
    def __method1(self, string: str) -> int:
        i, j, k, n = 0, 0, 0, len(string)
        lengths: List[int] = []
        while j < n:
            subString = string[i:j]
            if string[j] not in subString:
                k += 1
                j += 1
            else:
                lengths.append(k)
                i += 1
                k = len(string[i:j])
        lengths.append(len(string[i:j]))
        return max(lengths)

    # 基于滑动窗口的解法 （官方的优解
    def __method2(self, string: str) -> int:
        occur = set()
        n = len(string)

        pointer, result = -1, 0
        for i in range(n):
            if i != 0:
                occur.remove(string[i - 1])
            while pointer + 1 < n and string[pointer + 1] not in occur:
                occur.add(string[pointer + 1])
                pointer += 1
            result = max(result, pointer - i + 1)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))
