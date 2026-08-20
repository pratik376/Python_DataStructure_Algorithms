from typing import List
from collections import defaultdict,deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj=defaultdict(list) # a-> [b, a/b]

        for i, eq in enumerate(equations):

            a,b= eq

            adj[a].append([b,values[i] ])
            adj[b].append([a, 1/values[i]])


        

        def bfs(src, dest):

            if src not in adj or dest not in adj:
                return -1

            q=deque((src, 1))
            visited=set()

            visited.add(src)
            result=1

            while q:
                node, val =q.popleft()

                if node==dest:
                    return val

                for nei in adj[src]:

                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, adj[nei][1] * val))

        answer=[]
        for qx,qy in queries:
            answer.append(bfs(qx,qy))

        return answer


        