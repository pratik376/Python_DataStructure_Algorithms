# Time: O(n) Space: O(1)

def container_with_most_water(arr):

    left, right= 0, len(arr)-1

    area=0

    while(left < right):
        
        new_area=(right-left) * min(arr[left],arr[right])
        if (new_area> area):
            area=new_area

        if( arr[left]< arr[right]):
            left+=1
        elif (arr[left]==arr[right]):
            left+=1
            right-=1

        else:
            right-=1

    return area           



heights =  [1,8,6,2,5,4,8,3,7]

print(container_with_most_water(heights))




