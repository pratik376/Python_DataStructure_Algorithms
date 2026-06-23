def max_avg(arr,k):

    sum=0

    

    for i in range(k):
        sum+= arr[i]

    answer=sum/k


    for j in range(k, len(arr)):

        sum+=arr[j]
        sum-= arr[j-k]

        avg=sum/k

        answer=max(answer,avg)
    return answer        
