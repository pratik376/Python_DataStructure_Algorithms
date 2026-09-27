def dfs(start):

    if start == len(s):
        ans.append(path.copy())
        return

    for end in range(start + 1, len(s) + 1):

        piece = s[start:end]

        if valid(piece):
            path.append(piece)
            dfs(end)
            path.pop()