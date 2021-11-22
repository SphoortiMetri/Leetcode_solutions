from collections import deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        #initialize graph
        #keeps track of icoming nodes for each node - 0 is source 
        inDegree = {} 
        
        #adjacency graph 
        graph = {} 
        
        for word in words: 
            for c in word: 
                graph[c] = [] 
                inDegree[c] = 0 
        
        #Build graph 
        for j in range(0,len(words)-1): 
            word_1 = words[j]
            word_2 = words[j+1] 
            
            for i in range(min(len(word_1), len(word_2))): 
                if word_1[i] != word_2[i]: 
                    graph[word_1[i]].append(word_2[i]) 
                    inDegree[word_2[i]] += 1 
                    break
                    
            else:
                if len(word_2) < len(word_1): return ""
                    
        print(graph)
        print(inDegree)
        
        #Find all sources 
        sortedOrder = [] 
        sources = []
        for key, value in inDegree.items(): 
            if value == 0: 
                sources.append(key)
                
        
        #BFS - add sources - add their children to the queue and remove sources 
        queue = deque(sources) 
        while queue: 
            node = queue.popleft() 
            sortedOrder.append(node) 
            
            for child in graph[node]: 
                inDegree[child] -= 1 
                if inDegree[child] == 0: 
                    queue.append(child) 
                    
                    
        if len(sortedOrder) == len(inDegree): 
            return "".join(sortedOrder)
        else: 
            return ""

                
            
        
            
        