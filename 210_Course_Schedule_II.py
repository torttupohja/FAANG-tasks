from collections import defaultdict, deque

def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    # Build the graph and in-degree array
    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1

    # Initialize queue with courses having no prerequisites
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)

        for neighbor in graph[course]:
            in_degree[neighbor] -= 1  # Remove edge
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If we could schedule all courses, return the order
    if len(order) == numCourses:
        return order
    else:
        return []  # Cycle detected

"""
Time Complexity: O(V + E)
V = number of courses, E = number of prerequisites

Space Complexity: O(V + E)
Graph + in-degree array + queue
"""
