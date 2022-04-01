# def change_local_max(ls):
#     count = 0
#     copy_list = ls[:]
#     copy_2 = ls[:]
#     x = copy_2.pop()
#     v = copy_2.pop(0)
#     for i in range(1, len(ls) - 1):
#         if ls[i] > ls[i - 1] and ls[i] > ls[i + 1]: #local max
#             ls[i+1] += 1
#             if ls[-1] != copy_list[-1]:
#                 ls.pop()
#                 ls.append(x)
#             ls[i-1] += 1
#             if ls[i - 1] != copy_list[i - 1]:
#                 ls.pop(0)
#                 ls.insert(0, v)
#
#             count += 1
#     if count == 3:
#         print(count-1)
#     else:
#         print(count)
#     print(ls)
# lst = list(map(int,(input().split())))
# change_local_max(lst)







