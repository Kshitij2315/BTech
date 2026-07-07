# To find youngest of Three

print("To find youngest of Three:")

a1 = int(input("Enter age of Ram: "))
a2 = int(input("Enter age of Shyam: "))
a3 = int(input("Enter age of Ajay: "))

youngest = min(a1, a2, a3)

if a1 == a2 == a3:
    print("All are of the same age.")

elif a1 == youngest and a2 == youngest:
    print("Ram and Shyam are the youngest.")

elif a1 == youngest and a3 == youngest:
    print("Ram and Ajay are the youngest.")

elif a2 == youngest and a3 == youngest:
    print("Shyam and Ajay are the youngest.")

elif a1 == youngest:
    print("Ram is the youngest.")

elif a2 == youngest:
    print("Shyam is the youngest.")

else:
    print("Ajay is the youngest.")