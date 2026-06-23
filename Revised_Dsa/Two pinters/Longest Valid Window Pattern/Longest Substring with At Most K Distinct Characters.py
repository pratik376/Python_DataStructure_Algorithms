from collections import defaultdict

def longestSubString(str,k):
        

        if k==0 or not str:
                return 0
                

        
        left=0
        answer=float('-inf')
        freq=defaultdict(int)

        for right in range(len(str)):
                
                freq[str[right]]+=1

                while len(freq) > k:
                        
                        freq[str[left]]-=1

                        if freq[str[left]]==0:
                                del freq[str[left]]
                        left+=1    
                answer= max(answer, right-left+1)   
        return answer                     

        