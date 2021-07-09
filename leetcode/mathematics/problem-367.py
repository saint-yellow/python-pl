class Solution:
    def isPerfectSquare(self, number: int) -> bool:
        return self.__method2(number)

    def __method1(self, number: int) -> bool:
        if number < 2:
            return True

        left, right = 2, number//2
        while left <= right:
            middle = (left+right)//2
            square = middle*middle
            if number == square:
                return True
            elif number < square:
                right = middle-1
            else:
                left += 1
        return False

    def __method2(self, number: int) -> bool:
        if number < 2:
            return True

        x = number//2
        while x*x > number:
            x = (x+number//x)//2
        return x*x == number


if __name__ == '__main__':
    s = Solution()
    print(s.isPerfectSquare(16))
    print(s.isPerfectSquare(15))
