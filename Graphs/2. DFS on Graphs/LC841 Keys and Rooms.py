from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        dict= {index:val for index, val in enumerate(rooms)}

        stack=[0]
        seen=set()
        seen.add(0)


        while stack:


            room= stack.pop()




        