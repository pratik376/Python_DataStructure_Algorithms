

from typing import Optional

from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return root

        q=deque([root])

        while q:

            count=0
            size=len(q)

            for i in range(size):

                count+=1

                curr= q.popleft()

                if count <size:
                    curr.next=q[0]
                else:
                    curr.next=None

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)
        return root                



# optimized version


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return root
        
        leftmost=root

        while leftmost.left:
            curr=leftmost

            while curr:

                curr.left.next=curr.right

                if curr.next:
                    if curr.next.left:
                        curr.right.next=curr.next.left
                    else:
                        curr.right.next=curr.next.right
                
                curr=curr.next
            leftmost=leftmost.left
        return root


            

        
