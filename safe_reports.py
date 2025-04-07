def is_safe_report(levels):
    
    # Determine if the sequence is increasing, decreasing, or invalid
    is_increasing = None
    prev = levels[0]
    for current in levels[1:]:
        diff = current - prev
        if diff == 0:
            return False  # levels must be strictly increasing or decreasing
        if is_increasing is None:
            is_increasing = diff > 0
        else:
            if (diff > 0) != is_increasing:
                return False
        prev = current
    
    # Check all adjacent differences are between 1 and 3 in absolute value
    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i+1])
        if diff < 1 or diff > 3:
            return False
    
    return True

def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe_report(report):
            safe_count += 1
    return safe_count

def main():
    
    with open('puzzle2.csv', 'r') as file:
        reports = []
        for line in file:
            # Split the line by spaces and convert each element to an integer
            report = list(map(int, line.strip().split()))
            reports.append(report)
    print(count_safe_reports(reports))

if __name__ == "__main__":
    main()