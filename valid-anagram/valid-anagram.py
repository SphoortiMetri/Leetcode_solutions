from collections import Counter 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): 
            return False 
        
        dict_s = Counter(s) 
        dict_t = Counter(t) 
        
        for key in dict_t: 
            if dict_s[key] != dict_t[key]: 
                return False 
            
            
        return True
        
        
        
        
            
            
            
            
        