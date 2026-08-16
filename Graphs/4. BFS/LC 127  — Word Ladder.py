from typing import List
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        nei= defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):

                pattern= word[j:] + "*" + word[j+1:]
                wordList[pattern].append(word)

        visited= set()
        visited.add(beginWord)
        q=deque()
        q.append([beginWord])
        res=1

        while q:

              for i in range(len(q)):

                  word=q.popleft()

        