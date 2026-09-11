from typing import List

from collections import defaultdict,deque
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        answer=[0] * len(queries)

        adj=defaultdict(list)

        for i in range(n-1):
            adj[i].append(i+1)

        def bfs():

            visited= set()
            q=deque([0,0]) # node, steps_cost
            visited.add(0)


            while q:

                node, cost =q.popleft()

                if node==n-1:
                    return cost

                for  nei in adj[node]:

                    if nei not in visited:
                        q.append((nei,cost+1))
                        visited.add(nei)

        for index, val in enumerate(queries):
            a,b= val
            adj[a].append(b)

            answer[index]=bfs()

        return answer

        