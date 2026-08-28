from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

    
        if len(connections) < n-1:
            return -1
        
        parents= [i for i in range(len(n))]

        rank= [1] * len(n)


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

        component= n

        for a,b in connections:

            if not union(a,b):
                component-=1


        return component-1
            

        
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        parent = [i for i in range(n)]
        size = [1] * n

        def find(node):

            p = parent[node]

            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p

        def union(a, b):

            p1 = find(a)
            p2 = find(b)

            if p1 == p2:
                return False

            if size[p1] > size[p2]:

                parent[p2] = p1
                size[p1] += size[p2]

            else:

                parent[p1] = p2
                size[p2] += size[p1]

            return True

        extra_cables = 0
        components = n

        for a, b in connections:

            if union(a, b):
                components -= 1

            else:
                extra_cables += 1

        cables_needed = components - 1

        if extra_cables >= cables_needed:
            return cables_needed

        return -1
    
        

        
        