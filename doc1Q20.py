# # Q1.Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# # # Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
# a={}
# for i in (d1,d2):
#     a.update(i)
# print(a)

# (or)
# d1= {'a': 100, 'b': 200, 'c':300}
# d2= {'a': 300, 'b': 200, 'd':400}
# d={}
# for i in d1:
#     for j in d2:
#         if i not in d2:
#             d[i]=d1[i]   
#         elif j not in d1:
#             d[j]=d2[j]
#         elif i in d2:
#             d[j]=d1[i]+d2[i]
# print(d)

