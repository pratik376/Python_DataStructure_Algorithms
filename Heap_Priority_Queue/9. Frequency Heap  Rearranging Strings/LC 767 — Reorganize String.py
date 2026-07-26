from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        freq= Counter(s)

        Maxheap= [(-value,key)  for key, value in freq.items()]

        heapq.heapify(Maxheap)
        res=[]

        prev_char=''
        prev_freq=0


        while Maxheap:

            value, char =heapq.heappop(Maxheap)

            if prev_char !='' and prev_freq:
                heapq.heappush(Maxheap,(prev_freq,prev_char))

            res.append(char)
            value+=1

            prev_char=char
            prev_freq=value

        if prev_freq:
            return ""

        return "".join(res)
        







        