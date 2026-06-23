def numberOfSubarray(arr,k, threshold):


    window_sum=0
    sub_count=0


    for i in range(k):

        window_sum+= arr[i]

    answer= window_sum/k

    if answer>= threshold:
        sub_count+=1

    for j in range(k, len(arr)):

        window_sum+=arr[j]
        window_sum-= arr[j-k]

        answer= window_sum/k

        if answer>= threshold:
         sub_count+=1

    return sub_count     



