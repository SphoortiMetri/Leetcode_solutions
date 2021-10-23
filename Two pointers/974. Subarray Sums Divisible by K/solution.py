class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        curr_sum = 0 
        n = len(nums) 
        prefix = {0:1}
        count = 0 
        
        for i in range(n): 
            curr_sum += nums[i] 
            
            remainder = curr_sum % k
            complement = (k - remainder) % k 
            if complement in prefix: 
                count += prefix[complement] 
                
            prefix[complement] = prefix.get(complement,0) +1
                
        return count
