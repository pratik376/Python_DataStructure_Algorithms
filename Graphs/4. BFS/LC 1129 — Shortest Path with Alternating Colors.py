from typing import List
from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        blue=defaultdict(list)
        red=defaultdict(list)


        for  src,dst in redEdges:
            blue[src].append(dst)

        for src, dst in blueEdges:
            red[src].append(dst)

        q= deque()
        visited= set()

        answer=[-1] * n

        q.append([0,0,None])  # (node, length, color)
        visited.add((0,None)) #  (node, color)

        while q:

            node, length, color=q.popleft()

            if answer[node]==-1:
                answer[node]= length

            if color != 'RED':
                for nei in red[node]:

                    if nei not in visited:
                        visited.add((nei,'RED'))
                        q.append([nei,length +1, "RED"])

            if color != 'BLUE':
                for nei in red[node]:

                    if nei not in visited:
                        visited.add((nei,'BLUE'))
                        q.append([nei,length +1, "BLUE"])

        return answer


        

        

