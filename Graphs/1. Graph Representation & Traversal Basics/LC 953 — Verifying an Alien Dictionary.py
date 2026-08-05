from typing import List
from collections import defaultdict

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        ordrInd= {c:i for i,c in enumerate(order)}
        
        