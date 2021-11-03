import heapq 

class Solution:
    
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals: 
            return 0 
        
        free_rooms = [] 
        
        intervals.sort() 
        
        heapq.heappush(free_rooms, intervals[0][1]) 
        
        for i in range(1, len(intervals)): 
            #If the start time of new meeting is after the end time of old meeting - pop the old time and the new end time
            if free_rooms[0] <= intervals[i][0]: 
                heapq.heappop(free_rooms) 
                
            #Assign a new room irrespective of the if statement above 
            heapq.heappush(free_rooms, intervals[i][1]) 
            
        return len(free_rooms)
        

        