class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # Initialize the dummy head and tail nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_tail(self, node):
        # Remove the node from its current position only if it's already in the list
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

        # Move the node to the tail
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_tail(node)
            return node.v
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move the node to the tail
            node = self.cache[key]
            node.v = value
            self.move_to_tail(node)
        else:
            # Insert a new node
            node = Node(key, value)
            self.cache[key] = node
            self.move_to_tail(node)

            # Check if we exceed the capacity
            if len(self.cache) > self.capacity:
                # Remove the least recently used node, which is the node right after head
                lru = self.head.next
                self.head.next = lru.next
                lru.next.prev = self.head
                del self.cache[lru.k]
