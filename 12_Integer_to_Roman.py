def intToRoman(num):
    # Step 1: Create a list of tuples with (value, symbol) from largest to smallest
    val_to_roman = [
        (1000, "M"),
        (900,  "CM"),
        (500,  "D"),
        (400,  "CD"),
        (100,  "C"),
        (90,   "XC"),
        (50,   "L"),
        (40,   "XL"),
        (10,   "X"),
        (9,    "IX"),
        (5,    "V"),
        (4,    "IV"),
        (1,    "I"),
    ]

    result = ""  # Final Roman numeral string

    # Step 2: Loop through the values from largest to smallest
    for value, symbol in val_to_roman:
        # Count how many times current symbol fits into num
        count = num // value
        if count:
            result += symbol * count  # Append the symbol 'count' times
            num -= value * count      # Subtract the value from num

        # Optional: early exit if num is reduced to 0
        if num == 0:
            break

    return result

"""
Time: O(1) – Max 13 symbol-value pairs, constant number of operations
Space: O(1) – Fixed output string (bounded by Roman numeral rules)
"""
