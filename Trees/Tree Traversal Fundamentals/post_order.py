# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postrderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        answer=[]

        def postOrder(root):

            if root == None:
                return
            
            postOrder(root.left)
            postOrder(root.right)
            answer.append(root.val)
        return answer



# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postrderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        from collections import deque

class Solution:
    def postorderTraversal(self, root):
        ans = deque()
        if root is None:
            return []

        stack = [root]

        while stack:
            popped = stack.pop()
            ans.appendleft(popped.val)

            if popped.left:
                stack.append(popped.left)

            if popped.right:
                stack.append(popped.right)

        return list(ans)  

        
