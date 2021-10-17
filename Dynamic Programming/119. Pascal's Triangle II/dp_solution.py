class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        
        for row in range(rowIndex + 1): 
            current_row = [-1] * (row+1) 
            current_row[0] = 1
            current_row[-1] = 1
            
            for col in range(1,len(current_row)-1):                 
                current_row[col] = triangle[row-1][col-1] + triangle[row-1][col] 
            
            triangle.append(current_row)
            
        return triangle[-1]
