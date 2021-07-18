from typing import List


class Solution:
    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        return self.__method1(numbers)

    def __method1(self, numbers):
        result = []
        length = len(numbers)
        numbers.sort()

        for i in range(length):
            if numbers[i] > 0:
                return result

            if i > 0 and numbers[i] == numbers[i - 1]:
                continue

            left = i + 1
            right = length - 1
            while left < right:
                if numbers[i] + numbers[left] + numbers[right] == 0:
                    result.append([numbers[i], numbers[left], numbers[right]])

                    while left < right and numbers[left] == numbers[left + 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif numbers[i] + numbers[left] + numbers[right] > 0:
                    right -= 1
                else:
                    left += 1

        return result
