from typing import List


# trick is to think in terms of prefix and suffix product for every element
def productExceptSelf(nums: List[int]) -> List[int]:
    ans = [1] * len(nums)
    cur = 1

    for i in range(len(nums)):
        ans[i] *= cur
        cur *= nums[i]

    cur = 1
    for i in reversed(range(len(nums))):
        ans[i] *= cur
        cur *= nums[i]
    return ans
