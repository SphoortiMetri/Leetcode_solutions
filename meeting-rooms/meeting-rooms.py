class Solution:
    
    def overlap(self,interval1,interval2): 
        return (interval2[0] < interval1[1] or interval2[1] < interval1[1])
    
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        
        for i in range(1,len(intervals)): 
            if self.overlap(intervals[i-1], intervals[i]): 
                return False
            
        return True
        
        