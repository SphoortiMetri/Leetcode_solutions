class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.inner = 0 
        self.outer = 0 
        
    def advance_to_next(self): 
        
        while self.outer < len(self.vec) and self.inner == len(self.vec[self.outer]): 
            self.outer += 1
            self.inner = 0 
        

    def next(self) -> int:
        self.advance_to_next()
        
        result = self.vec[self.outer][self.inner] 
        self.inner += 1
        return result 
        

    def hasNext(self) -> bool:
        self.advance_to_next()
        return self.outer < len(self.vec)
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()