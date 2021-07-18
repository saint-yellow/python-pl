class Solution:
    def judgeSquareSum(self, number: int) -> bool:
        return self.__method1(number)

    def __method1(self, number: int) -> bool:
        from math import sqrt

        left = 0
        right = int(sqrt(number))
        while left <= right:
            total = left * left + right * right
            if total == number:
                return True
            elif total < number:
                left += 1
            else:
                right -= 1
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.judgeSquareSum(1))
