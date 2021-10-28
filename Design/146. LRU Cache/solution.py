

class LRUCache:
    
    class DLL:

        def __init__(self,key,val): 
            self.key = key 
            self.val = val 
            self.next = None 
            self.prev = None

    def __init__(self, capacity: int):
        self.m = {} 
        self.size = 0
        self.capacity = capacity 
        self.head = self.DLL(0,0) 
        self.tail = self.DLL(0,0) 
        self.tail.prev = self.head 
        self.head.next = self.tail 
    
    def remove_node(self, node): 
        _prev = node.prev
        _next = node.next 
        _prev.next = node.next
        _next.prev = node.prev 
        return 

    def get(self, key: int) -> int:
        #put(3)
        
        #Head -> 4
        
        # 2->3 -> 5
        
        if key in self.m: 
            # Promote to the front 
            node = self.m[key] 
            self.remove_node(node) 
            self.head.next.prev = node 
            node.next = self.head.next 
            self.head.next = node 
            node.prev = self.head 
            return node.val
        
        else: 
            return -1
            
        

    def put(self, key: int, value: int) -> None:
        if key in self.m: 
            self.get(key) 
            self.m[key].val = value 
            return 

        
        
        self.size += 1 
        if self.size > self.capacity: 
            #remove the node lru 
            lru = self.tail.prev 
            del self.m[lru.key]
            self.remove_node(lru) 
            self.size -= 1 
            
        new_head = self.DLL(key, value) 
        self.head.next.prev = new_head 
        new_head.next = self.head.next 
        self.head.next = new_head 
        new_head.prev = self.head 
        self.m[key] = new_head
        
           
