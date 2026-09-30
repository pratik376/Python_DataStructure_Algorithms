class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:

        mapping = {}
        used = set()

        def dfs(i, start):

            # consumed entire pattern
            if i == len(pattern):
                return start == len(s)

            # string finished but pattern remains
            if start == len(s):
                return False

            ch = pattern[i]

            # CASE 1:
            # this pattern character already has a mapping
            if ch in mapping:

                word = mapping[ch]

                # remaining string must start with that mapping
                if not s.startswith(word, start):
                    return False

                return dfs(i + 1, start + len(word))


            # CASE 2:
            # character has no mapping yet
            # try every possible substring
            for end in range(start + 1, len(s) + 1):

                piece = s[start:end]

                # another pattern character already uses this substring
                if piece in used:
                    continue

                # choose
                mapping[ch] = piece
                used.add(piece)

                # explore
                if dfs(i + 1, end):
                    return True

                # undo
                del mapping[ch]
                used.remove(piece)

            return False

        return dfs(0, 0)