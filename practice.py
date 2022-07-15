# a=int(input("enter number"))
# i=0
# b={}
# while i<a:
#     x=input("enter key")
#     y=int(input("enter value"))
#     b.update({x:y})
#     i+=1
# print(b)

# a=int(input("enter number"))
# i=0
# b={}
# c=[]
# while i<a:
#     x=input("enter Name:")
#     y=(input("enter Subject:"))
#     z=int(input("enter Marks:"))
#     b["Name"]=x
#     b["Subject"]=y
#     b["Marks"]=z
#     c.append(b)
#     i+=1
# print(c)


# a={"name":"pavi","class":12,"subject":"maths"}
# # ** add values
# a["name"]={"pavi":54}
# print(a)
###update::-
# a["name"]="khusbhu"
# a["class"]=14
# a["subject"]="science"
# print(a)
###add items:-
# a["marks"]=98
# a["score"]=60
# print(a)
#**del::-
# del a["class"]
# del a["subject"]
# print(a)
#**pop::-
# a.pop("class")
# a.pop("subject")
# print(a)
#***a.get[]::-
# b=a.get("class")
# print(b)
##***popiteam::-
# a.popitem()
# a.popitem()
# print(a)
###remove and add::-
# a.pop("class")
# a["score"]=80
# a["name"]="sanju"
# a["name"]=["Name"]["abhi"]
# print(a)
# a.clear()
# print(a)

# # #********** (7)o/p: ['2', '7', '9', '5', '1']
# a=[{"first":"1"},{"second":"2"},{"third":"1"}, 
# {"four":"5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
# b=[]
# for i in a:
#     for j,k in i.items():
#         if k not in b:
#             b.append(k)
# print(b)


# n=int(input('enter any number'))
# i=2
# while i<=n:
#     print(i)
#     i=i+5


# a={"pavi","navit","abhish"}
# b={}
# for i in a:
#     b.update({i:len(i)})
# print(b)

# a={"a":2,"b":4,"c":3,"d":1,"e":0,"f":9}
# b=[]
# for i in a:
#     b.append([i,a[i]])
# print(b)
# for i in range(0,len(b)-1):
#     for j in range(0,len(b)-1):
#         if b[j][1]<b[j+1][1]:
#             b[j][1],b[j+1][1]=b[j+1][1],b[j][1]
# print(b)


# a=["a","b","c","d","e","f"]
# b=["g","h","i","j","k","l"]
# i=0
# c={}
# while i<len(a):
#     d=a[i]+b[-i]
#     c.update({d:i})
#     i+=1
# print(c)



# a={1:10,2:20,3:30,4:40}
# n=int(input("enter the number"))
# if n in a:
#     print("exist")
# elif n not in a:
#     print("not exists")
# print(a)


# a={"khusbhu":[4,4],"sree":[6,2,1],"pavi":[3,9,6]}
# b={}
# for i in a:
#     sum=0
#     for j in range(len(a[i])):
#         sum+=a[i][j]
#         b.update({i:sum})
# print(b)


# # ##o/p::{"pavithra":{"sername":kuruba,"age":16},
# # "meena":{"sername":"mahto","age":17},
# # "tanuja":{"sername":"khose","age":18}}
   
# a=["pavithra","meena","tanuja"]
# b=[["kuruba",14],["mahto",15],["khose",16]]
# c={}
# for i in a:
#     for j,k in b.items():
#         c.update({i:k})
# print(c)

# ###o/p{1:{"name":"pavi","age":16}
# #       2:{"name":"abhi","age":18}}
# a=int(input("enter number"))
# i=0
# b={}
# c=[]
# while i<a:
#     x=int(input("enter number"))
#     y=str(input("enter number"))
#     z=int(input("enetr age"))
#     b["name"]=y
#     b["age"]=z
#     b.update({x:{y:z}})
#     c.append(b)
#     i+=1
# print(c)

# a={1:["a","b"],2:["c","d"]}
# b=list(a.values())
# for i in b[0]:
#     for j in b[1]:
#         print(i+j)

# a={"a":{"1":[4,5,6]},"b":{"2":[3,9,2]},"c":{"3":[4,5,6]}}
# # o/p--[4,5,6,3,9,2,4,5,6]
# b=[]
# for i in a.values():
#     for j,k in i.items():
#         b.append(k)
# print(b)


# a=[1,2,3,4,1]
# def fun():
#     i=0
#     sum=0
#     while i<len(a):
#         sum=sum+a[i]
#         i=i+1
#     print(sum)
# fun()

# a=["swathi","pavithra","baby"]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[j]>a[i]:
#             b=a[i]
#             a[i]=a[j]
#             a[j]=b
# print(a)


# d={}
# b=sorted(a.keys())
# c=sorted(a.values())
# for i in range(len(b)):
#     for i in range(len(c)):
#         d.update({b[i]:c[i]})
# print(d)


# i=5
# while i>=1:
#     j=6
#     while j>i:
#         print(j-i,end=" ")
#         j-=1
#     print()
#     i-=1


# for i in range(0,len(a)):
#     for j in a[i]:
#         if a[i][j] not in b:
#              b.append(a[i][j])
# print(b) 


# a=str(input("enetr number"))
# i=0
# c={}
# d={}
# while i<len(a):
#     b=int(a[i])
#     if b==1:
#         print({"one":1})
#     elif b==2:
#         print({"two":2})
#     elif b==3:
#         print({"three":3})
#         c.update(b)
#     i+=1




# a=int(input("enter numbre"))
# b=int(input("enter number"))
# print(str(a*2)+str(b*2))