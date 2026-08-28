from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

    

        parents= [i for i in range(len(connections))]

        rank= [1] * len(connections)


        def find(n):

            while n != parents[n]:
                parents[n]=parents[parents[n]]
                n=parents[n]

            return n

        def union(a,b):
            p1,p2= find(a),find(b)

            if p1 == p2:
                return False

            if rank[p1]> rank[p2]:

                parents[p2]=p1
                rank[p1]+=rank[p2]

            else:

                parents[p1]=p2
                rank[p2]+=rank[p1]
            return True

        cables=0

        for a,b in connections:

            if not union(a,b):
                cables+=1


        return cables if cables + len(connections) == n else -1
            

        

        

        
        