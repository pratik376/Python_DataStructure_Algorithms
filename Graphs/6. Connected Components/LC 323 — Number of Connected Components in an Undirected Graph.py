from typing import List
from collections import defaultdict


# If there are V vertices and E edges, we build an adjacency list and DFS:

# Time = O(V + E)
# Space = O(V + E)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        adj= defaultdict(list)

        for a,b in edges:   # time O(N) space # (n)
            adj[a].append(b)
            adj[b].append(a)

        visited= set()
        answer=0

        def dfs(i):

            stack=[i]
            visited.add(i)

            while stack:
                node= stack.pop()

                for nei in adj[node]:

                    if nei not in visited:
                        stack.append(nei)
                        visited.add(nei)

        for i in range(n):

            if i not in visited:
                dfs(i)
                answer+=1

        return answer






        



