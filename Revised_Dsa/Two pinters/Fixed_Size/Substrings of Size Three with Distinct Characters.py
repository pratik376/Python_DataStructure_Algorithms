from collections import defaultdict

def substringsOfsize(str):

    if len(str)< 3:
        return 0

    freq=defaultdict(int)
    my_count=0

    for i in range(3):

        freq[str[i]]+=1

    if len(freq)==3:
        my_count+=1

    for j in range(3, len(str)):
         freq[str[j]]+=1
         freq[str[j-3]] -=1

         if freq[str[j-3]] ==0:
             del freq[str[j-3]]


         if len(freq) ==3:
             my_count+=1

    return my_count         

            


