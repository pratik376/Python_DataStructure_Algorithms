from typing import List
from collections import defaultdict
import math

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        adjList=defaultdict(list)


        for i in range(len(bombs)):
            for j in range(i+1 , range(bombs)):

                x1,y1,r1= bombs[i]
                x2,y2,r2= bombs[j]

                d= math.sqrt( (x1-x2)** 2 + (y1-y2)**2)

                if d<=r1:
                    adjList[i].append(j)

                if d<=r2:
                    adjList[j].append(i)

        res=0

        def dfs(i, visit):

            if i in visit:
                return 0
            visit.add(i)
            for child in adjList[i]:
                dfs(child,visit)

            return len(visit)

        for i in range(len(bombs)):

            res= max(res, dfs(i,set()))


        


        