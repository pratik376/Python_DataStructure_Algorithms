def repeatedSubstringPattern(s: str) -> bool:
    # Trick: if you take s+s and remove the first and last character,
    # the original string will appear in it if it has a repeated pattern
    return s in (s + s)[1:-1]

# Example usage:
s = "abccba"
print(repeatedSubstringPattern(s))  # Output: False

s2 = "abcabc"
print(repeatedSubstringPattern(s2))  # Output: True



def repeated(s:str) -> bool:

    return s in (s+s) [1:-1]