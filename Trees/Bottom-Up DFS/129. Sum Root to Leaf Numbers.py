# Definition for a binary tree node.
from typing import Optional

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        q=deque([(root,root.val)])
        answer=0


        while q:

            node, number= q.popleft()

            if not node.left and not node.right:
                
                answer+=number
                continue

            if node.left:

                temp= number *10
                q.append((node.left, temp+node.left.val))

            if node.right:
                temp= number *10
                q.append((node.right, temp+ node.right.val))

        return answer            
        