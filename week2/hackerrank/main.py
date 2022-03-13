# arr = map(int, input().split())
# # n_dup = set(arr)
# # n_dup.remove(max(n_dup))
# # print(max(n_dup))
# print(tuple(arr))

# t = (1,3,5,7,9)
# def m_2(item):
#     return item*2
#
#
# print(list(map(m_2, t)))

# arr = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     arr.append([score, name])
# arr.sort()
# for i in range(len(arr)):
#     if arr[i][0] > arr[0][0]:
#         print(arr[i][1])
#         if i + 1 >= len(arr) or arr[i + 1][0] > arr[i][0]:
#             break


# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika


# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()
# output = list(student_marks[query_name])
# print()
# print(output)
# print()
# total = sum(output) / len(output)
# print(f'{total:.2f}')


# dic = {'a': [50,20],
#      'b': 63,
#      'c': 76,
#      'm': 48
#     }
#
# o = (dic['a'])
# print(sum(o)/len(o))
# t = sum(o)/len(o)
# print(t)
# av = sum(o)/len(o)
# print(f'{av:.2f}')


# d = {'a': 60,
#      'b': 63,
#      'c': 76,
#      'm': 48
#     }
# sum = 0
# for i in d.values():
#     sum += i/len(d)
# print(f'{sum:.2f}')


# s = input()
# print(any(a.isalnum() for a in s))
# print(any())
#

# import textwrap
# text = 'hello  dj;dfk'
# b = "\n".join(textwrap.wrap(text, width= len(text)))
# print(b)


# N, M = map(int, input().split())
#
# for i in range(1, N, 2):
#     print(str('.|.' * i).center(M, '-'))
#
# print('Welcome'.center(M, '-'))
#
# for j in range(N - 2, -1, -2):
#     print(str('.|.' * j).center(M, '-'))






# def rangoli(size):
#     n = size
#     l1 = list(map(chr, range(97, 123)))
#     x = l1[n-1:0:-1]+l1[0:n]
#     m = len('-'.join(x))
#     for i in range(1, n):
#         print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m, '-'))
#     for i in range(n, 0, -1):
#         print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m, '-'))
#
# rangoli(5)

