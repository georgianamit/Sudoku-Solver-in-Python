grid = [[3,0,6,5,0,8,4,0,0],
        [5,2,0,0,0,0,0,0,0],
        [0,8,7,0,0,0,0,3,1],
        [0,0,3,0,1,0,0,8,0],
        [9,0,0,8,6,3,0,0,5],
        [0,5,0,0,9,0,6,0,0],
        [1,3,0,0,0,0,2,5,0],
        [0,0,0,0,0,0,0,7,4],
        [0,0,5,2,0,6,3,0,0]]

def colIsValid(col, value):
    for i in range(9):
        if grid[i][col] == value:
            return False
    else:
        return True

def rowIsValid(row, value):
    for i in range(9):
        if grid[row][i] == value:
            return False
    else:
        return True

def boxIsValid(row, col, value):
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

def getBox(n):
    if n in range(0,3):
        return 0
    if n in range(3,6):
        return 1
    if n in range(6,9):
        return 2

def display():
    for i in range(9):
        for j in range(9):
            print(grid[i][j]," ",end="")
        print()
    print()

def gridIsValid(row, col, value):
    return boxIsValid(row, col, value) and rowIsValid(row, value) and colIsValid(col, value)

def isSolved():
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return False
    else:
        return True

def solveSudoku(row,col):
    if isSolved():
        return True
    else:
        for i in range(row,9):
            col = col % 9
            for j in range(col,9):
                if grid[i][j] == 0:
                    for k in range(1,10):                                           
                        if gridIsValid(i, j, k):
                            grid[i][j] = k
                            # display()                           
                            if solveSudoku(i, j+1):
                                return True
                            grid[i][j] = 0
                    else:
                        return False
def main():
    if solveSudoku(0,0):
        display()
    else:
        print("No Solution")

if __name__ == "__main__":        
    main()

