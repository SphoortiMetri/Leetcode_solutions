class Solution:
    def trap(self, elevations: List[int]) -> int:
        
        max_left_wall = [-1 for _ in range(len(elevations))] 
        max_right_wall = [-1 for _ in range(len(elevations))] 
      
        right_max = 0
        for i in range(len(elevations)-1, -1, -1): 
            max_right_wall[i] = right_max
            right_max = max(right_max, elevations[i]) 

        left_max = 0 
        for i in range(len(elevations)): 
            max_left_wall[i] = left_max 
            left_max = max(left_max, elevations[i]) 

        total = 0 

        for i in range(len(elevations)): 
            elevation = min(max_left_wall[i], max_right_wall[i]) 
            if elevation > elevations[i]: 
                  total += elevation - elevations[i] 

        return total
