def find_empty(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return r, c
    return None

def valid(grid, num, pos):
    row, col = pos

    if num in grid[row]:
        return False

    if num in [grid[i][col] for i in range(9)]:
        return False

    block_x = col // 3 * 3
    block_y = row // 3 * 3

    for r in range(block_y, block_y + 3):
        for c in range(block_x, block_x + 3):
            if grid[r][c] == num:
                return False

    return True

def solve(grid):
    empty = find_empty(grid)
    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if valid(grid, num, (row, col)):
            grid[row][col] = num

            if solve(grid):
                return True

            grid[row][col] = 0

    return False

# sample grid to test
grid = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9],
]

solve(grid)

for row in grid:
    print(row)
