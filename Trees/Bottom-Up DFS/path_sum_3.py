# Definition for a binary tree node.
from typing import Optional

from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:


        if not root:
            return 0

        prefix=defaultdict(int)
        result=0
        prefix[0]=1

        
        # state = 0 means "enter node"
        # state = 1 means "exit node" and remove its prefix sum

        stack= [(root, 0,0)]

        while stack:

            node, curr_sum, state= stack.pop()

            if state==0:
                curr_sum+= node.val

                result+= prefix[curr_sum-targetSum]
                prefix[curr_sum]+=1

                stack.append((node,curr_sum,1))

                if node.right:
                    stack.append((node.right,curr_sum,0))
                
                if node.left:
                    stack.append((node.left,curr_sum,0))

            else:
                prefix[curr_sum]-=1 

        return result           

from collections import defaultdict
from typing import Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        self.result = 0

        def dfs(node, curr_sum):
            if not node:
                return

            curr_sum += node.val
            self.result += prefix[curr_sum - targetSum]

            prefix[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            prefix[curr_sum] -= 1

        dfs(root, 0)
        return self.result