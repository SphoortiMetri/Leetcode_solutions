import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            print(point)
            return -(point[0] ** 2 + point[1] ** 2)
        
        max_heap = []
        
        for i in range(k): 
            heapq.heappush(max_heap, (distance(points[i]),points[i])) 
            
        for i in range(k, len(points)): 
            if distance(points[i]) > max_heap[0][0]: 
                heapq.heappop(max_heap) 
                heapq.heappush(max_heap, (distance(points[i]),points[i])) 
                
        res = []
            
        for i in range(k): 
            _, pt = heapq.heappop(max_heap) 
            res.append(pt) 
            
        return res
