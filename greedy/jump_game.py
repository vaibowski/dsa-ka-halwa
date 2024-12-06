from typing import List


def canJump(nums: List[int]) -> bool:
    gas = 0

    for n in nums:
        if gas < 0:
            return False
        if n > gas:
            gas = n
        gas -= 1

    return True
