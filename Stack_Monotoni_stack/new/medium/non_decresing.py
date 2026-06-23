

def nonDecreasing(arr):

    pre_element= arr[0]

    count=0


    for i in range (1, len(arr)):

        if arr[i] < pre_element :
            count+=1
           

            if count >1:
                return False
            
            if i >= 2 and arr[i] < arr[i-2]:
             continue

        pre_element = arr[i]

    return True             

