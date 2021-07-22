# LeetCode Problem Nr. 288: 汇总区间

from typing import List


class Solution:
    def summaryRanges(self, numbers: List[int]) -> List[str]:
        return self.__method1(numbers)

    def __method1(self, numbers: List[int]) -> List[int]:
        result: List[str] = []
        i, j, n = 0, 0, len(numbers)
        while j < n:
            # corner case
            if j == n - 1:
                result.append(self.__convert(numbers[i], numbers[j]))
                break

            if numbers[j] + 1 == numbers[j + 1]:
                j += 1
            else:
                result.append(self.__convert(numbers[i], numbers[j]))
                j += 1
                i = j
        print(f"i={i}, j={j}")
        return result

    def __convert(self, a: int, b: int) -> str:
        if a != b:
            return f"{a}->{b}"
        else:
            return f"{a}"


if __name__ == "__main__":
    examples = [
        [0, 1, 2, 4, 5, 7],
        [0, 2, 3, 4, 6, 8, 9],
        [],
        [-1],
        [0],
    ]
    s = Solution()
    for e in examples:
        print(s.summaryRanges(e))
