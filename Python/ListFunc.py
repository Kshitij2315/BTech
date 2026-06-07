#WAF which can return max out of list
'''import sys

def maxList(lst):
    if bool(lst):
        a = lst[0]

        for i in range(len(lst)):
            if lst[i] > a:
                a =lst[i]

        for i in lst:
            if i > a:
                a = i

        #print("Greatest Num: ", a)
        return a
    else:
        print("List is empty")
        sys.exit(0)'''

def sumList(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

lst = [2,4,5]
names = ["ram","Ramesh","Ramit"]
lst1 = list("Kshitij")

add = sumList(lst)
#max = maxList(lst)

#print("list1: ",lst1)
print("Sum: ",add)
print("Greatest Character: ", max(lst1))
print("Greatest Num: ", max(lst))
print("Greatest Name: ", max(names))
print("Sum of num: ", sum(lst))

#any()
print(any(lst))

l1 = [17,2,13,64,25,6,37,58,49]
l2 = [0,0,0,0,0]
l3 = [1,0,0,0,0]
l4 = []

print("any(l1): ",any(l1),"\nany(l2): ",any(l2),"\nany(l3): ",any(l3),"\nany(l4): ",any(l4))
print("bool(l1): ",bool(l1),"\nbool(l2): ",bool(l2),"\nbool(l3): ",bool(l3),"\nbool(l4): ",bool(l4))
print("all(l1): ",all(l1),"\nall(l2): ",all(l2),"\nall(l3): ",all(l3),"\nall(l4): ",all(l4))

del(l1[2])                         #Function
print("Using Function: L1: ",l1)

#l1.remove(4)                       #Method
print("Using Method: L1: ",l1)

l5 = sorted(l1)
print("Sorted: By Default Accending Order L1--->L5: \n",l1,"---->",l5)

l6 = sorted(l1, reverse = True)
print("Sorted: Decending Order L1--->L6: \n",l1,"---->",l6)

l7 = reversed(l1)
print("Reversed: L1--->L7: \n",l1,"---->",list(l7))