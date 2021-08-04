# LeetCode 主站 Problem Nr. 93: 分割回文串


from typing import List


class Solution:
    def __init__(self) -> None:
        self.result: List[str] = []
        self.track: List[str] = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.__method1(s)

    def __method1(self, s: str) -> List[str]:
        if not s or len(s) > 12:
            return self.result

        l: List[str] = list(s)
        self.__backtracking(l, 0, 0)
        return self.result

    def __backtracking(self, s: List[str], startIndex: int, dotNumber: int) -> None:
        if dotNumber == 3:
            if self.__isValid(s, startIndex, len(s) - 1):
                self.result.append(''.join(s))
            return

        for i in range(startIndex, len(s)):
            if self.__isValid(s, startIndex, i):
                s.insert(i + 1, '.')
                dotNumber += 1
                self.__backtracking(s, i + 2, dotNumber)
                dotNumber -= 1
                del s[i + 1]
            else:
                break

    def __isValid(self, s: List[str], start: int, end: int) -> bool:
        if start > end:
            return False

        if s[start] == '0' and start != end:
            return False

        number: int = 0
        for i in range(start, end + 1):
            if s[i] > '9' or s[i] < '0':
                return False

            number = number * 10 + int(s[i])
            if number > 255:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses('25525511135'))
