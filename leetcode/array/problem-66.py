from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return self.__method1(digits)

    def __method1(self, digits: List[int]) -> List[int]:
        length = len(digits)
        for i in range(length-1, -1, -1):
            digits[i] += 1
            digits[i] = digits[i] % 10
            if digits[i] != 0:
                return digits

        # 或者: digits.insert(0, 1)
        digits = [1] + digits

        return digits
