import heapq

class SeatManager:

    def __init__(self, n: int):
         self.reserve=[]

         for i in range(1,n):
              self.reserve.append(i)
        
         heapq.heapify(self.reserve)
        
            
    def reserve(self) -> int:
        

    def unreserve(self, seatNumber: int) -> None:
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)