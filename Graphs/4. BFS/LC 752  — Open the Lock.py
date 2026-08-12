from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        

        if target in deadends or "0000" in deadends:
            return -1

        visited= set(deadends)

        q=deque()
        q.append(("0000",0))

        visited.add("0000") # lock value

        def children(lock):

            res=[]

            for i in range(4):

                digit=str(int(lock[i]) +1 %10 )
                res.append(lock[:i]+digit+lock[i+1:])
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i]+digit+lock[i+1:])

                return res
                
        while q:

            lock, leval= q.popleft()

            if lock==target:
                return leval

            for child in children(lock):

                if child not in visited:
                    visited.add(child)
                    q.append((child,leval+1))

        return -1





        