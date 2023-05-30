import pytest

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

def test_run_program():
    assert run_program([1,0,0,0,99]) == [2,0,0,0,99]
    assert run_program([2,3,0,3,99]) == [2,3,0,6,99]
    assert run_program([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    assert run_program([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]