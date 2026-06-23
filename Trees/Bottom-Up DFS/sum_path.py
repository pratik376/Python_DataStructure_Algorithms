# Definition for a binary tree node.
from typing import Optional

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        
        def dfs(node, currSum):

            if not node:
                return False
            
            currSum+=node.val

            if not node.left and not node.right:
                return currSum==targetSum
            
            return (dfs(node.left,currSum) 
                    or
            dfs(node.right,currSum ))
        
        return dfs(root,0)

                


# Definition for a binary tree node.
from typing import Optional

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


       if not root:
           return False 
       
       stack= [[root,root.val]]

       while stack:
           
           curr, curr_sum= stack.pop()

           if not curr.left and not curr.right:
               
               if curr_sum==targetSum:
                   return True
               
           if curr.right:
               stack.append([curr.right, curr.right.val+ curr_sum])
           if curr.left:
               stack.append([curr.left, curr.left.val + curr_sum])

       return False           
                   




from typing import Optional

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = []
        curr = root
        currSum = 0

        while curr or stack:

            # Go as left as possible
            while curr:
                currSum += curr.val

                # Preorder: process current node first
                if not curr.left and not curr.right:
                    if currSum == targetSum:
                        return True

                # Save current node and current path sum
                stack.append((curr, currSum))

                curr = curr.left

            # Backtrack
            node, currSum = stack.pop()

            # Move to right subtree
            curr = node.right

        return False