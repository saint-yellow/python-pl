ord_A, ord_Z, ord_a, ord_z = ord("A"), ord("Z"), ord("a"), ord("z")


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return self.__method1(word)

    def __method1(self, word: str) -> bool:
        def isAllUpper(characters: str) -> bool:
            for c in characters:
                d = ord(c)
                if d < ord_A or d > ord_Z:
                    return False
            return True

        def isAllLower(characters: str) -> bool:
            for c in characters:
                d = ord(c)
                if d < ord_a or d > ord_z:
                    return False
            return True

        c = word[0]
        d = ord(c)
        if ord_A <= d <= ord_Z:
            return isAllLower(word[1:]) or isAllUpper(word[1:])
        elif ord_a <= d <= ord_z:
            return isAllLower(word[1:])
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print(s.detectCapitalUse("USA"))
    print(s.detectCapitalUse("leetcode"))
    print(s.detectCapitalUse("Google"))
    print(s.detectCapitalUse("FlaG"))
    print(s.detectCapitalUse("flaG"))
