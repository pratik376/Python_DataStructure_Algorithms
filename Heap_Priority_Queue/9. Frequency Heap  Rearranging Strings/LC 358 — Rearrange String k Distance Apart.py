from typing import List
from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        count= Counter(barcodes)
        
        