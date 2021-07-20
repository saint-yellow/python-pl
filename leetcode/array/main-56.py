# LeetCode Problem Nr. 56: 合并区间

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return self.__method1(intervals)

    def __method1(self, intervals: List[List[int]]) -> List[List[int]]:
        result: List[List[int]] = []
        if not intervals:
            return result
        intervals.sort(key=lambda x: x[0])
        result.append(intervals[0])
        for interval in intervals[1:]:
            merged_interval = result[-1]
            new_interval = self.__simpleMerge(merged_interval, interval)
            if not new_interval:
                result.append(interval)
            else:
                result[-1] = new_interval
        return result

    def __simpleMerge(self, interval1: List[int], interval2: List[int]) -> List[int]:
        a, b = interval1
        c, d = interval2
        if a <= b < c <= d:
            return []
        elif a <= c <= b <= d:
            return [a, d]
        else:
            return [a, b]


if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1, 3], [0, 6]]))
