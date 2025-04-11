def candy(ratings):
    n = len(ratings)
    
    # Step 1: Give each child 1 candy to start with
    candies = [1] * n

    # Step 2: Left to right pass
    # If a child has a higher rating than the left neighbor,
    # they get one more candy than them
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Step 3: Right to left pass
    # If a child has a higher rating than the right neighbor,
    # and doesn't already have more candies,
    # update their candy count
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    # Step 4: Return total number of candies
    return sum(candies)

"""
Time: O(n) – Two passes through the list
Space: O(n) – For the candies list
"""
