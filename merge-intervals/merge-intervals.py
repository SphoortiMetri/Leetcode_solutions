class Solution:
    
    def overlap(self,interval1, interval2): 
        return (interval2[0] <= interval1[1] or interval2[1] <= interval1[1]) 
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() 
        
        res = [] 
        
        for interval in intervals: 
            if not res or not self.overlap(res[-1],interval): 
                res.append(interval) 
                
            else: 
                res[-1][1] = max(res[-1][1], interval[1])
                
        return res
        