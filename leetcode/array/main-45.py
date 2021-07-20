from typing import List


class Solution:
    def jump(self, numbers: List[int]) -> int:
        return self.__method1(numbers)

    # 基于贪心策略的解法
    def __method1(self, numbers: List[int]) -> int:
        count, final = 1, len(numbers) - 1
        if final == 0:
            return count if numbers[0] > 0 else 0
        cover = 0
        i = 0
        while i <= 0:
            cover = max(i + numbers[i], cover)
            if cover >= final:
                return count
            count += 1
            i += 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.jump([2, 3, 0, 1, 4]))
