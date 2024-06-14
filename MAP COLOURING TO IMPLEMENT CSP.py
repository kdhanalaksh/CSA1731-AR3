def is_valid_coloring(node, color, graph, colors):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def map_coloring(graph, colors, node, color_assignment):
    if node == len(graph):
        return True
    
    for color in colors:
        if is_valid_coloring(node, color, graph, color_assignment):
            color_assignment[node] = color
            if map_coloring(graph, colors, node + 1, color_assignment):
                return True
            color_assignment[node] = None
    
    return False

def solve_map_coloring(graph, colors):
    color_assignment = [None] * len(graph)
    if not map_coloring(graph, colors, 0, color_assignment):
        return "No solution exists"
    return color_assignment

# Example usage
if __name__ == "__main__":
    # Graph representation (adjacency list)
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2]
    }
    
    # Available colors
    colors = ['Red', 'Green', 'Blue']
    
    # Solve the map coloring problem
    solution = solve_map_coloring(graph, colors)
    print("Color Assignment:", solution)
