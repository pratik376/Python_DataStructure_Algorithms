from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        visited=set()
       


        stack=[(0,"A")]

        visited.add(0)

        while stack:

            node, status =stack.pop()

            for nei in graph[node]:

                if nei not in visited:
                    

        
        






        