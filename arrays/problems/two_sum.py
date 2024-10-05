from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            if (target - nums[i]) in cache:
                return [cache[target - nums[i]], i]
            cache[nums[i]] = i