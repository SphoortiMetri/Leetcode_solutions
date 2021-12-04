class Solution:
    def __init__(self): 
        self.res = ""
        self.max_len = 0 
    
    def expand_around_center(self,s,l,r): 
        while l >= 0 and r < len(s) and s[l] == s[r]: 
            if r - l+ 1> self.max_len:
                self.res = s[l:r+1]
                self.max_len = r-l+1
                    
            l -= 1
            r += 1 
                
    def longestPalindrome(self, s: str) -> str:
        n = len(s)


        for i in range(n): 
            self.expand_around_center(s,i,i)
            self.expand_around_center(s,i,i+1)
            
            
        return self.res
    
        