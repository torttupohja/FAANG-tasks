from collections import defaultdict

def calcEquation(equations, values, queries):
    graph = defaultdict(dict)

    # Build the graph
    for (a, b), val in zip(equations, values):
        graph[a][b] = val
        graph[b][a] = 1 / val

    def dfs(curr, target, visited):
        if curr not in graph or target not in graph:
            return -1.0
        if curr == target:
            return 1.0
        visited.add(curr)

        for neighbor, weight in graph[curr].items():
            if neighbor not in visited:
                product = dfs(neighbor, target, visited)
                if product != -1.0:
                    return product * weight
        return -1.0

    results = []
    for c, d in queries:
        results.append(dfs(c, d, set()))
    return results

"""
Time Complexity:
Graph build: O(E) where E = number of equations
Each DFS: worst case O(N) where N = number of variables/nodes
For Q queries: O(Q * N)

Space Complexity: O(N + E)
N = number of variables (nodes)
E = number of connections (edges)
Plus recursion stack and visited set
"""
