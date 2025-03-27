def maxProfit(prices):
    # Initialize min_price to a very high number
    min_price = float('inf')
    # Initialize max_profit to 0
    max_profit = 0

    # Iterate through the list of prices
    for price in prices:
        # If we find a new minimum price, update min_price
        if price < min_price:
            min_price = price
        else:
            # Otherwise, calculate the profit from current price and min_price
            profit = price - min_price
            # Update max_profit if this profit is higher than what we've seen
            max_profit = max(max_profit, profit)

    return max_profit

"""
Time: O(n) – One pass through the array
Space: O(1) – Constant space
"""
