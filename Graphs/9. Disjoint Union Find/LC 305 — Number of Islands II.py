from typing import List

class Solution:
    def numIslands2( self,m: int,n: int,positions: List[List[int]] ) -> List[int]:

        parents= [i for i in range(m*n)]
        rank= [1] * (m *n)
        parents= [-1] * (m *n)

        directions= [ (1,0),(-1,0),(0,1),(0,-1)]

        isLand=0
        answer=[]

        def find(node):

            while node != parents[node]:

                node=parents[node]
                parents[node]= parents[parents[node]]

            return node

        def union(a,b):

            p1=find(a)
            p2=find(b)

            if p1==p2:
                return True

            if rank[p1]> rank[p2]:

                parents[p2]=p1
                rank[p1]+=rank[p2]

            else:
                parents[p1]=p2
                rank[p2]+=rank[p1]

            return False
        



