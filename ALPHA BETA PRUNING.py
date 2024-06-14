import math

def minimax(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or node.is_terminal_node():
        return node.evaluate(), None

    if maximizingPlayer:
        value = -math.inf
        best_move = None
        for child in node.get_children():
            score, _ = minimax(child, depth - 1, alpha, beta, False)
            if score > value:
                value = score
                best_move = child.move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value, best_move
    else:
        value = math.inf
        best_move = None
        for child in node.get_children():
            score, _ = minimax(child, depth - 1, alpha, beta, True)
            if score < value:
                value = score
                best_move = child.move
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value, best_move

# Example usage
class Node:
    def __init__(self, value, children=None, move=None):
        self.value = value
        self.children = children or []
        self.move = move

    def is_terminal_node(self):
        return len(self.children) == 0

    def evaluate(self):
        return self.value

    def get_children(self):
        return self.children

# Build a sample game tree
node1 = Node(3, [Node(5), Node(6)])
node2 = Node(2, [Node(7), Node(4)])
root = Node(1, [node1, node2])

# Call the minimax function
score, move = minimax(root, 2, -math.inf, math.inf, True)
print(f"Best move: {move}, Score: {score}")
