class Solution:
    def subarraySum(self, arr: List[int], target: int) -> int:
    
        prefix_sums = {0: 1}
        cur_sum = 0
        count = 0 
        for i in range(len(arr)):
            
            cur_sum += arr[i]
            compliment = cur_sum - target
            if compliment in prefix_sums:
                count += prefix_sums[compliment]
            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) +1 
        
        return count 
