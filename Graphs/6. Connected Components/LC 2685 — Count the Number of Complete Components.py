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


        for i in range(n):

            if i not in adj:
                adj[i].append([])
                edge_count[i]+=1

        def dfs(i):

            total_node=0
            stack=[i]
            visited.add(i)

            while stack:
                node=stack.pop()
                total_node+=1

                for nei in adj[node]:

                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)

            return total_node


        answer=0
        
        for i in range(n):

            if i not in visited:
                total_node=dfs(i)

                if edge_count[i] == total_node-1:
                    answer+=1

        return answer




        
        