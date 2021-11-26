class Solution:
    def minSubArrayLen(self, s: int, arr: List[int]) -> int:
        
        window_sum = 0 
        window_start = 0 
        min_len = float('inf')
        for window_end in range(len(arr)): 
            window_sum += arr[window_end] 

            while window_sum >= s:
                min_len = min(min_len, window_end-window_start+1)
                window_sum -= arr[window_start] 
                window_start += 1 

        return 0 if min_len == float('inf') else min_len
        