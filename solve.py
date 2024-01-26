# Define the board to move the 1-2-3 puzzle on
# # is the (wide) border around the board to make sure that
# the player does not step out of the board
# S is the starting position
# F is the end position
board = [
    '############',
    '############',
    '############',
    '###S########',
    '###      ###',
    '### # ## ###',
    '### #    ###',
    '### # ## ###',
    '### ####F###',
    '### #### ###',
    '###      ###',
    '############',
    '############',
    '############',
    '############',
]

# Find the starting position on the board
def startPosition(board):
    for y in range(0, len(board)):
        for x in range(0, len(board[y])):
            if board[y][x] == 'S':
                return (x, y,)

    raise ValueError("No valid start position")

# Find the end position on the board
def endPosition(board):
    for y in range(0, len(board)):
        for x in range(0, len(board[y])):
            if board[y][x] == 'F':
                return (x, y,)

    raise ValueError("No valid end position")

# Move to the new (x, y) position according to dir and step
def move(x, y, dir, step):
    # Directions are 1 to 4
    # 1 = down
    # 2 = right
    # 3 = up
    # 4 = left

    if dir == 1:
        y += step
    elif dir == 2:
        x += step
    elif dir == 3:
        y -= step
    elif dir == 4:
        x -= step

    return (x, y, )

# Determine if any of the paths has reached the end position
# If true, return the description of the path from start to finish
def hasReached(board, start, paths):
    (sx, sy,) = start
    for path in paths:
        (x, y) = (0, 0)
        for idx, dir in enumerate(path):
            step = (idx % 3)+1
            (x, y, ) = move(x, y, dir, step)

        if board[y+sy][x+sx] == 'F':
            describe = ""
            (x, y) = (0, 0)
            describe += f"Start at ({x}, {y})\n"
            for idx, dir in enumerate(path):
                step = (idx % 3)+1
                (x, y, ) = move(x, y, dir, step)
                if dir == 1:
                    describe += f"Down {step} to ({x}, {y})\n"
                elif dir == 2:
                    describe += f"Right {step} to ({x}, {y})\n"
                elif dir == 3:
                    describe += f"Up {step} to ({x}, {y})\n"
                elif dir == 4:
                    describe += f"Left {step} to ({x}, {y})\n"

            return (True, describe)

    return (False, "")

# Check to see if direction dir can be added to path
def canadd(board, start, path, dir):
    (sx, sy,) = start
    newpath = path + [dir]
    been = { }
    (x, y) = (0, 0)
    for idx, dir in enumerate(newpath):
        step = (idx % 3)+1
        for s in range(0, step):
            (x, y, ) = move(x, y, dir, 1)

            if not (board[y+sy])[x+sx] in ' SF':
                return False

        b = f"{x}{y}{step}"
        if b in been:
            return False

        been[b] = 1

    return True

# Main entry point
def main():
    paths = [[]]

    start = startPosition(board)
    end = endPosition(board)

    while True:
        (reached, description,) = hasReached(board, start, paths)
        if reached:
            print(description)
            exit()

        paths = [ path + [dir]
                 for path in paths
                 for dir in range(1, 5)
                 if canadd(board, start, path, dir)
                ]

if __name__ == "__main__":
    main()
