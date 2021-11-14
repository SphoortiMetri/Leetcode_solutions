from collections import Counter
class Solution(object):
    
    #Sliding window 
    
    """
    'ABAACBAB', t = 'ABC'
       |   | 
     
    """
                
        
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        #error handling 
        if t is None or s is None: 
            return "" 
        
        dict_t = Counter(t)
        dict_s= {} 
        window_counts = {} 
        required = len(dict_t)
        
        formed = 0 
        ans = float('inf'),None, None 
        
        l,r = 0,0
        
        while r < len(s): 
            
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            
            while l <= r and formed == required:
                character = s[l]
                
                if r - l + 1 < ans[0]: 
                    ans = r-l+1, l, r
        
                
                window_counts[character] -= 1 
                
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                l += 1         
             
            
            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]