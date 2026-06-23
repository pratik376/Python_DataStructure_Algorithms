from collections import defaultdict

def CountCompleteSubarray(arr):

    k= len(set(arr))

    def atMost(k):

        if  k<0:
            return 0
        
        answer=0
        left=0
        freq=defaultdict(int)
        for right in range(len(arr)):

            freq[arr[right]]+=1

            while len(freq) > k:

                freq[arr[left]]-=1

                if freq[arr[left]] == 0:
                    del freq[arr[left]]

                left+=1
            answer+=(right- left +1)
        return answer
    return atMost(k)- atMost(k-1)            

        
