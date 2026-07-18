import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap=[] # left
        self.min_heap=[] #right
        

    def addNum(self, num: int) -> None:

        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap,-num)
        else:
            heapq.heappush(self.min_heap, num)
        
        if len(self.max_heap) > len(self.min_heap) +1 :

            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))


    def findMedian(self) -> float:

        total_length= len(self.min_heap) + len(self.max_heap)
        answer=0

        if total_length %2 == 0:
            num1= -self.max_heap[0]
            num2= self.min_heap[0]

            answer= (num1 + num2)/2
        
        else:
            answer= -self.max_heap[0]
        
        return answer
        
        