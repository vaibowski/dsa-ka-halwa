from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph
        graph = [[] for _ in range(numCourses)]
        for course, dependency in prerequisites:
            graph[course].append(dependency)

        # visited to store 3 states: 0 if the node hasn't been visited
        # -1 if the node or its neighbors are being visited
        # 1 if the node and all neighbors have been visited and no cycle was detected
        visited = [0] * numCourses

        # dfs to return immediately with false if cycle is detected i.e visited is -1
        def dfs(course):
            if visited[course] == 1:
                return True
            if visited[course] == -1:
                return False

            # set the state to -1 while the node's neighbors are being visited
            visited[course] = -1
            for dependency in graph[course]:
                if not dfs(dependency):
                    return False
            # since no cycle was detected for neighbors, this node is fine as well
            visited[course] = 1
            return True

        # iteratively do dfs for all nodes
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
