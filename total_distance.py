import csv

def total_distance(filename):
    left = []
    right = []

    with open(filename) as file:
            for line in file:
                parts = line.strip().split()  # splits on any whitespace
                if len(parts) >= 2:
                    left.append(int(parts[0]))
                    right.append(int(parts[1]))

    # Sort both lists
    left_sorted = sorted(left)
    right_sorted = sorted(right)

    # Calculate total distance
    total = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    return total

# Replace 'puzz.csv' with your actual file name if needed
print("Total distance:", total_distance('puzzle.csv'))
