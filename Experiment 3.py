# Find a factorial of given number.

num = int(input("Enter a number: "))

fact = 1
for i in range(1, num + 1):
    fact *= i

print("Factorial of", num, "is:", fact)

# Find whether the given number is Armstrong number.

num = int(input("Enter a number: "))

temp = num
digits = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

# Print Fibonacci series up to given term.

n = int(input("Enter number of terms: "))

a, b = 0, 1

print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Write a program to find if given number is prime number or not.

num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

# Check whether given number is palindrome or not.

num = int(input("Enter a number: "))

temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if rev == num:
    print(num, "is a Palindrome number")
else:
    print(num, "is not a Palindrome number")

# Write a program to print sum of digits.

num = int(input("Enter a number: "))

sum_digits = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp //= 10

print("Sum of digits:", sum_digits)

# Count and print all numbers divisible by 5 or 7 between 1 to 100.

count = 0

print("Numbers divisible by 5 or 7 between 1 and 100:")

for i in range(1, 101):
    if i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")
        count += 1

print("\nTotal count:", count)

# Convert all lower cases to upper case in a string.

text = input("Enter a string: ")
print("Uppercase string:", text.upper())

# Print the table for a given number: 
#             5 * 1 = 5
#            5 * 2 = 10………..

num = int(input("Enter a number: "))

print("Multiplication Table of", num)

for i in range(1, 11):
    print(num, "*", i, "=", num * i)

# 11.Write a program to print the sum of the following series
#1+ ½ + 1/3 + ¼ +….+1/n

n = int(input("Enter the value of n: "))

sum_series = 0.0

for i in range(1, n + 1):
    sum_series += 1 / i

print("Sum of the series =", sum_series)
