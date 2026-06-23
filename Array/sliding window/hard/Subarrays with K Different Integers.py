from collections import defaultdict

def subarray(arr,k):

    def Atmost(k):

        if k <1:
            return 0
        
        left=0
        count=0
        freq=defaultdict(int)

        for right in range(len(arr)):

            freq[arr[right]]+=1

            while len(freq)>k:   # this is the rule

                freq[arr[left]]-=1

                if not freq[arr[left]]:
                    freq.pop(arr[left])
                left+=1  

            count+=right-left+1 # we always count sub array so its also a rule right-left+1

        return count

    return Atmost(k)- Atmost(k-1)            






