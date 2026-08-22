from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:

        q=deque()
        adj= defaultdict(list)
        degree = defaultdict(int)


        for a,b in relations:

            adj[a].append(b)
            degree[b]+=1

        answer=[]

        min_sem=0

        def bfs(q):
            nonlocal min_sem

            while q:

               course, semester =q.popleft()
               answer.append(course)
               min_sem=max(min_sem,semester)

               for nei in adj[course]:

                   degree[nei]-=1

                   if degree[nei]==0:

                       q.append((nei, semester+1))
                 
        for i in range(1,n+1):
            if degree[i]==0:
                q.append((i,1))

        bfs(q)

        return min_sem if len(answer)==n else -1
        