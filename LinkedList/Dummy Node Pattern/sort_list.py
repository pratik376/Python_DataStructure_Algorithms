class ListNode:

    def __init__(self, val=0, next=None):

        self.val=val
        self.next=None

class Solution:

    def sortList(self, head:ListNode)-> ListNode:

        if not head and not head.next:
            return head

        left=head
        right=self.getMid(head)

        temp= right.next
        right.next=None
        right=temp


        left=self.sortList(left)
        right= self.sortList(right)

        return self.merge(left,right)



    def getMid(self, head):

        slow, fast = head, head.next

        while fast or fast.next:

            fast=fast.next.next
            slow=slow.next
        return slow       

    def merge(self, left, right):
        tail=dummy= ListNode()

        while left and right:

            if left.val < right.val:
                tail.next=left
                left=left.next

            else:
                tail.next=right
                right=right.next

            tail=tail.next

        tail.next= left if left  else right

        return dummy.next            



        