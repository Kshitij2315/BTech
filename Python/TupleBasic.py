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
print("tuple('Kshitij'):",tpl,type(tpl))

print()

t1 = (10,20,30)
t2 = t1                          # Alias (Shallow Copy)
print("Alias/Shallow-Copy:")
print("t1:",t1,type(t1))
print("t2:",t2,type(t2))
# t1[1] = 200                    # Tuple is immutable
# print("t1:",t1,'    t2:',t2)
t1 = t1 + (50,)                  # Adding new element to verify Alias(Shallow Copy)
print("t1:",t1,type(t1))
print("t2:",t2,type(t2))         # Need to Ask Doubt

print()

t1 = (10,20,30)
t3 = copy.deepcopy(t1)            # Clone (Deep Copy)
print("Cloning/Deep-Copy:")
print("t1:",t1,type(t1))
print("t3:",t3,type(t3))
t2 = (40,)
t3 = t3 + t2                      # Adding new element to verify cloning(Deep Copy)
print("t1:",t1,type(t1))
print("t3:",t3,type(t3))

print()

tpl = tuple('Kshitij')            # Search
print("K in tpl:",'K' in tpl)
print("z not in tpl:",'z' not in tpl)

print()

t1 = (10,20,30)
t2 = t1
#t2 = t1 + (40,)
print("t2 is t1:",t2 is t1)
print("t1 is t2:",t1 is t2)

print()

emppty = ()
print("not empty: ",bool(None))      #Emptiness
print()