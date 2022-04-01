# def shorting(n):
#     ls = []
#     for i in range(len(n)-1):
#         temp = n[:]
#         sum = int(temp.pop(i)) + int(temp.pop(i))  #grftne jame index ha ba ham
#         temp.insert(i, str(sum))  #jaygozinie sum ba index 0
#         ls.append(int(''.join(temp)))
#     print(max(ls))
#
#
# n = list(map(str, input()))
# shorting(n)