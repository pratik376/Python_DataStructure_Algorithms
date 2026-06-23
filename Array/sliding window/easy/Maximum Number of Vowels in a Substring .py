def numberOfVowel(arr,k):
     vowel= {'a','e','i','o','u'}

     window_vowel=0
     max_result=float('-inf')
     l=0

     

     for j in range(k):
          window_vowel+=1 if arr[j] in vowel else 0

     max_result= window_vowel    

     for r in range(k, len(arr)):

          if arr[r] in vowel:
               window_vowel+=1

          if arr[l] in vowel:
               window_vowel-=1
          l+=1

          max_result=max(max_result,window_vowel)

     return max_result                      