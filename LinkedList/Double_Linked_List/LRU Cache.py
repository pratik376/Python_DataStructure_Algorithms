class Node:

    def __init__(self, key , val):

        self.key ,self.val =key, val

        self.next = self.pre = None

class LRUCache:

    def __init__(self, capacity: int):

        self.cap=capacity
        self.cache= {}

        self.left, self.right= Node(0,0), Node(0,0)

        self.left.next= self.right
        self.right.pre=self.left
        
    # remove from the list
    def remove(self, node):
        prev, next= node.pre, node.next

        prev.next= next
        next.pre= prev

    # we gonna add at right
    def insert(self, node):  
        prev, next= self.right.pre, self.right

        prev.next = next.pre= node
        node.next, node.pre = next, prev

    def get(self, key: int) -> int:

        if key in self.cache:

            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1
    
    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key]= None(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru= self.left.next
            self.remove(lru)
            del self.cache[lru.key]    
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)