class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.__method1(text1, text2)

    def __method1(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        length1, length2 = len(text1), len(text2)
        table = [[0 for _ in range(length1 + 1)] for _ in range(length2 + 1)]

        for i in range(length2):
            for j in range(length1):
                if text1[j] == text2[i]:
                    table[i + 1][j + 1] = table[i][j] + 1
                else:
                    table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j])
        return table[length2][length1]

    def __method2(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        length1, length2 = len(text1), len(text2)
        dp = [0 for _ in range(length2 + 1)]
        for i in range(1, length1 + 1):
            upLeft = dp[0]
            for j in range(1, length2 + 1):
                temp = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = upLeft + 1
                else:
                    dp[j] = max(dp[j - 1], dp[j])
                upLeft = temp

        return dp[length1]


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonSubsequence("qwert", "qwertyuio"))
