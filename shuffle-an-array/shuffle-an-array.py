class Solution:

    def __init__(self, nums):
        
        self.array = nums
        self.original_array = nums[:]
    

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.original_array
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        
        
        for i in range(len(self.array)): 
            remove_idx = random.randrange(0,len(self.array)) 
            self.array[remove_idx], self.array[i] = self.array[i], self.array[remove_idx]
            
        return self.array 
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()