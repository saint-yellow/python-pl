class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return self.method1(s, k)

    def method1(self, s: str, k: int) -> str:

        from functools import reduce
        def reverse(s: list):
            left, right = 0, len(s)-1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            return s

        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:(i+k)] = reverse(s[i:(i+k)])

        return reduce(lambda a, b: a+b, s)

