
    

class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.next = None
            self.prev = None
            self.val = val
            self.key = key

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.length = capacity
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.tail.prev = self.head
        self.head.next = self.tail
    

    def addNode(self, node):
        temp = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        temp.next = node
        node.prev = temp
    
    def deleteNode(self, node):
        node.prev.next  = node.next
        node.next.prev = node.prev


    def get(self, key: int) -> int:
        #if the key exists return its value and update its position
        if key in self.hashmap:
            node = self.hashmap[key]
            value  = node.val
            self.deleteNode(node)
            self.addNode(node)
            return value
        else:
            return -1
        #if the key does not exists return -1

        

    def put(self, key: int, value: int) -> None:
        #fix the value of the key if it exists
        if key in self.hashmap:
            node = self.hashmap[key]
            self.deleteNode(node)
            node.val = value
            self.addNode(node)
        #if the key does not exists add it to the cache
        else:
            if len(self.hashmap) == self.length:
                nodeDeleted = self.head.next
                key_deleted = nodeDeleted.key
                self.deleteNode(nodeDeleted)
                del self.hashmap[key_deleted]
                newNode = self.Node(key,value)
                self.addNode(newNode)
                self.hashmap[key] = newNode
            else:
                node = self.Node(key, value)
                self.hashmap[key] = node
                self.addNode(node)
                
        

