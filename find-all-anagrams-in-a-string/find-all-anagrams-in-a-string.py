from collections import Counter 

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = [] 
        ns, np = len(s), len(p)
        
        if ns < np: 
            return [] 
        
        dict_p = Counter(p)
        dict_s = Counter()
                
        for i in range(ns): 
            
            dict_s[s[i]] += 1 
            
            if i >= np: 
                if dict_s[s[i-np]] == 1: 
                    del dict_s[s[i-np]]
                    
                else: 
                    dict_s[s[i-np]] -= 1 
                    
            if dict_s == dict_p: 
                result.append(i-np+1)

        return result
    
    """
            def is_anagram(s,p): 
    
            dict_s = Counter(s) 
            dict_p = Counter(p) 

            if len(dict_s) == len(dict_p): 

                for ch in dict_s.keys(): 
                    if dict_p[ch] != dict_s[ch]: 
                        return False 

                return True
    """