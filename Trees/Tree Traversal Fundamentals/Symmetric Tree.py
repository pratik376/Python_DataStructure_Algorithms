# Definition for a binary tree node.
from typing import Optional

# think recursion returning calls
# think about null values
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def DFS(left, right):

            if not left and not right:
                return True
            
            if not left or not right:
                return False
            
            if left.val != right.val:
                return False
            
            return (
                DFS(left.left, right.right) and
                DFS(left.right,right.left)
            )
        if not root:
            return True

        return DFS(root.left,root.right)
        
# iterative


# Definition for a binary tree node.

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:


    def checkSymetric(self,q):

        elements=[]

        for node in q:

            elements.append(node.val)

        i=0
        j=len(elements)-1

        while i <=j:

            if elements[i]!=elements[j]:
                return False
            i+=1
            j-=1

        return True        
            
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return False

        q=deque([root])
        
    
        while q:
            levels= []

            for _ in range(len(q)):
                curr= q.popleft()

                if curr:
                    levels.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
                else:
                    levels.append(None)

            if levels != levels[::-1]:
                return False            
        return True
        



        


