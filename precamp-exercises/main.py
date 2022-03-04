# exercise 1

# r = 5.3
# pi = 3.14
# sphere = 4 / 3 * pi * r ** 3
# print(f'the volume of the sphere is {sphere}')

# exercise 2

# n = int(input('pls enter a number : '))
# if n % 2 == 0:
#     print(f'the number {n} is even')
# else:
#     print(f'the number {n} is odd')

# exercise 3

# n = int(input('pls enter the first number : '))
# m = int(input('pls enter the second number : '))
# c = int(input('pls enter the third number : '))
#
# if n > m and n > c:
#     print(f'max is {n}')
# elif m > n and m > c:
#     print(f'max is {m}')
# else:
#     print(f'max is {c}')

# exercise 4

# n = 0
# while n < 100:
#     if n % 2 == 0:
#         print(n)
#     n += 1

# exercise 5

# def my_multiple(x,y):
#     total = 0
#     count = 0
#     while count < y:
#         total += x
#         count += 1
#     return total
#
# print(my_multiple(2,7))

# exercise 6

# for i in range(22,105):
#     if i % 4 == 0:
#         print(i)

# exercise 7

# for i in range(200,20,-1):
#     if i % 5 == 0 and i % 3 != 0:
#         print(i)

# for i in range(200,20,-1):
#     if i % 3 == 0:
#         continue
#     elif i % 5 == 0:
#         print(i)

# exercise 8

# for i in range(1,11):
#     for j in range(1,11):
#         j = i * j
#         print(j,end=' ')
#     print()

# exercise 9

# rows = int(input('pls enter a row : '))
# columns = int(input('pls enter a column : '))
# for i in range(1, rows + 1):
#     for j in range(1, rows - i + 1):
#         print(end=" ")
#     for j in range(1, columns + 1):
#         if (i == 1 or i == rows or
#                 j == 1 or j == columns):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()

# exercise 10

# message = 'Babak Khorramdin'
# print(message[0])
#
# print(message[4])
#
# splitted_message = message.split()
# first = splitted_message[0]
# second = splitted_message[1]
# print(first,second)
#
# print(message[0:12:2])

# for i in message:
#     if i == 'm':
#         print(True)
#         break
#     else:
#         print('not found!')

# exercise 11

# import random
# import math
#
# lower = int(input("Enter Lower range: "))
# upper = int(input("Enter Upper range: "))
#
# x = random.randint(lower, upper)
# print("You've only", 5,
#       "chances to guess the integer!\n")
#
# count = 0
# while count < math.log(upper - lower + 1, 2):
#     count += 1
#     guess = int(input("Guess a number: "))
#     if x == guess:
#         print("Congratulations you did it in ",
#               count, " try")
#         break
#     elif x > guess:
#         print("You guessed too small!")
#     elif x < guess:
#         print("You Guessed too high!")
#
# if count >= math.log(upper - lower + 1, 2):
#     print(f"\nThe number is {x}")
#     print("\tBetter Luck Next time!")














