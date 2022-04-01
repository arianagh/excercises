# a       b       c       d       e
# 0       1       2       3       4
# n-5     n-4     n-3     n-2     n-1


# def rangoli(n):
#     alphabet_list = list(map(chr, range(97,123)))
#
#     x = alphabet_list[n-1::-1] + alphabet_list[1:n] # 1 vase inke az a dobar shoro nakone n-1 bara inke dar l dovomi n yelbar kam mishe khodesh
#     width = len('-'.join(x))
#     for i in range(1, n):
#         print('-'.join(alphabet_list[n-1:n-i:-1]+alphabet_list[n-i:n]).center(width,'-'))
#     for i in range(n, 0, -1):
#         print('-'.join(alphabet_list[n-1:n-i:-1]+alphabet_list[n-i:n]).center(width,'-'))
#
#
# rangoli(5)



## way 2
# import string
# alphabet = string.ascii_lowercase
# print(alphabet)
#
# def rang(n):
#     l = []
#     for i in range(n):
#         s = '-'.join(alphabet[i:n])
#         l.append(s[::-1]+s[1:])
#     for i in l[::-1]:
#         print(i.center(4*n-3,'-'))
#     for i in l[1:]:
#         print(i.center(4*n-3,'-'))
#
# rang(5)


## capitalize

# s = 'arian aghaee'
# ls = s.split()
# print(ls)
# for ele in ls:
#     s = s.replace(ele, ele.capitalize())
# print(s)



# ss = ''.join(ls[0])
# sss = ''.join(ls[1])
# first_name = ss.capitalize()
# last_name = sss.capitalize()
# print(first_name, last_name)


## minion

# s = 'banana'
# s = s.upper()
# print(s)
# vowel = ('A', 'I', 'E', 'O', 'U')
# kevin_scr = 0
# staurt_scr = 0
# for i in range(len(s)):
#     if s[i] in vowel:
#         kevin_scr += len(s) - i
#     else:
#         staurt_scr += len(s) - i
#
# if kevin_scr > staurt_scr:
#     print('kevin winned by', kevin_scr)
# elif kevin_scr == staurt_scr:
#     print('draw')
# else:
#     print('staurt winned by', staurt_scr)


## merge

# logic = aval leno bgirim be kesbat k badesh slice mikonim badesh append dar list
# badesh dobre ro har harf dar on list iterate mikonim ta be dic tabdilsh knim
# def merge_the_tools(string, k):
#     ls = []
#     m = 0
#     for i in range(len(string) // k):
#         ls.append(string[m:m+k])
#         m += k
#         print(ls)
#     for value in ls:
#         # print(list(value)) #mesl split kardane
#         # print(dict.fromkeys(list(value))) #chun dic fght mitone yek key gheyr tekrari dashte bashe
#         print(''.join(list(dict.fromkeys(list(value)).keys())))


# string, k = input(), int(input())
# merge_the_tools(string, k)


## itertools

# from itertools import product
# A = input().split()
# A = list(map(int,A))
# B = input().split()
# B = list(map(int, B))
# out = list(product(A,B))
# for i in out:
#     print(i,end=' ')

## collections


# from collections import Counter
#
# number_shoes = int(input())
# inventory = list(map(int, input().split()))
# size_availability = Counter(inventory)
# number_customers = int(input())
# income = 0
# for customer in range(number_customers):
#     size, price = list(map(int, input().split()))
#     if size_availability[size] > 0:
#         income += price
#         size_availability[size] -= 1
# print(income)


## permutaions

# from itertools import permutations
#
# word, num = input().split(" ")
# permutations = list(permutations(word, int(num)))
# permutations.sort()
#
# for i in permutations:
#     print("".join(i))



## polar coordinates

# import cmath
# num = input()
# z = complex(num)
# a = cmath.polar(z)[0]
# b = cmath.polar(z)[1]
# print(f'a is {a:.2f} and b is {b:.2f}',b)


## set introduction

# def average(array):
#     distinct_array = list(set(array))
#     total = 0
#     for ele in distinct_array:
#         total += ele
#         avg = total / len(distinct_array)
#     return avg
#
#
# n = int(input())
# arr = list(map(int, input().split()))
# result = average(arr)
# print(result)


## defaultdict

from collections import defaultdict

# n, m = map(int, input('pls enter the len group a and b : ').split())
# d = defaultdict(list)
# print(d)
# ls = []
# for i in range(1, n + 1):
#     d[input('pls enter group A : ')].append(i)
# print(d)
# for j in range(m):
#     ls.append(input('pls enter group B : '))
# for k in ls:
#     if k in d.keys():
#         print(*d[k])
#     else:
#         print(-1)



## calender

# import calendar
# d, m ,y  = map(int, input().strip().split())
# print(calendar.day_name[calendar.weekday(y,m,d)])

## exceptions

# testcases = int(input())
# for i in range(testcases):
#     try:
#         a, b = map(int, input().split())
#
#         print(a // b)
#
#     except ValueError as e:
#         print('Error code Value :', e)
#
#     except ZeroDivisionError as err:
#         print('Error code zero = ', err)


## namedtuple

from collections import namedtuple

# point = namedtuple(typename='s',field_names= 'x,y')
# pt1 = point(1,5)
# pt2 = point(2,7)
# product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
# print(product)



# number_of_students = int(input('num'))
# total = 0
# for i in range(number_of_students):
#     name_of_columns = namedtuple('xyzk','ID Marks Name Class')
#     xyzk = name_of_columns(ID=int(input('id')), Marks=int(input('marks')), Name=input('name'), Class=int(input('class')))
#     # points = name_of_columns(Marks=)
#     total += int(xyzk.Marks)
# print(total)



# n = int(input())
# a = input()
# total = 0
# Student = namedtuple('Student', a)
# for _ in range(n):
#     student = Student(*input().split())
#     total += int(student.MARKS)
# print('{:.2f}'.format(total/n))



## find angle mbc

# byd tanjant ab / bc ro bedst biarim
# import math
# ab = int(input())
# bc = int(input())
# print(round(math.degrees(math.atan(ab / bc))))


## no idea


# nm = input().split()
# n = int(nm[0])
# m = int(nm[1])
# arr = list(map(int, input().split()))
# set1 = set(map(int, input().split()))
# set2 = set(map(int, input().split()))
# hapiness = 0
# for ele in arr:
#     if ele in set1:
#         hapiness+=1
#     elif ele in set2:
#         hapiness-=1
#     else:
#         hapiness = hapiness
# print(hapiness)



## ordered dict

# from collections import OrderedDict
# n = int(input())
# inventory = OrderedDict()
# for i in range(n):
#     items = input().split()
#     v = int(items[-1])
#     k = ' '.join(items[:-1])
#     if k in inventory:
#         inventory[k] += v
#     else:
#         inventory[k] = v
# for k, v in inventory.items():
#     print(k, v)


## symmetric set

# n = int(input())
# set1 = set(map(int, input().split()))
# m = int(input())
# set2 = set(map(int, input().split()))
#
# d1 = set1.difference(set2)
# d2 = set2.difference(set1)
#
# uni = list(d1.union(d2))
#
# for ele in uni:
#     print(ele)


## itertools.combinations

# from itertools import combinations
#
# s, k =input().split()
# string = list(s)
# string.sort()
# for i in range(int(k)):
#     l = list(combinations(string,i+1))
#     for ele in l:
#         print(''.join(ele))


## incorrect regex

# import re
# for i in range(int(input())):
#     ans = True
#     try:
#         reg = re.compile(input())
#     except re.error:
#         ans = False
#     print(ans)


## set add

# n = int(input())
# s = set()
# for i in range(n):
#     s.add(input())
# print(len(s))



## ITER  combinamtion with

# from itertools import combinations_with_replacement
#
# s, k = input().split()
#
# for c in combinations_with_replacement(sorted(s), int(k)):
#     print("".join(c))


## word order

# n = int(input())
# # s = set()
# d = {}
# for i in range(n):
#     v = input()
#     # s.add(v)
#     v = v.split()
#     for ele in v:
#         if ele in d:
#             d[ele] += 1
#         else:
#             d[ele] = 1
# print(len(d))
# for k,va in d.items():
#     print(va,end=' ')


## discard pop remove

# n = int(input())
# s = set(map(int, input().split()))
# for i in range(int(input())):
#     command = input().split()
#     if command[0] == 'remove':
#         s.remove(int(command[1]))
#     elif command[0] == 'discard':
#         s.discard(int(command[1]))
#     else:
#         s.pop()
# print(sum(s))


## collection deque

from collections import deque

# n = int(input())
# storage = deque()
# for i in range(n):
#     d = (input().split())
#     if d[0] == 'append':
#         storage.append(d[1])
#     elif d[0] == 'appendleft':
#         storage.appendleft(d[1])
#     elif d[0] == 'popleft':
#         storage.popleft()
#     else:
#         storage.pop()
# print(' '.join(storage))


## compress string

# from itertools import groupby
#
# s = input()
# for k, g in groupby(map(int,list(s))):
#     print(tuple([len(list(g)),k]),end=' ')
#


## company logo

# from collections import Counter

# s = sorted(input()) # to get the output in alphabetical order
# c = Counter(s) # yek dic mide
# print(c)
# c = Counter(s).most_common(3) # tuple in a list
# print(c)
# for ele in c:
#     print(*ele)  # star to unpack the tuple


## set union

# n = int(input())
# a = set(map(int,input().split()))
# m = int(input())
# b = set(map(int,input().split()))
# un = a.union(b)
# print(len(un))



## pile up

# def solution(ls):
#     Yes = 'yes'
#     No = 'No'
#     lm = 0
#     rm = len(ls) - 1
#     current_value_stack = lm if lm > rm else rm
#
#
#     while lm <= rm:
#         left_val = ls[lm]
#         right_val = ls[rm]
#         if left_val > current_value_stack and right_val > current_value_stack:
#             print(No)
#             return  # for breaking the loop
#         else:
#             if left_val >= right_val and left_val <= current_value_stack:
#                 current_value_stack = left_val
#                 lm += 1
#             elif right_val > left_val and right_val <= current_value_stack:
#                 current_value_stack = right_val
#                 rm -= 1
#             else:
#                 print(No)
#                 return
#     print(Yes)
#
#
#
# num_of_test = int(input())
# for i in range(num_of_test):
#     n = int(input())
#     ls = [int(num) for num in input().split()]
#
#     solution(ls)
#

## triangle 2

# for i in range(1,int(input())+1):
#     print(((10 ** i)//9)**2)
#     '''
#     1 = i = 1
#     121 = i = 2
#     12321 = i = 3
#     baraye sakht in ha bayad 10 be tavan index bedim bad taghsim bar 9 knim bad be tavan 2
#     masalan : 1 = 10 ** 1 = 10 badesh / 9 = 1 bad 1 ** 2 = 1
#     masalan : 121 = 10 ** 2 = 100 badsh / 9 = 11 bad 11 ** 2 = 121
#     '''


## set intersection

# n = int(input())
# s1 = set(map(int, input().split()))
# n1 = int(input())
# s2 = set(map(int, input().split()))
# intersec = s1.intersection(s2)
# print(len(intersec))


## mod divmod

# a = int(input())
# b = int(input())
# print(a // b)
# print(a % b)
# print(divmod(a,b))


## mod power

# a = int(input())
# b = int(input())
# m = int(input())
# print(pow(a,b))
# print(pow(a,b,m))


## iterables and iterators

# from itertools import combinations
#
# N = int(input())
# char = input().split()
# K = int(input())
# count = 0
# total = 0
# for i in combinations(char, K):
#     # print(i)
#     count += 'a' in i
#     total += 1
# # print(count)
# # print(total)
# print(count / total)



## maxmize it

# from itertools import product
#
# # l1 = [5,4]
# # l2 = [7,8,9]
# # l3 = [5,7,8,9,10]
# # print(list(product(l1,l2,l3)))
#
# n, m = map(int, input().split())
# ls = []
# for i in range(n):
#     l = list(map(int, input().split()))[1:]
#     ls.append(l)
# r = map(lambda x:sum(i*i for i in x)%m, product(*ls))   #x barabare ba avalin tuple dar on list ta btonim ele haro bgirim azsh
# print(max(r))

## int in all size

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(a**b + c**d)


## set mutations

# n = int(input())
# s = set(map(int, input().split()))
# m = int(input())
# for i in range(m):
#     command = input().split()
#     b = set(map(int, input().split()))
#     if command[0] == 'intersection_update':
#         s.intersection_update(b)
#     elif command[0] == 'update':
#         s.update(b)
#     elif command[0] == 'symmetric_difference_update':
#         s.symmetric_difference_update(b)
#     elif command[0] == 'difference_update':
#         s.difference_update(b)
# print(sum(s))



## the captains room

# from collections import Counter
# n = int(input())
# rooms = [int(x) for x in input().split()]
# cnt = Counter(rooms)
# for k,v in cnt.items():
#     if v == 1:
#         print(k)
#         break

## check subset

# for i in range(int(input())):
#     n1 = int(input())
#     s1 = set(map(int, input().split()))
#     n2 = int(input())
#     s2 = set(map(int, input().split()))
#     print(s1.issubset(s2))


## strict superset

# s1 = set(map(int, input().split()))
# n = int(input())
# for i in range(n):
#     s2 = set(map(int, input().split()))
#
#     if not s1.issuperset(s2):
#         print(False)
#         break
# else:
#     print(True)


## zipped

# n,x = input().split()
# ls = []
# for i in range(int(x)):
#     marks = list(map(float,input().split()))
#     ls.append(marks)
# print(ls)
# for ele in zip(*ls):
#     print(ele)
#     print(len(ele))
#     print(sum(ele)/len(ele))


## triangle

# for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     print((i*10**i)//9)


## dealing with complex

import math

# class Complex(object):
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary
#
#     def __add__(self, no):
#         real = self.real + no.real
#         imaginary = self.imaginary + no.imaginary
#         return Complex(real, imaginary)
#
#     def __sub__(self, no):
#         real = self.real - no.real
#         imaginary = self.imaginary - no.imaginary
#         return Complex(real, imaginary)
#
#     def __mul__(self, no):
#         real = self.real * no.real - self.imaginary * no.imaginary
#         imaginary = self.real * no.imaginary + self.imaginary * no.real
#         return Complex(real, imaginary)
#
#     def __truediv__(self, no):
#         x = float(no.real ** 2 + no.imaginary ** 2)
#         y = self * Complex(no.real, -no.imaginary)
#         real = y.real / x
#         imaginary = y.imaginary / x
#         return Complex(real, imaginary)
#
#     def mod(self):
#         v = math.sqrt(self.real ** 2 + self.imaginary ** 2)
#         return Complex(v, 0)
#
#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.real)
#         elif self.real == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.real, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#         return result
#
#
# c = map(float, input().split())
# d = map(float, input().split())
# x = Complex(*c)
# y = Complex(*d)
# print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')


## class 2

# import math
#
# class Points(object):
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __sub__(self, no):
#         x = self.x - no.x
#         y = self.y - no.y
#         z = self.z - no.z
#         return Points(x,y,z)
#
#     def dot(self, no):
#         x = self.x * no.x
#         y = self.y * no.y
#         z = self.z * no.z
#         return x + y + z
#
#     def cross(self, no):
#         x = self.y * no.z - self.z * no.y
#         y = self.z * no.x - self.x * no.z
#         z = self.x * no.y - self.y * no.x
#         return Points(x, y, z)
#     def absolute(self):
#         return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
#
#
# points = list()
# for i in range(4):
#     a = list(map(float, input().split()))
#     points.append(a)
#
# a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
# x = (b - a).cross(c - b)
# y = (c - b).cross(d - c)
# angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
#
# print("%.2f" % math.degrees(angle))



## input():

# x, k = map(int,input().split(" "))
# print(eval(input()) == k)


# ui = input().split()
# x = int(ui[0])
# print(eval(input()) == int(ui[1]))


##athlete


# nm = input().split()
# n = int(nm[0])
# m = int(nm[1])
# arr = []
# for _ in range(n):
#     arr.append(list(map(int, input().rstrip().split())))
# k = int(input())
# print(arr)
#
# # arr.sort(key = lambda x : x[k]) # x = barabare ba har list jodayei ke darim
# # for ele in arr:
# #     print(*ele, sep=' ')
#
# for row in sorted(arr, key= lambda x : x[k]):
#     print(*row)


## any or all

# n = int(input())
# ls = list(input().split())
# print(all([int(ele) > 0 for ele in ls]) and any([j == j[::-1] for j in ls]))


## gnosritng

## way1
# s = input()
# ls1 = []
# ls2 = []
# ls3 = []
# ls4 = []
# for ele in s:
#     if ele.islower() and ele.isalpha():
#         ls1.append(ele)
#     elif ele.isupper():
#         ls2.append(ele)
#     elif int(ele) % 2 != 0:
#         ls3.append(ele)
#     elif int(ele) % 2 == 0:
#         ls4.append(ele)
#
# ls1.sort()
# ls2.sort()
# ls3.sort()
# ls4.sort()
# print(''.join(ls1+ls2+ls3+ls4))
#
# ## way2
# l,u,o,e=[],[],[],[]
# for i in sorted(input()):
#     if i.isalpha():
#         x = u if i.isupper() else l
#     else:
#         x = o if int(i)%2 else e
#     x.append(i)
# print("".join(l+u+o+e))
#
# ## way 3
# print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')
#
#
# ## way4
# import string
# print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')


## way5
# print(*(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')


## detecting floating point


# import re
# for i in range(int(input())):
#     s = input()
#     print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', s)))



##  map and lamda

#cube = lambda x : x ** 3
# def fibonacci(n):
#     ls = [0,1]
#     for i in range(2,n):
#         ls.append(ls[i-2]+ls[i-1])
#     return ls[0:n]
# print(fibonacci(20))


## group gropus

# import re
# s = input()
# m = r"([a-zA-Z0-9])\1+"
# search = re.search(m,s)
# if search:
#     print(search.group(1))
# else:
#     print(-1)

##validating email

# import re
# def fun(s):
#     pattern = r"(^[a-zA-Z-_0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$)"
#     return re.search(pattern,s)
# def filter_mail(emails):
#     return list(filter(fun, emails))
#
# if __name__ == '__main__':
#     n = int(input())
#     emails = []
#     for _ in range(n):
#         emails.append(input())
#
# filtered_emails = filter_mail(emails)
# filtered_emails.sort()
# print(filtered_emails)



