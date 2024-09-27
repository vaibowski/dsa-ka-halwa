from typing import List


class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        islands = 0
        # plan is to for every piece of land encountered, sink all attached land pieces by travelling using dfs
        # then on next iterations, we don't expect any attached land to be encountered
        # any new land found on subsequent iterations will belong to a new island
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    islands = islands + 1
                    self.dfs(grid, row, col)
        return islands

    def dfs(self, grid, row, col):
        # check boundary and base condtions
        if row >= len(grid) or row < 0 or col >= len(grid[row]) or col < 0 or grid[row][col] == '0':
            return

        # sink the island
        grid[row][col] = '0'

        # visit all four directions (down, right, up, left)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col - 1)
