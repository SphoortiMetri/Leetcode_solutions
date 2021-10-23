from collections import defaultdict 
from enum import Enum 

class State(Enum): 
    TO_VISIT = 0 
    VISITING = 1
    VISITED = 2

    
class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def build_graph(): 
            graph = defaultdict(list) 
            
            for course, prereq in prerequisites: 
                graph[course].append(prereq) 
                
            return graph
            
        def has_cycle(start, states): 
            
            #mark as visiting 
            states[start] = State.VISITING
            
            for next_vertex in graph[start]: 
                if states[next_vertex] == State.VISITED: 
                    continue 
                    
                if states[next_vertex] == State.VISITING: 
                    return True 
                
                if has_cycle(next_vertex,states): 
                    return True
                
            states[start] = State.VISITED
            return False 
        
        graph = build_graph()
        
        states = [State.TO_VISIT for _ in range(numCourses)] 
        
        for i in range(numCourses): 
            if has_cycle(i, states): 
                return False 
        
        return True
        
