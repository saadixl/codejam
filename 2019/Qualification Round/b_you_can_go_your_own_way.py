grid = []
original_grid = []

def init_grid(n, p):
    for i in range(n):
        row = []
        bow = []
        for j in range(n):
            row.append("O")
            bow.append("O")
        grid.append(row)
        original_grid.append(bow)

def fill_grid(p):
    row = 0
    col = 0
    for i in range(len(p)):
        if(p[i] == 'S'):
            row = row + 1
        if(p[i] == 'E'):
            col = col + 1
        grid[row][col] = 'L'
        original_grid[row][col] = 'L'

def print_grid():
    for r in grid:
        print(r)

def maze(n):
    row = 0
    col = 0
    path = ""
    stepped_on_lydia = False

    while grid[n-1][n-1] != "X":
        # if already reached, break
        if row == n-1 and col == n-1:
            break

        # going to empty on South
        if row < n-1 and grid[row+1][col] == "O" and len(path) < (2*n)-2:
            grid[row+1][col] = "X"
            path += "S"
            row = row + 1
            stepped_on_lydia = False

        # going to empty on East
        elif col < n-1 and grid[row][col+1] == "O" and len(path) < (2*n)-2:
            grid[row][col+1] = "X"
            path += "E"
            col = col + 1
            stepped_on_lydia = False

        # stepping on lydia on South
        elif row < n-1 and grid[row+1][col] == "L" and stepped_on_lydia == False and len(path) < (2*n)-2:
            grid[row+1][col] = "X"
            path += "S"
            row = row + 1
            stepped_on_lydia = True

        # stepping on lydia on East
        elif col < n-1 and grid[row][col+1] == "L" and stepped_on_lydia == False and len(path) < (2*n)-2:
            grid[row][col+1] = "X"
            path += "E"
            col = col + 1
            stepped_on_lydia = True

        # if can't go forward, then go back and mark path as wrong
        else:
            stepped_on_lydia = False
            grid[row][col] = "W"
            if path == "":
                row = 0
                col = 0
            else:
                last_move = path[-1]
                path = path[0:-1]
                if last_move == "E":
                    col = col -1
                else:
                    row = row - 1
            # If back to beginning, then restart
            if row == 0 and col == 0:
                grid[row][col] = "X"

            if original_grid[row][col] == "L":
                stepped_on_lydia = True

    return path

t = input()
for i in range(int(t)):
    n = int(input())
    p = input()
    init_grid(n, p)
    # Filling grid with lydias path
    fill_grid(p)
    # print_grid()
    # print("================================")
    result = maze(n)
    # print_grid()
    grid = []
    original_grid = []
    print("Case #"+str(i+1)+": "+result)
