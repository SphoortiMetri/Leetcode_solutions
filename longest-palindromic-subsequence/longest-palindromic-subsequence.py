class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        def dp(sI, eI, memo): 
            
            if sI > eI: 
                return 0 
            
            if sI == eI: 
                return 1 
            
            if memo[sI][eI] != -1: 
                return memo[sI][eI] 
            
            #case 1 
            if s[sI] == s[eI]: 
                return 2 + dp(sI+1, eI-1, memo) 
            
            #case 2 
            count1 = dp(sI+1,eI, memo) 
            count2 = dp(sI, eI-1,memo) 
            
            res =  max(count1, count2) 
            memo[sI][eI]  = res
            return memo[sI][eI] 
        
        n = len(s)
        
        memo = [[-1 for i in range(n)] for j in range(n)]
        return dp(0, len(s)-1, memo)
        