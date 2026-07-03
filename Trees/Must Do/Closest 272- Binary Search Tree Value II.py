from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, root: Optional[TreeNode], target:float, k:int) -> list[int]:


        self.left_stack=[]
        self.right_stack=[]


        def inorder(node):

            if not node:
                return
            
            inorder(node.left)

            if node.val < target:
                self.left_stack.append(node.val)
            else:
                self.right_stack.append(node.val)
            
            inorder(node.right)
        inorder(root)

        answer=[]

        self.right_stack= self.right_stack[::-1]

        while len(answer) <k:

            if not self.left_stack:
                answer.append(self.right_stack.pop())
            
            if not self.right_stack:
                answer.append(self.left_stack.pop())
            
            elif abs(self.left_stack[-1]- target) < abs(self.right_stack[-1] - target):
                answer.append(self.left_stack.pop())
                
        return answer
