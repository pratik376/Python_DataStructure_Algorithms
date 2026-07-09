def heapify_max(nums,n,index):

    largest=index
    left_child_index= 2 * index +1
    right_child_index= 2 * index +2

    if left_child_index < n and nums[left_child_index] > nums[largest]:
        largest=left_child_index
    
    if right_child_index < n and nums[right_child_index] > nums[largest]:
        largest= right_child_index
    
    if largest != index:
        nums[largest], nums[index]= nums[index], nums[largest]
        heapify_max(nums,n,largest)

# recursive




def heapify_max(nums,n,index):

    while True:

        largest=index
        left_child_index= 2 * index +1
        right_child_index= 2 * index +2

        if left_child_index < n and nums[left_child_index] > nums[largest]:
            largest=left_child_index
        
        if right_child_index < n and nums[right_child_index] > nums[largest]:
            largest= right_child_index
        
        if largest== index:
            break
        
        if largest != index:
            nums[largest], nums[index]= nums[index], nums[largest]
            index= largest
