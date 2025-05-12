# 1 .Write a program to find largest of three numbers.
n1 =int(input("Enters the numbers:"))
n2 =int(input("Enters the numbers:"))
n3= int(input("Enters the numbers:"))
if(n1>=n2) and (n1>=n3):
    print("n1 is largest number.")
elif(n2>=n1) and (n2>=n3):
    print("n2 is largest number.")
else:
    print("n3 is largest number.")


# 2. Print the first n even numbers using a loop.
N = int(input("Enter the value of N:"))
count = 0
number = 2
while count < N:
    print(number)
    number += 2
    count += 1

# 3. # Simple calculator using if-else conditions

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Addition:", num1 + num2)
elif op == '-':
    print("Subtraction:", num1 - num2)
elif op == '*':
    print("Multiplication:", num1 * num2)
elif op == '/':
    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operator.")


# 4. WAP to check number is prime.
def prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# 5. Print Fibonaccci sequence up to n terms.
n = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to 1 term:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1

# 6.WAP to find the sum of digits of a number.
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10        
    sum += digit  
    num = num // 10         

print("Sum of digits:", sum)

# 7.Count how many digts  a number has without convertinhg to string.
def count_digits(n):
    if n == 0:
        return 1
    n = abs(n)  # Handle negative numbers
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
n = int(input("enter the number:"))
print(count_digits(n))

# 8.Print a diamond pattern using Stars(*).
def diamond(n):
    for i in range(n):
        print(' '*(n-i-1) + "*" * (2*i+1))
    for i in range(n-2,-i,-1):
        print(' '*(n-i-1) + "*" * (2*i+1))
n = int(input("enter the value of n:"))
diamond(n)

# 9.Implement a loop that keeps asking the user for input a valid number > 0 is entered.
num = -1  
while not num > 0:
    user_input = input("Enter a number greater than 0: ")
    if user_input.isdigit():
        num = int(user_input)
        if num <= 0:
            print("Number must be greater than 0.")
    else:
        print("Please enter a valid positive number.",num)


# 10.Print the sum of all numbers divisible by 3 or 5 below 100.
sum = 0
for i in range(100):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)
