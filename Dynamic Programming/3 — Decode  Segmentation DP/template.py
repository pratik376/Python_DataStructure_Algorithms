def dfs(i):

    if i == len(s):
        return ...

    answer = ...

    # try valid segment starting at i
    for end in range(i + 1, len(s) + 1):

        piece = s[i:end]

        if not valid(piece):
            continue

        answer = combine(
            answer,
            dfs(end)
        )

    return answer