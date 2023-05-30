import unittest

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

class TestCalculateTotalFuel(unittest.TestCase):
    def test_calculate_total_fuel(self):
        self.assertEqual(calculate_total_fuel([12]), 2)
        self.assertEqual(calculate_total_fuel([14]), 2)
        self.assertEqual(calculate_total_fuel([1969]), 966)
        self.assertEqual(calculate_total_fuel([100756]), 50346)
        self.assertEqual(calculate_total_fuel([12, 14, 1969, 100756]), 51316)

    def test_calculate_fuel(self):
        self.assertEqual(calculate_fuel(12), 2)
        self.assertEqual(calculate_fuel(14), 2)
        self.assertEqual(calculate_fuel(1969), 654)
        self.assertEqual(calculate_fuel(100756), 33583)
        self.assertEqual(calculate_fuel(2), 0)

if __name__ == '__main__':
    unittest.main()