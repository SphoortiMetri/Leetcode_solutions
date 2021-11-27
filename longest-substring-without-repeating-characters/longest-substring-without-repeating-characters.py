from collections import Counter         

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0 
        window_start = 0 
        char_index = {}
        
        for window_end in range(len(s)): 
            right_char = s[window_end] 
            if right_char in char_index: 
                window_start = max(window_start, char_index[right_char]+1)
                
            char_index[right_char] = window_end
            max_len = max(max_len, window_end-window_start+1) 
            
        return max_len
            

        
        
                

        
