
# its not necessary to use hasmap always

def PartionSubArray(arr):

    if len(arr)<3:
        return False
    
    toatal_sum=sum(arr)

    if toatal_sum %3 != 0:
        return False
    
    target= toatal_sum//3  # this gives integer answer
    currSum=0
    count=0

    for  num in (arr):

        currSum+= num

        if currSum== target:
            count+=1
            currSum=0

    return True if count>=3 else False


def partitionArray(arr):
    if len(arr) < 3:
        return False
    total_sum = sum(arr)
    if total_sum % 3 != 0:
        return False

    target = total_sum // 3
    currSum = 0
    count = 0

    for i, num in enumerate(arr):
        currSum += num
        if currSum == target:
            count += 1
            currSum = 0
            if count == 2:
                # check if remaining elements sum to target
                remaining_sum = sum(arr[i+1:])
                return remaining_sum == target
    return False


