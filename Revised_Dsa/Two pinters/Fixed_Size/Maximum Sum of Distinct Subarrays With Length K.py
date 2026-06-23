from collections import defaultdict
def maximumSum(arr,k):

    if  len(arr) < k:
        return 0

    window_sum=0

    answer=0

    freq=defaultdict(int)

    for i in range(k):

        freq[arr[i]]+=1

        window_sum+=arr[i]

      

    if len(freq)==k:
        answer=window_sum

    for j in range(k, len(arr)):


        freq[arr[j]]+=1
        window_sum+= arr[j]
        window_sum-=arr[j-k]

        freq[arr[j-k]]-=1
        if freq[arr[j-k]]==0:
            del freq[arr[j-k]]
            
        if len(freq) == k:
           answer=max(answer, window_sum)

    return answer       



            