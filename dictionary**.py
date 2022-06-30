
# a={"Name":"Raju","Marks":56}
# b=(input("enter number"))
# if b in a:
#     print("Exit")
# else:
#     print("Not else")


# a={"a":2,"b":5,"c":6}
# for i,j in range(a.items()):
#     print(a)



# a={"a":1,"b":2,"c":3,"d":4}
# for i,j in a.items():
#     print((j))
# for i in a:
#     print(i)


# a={1:10,2:20}
# b={3:30,2:40}
# c={5:50,6:60}
# l={}
# for i in (a,b,c):
#     l.update(i)
# for i in l:
#     if i in a:
#         if i in b:
#             l.update({i:a[i]+b[i]})
# print(l)



# a={"k1":1,"k2":2,"k3":3,"k1":4}
# b=a.pop("k2")
# print(b)
# print(a)


# a={"k1","k2","k3"}
# c={ }
# b=c.fromkeys(a,9)
# print(b)

# a={"name":"mona","age":21,"surname":"jaiswak"}
# del a["age"]
# print(a)

# a={"Name":"mona","age":21,"surname":"jaiswak"}
# a.setdefault("name","sona")
# print(a)

# a={'t':1,'p':2,'b':3}
# b=a.popitem()
# print(b)

# a={'t':1,'p':2,'b':3}
# a.popitem()
# print((a))

# a={'t':1,'p':2,'b':3}
# b={}
# for i,j in a.items():
#     print((j))

# a={'t':1,'p':2,'b':3}
# b={}
# for i,j in a.items():
#     print((i))


# a={"a":1,"b":2,"c":3,"d":4}
# sum=0
# for i in a:
#     sum+=a[i]
# print(sum)


# a={"a":1,"b":2,"c":3,"d":4}
# max=0
# for i in a:
#     if max<a[i]:
#         max=a[i]
#         key=i
# print({key:max})


# a={"a":1,"b":2,"c":3,"d":4}
# b=list(a.values())
# i=0
# min=b[0]
# while i<len(b):
#     if min>b[i]:
#         min=b[i]
#     i+=1
# print({min})


# a={"A":1,"B":2,"c":3,"d":4}
# b=a.keys()
# print(b)

# b=a.values()
# print(b)

# b=a.get("B")
# print(b)

# b=a.items()
# print(b)

# # changable
# a={"a":1,"b":2,"c":3,"d":4}
# # a["d"]=10
# # print(a)
# a.update({"e":12})
# print(a)

# # update
# a={"a":1,"b":2,"c":3,"d":4}
# a.update({"d":10})
# print(a)

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# print(myfamily)


