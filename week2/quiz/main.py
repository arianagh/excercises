
# def turningpoints(x):
#   N = 0
#   for i in range(1,len(x)-1):
#      if ((x[i-1] < x[i] and x[i+1] < x[i])
#          or (x[i-1] > x[i] and x[i+1] > x[i])):
#        N += 1
#
#   return N
#
# ls = [1,2,3,8,9,13,4,5,8,42]
# print(turningpoints(ls))




# ls = [1,3,4,9,2,14,6]
# for i in range(1,len(ls)-1):
#     if (ls[i+1] < ls[i]):
#         print(True)
#     else:
#         print(False)




# ls = [1,3,4,9,2,14,6]
# for i in range(1,len(ls)-1):
#     print(ls[i-1] > ls[i])




def find_common(ls1,ls2):
    new_ls = []
    for i in range(1,len(ls1)-1):
        if ls1[i+1] < ls1[i] and ls2[i+1] < ls2[i]:



    # for i in range(1,len(ls2)):
    #     if ls2[i+1] < ls2[i] and i in ls1:
    #         new_ls.append(i)
    return new_ls

ls1 = [1,3,8,12,24,2,15,21,23]
ls2 = [1,8,9,21,2,15]
print(find_common(ls1,ls2))















