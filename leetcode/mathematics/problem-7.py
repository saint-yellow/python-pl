from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        if -2**31 > x or x > 2**31-1:
            return 0

        sign = 1 if x >= 0 else -1
        numbers = self.__decompose(abs(x))
        length = len(numbers)
        result = 0
        for i in range(length):
            result += numbers[i] * (10**(length-1-i)) * (10**(-i))

        if result > 2**31-1:
            return 0
        
        return sign * int(result)


    def __decompose(self, x: int) -> List[int]:
        '''
        123 -> [3, 20, 100]\n
        -123 -> [-3, -20, -100]
        '''
        c = 0
        n = 1
        l = []
        while c != x:
            e = x % (10**n) - c
            l.append(e)
            c += e
            n += 1
        return l

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123456789))
