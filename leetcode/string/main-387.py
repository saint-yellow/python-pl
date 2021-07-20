class Solution:
    def firstUniqChar(self, s: str) -> int:
        return self.__method1(s)

    # 基于哈希表的解法
    def __method1(self, s: str) -> int:
        if not s:
            return -1

        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i]
            else:
                d[s[i]].append(i)
        u = [v[0] for v in d.values() if len(v) == 1]
        return -1 if not u else min(u)


if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("leetcode"))
    print(s.firstUniqChar("loveleetcode"))
