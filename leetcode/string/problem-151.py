class Solution:
    def reverseWords(self, string: str) -> str:
        return self.__method1(string)

    # 基于Python语言特性的解法
    def __method1(self, string: str) -> str:
        if not string:
            return ''
        words = string.split()
        words.reverse()
        result = ' '.join(words)
        return result
