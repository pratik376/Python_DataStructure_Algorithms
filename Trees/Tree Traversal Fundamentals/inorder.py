# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        answer=[]

        def inorder(root):

            if not root:
                return
            
            inorder(root.left)
            answer.append(root.val)
            inorder(root.right)
        
        inorder(root)

        return answer  
    


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res=[]
        stack=[]
        curr= root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=res.pop()
            res.append(curr.val)

            curr=curr.right

        return res        




        
    
         