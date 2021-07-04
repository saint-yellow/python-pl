# LeetCode Problem Nr. 88: 合并两个有序数组

from typing import List


class Solution:
    def merge(self, numbers1: List[int], m: int, numbers2: List[int], n: int) -> None:
        """
        Do not return anything, modify numbers1 in-place instead.
        """

        # 或者：
        # for i in range(-1, -(n+1), -1):
        #     numbers1[i] = numbers2[i]

        self.method2(numbers1, m, numbers2, n)


    # 基于排序的解法
    def method1(self, numbers1: List[int], m: int, numbers2: List[int], n: int) -> None:
        # 或者：
        # for i in range(-1, -(n+1), -1):
        #     numbers1[i] = numbers2[i]

        numbers1[m:] = numbers2
        numbers1.sort()

    # 基于正向双指针的比较冗长的解法
    def method2(self, numbers1: List[int], m: int, numbers2: List[int], n: int) -> None:
        pointer1, pointer2 = 0, 0
        numbers3 = []
        while pointer1 < m and pointer2 < n:
            if numbers1[pointer1] < numbers2[pointer2]:
                numbers3.append(numbers1[pointer1])
                pointer1 += 1
            elif numbers1[pointer1] > numbers2[pointer2]:
                numbers3.append(numbers2[pointer2])
                pointer2 += 1
            else:
                numbers3.append(numbers1[pointer1])
                pointer1 += 1
                numbers3.append(numbers2[pointer2])
                pointer2 += 1
        if pointer1 < m:
            numbers3.extend(numbers1[pointer1:m])
        if pointer2 < n:
            numbers3.extend(numbers2[pointer2:n])        
        numbers1[:] = numbers3

    # 基于正向双指针的比较简洁的解法
    def method3(self, numbers1: List[int], m: int, numbers2: List[int], n: int) -> None:
        pointer1, pointer2 = 0, 0
        numbers3 = []
        while pointer1 < m or pointer2 < n:
            if pointer1 == m:
                numbers3.append(numbers2[pointer2])
                pointer2 += 1
            elif pointer2 == n:
                numbers3.append(numbers1[pointer1])
                pointer1 += 1
            elif numbers1[pointer1] < numbers2[pointer2]:
                # 选择较小者填充
                numbers3.append(numbers1[pointer1])
                pointer1 += 1
            else:
                numbers3.append(numbers2[pointer2])
                pointer2 += 1
        numbers1[:] = numbers3

    # 基于逆向双指针的解法
    def method4(self, numbers1: List[int], m: int, numbers2: List[int], n: int) -> None:
        pointer1, pointer2 = m-1, n-1
        tail = m+n-1
        while pointer1 >= 0 or pointer2 >= 0:
            if pointer1 == -1:
                numbers1[tail] = numbers2[pointer2]
                pointer2 -= 1
            elif pointer2 == -1:
                numbers1[tail] = numbers1[pointer1]
                pointer1 -= 1
            elif numbers1[pointer1] < numbers2[pointer2]:
                # 选择较大者填充
                numbers1[tail] = numbers1[pointer1]
                pointer1 -= 1
            else:
                numbers1[tail] = numbers2[pointer2]
                pointer2 -= 1
            tail -= 1
            