from collections import deque
from typing import List


class Solution:
    # 1. push all treasures to a queue with a distance counter set to zero
    # 2. pop left elements from queue:
    # 3. if it is treasure: push its land neighbors to the queue
    # 4. if it is land: set distance using the distance element(2nd index): take min with previous set value
    # then push the land's neighbors as well
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(grid), len(grid[0])
        queue = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append([r, c, 0])

        while queue:
            x, y, d = queue.popleft()
            if grid[x][y] > 0:
                grid[x][y] = min(grid[x][y], d)
            for dir in directions:
                row, col = x + dir[0], y + dir[1]
                if row < 0 or row == m or col < 0 or col == n or grid[row][col] <= grid[x][y]:
                    continue
                else:
                    queue.append([row, col, d + 1])

        return
