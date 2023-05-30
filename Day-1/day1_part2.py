def calculate_total_fuel(masses):
    total_fuel = 0
    for mass in masses:
        fuel = calculate_fuel(mass)
        total_fuel += fuel
        while fuel > 0:
            fuel = calculate_fuel(fuel)
            total_fuel += fuel
    return total_fuel

def calculate_fuel(mass):
    return max(0, (mass // 3) - 2)

with open("input") as f:
    masses = [int(line) for line in f]

print(calculate_total_fuel(masses))