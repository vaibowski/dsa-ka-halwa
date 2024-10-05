from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(grid), len(grid[0])
        queue = deque()

        fresh_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append([r, c, 0])  # Rotten oranges, time is 0 initially
                elif grid[r][c] == 1:
                    fresh_count += 1  # Count fresh oranges

        # If there are no fresh oranges, return 0 (no rotting needed)
        if fresh_count == 0:
            return 0

        # BFS to spread the rotting process
        mintime = 0
        while queue:
            row, col, time = queue.popleft()
            for dir in directions:
                x, y = row + dir[0], col + dir[1]
                if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
                    continue
                # Rot this fresh orange and add it to the queue
                grid[x][y] = 2
                queue.append([x, y, time + 1])
                fresh_count -= 1
                mintime = max(mintime, time + 1)

        if fresh_count != 0:
            return -1

        return mintime
