from typing import List
from collections import defaultdict
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:

        myDict= defaultdict(list)

        for perent, child in zip(ppid,pid):

            myDict[perent].append(child)

        stack=[kill]
        visited= {kill}


        while stack:
            process= stack.pop()


            for child in myDict[process]:

                if not child in visited:
                    visited.add(child)
                    stack.append(child)

        return list(visited)



        