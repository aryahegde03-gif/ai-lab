def dfs(tree, node, visited=None):
    if visited is None:
        visited = set()
    
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        for neighbor in tree[node]:
            dfs(tree, neighbor, visited)

# Example tree (same as above)
tree = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6','7'],
    '4': [],
    '5': [],
    '6': [],
    '7': []
}

print("DFS Traversal:", end=" ")
dfs(tree, '1')