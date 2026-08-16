from typing import List
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        adj = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        b= " ".join(str(c) for row in board for c in row)


        q=deque()
        visited=set()

        q.append((b.index('0'),b,0)) # index, string , lenghth
        visited.add(b)


        while q:
            index, string, length=q.popleft()

            if string=='123450':
                return length


            b=list(string)

            for j in adj[index]:

                new_b= b.copy()

                new_b[j],new_b[index]=new_b[index],new_b[j],

                new_b_str= str(new_b)

                if not new_b_str in visited:
                    visited.add(new_b_str)
                    q.append((j,new_b_str, length+1))
        return -1



