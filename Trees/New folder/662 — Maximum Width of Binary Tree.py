# # Definition for a binary tree node.
from typing import Optional

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        answer=1
        q=deque()
        q.append((root,1))

        while q:

            for i in range(len(q)):

             curr, i = q.popleft()

             if curr.left:
                 q.append((curr.left , 2*i))
             if curr.right:
                 q.append((curr.right, 2*i +1))
            if len(q)>1:

                answer= max(answer, q[-1][1]-q[0][1] +1)
        return answer

            


        

# we will implimet it later
# this sis  the fine for today


