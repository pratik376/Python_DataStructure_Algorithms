from typing import List
from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph= defaultdict(list)
        seen=set()

        stack=[source]
        seen.add(source)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)


        while stack:

            element= stack.pop()

            if element== destination:
                return True

            for vertes in graph[element]:

                if not vertes in seen:
                    seen.add(vertes)
                    stack.push(vertes)

        return False

        








        




        
        