import re

def main():
    with open('puzzle3.txt', 'r') as file:
        memory = file.read()
    
    # Patterns for do(), don't(), and mul(X,Y)
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all matches for each pattern in order
    instructions = []
    for match in re.finditer(do_pattern, memory):
        instructions.append(('do', match.start()))
    for match in re.finditer(dont_pattern, memory):
        instructions.append(('dont', match.start()))
    for match in re.finditer(mul_pattern, memory):
        x, y = map(int, match.groups())
        instructions.append(('mul', match.start(), x, y))
    
    # Sort all instructions by their position in the memory
    instructions.sort(key=lambda x: x[1])
    
    # Process instructions in order
    enabled = True
    total = 0
    for instr in instructions:
        if instr[0] == 'do':
            enabled = True
        elif instr[0] == 'dont':
            enabled = False
        elif instr[0] == 'mul' and enabled:
            x, y = instr[2], instr[3]
            total += x * y
    
    print(total)

if __name__ == "__main__":
    main()