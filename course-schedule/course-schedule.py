from collections import defaultdict,deque
from enum import Enum 

class State(Enum): 
    TO_VISIT = 0 
    VISITING = 1
    VISITED = 2

from collections import defaultdict 

class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        order = [] 
        if numCourses <= 0: 
            return []
        
        indegree = {i: 0 for i in range(numCourses)}  
        graph = defaultdict(list) 
        
        
        for course in prerequisites: 
            parent, child = course[0], course[1] 
            graph[parent].append(child) 
            indegree[child] = indegree.get(child,0) + 1

            
        sources = deque()

        for key in indegree: 
            if indegree[key] == 0: 
                sources.append(key)
                
                
        while sources: 
            node = sources.popleft()
            
            order.append(node) 
            
            for child in graph[node]: 
                indegree[child] -= 1 
                if indegree[child] == 0: 
                    sources.append(child) 
                    
                    
        return True if len(order) == numCourses else False
            
        