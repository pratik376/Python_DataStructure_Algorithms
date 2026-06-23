# Definition for a binary tree node.
from typing import List, Optional







class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        stack=[]

        curr_sum=0

        level_node=[]

        answer=[]

        curr= root


        while curr or stack:

            while curr:

                curr_sum+=curr.val
                level_node.append(curr.val)

                if not curr.left and not curr.right:

                    if curr_sum == targetSum:
                        answer.append(level_node.copy())
                stack.append((curr,curr_sum, level_node.copy()))
                curr=curr.left
            
            
            curr, curr_sum, level_node = stack.pop()
            curr=curr.right
        
        return answer
            

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

       
       stack=[(root, root.val, [root.val])]

       answer=[]

       while stack:
           
           curr, curr_sum, path= stack.pop()

           if not curr.left and not curr.right:
               
               if curr_sum == targetSum:
                   answer.append(path)

           if curr.right:
               
               stack.append(
                   (curr.right, curr_sum+curr.right, path  + [curr.right.val])
               )
           if curr.left:
               stack.append(
                   (curr.left, curr_sum+curr.left, path + [curr.left.val])
               )

       return answer
                      


      
            

        