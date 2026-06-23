


# def movie_zeros(arr):

#     left=0
#     right=0
#     n=len(arr)

#     while right<n:

#         if (arr[right]!=0 and arr[left]==0):
#             arr[right],arr[left]=arr[left],arr[right]
#             left+=1
#         if (arr[left]!=0 and left < right):
#             left+=1

#         right +=1  

#     return arr


def move_zeros(arr):

    left=0

    for right in range(len(arr)):

        if arr[right]!=0:
            arr[left],arr[right]= arr[right],arr[left]
            left+=1

    return arr



# # arr=[0, 1, 0, 1, 0, 1]
# # arr=movie_zeros(arr)

# print(arr)

