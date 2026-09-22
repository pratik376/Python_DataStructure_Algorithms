def dfs(pos):

    if pos == n:
        ans.append("".join(path))
        return

    for choice in choices:
        if valid(choice):
            path.append(choice)
            dfs(pos + 1)
            path.pop()