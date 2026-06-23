from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None

        parent = None
        curr = root

        # Step 1: Find the node to delete
        while curr and curr.val != key:
            parent = curr

            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        # key not found
        if not curr:
            return root

        # Step 2: If curr has two children
        if curr.left and curr.right:
            successor_parent = curr
            successor = curr.right

            # find inorder successor: smallest node in right subtree
            while successor.left:
                successor_parent = successor
                successor = successor.left

            # copy successor value into curr
            curr.val = successor.val

            # now delete successor instead
            parent = successor_parent
            curr = successor

        # Step 3: curr now has at most one child
        if curr.left:
            child = curr.left
        else:
            child = curr.right

        # Step 4: Delete curr by connecting parent to child
        if not parent:
            # deleting root node
            return child

        if parent.left == curr:
            parent.left = child
        else:
            parent.right = child

        return root
    
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return root
        
        if key > root.val:
            root.right= self.deleteNode(root.right, key)
        elif key < root.val:
            root.left=self.deleteNode(root.left,key)
        
        else:

            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            curr=root.right

            while curr.left:
                curr=curr.left
            
            root.val= curr.val

            root.right= self.deleteNode(root.right, root.val)
        return root