from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        neighbours=defaultdict(list)

        graph= { (a,b) for a,b in connections }

        visited= set()

        answer=0


        for a,b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)


        def dfs(city):

            nonlocal neighbours,graph,visited,answer

            for nei in neighbours[city]:

                if not nei in visited:
                    visited.add(nei)

                    if (city, nei)  in graph:
                        answer+=1
                    dfs(nei)

        visited.add(0)
        dfs(0)
        return answer



            

        