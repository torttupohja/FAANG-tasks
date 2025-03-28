def maxProfit(prices):
    # Initialize total profit to 0
    profit = 0

    # Loop through prices from the second day onwards
    for i in range(1, len(prices)):
        # If today's price is higher than yesterday's, we could have bought yesterday and sold today
        if prices[i] > prices[i - 1]:
            # Add the profit from this transaction
            profit += prices[i] - prices[i - 1]

    # Return total accumulated profit
    return profit

"""
Time: O(n) – One pass through the array
Space: O(1) – Constant space used
"""
