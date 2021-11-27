class Solution:
    def checkInclusion(self, pattern: str,str : str) -> bool:
        dict_pattern = Counter(pattern)
        dict_str = {} 
        left = 0 
        for i in range(len(str)): 
            right_char = str[i]
            dict_str[right_char] = dict_str.get(right_char,0) + 1 



            if i > len(pattern)-1: 
                if dict_str[str[left]] == 1: 
                    del dict_str[str[left]] 
                else: 
                    dict_str[str[left]] -= 1 
                    
                left += 1 
                
            if dict_str == dict_pattern: 
                return True

        return False