testInput = 'puzzle4.txt'
prodInput = 'puzzle4.txt'

filePath = testInput

lines = []
with open(filePath) as f:
    for line in f:
        lines.append(line.rstrip())

xMax = len(lines[0])
yMax = len(lines)

wordCount = 0
for y in range(1, yMax - 1):
    for x in range(1, xMax - 1):
        if lines[y][x] == 'A':
            # Check all 8 directions for MAS patterns
            directions = [
                
                lines[y-1][x+1],  # NE
                
                lines[y+1][x+1],  # SE
                
                lines[y+1][x-1],  # SW
                
                lines[y-1][x-1]   # NW
            ]
            
            # Check for X patterns formed by perpendicular MAS sequences
            # NE-SW diagonal
            if (directions[0] == 'M' and directions[2] == 'S') or \
               (directions[0] == 'S' and directions[2] == 'M'):
                # Check NW-SE diagonal
                if (directions[3] == 'M' and directions[1] == 'S') or \
                   (directions[3] == 'S' and directions[1] == 'M'):
                    wordCount += 1
            
            # Also check N-S and E-W directions
            elif (directions[0] == 'M' and directions[1] == 'S') or \
                 (directions[0] == 'M' and directions[1] == 'S'):
                if (directions[2] == 'M' and directions[3] == 'S') or \
                   (directions[2] == 'M' and directions[3] == 'S'):
                    wordCount += 1

print(f"Number of X-MAS patterns found: {wordCount}")