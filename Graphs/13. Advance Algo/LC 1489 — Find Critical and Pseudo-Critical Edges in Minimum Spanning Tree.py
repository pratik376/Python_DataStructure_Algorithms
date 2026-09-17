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
    def findCriticalAndPseudoCriticalEdges(self, n: int,edges: List[List[int]]) -> List[List[int]]:

        for i,e in enumerate(edges):
            e.append(i)  #[v1,c2,weight, index ]

        edges.sort(key=lambda e: e[2])

        mast_weight=0

        uf=UnionFind(n)

        for v1,v2,w , i in edges:

            if uf.union(v1,v2):
                mast_weight+=w

        