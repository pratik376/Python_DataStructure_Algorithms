from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        neighbours=defaultdict(list)

        graph= { (a,b) for a,b in connections }

        visited= set()

        answer=0


        for a,b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)


        def dfs()

        