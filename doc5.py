# 5QWrite a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary : {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value : [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# # Dictionary in descending order by value : {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}


# (1)
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# x= sorted(d.items())
# print(x)
# y = x[::-1]
# print(y)

# (2)
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# e = {}
# for v in reversed(sorted(d.values())):
#     for k in d:
#         if d[k] == v and k not in e:
#             e.update({k:v})
# print(e)

# (3)
# a= {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# b=[]
# for i in a:
#     b.append([i,a[i]])
# print(b)
# for i in range(0,len(b)-1):
#     for j in range(0,len(b)-1):
#         if b[j][1]<b[j+1][1]:
#             b[j][1],b[j+1][1]=b[j+1][1],b[j][1]
# print(b)





