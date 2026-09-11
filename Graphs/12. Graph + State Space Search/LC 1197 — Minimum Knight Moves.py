from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


        visited= set()
        q=deque()
        q.append((0,0,0)) # moves, x,y
        visited.add((0,0))


        while q:
            cost, r,c=q.popleft()

            if (r,c)==(x,y):
                return cost


            for R,C in moves:

                nr,nc= r+R ,c+ C

                if (nr,nc) not in visited:
                    visited.add((nr,nc))
                    q.append((cost+1, nr,nc))

        return -1
            
