def searchMatrix(matrix, target):
    r,c= 0, len(matrix[0])-1

    while (c>=0 and r< len(matrix[0])):

        if matrix[r][c]== target:
            return True
        elif matrix[r][c] < target:
            r+=1
        else:
            c-=1

    return False            