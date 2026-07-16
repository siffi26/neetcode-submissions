class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # Maps key -> node
        self.cache = {}

        # Dummy nodes
        self.left = Node()
        self.right = Node()

        # Connect dummy nodes
        self.left.next = self.right
        self.right.prev = self.left

    # Helper function 1
    def remove(self, node):
        # Remove from its current position
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # Helper function 2
    def insert(self, node):
        # Insert node at most recently used location (before right)
        previous_mru = self.right.prev

        # Update the previous MRU node
        previous_mru.next = node
        node.prev = previous_mru

        # Update the dummy right node
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # If it is present, get the node
        node = self.cache[key]

        # Move accessed node to MRU position
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        # Create a new node
        node = Node(key, value)

        # Store it in dictionary
        self.cache[key] = node

        # Add it as most recently used
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)