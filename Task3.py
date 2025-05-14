# find prime number
# num = int(input("Enter a positive integer: "))
# if num < 2:
#     print("Not Prime")
# else:
#     prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             prime = False
#             break
#     if prime:
#         print("Prime")
#     else:
#         print("Not Prime")

# Print factorial of a number 
# num = int(input("Enter a positive integer: "))
# factorial = 1
# i = 1
# while i <= num:
#     factorial *= i
#     i += 1
# print("Factorial:", factorial)

# Find the sum of digits of a number using loop
# num = int(input("Enter a positive integer: "))
# sum = 0
# while num > 0:
#     digit = num % 10
#     sum += digit
#     num = num // 10
# print("Sum of digits:", sum)

# checknumber is a palindrom
# num = int(input("Enter a number: "))
# original_num = num
# reversed_num = 0
# while num > 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num = num // 10
# if original_num == reversed_num:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# find least common multiple(LCM)
# num1 = int(input("Enter the first number:"))
# num2 = int(input("enter the second number:"))
# if num1 > num2:
#     greater = num1
# else:
#     greater = num2
# while True:
#     if (greater % num1 == 0) and (greater % num2 == 0):
#         lcm = greater
#         break
#     greater += 1
# print("LCM of", num1, "and", num2, "is", lcm)

# print a square matrix of numbers with diagonals as 0: 
# ?

# Continuous Numbers in Triangle
n = int(input("enter your number:"))
num = 1  
row = 1 
while num <= n:
    for i in range(row):
        if num > n:
            break
        print(num, end=' ')
        num += 1
    print()
    row += 1