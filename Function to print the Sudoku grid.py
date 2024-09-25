# Function to print the Sudoku grid
def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

# Function to check if placing a number in the grid is valid
def is_valid(grid, row, col, num):
    # Check if the number is already in the row
    if num in grid[row]:
        return False

    # Check if the number is already in the column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check if the number is already in the 3x3 sub-grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    # If it's valid, return True
    return True

# Function to find an empty cell in the grid
def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:  # Empty cells are represented by 0
                return (i, j)  # Return the row, column of the empty cell
    return None  # No empty cells found

# Function to solve the Sudoku grid using backtracking
def solve_sudoku(grid):
    empty_cell = find_empty(grid)
    if not empty_cell:  # No empty cells left, puzzle is solved
        return True
    row, col = empty_cell

    # Try placing numbers 1-9 in the empty cell
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num  # Place the number

            if solve_sudoku(grid):  # Recursively attempt to solve the rest
                return True

            grid[row][col] = 0  # Backtrack (reset the cell)

    return False  # Trigger backtracking if no numbers work

# Main function to run the Sudoku solver
if __name__ == "__main__":
    # Example Sudoku grid (0 represents an empty cell)
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Sudoku Puzzle:")
    print_grid(sudoku_grid)

    # Solve the Sudoku puzzle
    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku Puzzle:")
        print_grid(sudoku_grid)
    else:
        print("No solution exists for the given Sudoku puzzle.")
