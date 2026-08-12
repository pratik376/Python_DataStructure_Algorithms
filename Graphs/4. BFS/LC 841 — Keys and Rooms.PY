from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited=set()



        stack= [0]
        visited.add(0)


        while stack:

            room= stack.pop()

            for nei in rooms[room]:

                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)


        return len(visited)== len(rooms)
        