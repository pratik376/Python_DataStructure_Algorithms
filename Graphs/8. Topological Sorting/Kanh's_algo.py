from typing import List
from collections import deque,defaultdict

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:

        adj=defaultdict(list)
        degrees=defaultdict(int)
        answer=[]

        for  a, b in edges:
            adj[a].append(b)
            degrees[b]+=1



        q=deque()
        visited= set()

        def bfs(q):

            while q:
                node=q.popleft()
                visited.add(node)
                answer.append(node)

                for nei in adj[node]:

                    if degrees[nei]>1:
                        degrees[nei]-=1
                    else:
                        degrees[nei]=0
                        q.append(nei)

        for i in range(n):

            if degrees[i]==0:
                q.append(i)

        bfs(q)
        

        return len(answer)==n

