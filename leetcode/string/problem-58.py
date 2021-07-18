class Solution:
    def lengthOfLastWord(self, string: str) -> int:
        return self.__method2(string)

    def __method1(self, string: str) -> int:
        if not string:
            return 0

        words = string.split(" ")
        for w in words[::-1]:
            if w:
                return len(w)
        return 0

    def __method2(self, string: str) -> int:
        if not string:
            return 0

        count = 0
        i = len(string) - 1
        while i >= 0:
            if string[i] == " ":
                if count > 0:
                    break
                else:
                    i -= 1
            else:
                count += 1
                i -= 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))
    print(s.lengthOfLastWord(" "))
    print(s.lengthOfLastWord("saint-yellow"))
