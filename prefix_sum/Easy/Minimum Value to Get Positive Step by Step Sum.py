def minimumValue(arr):

    min_value=arr[0]
    for i in range(1,len(arr)):

        arr[i]=arr[i-1]+arr[i]

        if arr[i] < min_value:
            min_value=arr[i]

    return max(1, (1- (min_value)))         # startvalue should be atleast 1


def minimumValue(arr):

    min_sum=arr[0]
    current_sum=arr[0]

    for i in range(1, len(arr)):
        current_sum+= arr[i]

        min_sum= min(current_sum,min_sum)

    return 1- min_sum    