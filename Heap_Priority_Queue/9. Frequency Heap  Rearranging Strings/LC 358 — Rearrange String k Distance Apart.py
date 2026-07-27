from collections import Counter, deque
import heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:

        if k<=1:
            return s

        freq= Counter(s)

        max_heap= [(-count,char) for char,count in freq.items()]

        heapq.heapify(max_heap)

        q= deque()

        res=[]

        for i in range(s):

            while q and q[0][0] <= i:
               _,count,char =q.popleft()
               heapq.heappush(max_heap,(count,char))

            if not max_heap:
                return ""

            count, char= heapq.heappop(max_heap)
            res.append(char)
            count+=1

            if count<=0:
                q.append((i+k,count,char))

        return "".join(res)

            


