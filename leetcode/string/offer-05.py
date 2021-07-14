# 剑指Offer Problem Nr. 05: 替换空格

class Solution:
    def replaceSpace(self, string: str) -> str:
        return self.__method1(string)

    def __method1(self, string: str) -> str:
        if not string:
            return ''
        
        characters = list(string)
        for i in range(len(characters)):
            if characters[i] == ' ':
                characters[i] = '%20'
        return ''.join(characters)

    def __method2(self, string: str) -> str:
        return string.replace(' ', '%20')
