
def string_subsequent(word, s):
    i = j = 0
    while i < len(word) and j < len(s):
        if word[i] == s[j]:
            i += 1
        j += 1
    return i == len(word)


count=""





def longest_subsequence(my_str, d):

    for word in d:

        if string_subsequent(word,my_str):

            if(len(word) > len(count) or (len(word)== len(count) and word < count)) :

                count=word

    return count            
