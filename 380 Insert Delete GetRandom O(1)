import random

class RandomizedSet:
    def __init__(self):
        # List to store elements
        self.nums = []
        # Dictionary to map element -> index in the list
        self.val_to_index = {}

    def insert(self, val):
        # If val already exists, return False
        if val in self.val_to_index:
            return False

        # Otherwise, add val to the end of the list
        self.nums.append(val)
        # Save its index in the dictionary
        self.val_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        # If val doesn't exist, return False
        if val not in self.val_to_index:
            return False

        # Get index of the element to remove
        index = self.val_to_index[val]
        # Get the last element in the list
        last_element = self.nums[-1]

        # Swap the element to remove with the last element
        self.nums[index] = last_element
        self.val_to_index[last_element] = index

        # Remove the last element from the list
        self.nums.pop()
        # Delete val from the dictionary
        del self.val_to_index[val]
        return True

    def getRandom(self):
        # Return a random element from the list
        return random.choice(self.nums)
