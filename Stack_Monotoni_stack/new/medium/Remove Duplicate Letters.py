from collections import defaultdict


def RemoveDuplicate(str):

    stack = []
    seen = set()
    dict = defaultdict(int)

    for ch in str:
        dict[ch] += 1

    for ch in str:

        while (
            stack and ch < stack[-1]
        ):  # i am maintaing monotonic nature and i don't care same element repeats or not because it will remove during the set operation while maintainig smaller lexical order

            if ch in seen and dict[ch] > 1:
                continue

            else:

                last_char = stack[-1]

                if (
                    dict[last_char] > 1
                ):  # i will check if the same element appers in the future then only i will remove it other wise not need to remove
                    stack.pop()
                    dict[last_char] -= 1
                else:
                    break

        stack.append(ch)
        seen.add(ch)

    return " ".join(stack)


from collections import defaultdict

def RemoveDuplicate(s):

    stack = []
    seen = set()
    freq = defaultdict(int)

    for ch in s:
        freq[ch] += 1

    for ch in s:

        freq[ch] -= 1

        if ch in seen:
            continue

        while stack and ch < stack[-1] and freq[stack[-1]] > 0:
            removed = stack.pop()
            seen.remove(removed)

        stack.append(ch)
        seen.add(ch)

    return "".join(stack)