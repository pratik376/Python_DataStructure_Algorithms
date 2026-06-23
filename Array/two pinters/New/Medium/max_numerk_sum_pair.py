

# normal
# def max_k_pairs_sum(arr,k):
    
#     arr.sort()
#     left, right= 0, len(arr)-1
#     pairs=0
#     while (left < right):

#         if (arr[left]+arr[right]>k):

#             right-=1

#         elif(arr[left]+ arr[right]<k):

#             left+=1

#         else:
#             pairs+=1
#             left+=1
#             right-=1

#     return pairs


# nums = [5,5,5,5]
# k = 10

# print(max_k_pairs_sum(nums,k))



# indicies

def max_k_pairs_indices(arr, k):

    indexed=     [(val,idx) for idx, val in enumerate(arr)]
    indexed.sort()

    pairs=[]

    left,right=0, len(arr)-1

    while(left < right):
        sum= indexed[left][0]+ indexed[right][0]

        if (sum< k):
            left+=1
        elif (sum>k):
            right-=1
        else:
            pairs.append([indexed[left][1], indexed[right][1]])  
            left+=1
            right-=1

    return pairs

# def max_k_pairs_indices_hashmap(arr, k):
#     seen = {}  # value -> list of indices
#     pairs = []

#     for i, num in enumerate(arr):
#         complement = k - num

#         # Check if complement exists and has unused indices
#         if complement in seen and seen[complement]:
#             # Take one index from complement
#             j = seen[complement].pop()
#             pairs.append([j, i])
#         else:
#             # Store current index for future pairs
#             seen.setdefault(num, []).append(i)

#     return pairs
              


