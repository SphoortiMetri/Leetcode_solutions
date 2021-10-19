class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        #iterative solution 
        product = 1 
        index = abs(n) 
        
        while index: 
            if index % 2: 
                product *= x 
                
            x *= x 
            index = index //2 
            
        if n < 0: 
            return 1/product 
        else: 
            return product
