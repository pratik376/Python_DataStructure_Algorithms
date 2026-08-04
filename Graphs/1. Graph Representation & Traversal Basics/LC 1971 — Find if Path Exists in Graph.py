from typing import List
from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        edges= defaultdict(set)

        for a,b in edges:

            edges[a].append(b)
            edges[b].append(a)

        if destination in edges[source]:
            return True

        return False 




        
        