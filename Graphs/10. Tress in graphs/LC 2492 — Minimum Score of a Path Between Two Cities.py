from typing import List

from collections import defaultdict,deque
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        edgeList= defaultdict(list)

        q=deque()
        q.append((1,float('inf')))
        answer=float('inf')
        visited=set()
        visited.add(1)


        for a,b, weight in roads:

            edgeList[a].append((b,weight))
            edgeList[b].append((a,weight))


        def bfs():

            while q:
                node, w=q.popleft()

                answer=min(answer,w)

                for nei,weight in edgeList[node]:


                


        