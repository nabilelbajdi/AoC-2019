def run_intcode(mem):
    pc = 0
    while mem[pc] != 99:
        op = mem[pc]
        a, b, c = mem[pc+1:pc+4]
        if op == 1:
            mem[c] = mem[a] + mem[b]
        elif op == 2:
            mem[c] = mem[a] * mem[b]
        else:
            raise ValueError(f"Invalid opcode {op} at position {pc}")
        pc += 4
    return mem

def find_inputs(memory, target):
    for noun in range(100):
        for verb in range(100):
            mem = memory.copy()
            mem[1] = noun
            mem[2] = verb
            run_intcode(mem)
            if mem[0] == target:
                return noun, verb



memory = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0]
noun, verb = find_inputs(memory, 19690720)
result = 100 * noun + verb
print(result)