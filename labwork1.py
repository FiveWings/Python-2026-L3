import math

# ex1.py
radius = input("Enter circle radius:")
area = 3.14 * float(radius)**2
print(f"Circle area = {area}")

# ex2.py
c_temp = input("Enter the temperature in Celsius? ")
f_temp = (float(c_temp) * 1.8) + 32
print(f"{c_temp} (C) = {f_temp} (F)")

# ex3.py
num = int(input("Enter a number? "))

if num <=1:
    print(f"{num} is not a prime number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

# ex4.py
num = int(input("Enter a number? "))
if num <= 1:
    print(f"{num} is a NOT perfect number")
else:
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    if divisor_sum == num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")

# ex5.py
colors = ["Blue", "Yellow", "Purple", "Red", "Orange", "Black"]

u_color = input("What is your favorite color? ")

if u_color in colors:
    index = colors.index(u_color)
    print(f"Your color is at index {index} in my list")
else:
    print("Sorry, I could not find your color")

# ex6.py
range1 = list(range(7))
print("range1:", end=" ")
print(*range1, sep=", ")

range2 = list(range(1, 11, 3))
print("range2:", end=" ")
print(*range2, sep=", ")

range3 = list(range(5, 0, -1))
print("range3:", end=" ")
print(*range3, sep=", ")

range4 = list(range(6, -3, -2))
print("range4:", end=" ")
print(*range4, sep=", ")

# ex7.py
def remove_dollar(s):
    return s.replace("$", "")
price = input("Enter a price (e.g. $1,500.00): ")
clean = remove_dollar(price)
print(clean)

# ex8.py
def extract_even(l):
    return [x for x in l if x % 2 == 0]
sample_list = [int(x) for x in input("Enter integers separated by spaces: ").split()]
result = extract_even(sample_list)
print(result)

# ex9.py
def calculate_factorial(n):
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
n = int(input("Enter a number to compute its factorial: "))
print(f"{n}! = {calculate_factorial(n)}")

# ex10.py
def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]
number = int(input("Enter a number to find its divisors: "))
divisors = get_divisors(number)
print(divisors)

# ex11.py
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance = calculate_distance(x1, y1, x2, y2)
print(f"The distance is: {distance}")

# ex12.py
def print_pattern(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
print_pattern(m, n)
