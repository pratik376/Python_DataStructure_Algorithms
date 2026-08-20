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

# Graph given as adjacency list / edge list
# → Time usually O(V + E)
# → Space usually O(V + E) if you build/store adjacency list

# Grid of m × n cells
# → Time usually O(mn)
# → Space usually O(mn) worst case