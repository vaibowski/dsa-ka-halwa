from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    area = self.dfs(grid, row, col)
                    maxArea = max(maxArea, area)
                else:
                    continue

        return maxArea

    def dfs(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == 0:
            return 0

        grid[row][col] = 0
        return 1 + self.dfs(grid, row + 1, col) + self.dfs(grid, row, col + 1) + self.dfs(grid, row - 1,
                                                                                          col) + self.dfs(grid, row,
                                                                                                          col - 1)
