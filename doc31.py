# # Q31.. Write a Python program to get the top three items in a shop.
# #  Go to the editor
# a={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55,'item5': 24}
# # Expected Output:
# # item4 55
# # item1 45.5
# # item3 41.3

# top1=0
# for i in a.values():
#     if top1<i:
#         top1=i   
# top2=0
# for i in a.values():
#     if top2<i:
#         if top1!=i:
#             top2=i
# top3=0
# for i in a.values():
#     if top3<i:
#         if top1!=i and top2!=i:
#             top3=i
# # print(top1)
# # print(top2)
# # print(top3)
# for j in a:
#     if a[j]==top1:
#         print("top1",{j:a[j]})
# for j in  a:        
#     if a[j]==top2:
#         print("top2",{j:a[j]})  
# for j in a:        
#     if a[j]==top3:
#         print("top3",{j:a[j]})      













# a={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55,'item5': 24}
# b=[]
# for i in a:
#     b.append(a[i])
# for j in range(len(b)):
#     for k in range(len(b)):
#         if b[j]>b[k]:
#             b[j],b[k]=b[k],b[j]
# for l in range(0,3):
#     for m in a:
#         if b[l]==a[m]:
#             print({m:a[m]})


