from typing import List
from collections import defaultdict
class Solution:
    def leadsToDestination(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int
    ) -> bool:


        graph= defaultdict(list)

        for a,b in edges:

            graph[a].append(b)

        stack=[source]
        visited= set()


        while stack:

            node= stack.pop()

            if not node==destination and not graph[node]:
                return False


            for nei in graph[node]:

               if node in graph[nei]:
                   return False

               stack.append(nei)

        return True

    