class Solution:
    def intToRoman(self, number: int) -> int:
        return self.__method1(number)

    def __method1(self, number: int) -> str:
        mapping = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
        ]
        roman = []
        for s, n in mapping:
            while number >= n:
                number -= n
                roman.append(s)
            if number == 0:
                break
        return "".join(roman)
