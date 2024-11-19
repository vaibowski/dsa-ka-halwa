from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    snums = sorted(nums)  # Sort the input array
    ans = set()

    for i in range(len(snums) - 2):
        # Skip duplicates for the current index
        if i > 0 and snums[i] == snums[i - 1]:
            continue

        left, right = i + 1, len(snums) - 1

        while left < right:
            current_sum = snums[i] + snums[left] + snums[right]

            if current_sum == 0:
                ans.add((snums[i], snums[left], snums[right]))
                left += 1
                right -= 1

                # Skip duplicates for left and right
                while left < right and snums[left] == snums[left - 1]:
                    left += 1
                while left < right and snums[right] == snums[right + 1]:
                    right -= 1

            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    # Convert set of tuples to list of lists
    return [list(triplet) for triplet in ans]
