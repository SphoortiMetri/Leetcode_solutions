class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 1, len(arr)-2
        n = len(arr)
        
        while low < high: 
            mid = low + (high-low)//2 
            if arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]: 
                low = mid + 1 
            else:
                high = mid
                
        return low
                