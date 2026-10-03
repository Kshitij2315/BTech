import copy

t = ()
print(type(t))

t1 = (10)
print("t1:",t1,type(t1))

t2 =(10,)
print("t2:",t2,type(t2))

t3 = (10,)*5
print("t3:",t3,type(t3))

t4 = (10)*5
print("t4:",t4,type(t4))

t5 = (10, 'Kshitij', 33.6, 45.2, True)
print("t5:",t5,type(t5),t5[1:4])
print()

for i in t5:
    print(i)

print()

for i in range(len(t5)):
    print(t5[i])

print()

print("Using While Loop:")
i = 0
while i < len(t5):
    print(t5[i])
    i+=1

print()

print("Using Enumerate:")
for i,t in enumerate(t5, start=1):
    print(i,t)

print()

print("List within Tuple")
t6 = ([10,'Kshitij', 33.6, 45.2, True], [15,'Vaishnavi', 33.6, 45.2, True])
print("t6:",t6,type(t6))

print()

print("Tuple within Tuple")
t7 = ((10,'Kshitij', 33.6, 45.2, True), (15,'Vaishnavi', 33.6, 45.2, True))
print("t7:",t7,type(t7))

print()

print("Tuple within List")
t8 = [(10,'Kshitij', 33.6, 45.2, True), (15,'Vaishnavi', 33.6, 45.2, True), (13,'Jaishnavi', 33.6, 45.2, True)]
print("t8:",t8,type(t8))

print()

print("Printing t8 through FOR loop:")
for i,t in enumerate(t8):
    print(i,end=' ')
    for j in t:
        print(j,end=" ")
    print()

print()

print("Printing t8 through WHILE loop:")
i=0
while i < len(t8):
    j=0
    print(i,end=' ')
    while j < len(t8[i]):
        print(t8[i][j],end=' ')
        j+=1
    i+=1
    print()

print()

t9 = t7 + ((17,'Asha', 33.6, 45.2, True),)
print("t9:",t9,type(t9))
print()

t1 = (10,20,30)
t2 = (40,)
t = t1 + t2
print("t:",t,type(t))
print()

tpl = tuple('Kshitij')
print("tuple('Kshitij'):",tpl,type(tpl))      # Conversion

print()

# s1 = "Asha"
# s2 = s1
# print("s1:",s1,id(s1))
# print("s2:",s2,id(s2))
# s1 = s1 + "Pravesh"
# print("s1:",s1,id(s1))
# print("s2:",s2,id(s2))

t1 = (10,20,30)
t2 = t1                          # Alias (Shallow Copy)
print("Alias/Shallow-Copy:")
print("Initially:")
print("t1:",t1,type(t1),"id:",id(t1))
print("t2:",t2,type(t2),"id:",id(t2))
# t1[1] = 200                    # Tuple is immutable
# print("t1:",t1,'    t2:',t2)
t1 = t1 + (50,)                  # Adding new element to verify Alias(Shallow Copy)
print("After - : t1 = t1 + (50,):")
print("t1:",t1,type(t1),"id:",id(t1))
print("t2:",t2,type(t2),"id:",id(t2))

print()

t1 = (10,20,30)
t3 = copy.deepcopy(t1)            # Clone (Deep Copy)
print("Cloning/Deep-Copy:")       # Behaves the same as Alias due to immutability
print("Initially:")
print("t1:",t1,type(t1),"id:",id(t1))
print("t3:",t3,type(t3),"id:",id(t3))
t2 = (40,)
t3 = t3 + t2                      # Adding new element to verify cloning(Deep Copy)
print("After - t3 = t3 + t2:")
print("t1:",t1,type(t1),id(t1))
print("t3:",t3,type(t3),id(t3))

print()

tpl = tuple('Kshitij')            # Search
print("K in tpl:",'K' in tpl)
print("z not in tpl:",'z' not in tpl)

print()

t1 = (50,30,40)
t2 = (10,20,30)            # It is same as t2 = t1
#t2 = t1 + (40,)
print("t2 is t1:",t2 is t1,"id:",id(t2))
print("t1 is t2:",t1 is t2,"id:",id(t1))

print()

emppty = ()
print("not empty: ",bool(emppty))      #Emptiness
print()

t1 = (50,30,40,30)

print("len(t1):",len(t1))
# print("max(t1):",max(t1))
# print("min(t1):",min(t1))
# print("sum(t1):",sum(t1))
print('any(t1):',any(emppty))          # Any one value is true??
print('all(t1):',all(emppty))          # All values are true??  Since Python never finds a False value, the condition "all elements are True" is considered satisfied.
print("sorted(t1):",sorted(t1))        # Returns the output as list
print("reversed(t1):",reversed(t1))    # Returns the address of the object which is an iterable object
r = reversed(t1)

for i in r:
    print(i,end=" ")
print()

print("t1.count(30):",t1.count(30))
print("t1.index(30):",t1.index(30))

rec = ((12,'Ramesh',75.50,85.50,75.50),(10,'Ram',75.50,65.50,69.50),(11,'Ramu',65.50,85.50,75.50))
print(tuple(sorted(rec)))
print(sorted(rec))
print(reversed(sorted(rec)))
print(sorted(rec, key=lambda x: (x[2],x[3])))

# for i in reversed(sorted(rec)):
#     print(i,end=" ")
print()

# Exploding or Unpacking a Tuple
tpl = (10,20,30)
x,y,z = tpl
print(x,y,z)
tpl2 = (1,2,3,tpl,5,6)
print(tpl2)
tpl2 = (1,2,3,*tpl,5,6)          # Exploding
print(tpl2)

# tpl = (1,2,3)
# tpl.remove(3)
# tpl.discard(4)
# print(tpl)
# tpl.clear()
# print(tpl)