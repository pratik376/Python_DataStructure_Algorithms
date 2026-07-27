from typing import List
from collections import Counter
import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        count= Counter(barcodes)

        Maxheap=[(-freq,barcode) for barcode, freq in count.items() ]
        heapq.heapify(Maxheap)
        answer=[]

        prev_barcode =''
        prev_freq=0


        while Maxheap:

            freq, barcode = heapq.heappop(Maxheap)

            answer.append(barcode)
            freq += 1


            if prev_freq :
                heapq.heappush(Maxheap, (prev_freq,prev_barcode))

            prev_freq= freq
            prev_barcode= barcode

        return answer






        