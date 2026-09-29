def dfs(r, c):

    if goal:
        return True

    mark_visited(r, c)

    for dr, dc in directions:

        nr = r + dr
        nc = c + dc

        if valid(nr, nc):
            if dfs(nr, nc):
                return True

    unmark_visited(r, c)

    return False