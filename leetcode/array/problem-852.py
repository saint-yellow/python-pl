from math import ceil
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return self.__method1(arr)

    def __method1(self, arr: List[int])-> int:
        left = 0
        right = len(arr) - 1

        while left < right:
            middle = (left + right) // 2
            if arr[middle-1] < arr[middle] > arr[middle+1]:
                return middle
            elif arr[middle-1] < arr[middle] < arr[middle+1]:
                left = middle + 1
            elif arr[middle-1] > arr[middle] > arr[middle+1]:
                right = middle - 1
        return -1
