from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        Mydict= {index:val for index, val in enumerate(rooms)}

        stack=[0]
        seen=set()
        seen.add(0)


        while stack:


            room= stack.pop()

            for nei in Mydict[room]:

                if nei not in seen:
                    seen.add(nei)
                    stack.append(nei)

        if len(seen)==len(rooms):
            return True
        else:
            return False




        