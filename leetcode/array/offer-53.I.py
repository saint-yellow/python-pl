# 剑指Offer Problem Nr. 53-I: 在排序数组中查找数字 I

from typing import Dict, List


class Solution:
    def search(self, numbers: List[int], target: int) -> int:
        return self.__method2(numbers, target)

    def __method1(self, numbers: List[int], target: int) -> int:
        if not numbers:
            return 0

        d: Dict[int, int] = {}

        for n in numbers:
            d.update({n: d.get(n, 0) + 1})

        return 0 if target not in d else d[target]

    def __method2(self, numbers: List[int], target: int) -> int:
        index = self.__searchIndex(numbers, target)

        if index == -1:
            return 0

        count = 1
        minIndex, maxIndex = 0, len(numbers) - 1
        left, right = index, index
        while left > minIndex:
            left -= 1
            if numbers[left] != target:
                left += 1
                break
            else:
                count += 1
        while right < maxIndex:
            right += 1
            if numbers[right] != target:
                right -= 1
                break
            else:
                count += 1
        return count

    def __searchIndex(self, numbers: List[int], target: int) -> int:
        if not numbers:
            return -1

        left, right = 0, len(numbers) - 1
        while left <= right:
            middle = (left + right) // 2
            if target == numbers[middle]:
                return middle
            elif target < numbers[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([5, 7, 7, 8, 8, 10], 8))
