def canFinish(numCourses, prerequisites):
    from collections import defaultdict

    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[b].append(a)

    visited = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited

    def dfs(course):
        if visited[course] == 1:
            return False  # cycle detected
        if visited[course] == 2:
            return True   # already checked

        visited[course] = 1  # mark as visiting

        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False

        visited[course] = 2  # mark as visited
        return True

    for c in range(numCourses):
        if not dfs(c):
            return False

    return True

"""
Time Complexity: O(V + E)
V = number of courses, E = number of prerequisite pairs

Space Complexity: O(V + E)
For the graph and the visited list
DFS stack depth up to O(V) in worst case
"""
