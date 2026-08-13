from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n= len(board)
        board.reverse()
        q=deque() # squre and steps
        q.append([1,0])
        visited= set()

        def intToPosition(sqare):
            r= (sqare-1)// n
            c=(sqare-1) % n

            if r %2 :
                c=len -1 -c

            return [r,c]

        while q:

            sqare, step =q.popleft()

            if sqare == n **2:
                return step
            for i in range(1,7):

                nextSqaure=sqare+i
                r,c = intToPosition(nextSqaure)

                if board[r][c] != -1:
                    nextSqaure=board[r][c]

                if nextSqaure not in visited:
                    q.append([nextSqaure, step+1])
                    visited.add(nextSqaure)

        return -1















        