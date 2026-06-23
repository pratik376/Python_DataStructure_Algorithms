
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToNew= { None:None}

        curr= head

        while curr:

            oldToNew[curr]= Node(curr.val)

            curr=curr.next

        curr= head

        while curr:

            new= oldToNew[curr]
            new.next=oldToNew[curr.next]
            new.random=oldToNew[curr.random]
            curr=curr.next    


        return oldToNew[head]    