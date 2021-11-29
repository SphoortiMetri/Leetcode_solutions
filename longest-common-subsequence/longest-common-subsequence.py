from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)

        def helper(p1,p2): 
            
            if p1 == len(text1) or p2 == len(text2): 
                return 0 
            
            if text1[p1] == text2[p2]: 
                return 1 + helper(p1+1, p2+1) 
            
            else: 
                return max(helper(p1, p2+1), helper(p1+1,p2))
            
        dp = [[-1 for j in range(len(text2))] for i in range(len(text1))]
        return helper(0,0)
        