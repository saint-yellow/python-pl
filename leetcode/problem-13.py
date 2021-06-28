class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': lambda t: t - 1 if t >= 5 else t + 1,
            'V': lambda t: t + 5,
            'X': lambda t: t - 10 if t >= 50 else t + 10,
            'L': lambda t: t + 50,
            'C': lambda t: t - 100 if t >= 500 else t + 100,
            'D': lambda t: t + 500,
            'M': lambda t: t + 1000
        }

        n = 0

        for i in s[::-1]:
            n = d[i](n)

        return n