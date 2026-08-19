visited = set()
components = 0

for node in all_nodes:

    if node not in visited:

        dfs(node)
        components += 1

def dfs(node):

    stack = [node]
    visited.add(node)

    while stack:

        node = stack.pop()

        for nei in graph[node]:

            if nei not in visited:
                visited.add(nei)
                stack.append(nei)