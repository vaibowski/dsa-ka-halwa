import heapq
from collections import Counter
from random import random
from typing import List


def topKFrequentEasy(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    k_frequent = count.most_common(k)
    ans = []
    for ele, count in k_frequent:
        ans.append(ele)

    return ans


def topKFrequentSpaceOptimized(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    ans = []
    for ele, freq in count.items():
        if len(ans) == k:
            heapq.heappushpop(ans, (freq, ele))
        else:
            heapq.heappush(ans, (freq, ele))

    return [ele for _, ele in ans]


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    unique = list(count.keys())

    def partition(left, right, pivot_index) -> int:
        pivot_frequency = count[unique[pivot_index]]
        # 1. Move the pivot to end
        unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

        # 2. Move all less frequent elements to the left
        store_index = left
        for i in range(left, right):
            if count[unique[i]] < pivot_frequency:
                unique[store_index], unique[i] = unique[i], unique[store_index]
                store_index += 1

        # 3. Move the pivot to its final place
        unique[right], unique[store_index] = unique[store_index], unique[right]

        return store_index

    def quickselect(left, right, k_smallest) -> None:
        """
        Sort a list within left..right till kth less frequent element
        takes its place.
        """
        # base case: the list contains only one element
        if left == right:
            return

        # Select a random pivot_index
        pivot_index = random.randint(left, right)

        # Find the pivot position in a sorted list
        pivot_index = partition(left, right, pivot_index)

        # If the pivot is in its final sorted position
        if k_smallest == pivot_index:
            return
            # go left
        elif k_smallest < pivot_index:
            quickselect(left, pivot_index - 1, k_smallest)
        # go right
        else:
            quickselect(pivot_index + 1, right, k_smallest)

    n = len(unique)
    # kth top frequent element is (n - k)th less frequent.
    # Do a partial sort: from less frequent to the most frequent, till
    # (n - k)th less frequent element takes its place (n - k) in a sorted array.
    # All elements on the left are less frequent.
    # All the elements on the right are more frequent.
    quickselect(0, n - 1, n - k)
    # Return top k frequent elements
    return unique[n - k:]
