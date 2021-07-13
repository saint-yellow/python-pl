# LeetCode Problem Nr. 905: 按奇偶排序数组

from typing import List


class Solution:
    def sortArrayByParity(self, numbers: List[int]) -> List[int]:
        return self.__method1(numbers)


    def __method1(self, numbers: List[int]) -> List[int]:
        # numbers.sort()
        left, right = 0, len(numbers)-1
        while left <= right:
            a, b = numbers[left]%2, numbers[right]%2
            if a == 1 and b == 0:
                numbers[left], numbers[right] = numbers[right], numbers[left]
                left += 1
                right -= 1
            elif a == 0 and b == 1:
                left += 1
                right -= 1
            elif a == 1 and b == 1:
                right -= 1
            else:
                left += 1

        return numbers


if __name__ == '__main__':
    numbers = [3,1,2,4]
    print(numbers)

    s = Solution()
    print(s.sortArrayByParity(numbers))
