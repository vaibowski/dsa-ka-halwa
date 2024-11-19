from typing import List


def maxArea(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    all_max = 0
    while left < right:
        water = min(height[left], height[right]) * (right - left)
        all_max = max(all_max, water)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return all_max
