import heapq

class SeatManager:

    def __init__(self, n: int):
         self.reserve_heap=[i for i in range(1,n+1)]    
        #  heapq.heapify(self.reserve)
        
            
    def reserve(self) -> int:
         
         return heapq.heappop(self.reserve_heap)
        

    def unreserve(self, seatNumber: int) -> None:
         heapq.heappush(self.reserve_heap,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)