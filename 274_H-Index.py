def hIndex(citations):
    # Step 1: Sort citations in descending order
    citations.sort(reverse=True)

    # Step 2: Initialize h-index
    h = 0

    # Step 3: Iterate through sorted citations
    for i, citation in enumerate(citations):
        # If the citation count is at least the paper count so far (i+1),
        # then update h-index to i+1
        if citation >= i + 1:
            h = i + 1
        else:
            break  # No need to check further if this condition fails

    return h
"""
Time: O(n log n) due to sorting
Space: O(1) (in-place sort, no extra space used)
"""
