from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    def dfs(x, y, w):
        if len(w) == 0:
            return True

        # check for edge conditions and only proceed further if cell matches the first character of the word substring
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or w[0] != board[x][y]:
            return False

        board[x][y] = "#"  # set cell so that we don't visit it again in this track
        res = dfs(x + 1, y, w[1:]) or dfs(x, y + 1, w[1:]) or dfs(x - 1, y, w[1:]) or dfs(x, y - 1, w[1:])
        board[x][y] = w[0]  # unset cell

        return res

    if not board:
        return False

    # dfs from every cell on the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, word):
                return True

    return False
