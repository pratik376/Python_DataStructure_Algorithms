from collections import Counter
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        arr= [('a', a),('b',b),('c',c)]

        Maxheap = [(-fre,char) for char, fre in arr]

        heapq.heapify(Maxheap)

        res=[]
   

        while Maxheap:

            freq, char =heapq.heappop(Maxheap)
            freq= -freq

            

     

        return res

            
            


            
            




        