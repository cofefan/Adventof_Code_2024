def is_safe_report(levels):
    if len(levels) < 2:
        return True
    
    is_increasing = None
    prev = levels[0]
    for current in levels[1:]:
        diff = current - prev
        if diff == 0:
            return False
        if is_increasing is None:
            is_increasing = diff > 0
        else:
            if (diff > 0) != is_increasing:
                return False
        prev = current
    
    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i+1])
        if diff < 1 or diff > 3:
            return False
    
    return True

def can_be_made_safe(levels):
    if is_safe_report(levels):
        return True
    
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_safe_report(new_levels):
            return True
    
    return False

def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if can_be_made_safe(report):
            safe_count += 1
    return safe_count

def main():
    with open('puzzle2.csv', 'r') as file:
        reports = []
        for line in file:
            report = list(map(int, line.strip().split()))
            reports.append(report)
    print(count_safe_reports(reports))

if __name__ == "__main__":
    main()