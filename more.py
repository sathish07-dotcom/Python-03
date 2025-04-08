
### 1. **Print Numbers from 1 to 10**

for i in range(1, 11):
    print(i)

### 2. **Print Even Numbers from 1 to 20**

for i in range(2, 21, 2):
    print(i)

### 3. **Print Odd Numbers from 1 to 20**

for i in range(1, 21, 2):
    print(i)

### 4. **Sum of First N Natural Numbers**

n = int(input("Enter a number: "))
total = sum(range(1, n+1))
print("Sum:", total)

### 5. **Factorial of a Number**

n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)



## **Intermediate Problems**
### 6. **Reverse a Number**

num = int(input("Enter a number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed Number:", rev)

### 7. **Check if a Number is Prime**

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

### 8. **Multiplication Table of a Given Number**

n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

### 9. **Fibonacci Series (First N Terms)**

n = int(input("Enter the number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

### 10. **Check if a Number is Palindrome**

num = input("Enter a number: ")
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")



## **Advanced Problems**
### 11. **Print a Pattern (Triangle)**

n = 5
for i in range(1, n+1):
    print("* " * i)


### 12. **Print a Pyramid Pattern**

n = 5
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)


### 13. **Reverse a String using a Loop**

s = input("Enter a string: ")
rev = ""
for char in s:
    rev = char + rev
print("Reversed String:", rev)

### 14. **Find LCM of Two Numbers**

a, b = map(int, input("Enter two numbers: ").split())
lcm = max(a, b)
while True:
    if lcm % a == 0 and lcm % b == 0:
        print("LCM:", lcm)
        break
    lcm += 1


### 15. **Print Prime Numbers in a Given Range**

start, end = map(int, input("Enter range: ").split())
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")




## **Real-World Problems**
### 16. **ATM Transaction (While Loop)**

balance = 5000
while True:
    amt = int(input("Enter withdrawal amount (0 to exit): "))
    if amt == 0:
        break
    elif amt > balance:
        print("Insufficient Balance")
    else:
        balance -= amt
        print("Remaining Balance:", balance)


### 17. **Sum of Digits of a Number**

num = int(input("Enter a number: "))
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of Digits:", total)


### 18. **Armstrong Numbers in a Range**

start, end = map(int, input("Enter range: ").split())
for num in range(start, end + 1):
    sum_of_digits = sum(int(digit) ** len(str(num)) for digit in str(num))
    if num == sum_of_digits:
        print(num, end=" ")


### 19. **Reverse a List using Loop**

lst = list(map(int, input("Enter numbers: ").split()))
rev_lst = []
for i in range(len(lst)-1, -1, -1):
    rev_lst.append(lst[i])
print("Reversed List:", rev_lst)

### 20. **Number Guessing Game**

import random
target = random.randint(1, 100)
while True:
    guess = int(input("Guess the number (1-100): "))
    if guess == target:
        print("Correct! You guessed it.")
        break
    elif guess > target:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
