# Comprehension ---> simple, easy and quick way of coding
# Only applicable to Lists, Sets and Dictionaries

import random

lst =[]
for i in range(10):
    lst = lst + [i]
    # lst.append(i)
print("lst:",lst)

# Comprehension Syntax:  <var> = [<expr> for <itr> in <seq> <optional for/if>]

lst = [i for i in range(10)]
print("Using Comprehension:",lst)

lst = [i for i in range(10) if i%2==0]
print("Using Comprehension (Only Even Numbers):",lst)

lst = [i if i%2==0 else '*' for i in range(10)]
print("Using Comprehension:",lst)

lst = [(i , i**2, i**3) for i in range(10)]
print("Using Comprehension:",lst)

lst = [random.randint(10,60) for i in range(10)]
print("Random Numbers:",lst)

lst = [i for i in lst if not 20<=i<=40]    #Only num not 20<=i<=40
print("lst:",lst)

s='Kshitij'
# vowel = ['a','e','i','o','u']
vowel ='aeiou'
# s = ''.join(list(i if not i in vowel else '!' for i in s ))
s = ''.join([i if not i in vowel else '!' for i in s ])
print("s:",s)

print("Unique Numbers of 1,2,3:")
lst = [(i,j,k) for i in range(1,4) for j in range(1,4) for k in range(1,4) if i!=j and i!=k and j!=k]
print("lst:",lst)

print()

print("Sum of 2 Lists:")
lst1 = [1,2,3,4]
lst2 = [5,6,7,8]
lst3 = []
for i in range(len(lst1)):
    lst3.append(lst1[i] + lst2[i])
print("lst3:",lst3)
lst4 = [lst1[i]+lst2[i] for i in range(min(len(lst1),len(lst2)))]
print("lst4 Using Comprehension:",lst4)
lst5 = [i+j for i,j in zip(lst1,lst2)]
print("lst5 Using Comprehension:",lst5)

print()

print("Sum of Matrix:")
mtx = [[1,2,3],
       [4,5,6],
       [7,8,9]]
add = 0
for i in mtx:
    for j in i:
        add += j
print("sum:",add)
lst = [j for i in mtx for j in i]          # Flatten List
print("lst:",lst)
print("sum using comprehension:",sum(lst))

lst = [mtx[i][j] for i in range(3) for j in range(3)]    # Flatten List
print("lst:",lst)

print()

print("Summing of 2 Matrix:")
mtx1 = [[1,2,3],
       [4,5,6],
       [7,8,9]]
mtx2 = [[1,2,3],
       [4,5,6],
       [7,8,9]]
mtx3=[[0,0,0],
       [0,0,0],
       [0,0,0]]
for i in range(len(mtx1)):
    for j in range(len(mtx2)):
        mtx3[i][j] = mtx1[i][j] + mtx2[i][j]
print("mtx3:",mtx3)
mtx4 = [[x+y for x,y in zip(i,j)] for i,j in zip(mtx1, mtx2)]
print("mtx4 Using Comprehension:",mtx4)

print()

# Multiplication of 2 matrix  (H.W)

print("Multiplication of 2 Matrix:")
mtx1 = [[1,2,3],
        [4,5,6],
        [7,8,9]]
mtx2 = [[1,2,3],
        [4,5,6],
        [7,8,9]]
mtx3=[[0,0,0],
       [0,0,0],
       [0,0,0]]
for i in range(len(mtx1)):
    for j in range(len(mtx2[0])):
        for k in range(len(mtx2)):
            mtx3[i][j] += mtx1[i][k] * mtx2[k][j]
mtx4 = [[i for i in range(len(mtx2[0]))] for j in range(len(mtx1))]
print("mtx3:", mtx3)
print("mtx4 Using Comprehension:",mtx4)

print()

print("First n Natural Number in Set:")
st = { i for i in range(10)}
print("st:",st)
st ={1,2,3,4,5,6,7,8,9}
st ={i for i in st if i<4 or i>7}
print("st:",st)

print()

print("In Dictionaries:")
d = {1:'Ram',
     2:'Shyam',
     3:'Krishan',
     4:'Mohan'}
d1 = {k:v for k,v in d.items()}
print("d1:",d1)
d1 = {k:v if k%2==0 else v+'!' for k,v in d.items()}
print("d1:",d1)

d2 = {1:10,
      2:20,
      3:30,
      4:40}
d3 = {k:v**2 for k,v in d2.items()}
print("d2:",d2)
print("d3:",d3)

lst = [1,2,3,4,5,6,7,8,9]

# Read C Lang. Operator Chapter