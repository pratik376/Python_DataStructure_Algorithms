from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent= [i for i in range(len(edges)+1)]
        rank= [1] * (len(edges)+1)
        