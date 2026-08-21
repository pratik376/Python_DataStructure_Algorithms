from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        visited=set()
        status={}


        stack=[(0)]
        status[0]="A"

        visited.add(0)

        while stack:

            node=stack.pop()

            for nei in graph[node]:

                if nei not in visited:

                    if status=="A":
                        status[nei]="B"
                    else:
                        status[nei]="A"

                elif status[node]==
                      

                


        
        






        