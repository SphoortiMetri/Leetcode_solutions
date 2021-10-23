class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: 
        
        low = 0 
        high = len(numbers) -1 
        
        while low < high: 
            sum_of_two = numbers[low] + numbers[high] 
            
            if sum_of_two == target: 
                return [low+1,high+1] 
            
            if target < sum_of_two: 
                high -= 1 
            
            else: 
                low += 1 
                
        
