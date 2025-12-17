num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2
print(f"The sum of {num1} and {num2} is {total}")

def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
result1 = check_even_odd(num1)
result2 = check_even_odd(num2)
print(f"{num1} is {result1}")
print(f"{num2} is {result2}")