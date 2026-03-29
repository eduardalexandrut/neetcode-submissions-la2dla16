class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.Map = {}
        self.left, self.right = Node(0, 0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    #To insert at the beginnig of a list
    def insert(self, node):
       prev, nxt = self.right.prev, self.right
       prev.next = node
       nxt.prev = node
       node.next = nxt
       node.prev = prev

    def get(self, key: int) -> int:
        if key in self.Map:
            self.remove(self.Map[key])
            self.insert(self.Map[key])
            return self.Map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.Map:
          self.remove(self.Map[key])
        self.Map[key] = Node(key, value)
        self.insert(self.Map[key])

        if len(self.Map) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.Map[lru.key]
        
