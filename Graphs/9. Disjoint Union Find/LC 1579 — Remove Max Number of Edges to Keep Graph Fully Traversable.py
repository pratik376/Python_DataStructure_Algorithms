from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        parents= [i for i in range(n+1)]
        rank= [1] * (n+1)

        edges_storage={}


        def find(n):

            while n != parents[n]:
                parents[n]= parents[parents[n]]   
                n=parents[n]
            return n

        