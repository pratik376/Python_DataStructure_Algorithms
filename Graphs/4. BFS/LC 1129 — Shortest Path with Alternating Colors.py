from typing import List
from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        blue=defaultdict(list)
        red=defaultdict(list)


        for  src,dst in redEdges:
            blue[src].append(dst)

        for src, dst in blueEdges:
            red[src].append(dst)

        q= deque()
        visited= set()

        answer=[-1] * n

        

        

