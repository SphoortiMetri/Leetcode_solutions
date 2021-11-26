class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window_start = 0 
        max_len = 0 
        char_freq = {}
        
        for window_end in range(len(fruits)): 
            right_char = fruits[window_end] 
            char_freq[right_char] = char_freq.get(right_char,0) + 1 
            
            while len(char_freq) > 2: 
                left_char = fruits[window_start]
                char_freq[left_char] -= 1
                
                if char_freq[left_char] == 0: 
                    del char_freq[left_char]
                
                window_start += 1 
            max_len = max(max_len, window_end - window_start +1)
            
        return max_len
        