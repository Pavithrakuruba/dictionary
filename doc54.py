# Q54.
# Write a Python program to create a key-value list pairings in a given dictionary.
# Original dictionary:
# {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'],
#  4: ['Lynne Foster'], 5: ['Zachary Simon']}
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 
# 4: 'Lynne Foster', 5: 'Zachary Simon'}]
        
    
a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'],
4: ['Lynne Foster'], 5: ['Zachary Simon']}
# b={}
# # c={}
# for i in a:
#     for j in a[i]:
#         b.update({i:j[0]})
# print(b)
li=[]
dic={}
for i in a:
    for j in a[i]:
        dic.update({i:j})  
li.append(dic)          
print(li)    
# a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'],
# 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# b={}
# # c={}
# for i in a:
#     for j in a[i]:
#         b.update({i:j[0]})
# print(b)