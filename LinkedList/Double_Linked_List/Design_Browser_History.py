class ListNode:

    def __init__(self,val, prev=None, next= None):

        self.val= val
        self.prev=prev
        self.next=next


class BrowserHistory:

    def __init__(self, homepage:str):

        self.curr= ListNode(homepage)

    def visit (self, url) -> str:

        self.curr.next= ListNode(url, self.curr)
        self.curr= self.curr.next

    def back(self, steps: int) -> str:

        while self.curr.prev and steps > 0:
            self.curr= self.curr.prev
            steps-=1
        return self.curr.val

    def forward(self, steps: int) -> str:

        while self.curr.next and steps > 0:
            steps-=1
            self.curr= self.curr.next

        return self.curr          

        
        