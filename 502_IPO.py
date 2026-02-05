import heapq

def find_maximized_capital(k, w, profits, capital):
    projects = sorted(zip(capital, profits))
    i = 0
    max_heap = []
    for _ in range(k):
        while i < len(projects) and projects[i][0] <= w:
            heapq.heappush(max_heap, -projects[i][1])
            i += 1
        if not max_heap:
            break
        w += -heapq.heappop(max_heap)
    return w

"""
Time complexity: O(n log n + k log n)
Space complexity: O(n)
"""
