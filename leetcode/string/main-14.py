from typing import List


class Solution:
    def longestCommonPrefix(self, strings: List[str]) -> str:
        return self.__method1(strings)

    def __method1(self, strings: List[str]) -> str:
        if not strings:
            return ""

        strings.sort()
        shortest = strings[0]
        longest = strings[-1]

        i = 0
        while i < len(shortest) and shortest[i] == longest[i]:
            i += 1

        return shortest[:i]


if __name__ == "__main__":
    strings = ["flowers", "fish", "flight"]
    s = Solution()
    print(s.longestCommonPrefix(strings))
