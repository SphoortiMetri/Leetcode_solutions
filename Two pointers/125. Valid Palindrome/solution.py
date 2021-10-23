class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        """
        1. only alpha numeric characters are considered 
        2. case can be ignored 
        
        Base cases: 
        empty string, string of length 1 
        
        2 pointers 
        
        """

        
        left = 0 
        right = len(s) -1
        while left < right: 
            while left < right and not s[left].isalnum(): 
                  left += 1
            while left < right and not s[right].isalnum(): 
                  right -= 1
            if s[left].lower() != s[right].lower(): 
                  return False 
            left += 1
            right -= 1 
        return True
