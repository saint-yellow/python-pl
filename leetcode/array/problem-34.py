from typing import List


class Solution:
    def searchRange(self, numbers: List[int], target: int) -> List[int]:
        return self.__method1(numbers, target)

    def __method1(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [-1, -1]

        n = len(numbers)

        def findTarget(numbers: List[int], length: int, target: int) -> int:
            left, right = 0, length-1
            while left <= right:
                middle = (left+right)//2
                if target == numbers[middle]:
                    return middle
                elif target < numbers[middle]:
                    right = middle-1
                else:
                    left = middle+1
            return -1

        t = findTarget(numbers, n, target)
        if t == -1:
            return [-1, -1]
        first = t
        second = t
        while first >= 0:
            if first-1 >= 0 and numbers[first-1] == numbers[first]:
                first -= 1
            else:
                break
        while second < n:
            if second+1 < n and numbers[second+1] == numbers[second]:
                second += 1
            else:
                break
        
        return [first, second]

    def __method2(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [-1, -1]

        result = []
        for i in range(len(numbers)):
            if numbers[i] == target:
                result.append(i)
        if len(result) == 0:
            return [-1, -1]
        if len(result) == 1:
            return [result[0], result[0]]
        return [result[0], result[-1]]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(s.searchRange([5, 7, 7, 8, 8, 10], 10))
    print(s.searchRange([5, 7, 7, 8, 8, 10], 5))
    print(s.searchRange([5, 7, 6, 8, 8, 10], 6))
