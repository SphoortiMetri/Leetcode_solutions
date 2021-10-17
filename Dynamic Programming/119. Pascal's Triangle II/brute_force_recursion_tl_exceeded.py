class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        
        def helper(i,j): 
            if i == j or j == 0:
                return 1 
            
            return helper(i-1,j-1) + helper(i-1,j) 
        
        
        for col in range(rowIndex+1): 
            triangle.append(helper(rowIndex,col))
            
        return triangle
