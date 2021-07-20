class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return self.__method1(J, S)

    def __method1(self, J: str, S: str) -> int:
        count = 0
        for s in S:
            if s in J:
                count += 1
        return count

    def __method2(self, J: str, S: str) -> int:
        j = set(J)
        return sum(s in j for s in S)
