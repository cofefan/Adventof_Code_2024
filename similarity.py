import csv
from collections import Counter

def similarity_score(filename):
    left = []
    right = []

    # Read the file with tab-separated values
    

    with open(filename) as file:
        for row in file:
            parts = row.strip().split()  # splits on any whitespace
            if len(parts) >= 2:
                try:
                    left.append(int(parts[0]))
                    right.append(int(parts[1]))
                except ValueError:
                    print(f"Skipping invalid row: {row}")


    # Count occurrences of each number in the right list
    right_counter = Counter(right)

    # Calculate similarity score
    score = sum(num * right_counter[num] for num in left)

    return score


print("Similarity score:", similarity_score('puzzle.csv'))
