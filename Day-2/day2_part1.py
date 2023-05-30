def run_program(program):
    pc = 0  # program counter
    while True:
        opcode = program[pc]
        if opcode == 1:
            a, b, c = program[pc+1:pc+4]
            program[c] = program[a] + program[b]
        elif opcode == 2:
            a, b, c = program[pc+1:pc+4]
            program[c] = program[a] * program[b]
        elif opcode == 99:
            break  # halt
        else:
            raise ValueError(f"Invalid opcode {opcode} at position {pc}")
        pc += 4
    return program

# Read the input
with open("input", "r") as f:
    input_str = f.read().strip()

# Parse the input string into a list of integers
program = list(map(int, input_str.split(",")))

# Restore "1202 program alarm" state
program[1] = 12
program[2] = 2

# Run the program
program = run_program(program)

# Print the output
print(program[0])