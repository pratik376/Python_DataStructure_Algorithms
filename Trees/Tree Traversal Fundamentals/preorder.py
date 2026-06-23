# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        answer=[]

        def preorder(root):
            
            if not root:
                return
            
            answer.append(root.val)
            preorder(root.left)
            preorder(root.right)
        return answer    
    

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        answer=[]
        stack=[]
        curr= root

        while curr or stack:
            while curr:
                answer.append(curr.val)
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            curr=curr.right  # if curr else None No need because while condition make sure we push non null 
        return answer    


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        answer=[]
        stack=[]
        curr= root

        while curr or stack:
            if curr:
                answer.append(curr.val)
                stack.append(curr.right)
                curr=curr.left

            else:    
             curr=stack.pop()
             
        return answer    




        