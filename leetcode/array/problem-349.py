from typing import List


class Solution:
    def intersection(self, numbers1: List[int], numbers2: List[int]) -> List[int]:
        return self.__method1(numbers1, numbers2)


    def __method1(self, numbers1: List[int], numbers2: List[int]) -> List[int]:
        result: List[int] = []
        if not (numbers1 and numbers2):
            return result

        numbers1.sort()
        numbers2.sort()
        i, j = 0, 0
        length1, length2 = len(numbers1), len(numbers2)
        while i < length1 and j < length2:
            if numbers1[i] == numbers2[j] and numbers1[i] not in result:
                result.append(numbers1[i])
                i += 1
                j += 1
            elif numbers1[i] < numbers2[j]:
                i += 1
            else:
                j += 1
        return result


    def __method2(self, numbers1: List[int], numbers2: List[int]) -> List[int]:
        pass


if __name__ == '__main__':
    s = Solution()
    print(s.intersection([1, 2, 2, 1], [2, 2]))
    print(s.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
