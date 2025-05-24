class Node:
    def __init__(self, key, val):
        self.key = key        # Needed to delete from dict when evicting
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key → Node

        # Dummy head and tail to avoid empty checks
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # Internal helper: remove a node from the linked list
    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # Internal helper: insert node right after head (most recently used)
    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)         # Remove from current position
            self._add_to_front(node)   # Move to front (most recently used)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move to front
            self._remove(self.cache[key])
        
        # Add new node to front
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_front(new_node)

        # Evict least recently used if over capacity
        if len(self.cache) > self.capacity:
            # Node to remove is before tail (least recently used)
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

"""
Time:
get() → O(1)
put() → O(1)

Space: O(capacity) — for storing up to capacity nodes in the dict and list
"""
