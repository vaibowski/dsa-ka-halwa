from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    ans = []
    q = deque()

    # naive 2 pointer approach would run in O(n^2)
    # here we optimize the inner loop (used to find the max element in the subarray) to run in less time than O(n)
    # by maintaining a monotonic dequeue
    for i in range(len(nums)):
        while q and nums[q[-1]] <= nums[i]:
            q.pop()

        q.append(i)

        if q[0] <= i - k:
            q.popleft()

        if i < k - 1:
            continue

        ans.append(q[0])

    return ans


