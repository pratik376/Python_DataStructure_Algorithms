

def decodeString(str):

    nuber_stack=[]
    word_stack=[]
    current_string=""
    final_string=""
    char=''
    count=0

    for j in str:

        if j == ']':

            while word_stack and nuber_stack and word_stack[-1] != '[':
                char+= word_stack.pop()

                if count == 0:
                    count=nuber_stack.pop()

                if word_stack[-1]=='[':
                    word_stack.pop()
                    break

            current_string= count * char
            final_string+= current_string 
            count=0
            char=""
            current_string=''

        elif j.isdigit():
            
            nuber_stack.append(int(j))

        else:
            word_stack.append(j)

    return "".join(reversed(final_string))


s = "3[a2[c]]"
print(decodeString(s))




# this is the original and working solution

def decodeString(s):
    num_stack = []
    word_stack = []
    
    current_num = 0
    
    for ch in s:
        
        if ch.isdigit():
            current_num = current_num * 10 + int(ch)
        
        elif ch == '[':
            num_stack.append(current_num)
            word_stack.append('[')
            current_num = 0
        
        elif ch == ']':
            temp = ""
            
            while word_stack and word_stack[-1] != '[':
                temp = word_stack.pop() + temp
            
            word_stack.pop()  # remove '['
            
            repeat = num_stack.pop()
            expanded = temp * repeat
            
            # push back to stack (IMPORTANT)
            for c in expanded:
                word_stack.append(c)
        
        else:
            word_stack.append(ch)
    
    return "".join(word_stack)

# ✅ Correct way
# temp = ""
# temp = 'c' + ""   → "c"
# temp = 'b' + "c"  → "bc"
# temp = 'a' + "bc" → "abc"

# ✔ Final: "abc" ✅

# ❌ Your version
# temp = ""
# temp += 'c' → "c"
# temp += 'b' → "cb"
# temp += 'a' → "cba"

# ❌ Final: "cba" (reversed)