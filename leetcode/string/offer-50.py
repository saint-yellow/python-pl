# 剑指Offer Problem Nr. 50: 第一个只出现一次的字符

from typing import Dict, List


class Solution:
    def firstUniqChar(self, s: str) -> str:
        return self.__method1(s)

    def __method1(self, s: str) -> str:
        if not s:
            return " "

        d: Dict[int, List[int]] = {}

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i]
            else:
                d[s[i]].append(i)

        for k in d.keys():
            if len(d[k]) == 1:
                return k
        return " "


if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("leetcode"))
    print(s.firstUniqChar("loveleetcode"))
    print(s.firstUniqChar("abaccdeff"))
