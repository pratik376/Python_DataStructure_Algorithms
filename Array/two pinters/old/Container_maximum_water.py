

def containerWithMaximumWater(arr):

    i,j=0,len(arr)-1
    max_area=0
    area=0

    while(i<j):
        area= (j-i) * min(arr[i],arr[j])
        max_area=max(max_area,area)

        if (arr[i]<arr[j]):
            i+=1
        elif(arr[j]<arr[i]):
            j-=1
        else:
            i+=1
            j-=1

    return max_area 

height = [2,3,4,5,18,17,6]

print(containerWithMaximumWater(height))

    
