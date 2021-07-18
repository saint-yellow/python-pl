from typing import List


class Solution:
    def findKthLargest(self, n: List[int], k: int) -> int:
        return self.__method1(n, k)

    def __quick_sort(self, numbers: List[int], left_pointer: int, right_pointer: int):
        if right_pointer - left_pointer <= 0:
            return
        pivot_pointer = self.__partition(numbers, left_pointer, right_pointer)
        self.__quick_sort(numbers, left_pointer, pivot_pointer - 1)
        self.__quick_sort(numbers, pivot_pointer + 1, right_pointer)

    def __partition(
        self, numbers: List[int], left_pointer: int, right_pointer: int
    ) -> int:
        pivot_pointer = right_pointer
        pivot_number = numbers[pivot_pointer]

        right_pointer -= 1

        while True:
            while numbers[left_pointer] < pivot_number:
                left_pointer += 1
            while numbers[right_pointer] > pivot_number:
                right_pointer -= 1

            if left_pointer >= right_pointer:
                break
            else:
                self.__swap(numbers, left_pointer, right_pointer)

        self.__swap(numbers, left_pointer, pivot_pointer)

        return left_pointer

    def __swap(self, numbers: List[int], pointer1: int, pointer2: int):
        numbers[pointer1], numbers[pointer2] = numbers[pointer2], numbers[pointer1]

    # 基于快速排序的选择方法
    def __method1(self, numbers: List[int], k: int) -> int:

        self.__quick_sort(numbers, 0, len(numbers) - 1)

        return numbers[k - 1]

    # 基于堆排序的选择方法
    def __method2(self, n: List[int], k: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3, 3, 3, 3, 3, 3, 3, 3, 3], 2))
