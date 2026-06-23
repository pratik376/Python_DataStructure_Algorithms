# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return root
        
        curr=root

        while curr:

            if val < curr.val:
                curr=curr.left
            elif val > curr.val:
                curr=curr.right
            else:
                return curr
            
        return None
        