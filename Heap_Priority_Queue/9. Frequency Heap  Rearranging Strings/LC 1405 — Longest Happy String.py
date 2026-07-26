from collections import Counter
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        arr= [('a', a),('b',b),('c',c)]

        Maxheap = [(-fre,char) for char, fre in arr]

        heapq.heapify(Maxheap)

        res=''
        prev_char=''
        prev_freq=0

        while Maxheap:

            freq, char =heapq.heappop(Maxheap)
            freq= -freq

            if freq >= 2:
                freq-=2
                res += char *2
            elif freq>0:
                freq-=1
                res+= char

            if prev_char !='' and prev_freq:

                heapq.heappush(Maxheap,(-prev_freq, prev_char))

            prev_char=char
            prev_freq=freq

        return res

            
            


            
            




        