class Node: 
    def __init__(self, val): 
        self.val = val 
        self.child = {} 
        self.end = False 
        

class Trie:

    def __init__(self):
        self.root = Node("#")
        

    def insert(self, word: str) -> None:
        pointer = self.root 
        
        for char in word: 
            if char not in pointer.child: 
                pointer.child[char] = Node(char) 
            pointer = pointer.child[char] 
        pointer.end = True 
        

    def search(self, word: str) -> bool:
        pointer = self.root 
        for char in word: 
            if char not in pointer.child: 
                return False 
            pointer = pointer.child[char] 
        if pointer.end == True: 
            return True 
        
        return False 
                
        

    def startsWith(self, prefix: str) -> bool:
        pointer = self.root 
        for char in prefix: 
            if char not in pointer.child: 
                return False 
            pointer = pointer.child[char] 
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)