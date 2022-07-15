# {student:pavi,subject:maths,class:12}
# a=int(input("enter the number"))
# i=0
# b={}
# while i<a:
#     n=str(input("enter values"))
#     m=int(input("enter values"))
#     b.update({n:m})
#     i+=1
# print(b)


# a=int(input("enter the number"))
# i=0
# b={}
# c=[]
# while i<a:
#     n=(input("enter name"))
#     m=(input("enter subject"))
#     p=int(input("enter class"))
#     b["name"]=n
#     b["subject"]=m
#     b["class"]=p
#     c.append(b)
#     i+=1
# print(c)


# a={"pavi":5,"khusbu":8,"sree":6}
# a={"name":"pavi","class":12,"subject":"maths"}
# a["name"]="khusbhu"
# a["class"]=14
# a["subject"]="science"
# print(a)
# b=a.get("class")
# print(b)


# a={"pavi":34,"bulbul":87}
# # o/p:-{["p","a","v","i"]:34,["b","u","l","b","u","l"]:87}
# b={}
# for i in a:
#     l=[]
#     for j in i:
#         l.append(j)
#     b.update({a[i]:l})
# print(b)   


# a={'khushbu':'katyura','pavipavi':'mom','pinki':"12321",3045:'delted'}
# a={"a":"pavap","b":"mom","c":"riya"}
# b=[]
# for i in a.values():
#     b.append(i)
# print(b)
# i=0
# while i<len(b):
#     if b[i]==b[i][::-1]:
#         print("palindrome")
#     else:
#         print("not palindrome")
#     i+=1

# a=["pavap","madam","priya"]
# i=0
# while i<len(a):
#     if a[i]==a[i][::-1]:
#         print("palindrome")
#     else:
#         print("not palindrome")
#     i+=1


# a={1,2,3,4}
# b=k={}
# for i in a:
#     k[i]={}
#     k=k[i]
# print(b)


# a={"khusbhu":"pavithra","hushna":"pinki"}
# a["khusbhu"]="hushna"
# del a["hushna"]
# a.update({"pavithra":"pinki"})
# print(a)


# a={"a":[1,2,3],"b":[4,5,6],"d":[7,8,9]}
# i=0
# b={}
# for i in a:
#     sum=0
#     for j in range(len(a[i])):
#         sum=sum+a[i][j]
#         b.update({i:sum})
# print(b)
       


# a={"a":12,"b":9,"c":10,"d":15}
# b=[]
# for i in a.values():
#     b.append(i)
# print(b)

