# Definition for a binary tree node.
from typing import Optional

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfAllLeaves(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        q=deque([root])
        my_sum=0


        while q:

            curr=q.popleft()

            if not curr.left and not curr.right:
                my_sum+=curr.val
            
            if curr.left:
                q.append(curr.left)
            
            if curr.right:
                q.append(curr.right)

        return  my_sum     




# Definition for a binary tree node.
from typing import Optional

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfAllLeaves(self, root: Optional[TreeNode]) -> int:
      

      if not root:
          return 0


      curr=root
      q=deque([root])

      window_sum=0


      while q:
          
          curr= q.popleft()

         

          if curr.left:
               
               if not curr.left.left and not curr.left.right:
                   window_sum += curr.left.val
                 
               q.append(curr.left)

          if curr.right:
              q.append(curr.right)

      return window_sum      
              






           


        