# LeetCode 主站 Problem Nr. 78: 子集

from typing import List


class Solution:
    def subsets(self, numbers: List[int]) -> List[List[int]]:
        return self.__method1(numbers)

    def __method1(self, numbers: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        track: List[int] = []

        def backtracking(numbers: List[int], startIndex: int) -> None:
            result.append(track[:])

            if startIndex >= len(numbers):
                return

            for i in range(startIndex, len(numbers)):
                track.append(numbers[i])
                backtracking(numbers, i+1)
                track.pop()

        backtracking(numbers, 0)
        return result


if __name__ == '__main__':
    numbers = [1, 2, 3, 4]
    s = Solution()
    print(s.subsets(numbers))
