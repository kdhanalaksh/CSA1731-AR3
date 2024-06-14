def dfs_iterative(graph, start_node):
    visited = set()
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# Example usage
if __name__ == "__main__":
    # Graph representation (adjacency list)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B'],
        'E': ['B', 'H'],
        'F': ['C'],
        'G': ['C'],
        'H': ['E']
    }
    
    # Perform DFS (Iterative)
    print("Iterative DFS:")
    dfs_iterative(graph, 'A')
