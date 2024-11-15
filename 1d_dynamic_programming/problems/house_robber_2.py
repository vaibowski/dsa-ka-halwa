from typing import List


def rob(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    dp0 = [*nums]
    dp1 = [*nums]

    dp0[1] = dp0[0]
    dp1[0] = 0
    for i in range(2, len(nums) - 1):
        dp0[i] = max(dp0[i - 1], dp0[i - 2] + dp0[i])

    for i in range(2, len(nums)):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + dp1[i])

    return max(dp0[-2], dp1[-1])


# constant space solution
def robOptimized(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    dp0 = nums[:-1]
    dp1 = nums[1:]

    def robHelper(dp):
        prev, cur = 0, 0
        for loot in dp:
            temp = prev
            prev = cur
            cur = max(prev, temp + loot)

        return cur

    return max(robHelper(dp0), robHelper(dp1))
