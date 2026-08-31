from typing import List
from collections import defaultdict
import math

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        adj= defaultdict(list)

        for src, des in roads:
            adj[src].append(des)
            adj[des].append(src)

        def dfs(node, parent):

            nonlocal res
            passangers=0

            for child in adj[node]:

                if child != parent:
                    p=dfs(child,node)
                    passangers+=p
                    res += int(math.ceil(p/seats))
            return passangers+1

        res=0
        dfs(0,-1)

        return res


        
        