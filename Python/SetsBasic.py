# import copy

st = {1,5,6,10}      #Declaring a set
print(st,type(st))

st1 = {None}
print(st1,type(st1),len(st1))

st1 = set()                      #Empty set
print(st1,type(st1),len(st1))

# Hashing: Hash value is calculated (Where to store the object)

st.add(2)
print(st)

# st1 = {5,7}
# st2 =  st + st1    # Cannot concatenate and merge two sets because it is unordered
# print(st2)

# a = h(k)   a---> address (hash code/value), h()---> hash func., k---> key
# Formula of Hash Function is internally known to the system eg: k%10*5 (not exact formula)... Might be known by system engineers

st3 = {2,(30,40,50),3,4,5,6,10}    # Set within Set not possible because sets cannot contain any mutable container type
print(st3)

# lst = [10,2,3,4,5,6]
# print(lst)

st4 = st3             # Shallow Copy/ Alias
print(id(st4), id(st3))
st3.add(20)
print(st3,st4)

# st4 = copy.deepcopy(st3)
# print(id(st3),id(st4))

for i,x in enumerate(st4):
    print(i,x)

# frozen set: Immutable

st4 = frozenset(st3)
print(id(st3),id(st4))
# st4.add(43)   # Cannot use add() as it is frozenset

print(st4,type(st4))
# Searching
print(20 in st4)

# st4 = copy.deepcopy(st3)
# print(id(st3),id(st4))
# Identity
print(st3 is st4)
st4 = st3
print(st3 is st4)           # is: checks the address

# st4 = copy.deepcopy(st3)
# print(st4 == st3)           # ==: checks the objects

#Emptiness
st4 = set()
print(bool(st4))

st = {'Kshitij', 30, 30.5, 3+2j}
print(st)

# Bitwise Operator
p = 13         # 1101
q = 12         # 1100
# r = p&q        # 1100
# r = p|q        # 1101
r = p ^ q      # 0001
print(r)

print()

name = {"Ram","Shyam","Krishan","Mohan"}
st = {10,5,7,6}
print(st)
print(max(name))
print(min(name))
print(sorted(name))     # Returns List
print(any(name))
print(all(name))
st1 = {0, None}
print(any(st1))
print(all(st1))
st1 = set()
print(any(st1))         # Checks for True value
print(all(st1))         # Checks for False value

print()

st = {0, 1, 2, 3}
st1 = {'a', 'b', 'c'}
st.add('Ram')
print(st)
st.update(st1)         # Concatenate
print(st)
st2 = st.copy()        # Cloning (Deepcopy)---> same as copy.deepcopy(st)
print(id(st2),id(st))
print(st)
st.remove('Ram')
print(st)
st.discard("Rama")     # Does not return an error when object not found in the set whereas remove does return an error
print(st)
st.clear()             # Deletes all objects... makes empty set

print()

t = {1,2,3,4,5,6}
x = {3,4,5}
print(t.issuperset(x)) 
print("t>=x:",t>=x)                           # This also finds the Superset
print(x.issubset(t))
print("x<=t:",x<=t)                           # This also finds the Subset
x = {3,4,5,-1,7}
print(t.union(x))
print("t|x:",t|x)                     # This also finds the Union
print(t.intersection(x))
print("t&x:",t&x)                     # This also finds the Intersection
print(t.difference(x))
print("t-x:",t-x)                     # This also finds the Difference
print(x.difference(t))
print("x-t:",x-t)                     # This also finds the Difference
print(x.symmetric_difference(t))
print("x^t:",x^t)                     # This also finds the Symmetric-Difference
x|=t                       # Stores Union
x&=t                       # Stores intersectio
x-=t                       # Stores difference
x^=t                      # Stores symmetric difference

print()

st ={1,2,3}
y = {'a','b',*st}      #Explode
print(y)

print()

lst = [1,2,2,3,4,5]
st = set(lst)
print(st)

print()

print(list(set(lst)))    # Removing duplicates from the list

print()

tpl = (1,2,3,3,4,5.151,"Kshitij",2+7j)
print(tpl)
st = set(tpl)
print(st)

print()

print(list(st))
print(list(tpl))

s = 'Kshitij Bhardwaj'
print(list(s))

print(s.split())