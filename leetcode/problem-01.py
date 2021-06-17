class Solution:
    def twoSum(self, nums: list, target: int):
        n = len(nums)
        d = {}
        for i in range(n):
            a = target - nums[i]
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[a] = i