import unittest

def calculate_fuel_requirement(modules_mass):
    total_fuel = 0
    for mass in modules_mass:
        fuel = mass // 3 - 2
        total_fuel += fuel
    return total_fuel

class TestFuelRequirement(unittest.TestCase):
    def test_calculate_fuel_requirement(self):
        self.assertEqual(calculate_fuel_requirement([12]), 2)
        self.assertEqual(calculate_fuel_requirement([12, 14, 1969, 100756]), 34241)

if __name__ == '__main__':
    unittest.main()