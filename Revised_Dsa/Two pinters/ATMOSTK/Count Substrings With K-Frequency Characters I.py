from collections import defaultdict
def numberOfSubstrings(self, s: str, k: int) -> int:

    

    def atMost(k):

        if k < 0:
            return 0
        
        left=0
        answer=0
        freq=defaultdict(int)


        for right in range(len(s)):

            freq[s[right]]+=1

            while len(freq) > k:

                freq[s[left]]-=1

                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
            answer+= (right-left+1)
        return answer
    return atMost(k)-atMost(k-1)            
    
    
