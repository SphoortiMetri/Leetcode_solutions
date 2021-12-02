from heapq import *
import heapq
class Solution:
    def __init__(self): 
        self.min_heap = [] 
        self.max_heap = [] 
        
    def balance(self): 
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
        
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = [0.0 for x in range(len(nums) - k + 1)]

        for i in range(len(nums)): 
            if not self.max_heap or nums[i] <= -self.max_heap[0]: 
                heapq.heappush(self.max_heap, -nums[i]) 
                
            else: 
                heapq.heappush(self.min_heap, nums[i]) 
                
            self.balance() 
            
            if i-k+1 >= 0: 
                # add the median to the the result array
                if len(self.max_heap) == len(self.min_heap):
                    # we have even number of elements, take the average of middle two elements
                    result[i-k+1] = (-self.max_heap[0] / \
                                      2.0 + self.min_heap[0] / 2.0)
                else:  # because max-heap will have one more element than the min-heap
                    result[i-k+1] = (-self.max_heap[0] / 1.0)

                # remove the element going out of the sliding window
                elementToBeRemoved = nums[i - k + 1]
                if elementToBeRemoved <= -self.max_heap[0]:
                    self.remove(self.max_heap, -elementToBeRemoved)
                else:
                    self.remove(self.min_heap, elementToBeRemoved)

                self.balance()
        return result
            
        
    def remove(self, heap, element): 
        print(heap[0])
        ind = heap.index(element)  # find the element
        # move the element to the end and delete it
        heap.append(heap.pop(ind))
        del heap[-1] 

        heapify(heap)
        