from typing import List

from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:


        adj= defaultdict(list)

        for a,b , prob in zip(edges,succProb):
            adj[a].append((b,prob))
            adj[b].append((a,prob))

        

        