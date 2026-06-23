# revise this        
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return self.helper(s, 0, len(s), k)

    def helper(self, s, start, end, k):
        # base case
        if end - start < k:
            return 0

        # frequency count for current segment
        freq = [0] * 26
        for i in range(start, end):
            freq[ord(s[i]) - ord('a')] += 1

        # find a split character
        for mid in range(start, end):
            if freq[ord(s[mid]) - ord('a')] < k:
                left = self.helper(s, start, mid, k)
                right = self.helper(s, mid + 1, end, k)
                return max(left, right)

        # if no split character found → whole segment is valid
        return end - start
     

    




    

