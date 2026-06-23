
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)

        curr=root

        while curr.left or curr.right:

            if val > curr.val and curr.right:
                curr=curr.right
            elif val < curr.val and curr.left:
                curr=curr.left
            else:
                break
        
        if val< curr.val:
            curr.left=TreeNode(val)
        else:
            curr.right=TreeNode(val)  
        
        return root

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)

        curr=root

        while True:

            if val > curr.val:

                if not curr.right:
                    curr.right= TreeNode(val)
                    return root
                curr=curr.right
            else:

                if not curr.left:
                    curr.left= TreeNode(val)
                    return root
                curr=curr.left
        


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root

        