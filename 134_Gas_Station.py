def canCompleteCircuit(gas, cost):
    total_gas = 0      # Total net gas available across all stations
    current_gas = 0    # Current gas in the tank during the trip
    start_index = 0    # Candidate starting station

    # Loop through each station
    for i in range(len(gas)):
        # Net gas at station i
        gain = gas[i] - cost[i]
        total_gas += gain      # Update total gas
        current_gas += gain    # Update current trip gas

        # If current_gas drops below 0, we can't reach station i + 1
        if current_gas < 0:
            # So we reset the journey to the next station
            start_index = i + 1
            current_gas = 0    # Reset gas in tank for new start

    # If total_gas is negative, the trip is impossible
    return start_index if total_gas >= 0 else -1

"""
Time: O(n) – One pass through the arrays
Space: O(1) – No extra space
"""
