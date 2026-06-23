# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        stack= [[root,1]]

        answer=float('inf')

        while stack:

            curr, depth = stack.pop()

            if not curr.left and not curr.right:
                answer=min(answer, depth)
            
            if curr.left:
                stack.append([curr.left, depth+1])

            if curr.right:
                stack.append([curr.right, depth+1])   

        return answer         




    

        