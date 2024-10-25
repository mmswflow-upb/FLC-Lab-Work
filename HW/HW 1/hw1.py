def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    print(" ".join(map(str, series)))

n = int(input("Enter the number of terms: "))
fibonacci_series(n)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("GCD:", gcd(num1, num2))


def lcm(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return abs(a * b) // gcd(a, b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("LCM:", lcm(num1, num2))


class Cube:
    def __init__(self, side_length):
        self.side_length = side_length

    def surface_area_one(self):
        return self.side_length ** 2

    def surface_area_all(self):
        return 6 * (self.side_length ** 2)

    def volume(self):
        return self.side_length ** 3

side = float(input("Enter the side length of the cube: "))
cube = Cube(side)
print("Surface area of one face:", cube.surface_area_one())
print("Surface area of all faces:", cube.surface_area_all())
print("Volume of the cube:", cube.volume())


power_of_number = lambda num, power: num ** power


number = int(input("Enter the number: "))
power = int(input("Enter the power: "))
print(f"{number} to the power of {power} is: {power_of_number(number, power)}")
