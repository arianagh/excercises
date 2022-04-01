# def chek_khosh_tarif(string):
#     i = 0
#     ls = []
#     while i < len(string):
#         if i % 2 == 0:
#             if string[i] == '0':
#                 ls.append(string[i])
#             elif string[i] == '?':
#                 string.replace(string[i], '0')
#                 ls.append(string[i])
#         elif i % 2 == 1:
#             if string[i] == '1':
#                 ls.append(string[i])
#             elif string[i] == '?':
#                 string.replace(string[i], '1')
#                 ls.append(string[i])
#         i += 1
#     if len(ls) == len(string):
#         print(True)
#     elif len(ls) != len(string):
#         print(False)
#
# string = input()
# chek_khosh_tarif(string)