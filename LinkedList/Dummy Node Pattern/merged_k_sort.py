from typing import List


class ListNode:

    def __init__(self, val=0, next=None):

        self.val=val
        self.next= next


class Solution:

    def mergeKLists(self, lists:List[ListNode]) -> ListNode:

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:

            mergedList= []

            for i in range (0, len(lists),2):

                l1= lists[i]
                l2=lists[i+1] if i+1 < len(lists) else None
                mergedList.append(mergedList(l1,l2))
            lists=mergedList
        return lists[0]        


    def mergeList(self, list1 , list2):
        pass                  
        