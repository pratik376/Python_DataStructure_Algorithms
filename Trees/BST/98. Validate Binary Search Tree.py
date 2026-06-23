# Definition for a binary tree node.

from typing import Optional

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack=[]
        answer=[]

        curr=root

        while curr or stack:

            while curr:
                stack.append(curr)
                curr=curr.left
            
            curr=stack.pop()

            if answer and curr.val <=answer[-1]:
                return False
            answer.append(curr.val)
            curr=curr.right
 
        return True

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack=[]
        prev=None

        curr=root

        while curr or stack:

            while curr:
                stack.append(curr)
                curr=curr.left
            
            curr=stack.pop()

            if prev and prev.val >= curr.val:
                return False
            prev=curr
            curr=curr.right
 
        return True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float("-inf"), float("inf"))

        