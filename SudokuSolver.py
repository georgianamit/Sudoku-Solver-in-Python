# function for checking whether the column is valid or not
def colIsValid(grid, col, value):
    for i in range(9):
        if grid[i][col] == value:
            return False
    else:
        return True

# function for checking whether the row is valid or not
def rowIsValid(grid, row, value):
    for i in range(9):
        if grid[row][i] == value:
            return False
    else:
        return True

# function for checking whether the small 3 X 3 box is valid or not
def boxIsValid(grid, row, col, value):
    box_row = getBox(row)
    box_col = getBox(col)
    for i in range(0,3):
        row = (3 * box_row) + i
        for j in range(0,3):
             col = (3 * box_col) + j
             if grid[row][col] == value:
                 return False
    else:
        return True

# # function for getting the small boxes starting row and column
def getBox(n):
    if n in range(0,3):
        return 0
    if n in range(3,6):
        return 1
    if n in range(6,9):
        return 2

# function for displaying the sudoku board
def display(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j]," ",end="")
        print()
    print()

# function for checking whether the sudoku board(grid) is valid or not
def gridIsValid(grid,row, col, value):
    return boxIsValid(grid, row, col, value) and rowIsValid(grid, row, value) and colIsValid(grid, col, value)

# function for getting the unassigned locations
def getUnassignedLocation(grid,d):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                d['row'] = i
                d['col'] = j
                return True
    else:
        return False    

# recursive function for solving the sudoku using backtracking
def solveSudoku(grid):
    d = {'row': 0, 'col': 0}

    if not getUnassignedLocation(grid, d):
        return True
    
    for k in range(1,10):                                           
        if gridIsValid(grid, d['row'], d['col'], k):
            grid[d['row']][d['col']] = k
            # display(grid)                                        
            if solveSudoku(grid):
                return True
            grid[d['row']][d['col']] = 0
    else:
        return False

# main function
def main():  
    grid = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
            [6, 8, 0, 0, 7, 0, 0, 9, 0],
            [1, 9, 0, 0, 0, 4, 5, 0, 0],
            [8, 2, 0, 1, 0, 0, 0, 4, 0],
            [0, 0, 4, 6, 0, 2, 9, 0, 0],
            [0, 5, 0, 0, 0, 3, 0, 2, 8],
            [0, 0, 9, 3, 0, 0, 0, 7, 4],
            [0, 4, 0, 0, 5, 0, 0, 3, 6],
            [7, 0, 3, 0, 1, 8, 0, 0, 0]]
    
    if solveSudoku(grid):
        display(grid)
    else:
        print("No Solution")

if __name__ == "__main__":        
    main()

