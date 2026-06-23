def clean_string(s):
    return "".join(ch.lower() for ch in s if ch.isalnum())

def is_valid_palindrome(str):
    str =clean_string(str)
    

    left=0
    right=len(str)-1

    while(left<right):

        if (str[left] != str[right]):
            return "FALSE"
        left+=1
        right-=1

    return "TRUE" 



# ⭐ Bonus: O(1) Space Version (Advanced)

def is_valid_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


s = "   "

print(is_valid_palindrome(s))



