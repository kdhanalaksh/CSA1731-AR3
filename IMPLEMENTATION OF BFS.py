from collections import deque

def bfs(graph, start):
    """
    Perform BFS traversal on a graph.

    Parameters:
    graph (dict): The adjacency list representing the graph.
    start: The starting node for the BFS traversal.

    Returns:
    list: The list of nodes in the order they are visited.
    """
    # Initialize the queue with the start node and the set of visited nodes
    queue = deque([start])
    visited = set([start])
    order = []  # List to keep track of the traversal order

    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        order.append(node)

        # Iterate over all adjacent nodes
        for neighbor in graph[node]:
            if neighbor not in visited:
                # If the neighbor hasn't been visited, mark it visited and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)

    return order

# Example usage:
if __name__ == "__main__":
    # Define a graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    # Start BFS from node 'A'
    traversal_order = bfs(graph, 'A')
    print("BFS Traversal Order:", traversal_order)
