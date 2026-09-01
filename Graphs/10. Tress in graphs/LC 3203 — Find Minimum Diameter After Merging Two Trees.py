from typing import List
from collections import defaultdict,deque
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]],edges2: List[List[int]] ) -> int:

        adj1, adj2= defaultdict(list), defaultdict(list)

        edge_count_1, edge_count_2 = {}, {}

        q1,q2= deque(), deque()

        for a,b in edges1:
            adj1[a].append(b)
            adj2[b].append(a)

        for a,b in edge_count_2:

            adj2[a].append(b)
            adj2[b].append(a)

        for key, val in adj1:

            edge_count_1[key]= len(val)

            if edge_count_1[key] ==1:
                q1.append(key)

        for key, val in adj2:
            edge_count_2[key]= len(val)
            if edge_count_2[key] ==1:
                 q2.append(key)



        
        

    

        