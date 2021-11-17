class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        res = ""
        max_len = 0 

        for i in range(n): 
            
            l = i 
            r = i 
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if r - l+ 1> max_len:
                    res = s[l:r+1]
                    max_len = r-l+1
                    
                l -= 1
                r += 1 
                
            
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if r - l+ 1> max_len:
                    res = s[l:r+1]
                    max_len = r-l+1
                    
                l -= 1
                r += 1 
            
        return res
            
            
        

            
            
            
    
            

            
            
            
                
                
                    
        
            
                        

            
            
            
            
                    
                
                    
            

        
        
        
        
                
        