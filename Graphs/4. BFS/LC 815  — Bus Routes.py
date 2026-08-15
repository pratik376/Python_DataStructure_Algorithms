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


        for bus in map[source]:
            q.append((bus,1))
            visited.add(bus)

        while q:

            station,bus_number =q.popleft()

