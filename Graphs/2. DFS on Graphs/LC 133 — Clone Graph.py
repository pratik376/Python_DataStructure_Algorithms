
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        stack=[node]
        head= Node(node.val)
        stack2=[head]



        seen=set()
        seen.add(node)

        while stack:

            node=stack.pop()
            clone=stack2.pop()

            for neighbour in node.neighbors:

                if not neighbour in seen:
                    clone_neigh=Node(neighbour.val)
                    clone.neighbors.append(clone_neigh)
                    stack2.append(clone_neigh)
                    seen.add(neighbour)
                    stack.append(neighbour)

        