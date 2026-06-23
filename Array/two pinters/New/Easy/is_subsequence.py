# Time: O(|t|) (or O(|s|+|t|)) Space: O(1)



def isSubsequence(s: str, t: str) -> bool:
    i = 0  # pointer for s
    j = 0  # pointer for t

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)