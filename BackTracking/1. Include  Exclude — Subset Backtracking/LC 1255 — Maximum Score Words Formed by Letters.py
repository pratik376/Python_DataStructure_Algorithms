from typing import List
from collections import defaultdict


class Solution:
    def maxScoreWords(
        self,
        words: List[str],
        letters: List[str],
        score: List[int]
    ) -> int:

        freq = defaultdict(int)

        for ch in letters:
            freq[ch] += 1


        def calculate_word(word, current_freq):

            temp = current_freq.copy()
            word_score = 0

            for ch in word:

                # not enough characters
                if temp[ch] == 0:
                    return 0, None

                temp[ch] -= 1

                idx = ord(ch) - ord('a')
                word_score += score[idx]

            return word_score, temp


        def dfs(i, current_freq):

            if i >= len(words):
                return 0


            # -------------------
            # EXCLUDE words[i]
            # -------------------

            exclude = dfs(
                i + 1,
                current_freq
            )


            # -------------------
            # INCLUDE words[i]
            # -------------------

            word_score, new_freq = calculate_word(
                words[i],
                current_freq
            )

            include = 0

            if new_freq is not None:

                include = word_score + dfs(
                    i + 1,
                    new_freq
                )


            return max(include, exclude)


        return dfs(0, freq)