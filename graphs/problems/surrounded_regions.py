from typing import List


class Solution:
    # trick is 1. set all 'O's to 'S's
    # 2. start from the border cells that are Ss and start dfs traversal
    # 3. set all the reachable cells as Os, because they are not surrounded
    # 4. at the end, set all the remaining Ss as Xs
    def solve(self, board: List[List[str]]) -> None:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        m, n = len(board), len(board[0])

        for x in range(m):
            for y in range(n):
                if board[x][y] == 'O':
                    board[x][y] = 'S'

        def dfs(x, y):
            board[x][y] = 'O'
            for d in directions:
                row, col = x + d[0], y + d[1]
                if row < 0 or row == m or col < 0 or col == n:
                    continue
                if board[row][col] == 'S':
                    dfs(row, col)

        for x in range(m):
            if board[x][0] == 'S':
                dfs(x, 0)
            if board[x][n - 1] == 'S':
                dfs(x, n - 1)

        for y in range(n):
            if board[0][y] == 'S':
                dfs(0, y)
            if board[m - 1][y] == 'S':
                dfs(m - 1, y)

        for x in range(m):
            for y in range(n):
                if board[x][y] == 'S':
                    board[x][y] = 'X'

        return
