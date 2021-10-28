import heapq
class MedianFinder:

    def __init__(self):
        #small_pile
        self.max_heap = []
        #large pile 
        self.min_heap = [] 
        
    def balance(self): 
        if len(self.max_heap) > len(self.min_heap) + 1:
            num = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,-num) 
        
        if len(self.max_heap) < len(self.min_heap): 
            num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-num) 
            
        
    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0 or num < self.min_heap[0]: 
            heapq.heappush(self.max_heap,-num) 
        else: 
            heapq.heappush(self.min_heap,num)
        
        self.balance()
        
    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap): 
            return (self.min_heap[0] - self.max_heap[0]) / 2
        
        if len(self.max_heap) > len(self.min_heap): 
            return - self.max_heap[0] 
        
        else: 
            return self.min_heap[0]
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
