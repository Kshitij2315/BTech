# Dictionary is Key-Value Pair
# Dictionary is also known as 'Map/Associative Array'
# Different Key-Value Pairs are comma(,) separated
# Keys are unique
# Values can be anything
# Keys are immutable whereas Values are mutable

d = {}   # Empty Dictionary
print(d, type(d))

print()

d = {10:"Kshitij Bhardwaj",11:"Pravesh Kumar"}
print(d[10])     # 10 is not index but Key

print()

d = {"10":"Kshitij Bhardwaj","11":"Pravesh Kumar"}
print(d["10"])

print()

#print(d["12"])      # Returns error if key not found

print("Number of Key-Value Pairs:",len(d))

print()

print(d.keys())      # Returns list(all) Keys
print(d.values())    # Returns list(all) Values
print(d.items())     # Returns all(list) Key-Value Pairs in a form of Tuple within List

print()

d = {10:"Kshitij Bhardwaj",
     11:"Pravesh Kumar",
     12:"Ram",
     13:"Shyam",
     14:"Krishan",
     15:"Mohan"}
for i in d.items():         # Output: (k,v)
    print(i)
print()

for k in d.keys():
    print(k)
print()

for v in d.values():
    print(v)
print()

print("Printing Index number with Key-Value Pairs:")
print(d.keys())
print(d.values())
for index,i in enumerate(d.items()):
    print(index,i)
print()

print("Printing Values through Keys:")
for k in d.keys():
    print(d[k])
print()

print("Printing Key-Value Pairs:")        #
for k in d.keys():
    print(k,":",d[k])
print()

print("Fetching out Keys and Values from each item:")
for k,v in d.items():
    print(k,":",v)
print()
for i in d.items():                # Because d.items() returns tuples (Key, Values) and tuples can be accessed by index number
    print(i[0],":",i[1])
print()

print("Adding/Modifying Key-Value Pairs:")
d[16]= "John"                      # Adding/Modifying Key-Value Pairs
print(d)
d[11] = "Sohan"
print(d)                           # Adding/Modifying Key-Value Pairs
print()

print("Deleting Key-Value Pairs:")
del(d[10])                         # Deleting Key-Value Pairs
print(d)
print()

print("Accessing Values from List within Dictionary:")
d1 = {1541:['Ram','Address 1','4518764568','KA'],         # Accessing Values from List within Dictionary
      1542:['Shyam','Address 2','5515646789','HR'],
      1544:['Krishan','Address 3','8515654415','KA']}
for i in d1.items():
    if i[1][3] == 'KA':
        print(i)
print()

print("Accessing Values from Tuple within Dictionary:")
d1 = {1541:('Ram','Address 1','4518764568','KA'),          # Accessing Values from Tuple within Dictionary
      1542:('Shyam','Address 2','5515646789','HR'),
      1544:('Krishan','Address 3','8515654415','KA')}
for i in d1.items():
    if i[1][3] == 'KA':
        print("Name:",i[1][0],"   ","Phone:",i[1][2] )

print()

print("Accessing Values from Set within Dictionary:")
d1 = {1541:{'Ram','Address 1','4518764568','KA'},          # Accessing Values from Set within Dictionary
      1542:{'Shyam','Address 2','5515646789','HR'},
      1544:{'Krishan','Address 3','8515654415','KA'}}
for i in d1.items():
    if 'KA' in i[1]:
        print(i)                    # Cannot access particular element from a set Eg: Name, Phone Number

print()

print("Accessing Values from Dictionary within Dictionary:")
d1 = {1541:{541:['Ram','Address 1','4518764568','KA']},          # Accessing Values from Dictionary within Dictionary
      1542:{542:['Shyam','Address 2','5515646789','HR']},
      1544:{544:['Krishan','Address 3','8515654415','KA']}}      # Most important
for i in d1.items():
    # print(i[1])
    for j in i[1].keys():
        if i[1][j][3] == 'KA':
            print('Name:',i[1][j][0],'  ','Phone:',i[1][j][2])

print()

# Concatenation is not possible
# One object Multi reference = Alias/ Shallow Copy

d1 = {10:"Kshitij Bhardwaj",          # Alias/ Shallow Copy
     11:"Pravesh Kumar",
     12:"Ram",
     13:"Shyam",
     14:"Krishan",
     15:"Mohan"}
d2 = d1
print('id(d2):',id(d2),'   ','id(d1):',id(d1))
d1[14] = 'Krishna'
print("d2:",d2)
a = 5
b = a
c = 5

print()

print("Cloning/ Deep Cloning:")
d1 = {10:"Kshitij Bhardwaj",          # Cloning/ Deep Cloning
     11:"Pravesh Kumar",
     12:{"Ram"},
     13:("Shyam",),
     14:["Krishan"],
     15:"Mohan"}
print("d1:",d1)
d2 = d1.copy()
print('id(d2):',id(d2),'   ','id(d1):',id(d1))

print(bool(d1))    #Emptyness

# del(d1[16])   # Returns Error if key doesn't exist

print()

d3 = {1:"Hello",
      2: d1,
      3:"World"}
print("d3:",d3)

print()

print("Exploding/ Unpacking:")
d4 = {*d1}                     # Explodes only keys in the form of set
print("d4:",d4)
d4 = {**d1, **d3}              # Explodes key value-pair
print("d4:",d4)

print()

d1 = {10:"Kshitij Bhardwaj",
     11:"Pravesh Kumar",
     12:{"Ram"},
     15:("Shyam",),
     13:["Krishan"],
     14:"Mohan"}
print("len(d1):",len(d1))
print("max(d1):",max(d1))
print("min(d1):",min(d1))
print("sorted(d1):",sorted(d1))
print("sorted(d1,reverse=True):",sorted(d1, reverse=True))
print("sum(d1):",sum(d1))
r = reversed(d1)

print("reversed(d1):",end=' ')
for i in r:
    print(i,end=" ")
print()

print()

d1 = {10:"Kshitij Bhardwaj",
     11:"Pravesh Kumar",
     12:{"Ram"},
     15:("Shyam",),
     13:["Krishan"],
     14:"Mohan",
     None: 'none',
     False: 'false',
     True: 'true'}
print("d1:",d1)
print("all(d1):",all(d1))
print("any(d1):",any(d1))
print("13 in d1:",13 in d1)
print("d2 is d1:",d2 is d1)

print()


print("If values are a Tuple:")
d1 = {10:"Kshitij Bhardwaj",
     11:"Pravesh Kumar",
     12:{"Ram"},
     15:("Shyam",),
     13:["Krishan"],
     14:"Mohan"}
# print("max(d1.values():",max(d1.values()))    # Returns error as the values are string
# print("min(d1.values()):",min(d1.values()))

print()

print("If values are int:")
d1 = {10: 10,
     11: 11,
     12: 12,
     15: 15,
     13: 13,
     14: 14}
print("max(d1.values():",max(d1.values()))    # Can find max of a value if they are int
print("min(d1.values()):",min(d1.values()))

print()

print("If values are String:")
d1 = {10: '10',
     11: '11',
     12: '12',
     15: '15',
     13: '13',
     14: 'AB'}
print("max(d1.values():",max(d1.values()))    # Can find max of a value if they are string
print("min(d1.values()):",min(d1.values()))   # min(), max() only works on basicclasses data-type or one type of container-type

print()

print("If keys are a String:")
d1 = {'10':"Kshitij Bhardwaj",
     '11':"Pravesh Kumar",
     '12':{"Ram"},
     '15':("Shyam",),
     'AB':["Krishan"],
     'CD':"Mohan"}
print("max(d1):",max(d1))             # Can find max of a key if they are strings
print("min(d1):",min(d1))

print()

print("If keys are a Tuple:")
d1 = {('10',):"Kshitij Bhardwaj",
      ('11',):"Pravesh Kumar",
      ('12',):{"Ram"},
      ('15',):("Shyam",),
      ('CD',):["Krishan"],
      ('AB','EF'):"Mohan"}
print("max(d1):",max(d1))             # Can find max of a key if they are tuple of same data-type and with single object in it.
print("min(d1):",min(d1))

print()

print("Dictionary Methods:")
d1 = {1:"Ram",
      2:"Shyam",
      3:"Krishan",
      4:"Mohan"}
print("d1:",d1)
print('d1.get(5):',d1.get(5))
# print('d1[5]:',d1[5])        # Returns Error if key doesn't exist
print('d1.get(5):',d1.get(5,'Key Not Found'))

d = {3: 'John'}
d1.update(d)
print('d1 after update:',d1)

d = {5: 'Krishan'}
d1.update(d)
print('d1 after update:',d1)

print('d1.popitem():',d1.popitem())
print('d1:',d1)
print('d1.pop(3):',d1.pop(3))
print('d1:',d1)