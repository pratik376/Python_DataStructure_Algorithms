from typing import List
import heapq
from collections import defaultdict, Counter


from typing import List
from collections import Counter
import heapq

class ReverseWord:
    def __init__(self, word: str):
        self.word = word

    def __lt__(self, other: "ReverseWord") -> bool:
        # reverse alphabetical order:
        # "z" < "a" in heap terms
        return self.word > other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        heap = []

        for word, count in freq.items():
            # smaller count is worse
            # if count ties, lexicographically larger word is worse
            heapq.heappush(heap, (count, ReverseWord(word), word))

            if len(heap) > k:
                heapq.heappop(heap)

        # heap now contains the best k words, but not in final order
        result = []
        while heap:
            count, _, word = heapq.heappop(heap)
            result.append(word)

        # popped from worst -> best, so reverse to get best -> worst
        return result[::-1]

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq=Counter(words)

        return sorted(freq.keys(), key=lambda w : (-freq[w],w))[:k]
        
        
            
        
        
        
        
        
