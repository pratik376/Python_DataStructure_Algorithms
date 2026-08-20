from typing import List
from collections import defaultdict


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        adj= defaultdict(list)
        edge_count=defaultdict(int)
        visited=set()


        for a,b in edges:

            adj[a].append(b)
            adj[b].append(a)
            edge_count[a]+=1
            edge_count[b]+=1

        def dfs(i):

            total_node=0
            total_edge=0
            stack=[i]
            visited.add(i)

            while stack:
                node=stack.pop()
                total_node+=1

                for nei in adj[node]:

                    if nei not in visited:
                        
                        visited.add(nei)
                        stack.append(nei)
                    total_edge+=1
                    

            return total_node,total_edge //2
        answer=0
        
        for i in range(n):

            if i not in visited:
                total_node,total_edge=dfs(i)
                final_edge=  (total_node) * (total_node-1) /2

                if total_edge ==final_edge :
                    answer+=1

        return answer




        
        