from typing import List
from collections import defaultdict,deque
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]],edges2: List[List[int]] ) -> int:

        adj1, adj2= defaultdict(list), defaultdict(list)

        n1,n2= len(edges1)+1, len(edges2)+1

        edge_count_1, edge_count_2 = {}, {}

        q1,q2= deque(), deque()

        for a,b in edges1:
            adj1[a].append(b)
            adj1[b].append(a)

        for a,b in edges2:

            adj2[a].append(b)
            adj2[b].append(a)

        for key, val in adj1.items():

            edge_count_1[key]= len(val)

            if edge_count_1[key] ==1:
                q1.append(key)

        for key, val in adj2.items():
            edge_count_2[key]= len(val)
            if edge_count_2[key] ==1:
                 q2.append(key)

        answer1,answe2= [], []
        while q1:
            if n1 <=2:
                answer1.append(list(q1))
                break

            for _ in range(len(q1)):
                leaf= q1.popleft()
                n1-=1
                for nei in adj1[leaf]:
                    edge_count_1[nei]-=1
                    if edge_count_1[nei]==1:
                        q1.append(nei)

        while q2:
            if n2 <=2:
                answe2.append(list(q2))
                break
            for _ in range(len(q2)):
                leaf= q2.popleft()
                n2-=1
                for nei in adj2[leaf]:
                    edge_count_2[nei]-=1
                    if edge_count_2[nei]==1:
                        q2.append(nei)

        



        
        

    

        