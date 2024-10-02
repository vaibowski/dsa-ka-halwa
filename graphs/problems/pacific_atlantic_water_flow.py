from typing import List


class Solution:
    def __init__(self):
        self.directions = None

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights:
            return[]

        # the trick is to make the direction traversal concise by using for loop
        # and to start dfs from the edges exposed to the either oceans, and store all
        # reachable coordinates per ocean in a set and in the end, return the intersection of the 2 sets
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(heights)
        cols = len(heights[0])

        p_drain = set()
        a_drain = set()

        for i in range(rows):
            self.dfs(heights, i, 0, p_drain, rows, cols)
            self.dfs(heights, i, cols-1, a_drain, rows, cols)
        for j in range(cols):
            self.dfs(heights, 0, j, p_drain, rows, cols)
            self.dfs(heights, rows-1, j, a_drain, rows, cols)

        return list(p_drain & a_drain)

    def dfs(self, heights, row, col, visited, rows, cols):
        visited.add((row, col))
        for direction in self.directions:
            x, y = row + direction[0], col + direction[1]
            if x < 0 or x >= rows or y < 0 or y >= cols or (x,y) in visited or heights[x][y] < heights[row][col]:
                continue
            self.dfs(heights, x, y, visited, rows, cols)