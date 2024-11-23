from typing import List


def longestConsecutive(nums: List[int]) -> int:
    nums = set(nums)
    best = 0

    # since we have to solve this question in O(n) we can ony pass through the array once
    # that should be hint enough that either a hashmap or a set will be involved

    # trick is to create a set of all elements in the array and iterate through each
    # for each element, check if it is the start of a streak: x - 1 doesn't exist in the set
    # then while consecutive numbers exist for x, keep moving forward and at the end, update the best
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)

    return best
