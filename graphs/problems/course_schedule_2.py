from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # the solution is very similar to course schedule-1
        # the only change is to store the neighbors(dependencies) of the nodes before storing the node itself
        # this will maintain the chronology needed to be followed
        graph = {course: [] for course in range(numCourses)}
        for course, dependency in prerequisites:
            graph[course].append(dependency)
        visited = [0] * numCourses

        result = []

        def dfs(course):
            if visited[course] == -1:
                return False
            if visited[course] == 1:
                return True

            visited[course] = -1
            for dependency in graph[course]:
                if not dfs(dependency):
                    return []

            visited[course] = 1
            result.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return result


