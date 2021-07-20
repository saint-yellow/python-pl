from typing import List


class Solution:
    def singleNonDuplicate(self, numbers: List[int]) -> int:
        return self.__method1(numbers)

    # 基于栈的解法
    def __method1(self, numbers: List[int]) -> int:
        n = len(numbers)
        while n > 2:
            i = numbers.pop()
            j = numbers.pop()
            if i != j:
                return i
            n -= 2
        return numbers[0]

    # 基于双指针的解法
    def __method2(self, numbers: List[int]) -> int:
        n = len(numbers)
        i, j = n - 1, n - 2
        while i > 0:
            if numbers[i] != numbers[j]:
                return numbers[j]
            else:
                i -= 2
                j -= 2
        return numbers[0]

    # 基于二分搜索的解法
    def __method3(self, numbers: List[int]) -> int:
        low, high = 0, len(numbers) - 1
        while low < high:
            middle = low + (high - low) // 2
            halves_are_even = (high - middle) % 2 == 0
            if numbers[middle + 1] == numbers[middle]:
                if halves_are_even:
                    low = middle + 2
                else:
                    high = middle - 1
            elif numbers[middle - 1] == numbers[middle]:
                if halves_are_even:
                    high = middle - 2
                else:
                    low = middle + 1
            else:
                return numbers[middle]
        return numbers[low]

    # 仅对偶数索引进行二分搜索
    def __method4(self, numbers: List[int]) -> int:
        low, high = 0, len(numbers) - 1
        while low < high:
            middle = low + (high - low) // 2
            if middle % 2 == 1:
                middle -= 1
            if numbers[middle] == numbers[middle + 1]:
                low = middle + 2
            else:
                high = middle
        return numbers[low]
