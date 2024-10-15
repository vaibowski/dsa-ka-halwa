import heapq
from typing import List, Any


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> list[tuple[Any, Any]]:
        # when dealing with k smallest/biggest elements, there is always a scope to optimize space. look out for it
        heap = []
        for x, y in points:
            distance = -(x * x + y * y)
            if len(heap) == k:
                heapq.heappushpop(heap, (distance, x, y))
            else:
                heapq.heappush(heap, (distance, x, y))

        return [(x, y) for (dist, x, y) in heap]
