
from collections import defaultdict
def longest_substring(s):

    left=0
    freq=defaultdict(int)
    max_length=0


    for right in range(len(s)):

        freq[s[right]]+=1

        while freq[s[right]]>1:
            freq[s[left]]-=1
            left+=1

        max_length=max(right-left+1, max_length)

    return max_length        

def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}  # stores last seen index of characters
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            # character repeats, move left pointer
            left = char_index[char] + 1
        char_index[char] = right  # update last seen index
        max_length = max(max_length, right - left + 1)

    return max_length


def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        while char in seen:
            seen.remove(s[left])
            left += 1
        seen.add(char)
        max_len = max(max_len, right - left + 1)

    return max_len