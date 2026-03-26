from collections import deque

def bfs(tree, start):
    visited = set()
    queue = deque([start])
    
    print("BFS Traversal:", end=" ")
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            
            # Add all neighbors to queue
            for neighbor in tree[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example tree (adjacency list)
tree = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6','7'],
    '4': [],
    '5': [],
    '6': [],
    '7':[]
}

bfs(tree, '1')