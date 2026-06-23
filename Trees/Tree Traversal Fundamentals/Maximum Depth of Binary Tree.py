# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))


# solution 2 BFS


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        q=deque([root])
        level=0
        curr= root

        while q:


            for  _ in range(len(q)):

                curr=q.popleft()

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            curr+=1
        return level            




# solution 3 DFS


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        stack=[[root,1]]
        res=0

        while stack:

            node, depth= stack.pop()

            if node:

                res= max(res,depth)
                stack.append([node.left, depth+1])
                stack.append([node.right,depth+1])

        return res        



        