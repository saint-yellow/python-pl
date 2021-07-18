# LeetCode Problem Nr. 350: 两个数组的交集II

from typing import List


class Solution:
    def intersect(self, numbers1: List[int], numbers2: List[int]) -> List[int]:
        return self.__method1(numbers1, numbers2)

    # 基于排序和双指针的解法
    def __method1(self, numbers1: List[int], numbers2: List[int]) -> List[int]:
        if not (numbers1 and numbers2):
            return []

        numbers1.sort()
        numbers2.sort()

        length1, length2 = len(numbers1), len(numbers2)
        pointer1, pointer2 = 0, 0
        result = []
        while pointer1 < length1 and pointer2 < length2:
            if numbers1[pointer1] < numbers2[pointer2]:
                pointer1 += 1
            elif numbers1[pointer1] > numbers2[pointer2]:
                pointer2 += 1
            else:
                result.append(numbers1[pointer1])
                pointer1 += 1
                pointer2 += 1
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.intersect([1, 2, 2, 1], [2, 2]))
