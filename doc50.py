
# Q50.Write a Python program to convert a given dictionary into a list of lists.
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# Original Dictionary:
# {'1':'Austin Little','2':'Natasha Howard','3': 'Alfred Mullins','4':'Jamie Rowe'}
# Convert the said dictionary into a list of lists:
# [['1','Austin Little'],['2','Natasha Howard'],['3','Alfred Mullins'],
# ['4','Jamie Rowe']]

# a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# b=[]
# for i in a:
#         b.append([i,a[i]])
# print(b)



# a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# b=[]
# for i in a:
#     for j in a[i]:
#         b.append([i,j])
# print(b)