from typing import List
from collections import defaultdict

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj=defaultdict(list)
        visited=set()

        for a,b in edges:
            adj[a].append(b)

        answer_stack=[]


        def dfs(i):

            stack=[i]
            visited.add(i)

            while stack:
                node=stack.pop()

                for nei in adj[node]:

                    if nei not in visited:
                        dfs(nei)

            answer_stack.append(i)

   
            
  
        for i in range(n):

            if i not in visited:
                dfs(i)

        answer=[]

        while answer_stack:
            answer.append(answer_stack.pop())

        return answer