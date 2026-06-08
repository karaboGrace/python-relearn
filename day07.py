grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]
# Outer loop goes through each vertical level (y)
for y in range(len(grid[0])):
    
    # Inner loop goes through each horizontal column (x)
    for x in range(len(grid)):
        # Print the character at x,y without dropping to a new line
        print(grid[x][y], end="")
        
    print()