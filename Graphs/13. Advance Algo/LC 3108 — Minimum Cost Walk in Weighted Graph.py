from typing import List


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, v1):
        while v1 != self.par[v1]:
            self.par[v1] = self.par[self.par[v1]]
            v1 = self.par[v1]
        return v1

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p2]
        return True


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

        uf=UnionFind(n)

        for u,v, w in edges:
            uf.union(u,v)

        component_cost={} # root ->cost

        for u,v ,w in edges:

            root=uf.find(u)

            if root not in component_cost:
                component_cost[root]=w
            else:
                component_cost[root] &=w

        res=[]
        





         

        