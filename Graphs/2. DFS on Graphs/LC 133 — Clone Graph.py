
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        stack=[node]


        seen=set()
        seen.add(node)

        while stack:

            node=stack.pop()

            for neighbour in node.neighbors:

                if not neighbour in seen:
                    seen.add(neighbour)
                    stack.append(neighbour)

        