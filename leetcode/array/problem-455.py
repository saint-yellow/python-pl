from typing import List


class Solution:
    def findContentChildren(self, children: List[int], cookies: List[int]) -> int:
        return self.__method2(children, cookies)

    # 基于贪心策略的解法
    def __method1(self, children: List[int], cookies: List[int]) -> int:
        children.sort()
        cookies.sort()
        index = len(cookies) - 1
        result = 0
        for i in range(len(children) - 1, -1, 0):
            if index >= 0 and cookies[index] >= children[i]:
                result += 1
                index -= 1
        return result

    def __method2(self, children: List[int], cookies: List[int]) -> int:
        children.sort()
        cookies.sort()
        index = 0
        for i in range(len(cookies)):
            if index < len(children) and children[index] <= cookies[i]:
                index += 1
        return index
