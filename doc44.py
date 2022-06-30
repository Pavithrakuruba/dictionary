# Q44.Write a Python program to split a given dictionary of lists into list 
# of dictionaries.Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78},
# {'Science': 62, 'Language':84}, {'Science': 95, 'Language': 80}]

# a={'Science':[88, 89, 62, 95],'Language':[77, 78, 84, 80]}
# b={}
# for i in a:
#     # print(i)
#     c={}
#     for j in a[i]:
#         c.update({i:j})
#     print(c)
        

# for i in a.keys():
#     for j in a.values():
#         for k in j:
#             b.update({i:k})



# A= {'1':['a', 'b'], '2':['c', 'd']}
# B= list(A.values())
# for i in B[0]:
#     for j in B[1]:
#         print(i+j)
   







a={'Science':[88, 89, 62, 95],'Language':[77, 78, 84, 80]}
b={}
for i in a:
    k=0
    for j in range(len(a[i])):
        b.update({i:a[i][k]})
    k=k+1    

print(b)