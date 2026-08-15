from typing import List

from collections import deque, defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        map=defaultdict(list)

        for i in range(len(routes)):

            for j in routes[i]:

                map[j].append(i)

        if source==target:
            return 0

        q=deque()
        visited=set()

        q.append([source, map[source]])
        visited.add(source)


        while q:

            station,bus_number =q.popleft()

