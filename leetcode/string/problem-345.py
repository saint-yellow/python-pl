class Solution:
    def reverseVowels(self, string: str) -> str:
        return self.__method1(string)

    def __method1(self, string: str) -> str:
        if not string:
            return ""

        letters = list(string)
        vowels = "AaEeIiOoUu"
        left, right = 0, len(letters) - 1
        while left < right:
            if letters[left] in vowels and letters[right] in vowels:
                letters[left], letters[right] = letters[right], letters[left]
                left += 1
                right -= 1
            elif letters[left] not in vowels:
                left += 1
            elif letters[right] not in vowels:
                right -= 1
            else:
                left += 1
                right -= 1
        return "".join(letters)


if __name__ == "__main__":
    s = Solution()
    print(s.reverseVowels("hello"))
    print(s.reverseVowels("leetcode"))
