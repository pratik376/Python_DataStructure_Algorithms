# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        if not head:
            return []
        
        count=0

        temp=head

        while temp:
            count+=1
            temp=temp.next

        answer=[0] * (count+1)  # because we are using 1 based i
        stack=[] # (value, index)

        index=0

        while head:

            index+=1

            while stack and head.val > stack[-1][0]:

                _, stack_index = stack.pop()

                answer[stack_index]=head.val

            stack.append([head.val, index]) 

            head=head.next  

        return answer[1:]    

# now this is 0 based index 




        # Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        if not head:
            return []
        
        count=0

        temp=head

        while temp:
            count+=1
            temp=temp.next

        answer=[0] * (count) 
        stack=[] # (value, index)

        index=0

        while head:

            

            while stack and head.val > stack[-1][0]:

                _, stack_index = stack.pop()

                answer[stack_index]=head.val

            stack.append([head.val, index]) 
            index+=1
            head=head.next  

        return answer  