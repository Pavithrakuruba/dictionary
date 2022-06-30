# (1)

# c_p= {"NewYorkCity":8550405,
# "LosAngeles":3971883, 
# "Toronto":2731571, 
# "Chicago":2720546, 
# "Houston":2296224, 
# "Montreal":1704694, 
# "Calgary":1239220, 
# "Vancouver":631486, 
# "Boston":667137
# }
# print(c_p["NewYorkCity"])
# print(c_p)
# print(type(c_p))


# # Keys Case Sensitive
# Dict = {
# 'ball' : 'green',
# 'Ball': 'red'
# }
# print(Dict['ball'])
# print(Dict['Ball'])
# print(Dict['bat'])


# # dict() function
# student=dict(name= "Ravina",age= 20)
# print(student)


# # # dict with int
# my_dict = {1: 'apple', 2: 'ball'}
# print(my_dict)

# # dictionary with mixed keys
# my_dict = {'name': 'John',1: [2, 4, 3]}
# print(my_dict)

# # nested dictionary
# Dic= {
#  1: 'NAVGURUKUL',
#  2: 'IN',  
#  3:{ 'A' : 'WELCOME','B' : 'To', 'C' : 'DHARAMSALA' }
# }
# print(Dic)



# # (2)
# # Accessing Elements from a Dictionary:
# person={
# 'name':'jack',
# 'age':20,
# 'gender':'male',
# 4:'organisation'}

# result = person['age'] 
# x = person.get("gender")
# # x=person["gender"]
# # print(person[4])
# print(x)
# print(result)


# #(2)(i)get()
# person={
# 'name':'jack',
# 'age':20,
# 'gender':'male',
# 4:{'organisation':'navgurukul','place':'dharamsala'}}
# print(person['gender'])
# print(person[4])
# result=person.get(4)
# person[4]['place']="Paris"
# print(person)  

# # # (3)accessing Elements from a Dictionary:-
# a={"a":1,"b":2,"c":3}
# x=a["c"]
# y=a.get("c")
# print(x)
# print(y)
# print(a["c"])

# a={"a":1,"b":2,"c":{"d":4,"e":5,"f":6}}
# print(a["a"])
# print(a["c"])
# x=a["c"]["e"]
# print(x)


# # #(4) Adding Elements to a Dictionary:
# d= {'Name': 'RAM', 'Age': 17}
# d['ORGANIZATION'] = "NAV GURUKUL"
# d['place'] = 'dharamsala'
# d['student']='pavithra'
# print(d)

# dic= {'Name': 'RAM','Age': 17,}
# dic['student']={  'id':22, 'place':'dharamsala'}
# print(dic)


# # # key exist or not
# a={"brand":  "ford",
# "model":  "mustang",
# "year":  1964}
# if "model" in a:
#     print("Yes, 'model' is one of the keys in the car dictionary.")

# (5)Updating Dictionary 
# person= {'1': 'RAM', '2': 17,}
# person[3] = 'male'
# print(person)

# details={
# 'Name': 'RAM',
# 'Age': 17, 
# 'student': {
# 'id': 22,
# 'place': 'dharamsala'}
# } 
# details['student']['id']=35
# print(details)

# classes ={
# "room1":  "6th",
# "room2":  "7th",
# "room3":  "8th"
# }
# a={"a":1,"b":2,"c":3}
# mydict=classes.copy()
# print(mydict)

# # (6)
# # Removing Elements from a Dictionary:-
# C={
# "brand": "Ford",
# "model": "jason",
# "year": 1964
# }
# C.pop("model")
# print(C)

# p={
# 'name':'jack',
# 'id':22,
# 'place':'dharamsala'
# }
# p.popitem()
# print(p)

# person={
# 'name':'jack',
# 'id':22,
# 'place':'dharamsala'
# }
# del person['place']
# print(person)

# tuple={"a":1,"b":2,"c":3}
# print(tuple)

# # # (8)Iterate through all keys:-
# a = {
#   'Gujarat' : 'Gandhinagar',
#   'Maharashtra' : 'Mumbai',
#   'Rajasthan' : 'Jaipur',
#   'Bihar' : 'Patna'
#   }
# for i in a:
#   print(i)


# # Iterate through all values:-
# a = {
# 'Gujarat' : 'Gandhinagar',
# 'Maharashtra' : 'Mumbai',
# 'Rajasthan' : 'Jaipur',
# 'Bihar' : 'Patna'
# }
# for state in a:
#     print(a[state])


# # iteration ,iteration through all items:-
# for i in a:
#     print({i:a[i]})

# for i in a.values():
#     print(i)
# for i in a.keys():
#     print(i)
# for i,j in a.items():
#     print(i,j)
# print(len(a))


# # (1)question using by python dict:-
# a={1:10, 2:20}
# b={3:30,2:40}
# c={5:50,6:60}
# d={ }
# for i in a:
#     d.update(a)
#     d.update(b)
#     d.update(c)
# print(d)

# # (2)
# dict={"name":"Raju","marks":56}
# for i in dict.keys():
#     if i=="name":
#         print("exist")
#     elif i=="class":
#         print("not exist")

# (3)
# a= {'data1':100,'data2': -54,'data3': 247}
# sum=0
# for i in a.values():
#     sum+=i
# print(sum)

# (4)
# dic= {1: 'NAVGURUKUL',2: 'IN',  3:
# {'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
# del dic[3]["A"]
# print(dic)
    
# # (5)
# a=["one","two","three","four","five"]
# b=[1,2,3,4,5,]
# i=0
# d={ }
# while i<len(a):
#     c=({a[i]:b[i]})
#     d.update(c)
#     i+=1
# print(d)

# # (6)
# dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}

# dic.popitem()
# print(dic)
# keys=["ball",'bat']
# for i in keys:
#     dic.pop(i)
# print(dic)
# o/p{“ball”:”red”,”bat”:4,”wickets”:8}
# b={ }
# for i in dic.items():
    # print(i)
    # b.updtate(i)
# print(dic)
# dic.pop("ball")
# print(dic)
# del dic["ball"]
# print(dic)


# # #********** (7)o/p: ['2', '7', '9', '5', '1']
# a=[{"first":"1"},{"second":"2"},{"third":"1"}, 
# {"four":"5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
# b=[]
# for i in a:
#     for j,k in i.items():
#         if k not in b:
#             b.append(k)
# print(b)


# # (8)Take input of name and marks of 10 students and store to a dictionary.
# a=int(input("enter the number"))
# d={}
# i=0
# while i<a:
#     b=str(input("enter the key"))
#     c=int(input("enter the values"))
#     d.update({b:c})
#     i+=1
# print(d)

# # (9)
# # {'M':1,'I':4,'S':4,'P':2}
# a="mississippi"
# d={}
# i=0
# while i<len(a):
#     j=0
#     c=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c=c+1
#         j=j+1
#     d.update({a[i]:c})
#     i=i+1
# print(d)

# (10)
# dict1 =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# c=0
# for i in dict1:
#     for j in dict1[i]:
#         c=c+1
# print(c)

        

# # (11)
# my_dict= {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# # o/p:-[58,56,100]
# b=[]
# for i in my_dict:
#     if my_dict[i]>50:
#         b.append(my_dict[i])
# print(b)

# (12)
# a={ }
# for i in range(1,16):
#     a.update({i:i*i})
# print(a)

# (13)
# my_dict = {'a':50, 
# 'b':58,
# 'c': 56,
# 'd':40,
# 'e':100, 
# 'f':20}
# b=[]
# for i in my_dict:
#     if my_dict[i]>50:
#         b.append(i)
# print(b)

# # (14)Write a program to sort a dictionary in ascending or descending 
# # according to its values .
# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# # a.popitem()
# # print(a)
# a.update({"deepak":"pavi"})
# # print(a)

# b=sorted(a.items(),key=lambda t:t[1],reverse=False)
# print(dict(a))





from re import A


a="2"
b="4+5i"
c="1"
d=a+b+c
d=(type(d))


