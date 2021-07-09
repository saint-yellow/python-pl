from typing import List


class Solution:
    def containsNearbyDuplicate(self, numbers: List[int], k: int) -> bool:
        return self.__method1(numbers, k)

    def __method1(self, numbers: List[int], k: int) -> bool:
        n = len(numbers)

        if not numbers or n < 2:
            return False

        d = {}
        for i, v in enumerate(numbers):
            if v not in d:
                d[v] = i
            else:
                if abs(d[v]-i) <= k:
                    return True
                else:
                    d[v] = i
        return False



if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(s.containsNearbyDuplicate([1, 0, 1, 1], 1))
    print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))
