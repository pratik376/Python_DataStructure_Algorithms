

def remove_duplicate_sorted_array(arr):

    i,j=0,1
    count=1

    while (j< len(arr)):

        if arr[i] != arr[j] :
            i+=1
            arr[i]=arr[j]
            
            count+=1  # or you can last return i+1

        j+=1

    return count


nums = [-3, -3, -1, 0, 0, 2, 2, 2]

print(remove_duplicate_sorted_array(nums))