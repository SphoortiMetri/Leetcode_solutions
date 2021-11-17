from collections import defaultdict
class Solution:
    
    def __init__(self): 
        self.adjacency_list = defaultdict(list)
    
    def get_neighbors(self, wordList):     
        for word in wordList: 
            for i in range(len(word)): 
                key  = word[:i] + '*' + word[i+1:] 
                self.adjacency_list[key].append(word)
                
    def get_keys(self, word): 
        ret_list = []
        for i in range(len(word)): 
            ret_list.append(word[:i] + '*' + word[i+1:] )
            
        return ret_list
            
        
        
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.get_neighbors(wordList)
        
        if endWord not in wordList:
            return 0 
        
        queue = deque([(beginWord,1)]) 
        visited = set()
        
        while queue: 
            curr_word,level = queue.popleft()
            
            for key in self.get_keys(curr_word): 
                if key in self.adjacency_list: 
                    neighbors = self.adjacency_list[key] 
                    
                    for neighbor in neighbors: 
                        if neighbor in visited: 
                            continue 
                            
                        if neighbor == endWord:
                            return level + 1 
                        
                        queue.append((neighbor,level+1)) 
                        visited.add(neighbor)
                        
        return 0
            
            
            
        
        