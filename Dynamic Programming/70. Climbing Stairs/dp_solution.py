    def climbStairs(self, n: int) -> int: 
        
        lookup_table = [-1] * (n+1)
        lookup_table[0] = 1 
        lookup_table[1] = 1
        
        for i in range(2,n+1): 
            lookup_table[i] = lookup_table[i-1] + lookup_table[i-2]
            
        return lookup_table[n]
