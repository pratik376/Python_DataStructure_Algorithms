from typing import List
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:


        adj=defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited= set()

        stack=[(0,-1)]
        visited.add(0)

        while stack:

            node, parent= stack.pop()

            for nei in adj[node]:

                if nei not in visited:
                    stack.append((nei,node))
                    visited.add(nei)

                elif nei != parent:
                    return False


        return len(visited)==n 