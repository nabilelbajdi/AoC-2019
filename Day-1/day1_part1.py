def calculate_fuel_requirement(modules_mass):
    total_fuel = 0
    for mass in modules_mass:
        fuel = mass // 3 - 2
        total_fuel += fuel
    return total_fuel

#Read the input
with open("input", "r") as file:
    inputs = file.read().splitlines()
inputs = [int(i) for i in inputs]

#calculate the fuel and print the result
fuel_requirement = calculate_fuel_requirement(inputs)
print(fuel_requirement)