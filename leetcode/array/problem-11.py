from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        return self.__method1(height)

    def __method1(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            new_area = min(height[left], height[right]) * (right - left)
            area = max(area, new_area)

        return area
