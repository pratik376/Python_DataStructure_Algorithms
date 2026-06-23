
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        


        def myinvert(root):

            if not root:
                return None

            myinvert(root.left)
            myinvert(root.right)

            temp=root.right
            root.right=root.left
            root.left= temp

            return root  
        
        return myinvert(root)

        
    


from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        q=deque([root])

        while q:

            curr= q.popleft()

            curr.left, curr.right= curr.right, curr.left

            if curr.left:
                q.append(curr.left)
            
            if curr.right:
                q.append(curr.right)
        
        return root

        
    
