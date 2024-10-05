from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        visited = [0] * n

        def dfs(node, prev):
            if visited[node] == 1:
                return True
            if visited[node] == -1:
                return False

            visited[node] = -1
            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                else:
                    if not dfs(neighbor, node):
                        return False

            visited[node] = 1
            return True

        noCycles = dfs(0, -1)

        print(visited)
        if not noCycles or 0 in visited:
            return False

        return True

