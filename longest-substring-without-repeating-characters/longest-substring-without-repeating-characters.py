from collections import Counter         

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0 
        n = len(s) 
        dict_ = [0]*128
        
        res = 0 
        
        while right < len(s): 
            r = s[right] 
            dict_[ord(r)] += 1 
            
            while dict_[ord(r)] > 1: 
                l = s[left] 
                dict_[ord(l)] -= 1 
                left += 1 
                
            res = max(res, right -left+1) 
            
            right += 1 
            
        return res
                

        
