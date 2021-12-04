class Solution:
    def __init__(self): 
        self.res = []
        
    def partition(self, s: str) -> List[List[str]]:
        

        def dfs(sI, path): 
            if sI >= len(s): 
                self.res.append(path) 
                
            for l in range(len(s)-sI): 
                if is_palindrome(sI, sI+l): 
                    dfs(sI+l+1, path+[s[sI:sI+l+1]])
        
        
        def is_palindrome(sI, eI): 
            
            while sI < eI: 
                if s[sI] != s[eI]: 
                    return False 
                
                sI += 1 
                eI -= 1
                
            return True 
        
        dfs(0,[])
        return self.res
        
        
            
        