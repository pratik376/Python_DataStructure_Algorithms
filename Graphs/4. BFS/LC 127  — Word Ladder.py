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

                  if word == endWord:
                      return res

                  for j in range(len(word)):
                      pattern= word[j:] + "*" + word[j+1:]

                      for words in nei[pattern]:

                          if words not in visited:
                              visited.add(words)
                              q.append(words)
              res+=1
        return 0

                      

from typing import List
from collections import deque

class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> int:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        q = deque()
        q.append((beginWord, 1))

        visited = set()
        visited.add(beginWord)

        while q:

            word, length = q.popleft()

            if word == endWord:
                return length

            # Change each position one at a time
            for i in range(len(word)):

                # Try every possible letter
                for char in "abcdefghijklmnopqrstuvwxyz":

                    newWord = word[:i] + char + word[i + 1:]

                    if newWord in wordSet and newWord not in visited:

                        visited.add(newWord)
                        q.append((newWord, length + 1))

        return 0