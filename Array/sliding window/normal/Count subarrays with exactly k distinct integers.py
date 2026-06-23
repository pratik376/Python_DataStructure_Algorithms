from collections import defaultdict
def countSubarray(arr, k):

    def atMostK(k):

        if k<1:
            return 0
        
        left=0

        freq= defaultdict(int)  
        answer=0

        for right in range(len(arr)):

            freq[arr[right]]+=1

            while len(freq) > k:

                freq[arr[left]]-=1

                if freq[arr[left]] ==0:
                    del freq[arr[left]]

                left+=1
            answer+=right-left+1      

        return answer
    return atMostK(k) - atMostK(k-1)          

