class Puzzle8:
    def __init__(self, initial_state=None):
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        if initial_state:
            self.state = initial_state
        else:
            self.state = self.goal_state.copy()
        self.moves = 0

    def get_user_input(self):
        print("Enter the initial state of the puzzle row by row, use '0' for the blank tile:")
        self.state = []
        for _ in range(3):
            row = input().split()
            self.state.append([int(cell) for cell in row])

    def get_valid_moves(self):
        row, col = self.find_blank()
        valid_moves = []
        if row > 0:
            valid_moves.append((-1, 0))  # Move the blank tile up
        if row < 2:
            valid_moves.append((1, 0))   # Move the blank tile down
        if col > 0:
            valid_moves.append((0, -1))  # Move the blank tile left
        if col < 2:
            valid_moves.append((0, 1))   # Move the blank tile right
        return valid_moves

    def move(self, direction):
        row, col = self.find_blank()
        dr, dc = direction
        self.state[row][col], self.state[row + dr][col + dc] = self.state[row + dr][col + dc], self.state[row][col]
        self.moves += 1

    def find_blank(self):
        for i, row in enumerate(self.state):
            if 0 in row:
                return i, row.index(0)

    def __str__(self):
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.state)

# Example usage
puzzle = Puzzle8()
puzzle.get_user_input()
print("Entered puzzle:")
print(puzzle)
print("Valid moves:", puzzle.get_valid_moves())
