class Solution:
    def kthGrammar(self, n: int, k: int) -> int: 
        """
        0
        0 1 
        0 1 1 0 
        0 1 1 0 1 0 0 1 
        
        """
        #Base case: 1st row is always 0 
        if n == 1: 
            return 0
        
        parent = self.kthGrammar(n-1 ,ceil(k/2)) 
        is_k_odd = (k%2 == 1) 
        if parent is 1: 
            return 1 if is_k_odd else 0 
        else: 
            return 0 if is_k_odd else 1
