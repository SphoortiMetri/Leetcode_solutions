class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(path,used,res): 
            #exit condition 
            if len(path) == len(nums): 
                res.append(path[:]) 
                return 
            
                
            for i, letter in enumerate(nums): 
                if used[i] == True: 
                    continue 
                    
                used[i] = True 
                path.append(letter) 
                dfs(path, used,res) 
                path.pop()
                used[i] = False 
                
        
        
        
    
    
        res = [] 
        dfs([], [False]*len(nums), res)
        return res