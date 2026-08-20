dfs(node, parent)

for nei in adj[node]:

    if nei not in visited:
        dfs(nei, node)

    elif nei != parent:
        # cycle