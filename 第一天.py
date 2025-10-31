# 用1到5五个数组成多少个不同的5位数
# a = range(1,6)
#
#
# count = 0
# for i in a:
#     for j in a:
#         for k in a:
#             for l in a:
#                 for m in a:
#                     if i != j and j != k and k != l and l != m:
#                         print(i,j,k,l,m)
#                         count += 1
#
#
# print(count)




count = 0
a = range(1,6)
print(a)
for i in a:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    number = i * 10000 + j * 1000 + k * 100 + l * 10 + m
                    count += 1
                    print(number)
print(count)





