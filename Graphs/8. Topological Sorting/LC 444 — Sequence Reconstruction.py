from typing import List
from collections import defaultdict,deque
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:

        q=deque()
        adj= defaultdict(set)
        indegree= defaultdict(int)

        for sequence in sequences:

            for i in range(len(sequence)-1):

                u= sequence[i]
                v=sequence[i+1]

                if v not in adj[u]:
                 adj[u].add(v)
                 indegree[v]+=1  

        answer=[]


        def bfs(q):
            nonlocal answer

            while q:
                if len(q)>1:
                    return False
                number=q.popleft()
                answer.append(number)
               
                for nei in adj[number]:
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        q.append(nei)
            return True

        for num in nums:

            if indegree[num]==0:
                q.append(num)

        if len(q)>1:
            return False
        else:
            if not bfs(q):
                return False
            
        return True if answer == nums else False
            

        


        
        