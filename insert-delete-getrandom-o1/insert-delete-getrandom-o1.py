class RandomizedSet:

    def __init__(self):
        
        self.array = [] 
        self.hash_map = {}
        

    def insert(self, val: int) -> bool:
        if val in self.hash_map: 
            return False 
        
        self.array.append(val) 
        self.hash_map[val] = len(self.array) -1 
        return True 
        

    def remove(self, val: int) -> bool:
        if val in self.hash_map: 
            idx = self.hash_map[val]
            last_element = self.array[-1]
            self.hash_map[last_element] = idx
            self.array[idx] = self.array[len(self.array)-1]
            self.array.pop() 
            del self.hash_map[val]
            return True 
        
        return False 
        
    
    def getRandom(self) -> int:
        return random.choice(list(self.array))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()