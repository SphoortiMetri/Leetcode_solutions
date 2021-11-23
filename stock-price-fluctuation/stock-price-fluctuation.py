from heapq import * 

class StockPrice:

    def __init__(self):
        self.highest_timestamp = -float('inf')
        self.timestamps = {} 
        self.max_heap = [] 
        self.min_heap = []
        

    def update(self, timestamp: int, price: int) -> None:
        self.timestamps[timestamp] = price
        self.highest_timestamp = max(self.highest_timestamp, timestamp) 
        
        heappush(self.max_heap, (-price,timestamp)) 
        heappush(self.min_heap, (price,timestamp)) 
        

    def current(self) -> int:
        return self.timestamps[self.highest_timestamp]

    def maximum(self) -> int:
        curr_price, timestamp = heappop(self.max_heap)
        
        while self.timestamps[timestamp] != -curr_price: 
            curr_price, timestamp = heappop(self.max_heap)
            
        heappush(self.max_heap, (curr_price, timestamp)) 
        return -curr_price


    def minimum(self) -> int:
        curr_price, timestamp = heappop(self.min_heap) 
        
        while self.timestamps[timestamp] != curr_price: 
            curr_price, timestamp = heappop(self.min_heap)
            
        heappush(self.min_heap, (curr_price, timestamp))
        return curr_price
        

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()