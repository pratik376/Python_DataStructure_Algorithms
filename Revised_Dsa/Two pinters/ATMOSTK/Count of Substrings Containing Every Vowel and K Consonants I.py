from collections import defaultdict
def countOfSubstrings(self, word: str, k: int) -> int:

    def atLeast(k):

        if k < 0:
            return 0
        
        left=0
        vowel=set("aeiou")
        consonants=0
        answer=0
        freq= defaultdict(int)

        for right in range(len(word)):

            ch= word[right]

            if ch in vowel:
                freq[ch]+=1
                
            else:
                consonants+=1

            while len(freq)==5 and consonants>= k:

                left_word= freq[left]
                if left_word in vowel:
                    freq[left_word]-=1

                    if freq[left_word]==0:
                     del vowel[word[left]]
                else:
                    consonants-=1
                left+=1
            answer+= left
        return answer
    return atLeast(k)- atLeast(k+1)            



#Easy rule to remember
#If the window is bad because it has too much, think atMost
#If the window is good because it has enough, think atLeast