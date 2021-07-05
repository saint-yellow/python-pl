class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        pass


    def __method1(self, s: str, n: int) -> str:
        l = list(s)
        left = 0
        right = n - 1
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

        left = n
        right = len(s) - 1
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

        left = 0
        right = len(s) - 1
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

        return "".join(l)

    def __method2(self, s: str, n: int) -> str:
        return s[n:] + s[:n]
