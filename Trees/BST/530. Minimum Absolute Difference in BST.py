# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        
        stack=[]
        answer= float('inf')
        prev=None

        curr=root

        while stack or curr:

            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
           
            if prev:
                answer= min(answer, abs(prev.val-curr.val)) # we don't need abs for curr.val- prev.val because in BST its sorted and alsways difference will be the positive
            
            prev=curr  
            curr=curr.right
        return answer