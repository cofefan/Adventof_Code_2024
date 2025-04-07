import re

def main():
    with open('puzzle3.txt', 'r') as file:
        memory = file.read()
    
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, memory)
    
    total = 0
    for match in matches:
        x, y = map(int, match)
        total += x * y
    
    print(total)

if __name__ == "__main__":
    main()