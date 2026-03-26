def dls_for_iddfs(tree, node, limit, visited):
    if limit < 0:
        return
    
    print(node, end=" ")
    visited.add(node)
    
    for neighbor in tree[node]:
        if neighbor not in visited:
            dls_for_iddfs(tree, neighbor, limit - 1, visited)


def iddfs(tree, start, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nIDDFS Iteration with depth = {depth}:", end=" ")
        visited = set()
        dls_for_iddfs(tree, start, depth, visited)


# Same example tree
tree = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6','7'],
    '4': [],
    '5': [],
    '6': [],
    '7':[]
}

iddfs(tree, '1', 3)