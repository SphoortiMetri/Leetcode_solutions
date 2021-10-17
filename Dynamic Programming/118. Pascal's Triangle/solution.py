class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for row_num in range(numRows): 
            row = [[-1] for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            for col in range(1, len(row)-1): 
                row[col] = result[row_num-1][col-1] + result[row_num-1][col]
                    
            result.append(row)
                    
        return result
