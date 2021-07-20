class Solution:
    def mySqrt(self, x: int) -> int:
        s = x

        def sqrt(x):
            r = (x + s / x) / 2
            print(f"x={x} x*x={x*x}; r={r}, r*r={r*r}")
            if r == x:
                return x
            else:
                return sqrt(r)

        if x == 0:
            return x
        else:
            return int(sqrt(x))


if __name__ == "__main__":
    s = Solution()
    s.mySqrt(8)
