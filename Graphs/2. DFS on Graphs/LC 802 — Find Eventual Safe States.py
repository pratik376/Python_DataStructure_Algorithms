from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        n= len(graph)
        safe= {}

        def dfs(i):

            if i in safe:
                return safe[i]
            







        res=[]

        for i in len(n):

            if dfs(i):
                res.append(i)
        return res
        