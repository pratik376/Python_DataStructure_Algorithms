def longestNiceSubstring(s: str) -> str:
    if len(s) < 2:
        return ""

    chars = set(s)

    for i, c in enumerate(s):
        if c.lower() not in chars or c.upper() not in chars:
            left = longestNiceSubstring(s[:i])
            right = longestNiceSubstring(s[i+1:])
            return left if len(left) >= len(right) else right

    return s
