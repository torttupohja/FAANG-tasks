from collections import deque

def minMutation(startGene, endGene, bank):
    bank_set = set(bank)
    if endGene not in bank_set:
        return -1

    queue = deque([(startGene, 0)])  # (current_gene, mutation_count)
    possible_chars = ['A', 'C', 'G', 'T']
    visited = set([startGene])

    while queue:
        gene, steps = queue.popleft()
        if gene == endGene:
            return steps

        for i in range(len(gene)):
            for char in possible_chars:
                if char == gene[i]:
                    continue
                mutated = gene[:i] + char + gene[i+1:]
                if mutated in bank_set and mutated not in visited:
                    visited.add(mutated)
                    queue.append((mutated, steps + 1))

    return -1  # No path found

"""
Time Complexity: O(N * L * 4)
N = number of genes in the bank
L = length of each gene (8)
We try 3 mutations per position (4 options − 1 current letter)

Space Complexity: O(N)
For visited set and queue
"""
