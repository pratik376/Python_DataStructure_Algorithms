def maxavgsub(arr,k):
    sum=0
    max_sum= float("-inf")

    for i in range(k):
        sum+=arr[i]

    max_sum=sum

    for i in range(k, len(arr)):
        sum+=arr[i]-arr[i-k]
        max_sum=max(max_sum,sum)

    return max_sum/k      
