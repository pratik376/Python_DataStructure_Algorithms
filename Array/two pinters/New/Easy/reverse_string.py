from typing import List


def reverse_string(s: List[str]):
    
    left=0
    right=len(s)-1
    while (left < right):
        s[left], s[right]= s[right],s[left]
        left +=1
        right-=1

    return s


str="pratikbabariyathegreat"
print(reverse_string(str))