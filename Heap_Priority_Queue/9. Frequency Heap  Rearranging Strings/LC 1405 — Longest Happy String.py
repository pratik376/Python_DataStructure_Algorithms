from collections import Counter
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        Maxheap=[]
        arr= [(-a, 'a'),(-b,'b'),(-c,'c')]

        for count, char in arr:

            if count:
                heapq.heappush(Maxheap,(count,char))

        heapq.heapify(Maxheap)

        res=[]
   

        while Maxheap:

            freq, char =heapq.heappop(Maxheap)
            freq= -freq

            if len(res)>=2 and res[-1]==res[-2]==char:

                if not Maxheap:
                    break

                freq2, char2= heapq.heappop(Maxheap)
                freq2=-freq2

                res.append(freq2)
                freq2-=1

                if freq2 >0:
                    heapq.heappush(Maxheap,(freq2,char2))

                heapq.heappush(Maxheap,(-freq,char))

            else:
                res.append(char)
                freq-=1

                if freq:
                    heapq.heappush(Maxheap,(freq,char))
    
        return ''.join(res)

            
            


            
            




        