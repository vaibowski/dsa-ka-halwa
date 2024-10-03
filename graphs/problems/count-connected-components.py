from typing import List


class Solution:
    # same logic to be applied as redundant connection: union find
    # trick is to count the nodes which are a parent to themselves at the end
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            p = par[node]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return

            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return

        for n1, n2 in edges:
            union(n1, n2)

        count = 0
        for i in range(n):
            if i == par[i]:
                count += 1

        return count
