class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        
        if len(nums1) > len(nums2): 
            nums1, nums2 = nums2, nums1
            
        m = len(nums1)
        n = len(nums2) 
        
        left = 0 
        right = m
        
        while left <= right: 
            partition_1 = left + (right-left) // 2 
            partition_2 = (m + n + 1)//2 - partition_1
            
            partition_1_left_max = -float('inf') if partition_1 == 0 else nums1[partition_1 -1]
            partition_1_right_min = float('inf') if partition_1 == m  else nums1[partition_1]
            
            partition_2_left_max = -float('inf') if partition_2 == 0 else nums2[partition_2 -1]
            partition_2_right_min = float('inf') if partition_2 == n else nums2[partition_2]
            
            if partition_1_left_max <= partition_2_right_min and partition_2_left_max <= \
            partition_1_right_min: 
                #found it 
                if (m + n) % 2 == 0: 
                    x = max(partition_1_left_max,partition_2_left_max)
                    y = min(partition_1_right_min,partition_2_right_min )
                    return (x + y) / 2
                
                else:
                    return max(partition_1_left_max,partition_2_left_max)
                
            elif partition_1_left_max > partition_2_right_min: 
                right = partition_1 - 1 
                
            else: 
                #look right 
                left = partition_1 + 1
                    
        
                
            
            
            
        