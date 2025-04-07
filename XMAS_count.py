def count_xmas_occurrences(grid):
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    word = "XMAS"
    length = len(word)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:
                for di, dj in directions:
                    ni, nj = i, j
                    matched = True
                    for k in range(1, length):
                        ni += di
                        nj += dj
                        if ni < 0 or ni >= rows or nj < 0 or nj >= cols:
                            matched = False
                            break
                        if grid[ni][nj] != word[k]:
                            matched = False
                            break
                    if matched:
                        count += 1
    return count

def main():
    with open('puzzle4.txt', 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    print(count_xmas_occurrences(grid))

if __name__ == "__main__":
    main()