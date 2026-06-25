# ASCII- American Standard Code for Information Interchange

s1 = "Kshitij"                           #Collection of unicode characters
s2 = 'Bhardwaj'                          #Unicode----> Beyond English
s3 = '''Pravesh'''
s4 = """Kumar"""
s5 = "This is Kshitij's book"

s6 = 'This is \\ Kshitij\'s \t b\rook'        #Escape Sequence
#s7 = r'This is Kshitij's book'

print(s6)
print("Hello\rHi")

s8 = "Hello"

print(s8[-1]," ",s8[4])
print(s8[-2]," ",s8[3])
print(s8[-3]," ",s8[2])
print(s8[-4]," ",s8[1])
print(s8[-5]," ",s8[0])

for ch in  s8:
    print(ch)

print()

for i in range(len(s8)):
    print(s8[i])

print()

print("Printing reversed string")

i = -1

while i >= len(s8)*-1:
    print(s8[i])
    i -= 1

print()

j = len(s8)-1

while j >= 0:
    print(s8[j])
    j -= 1

s8 = "bye"       # Strings are immutable

print(s8)

full_name = s1 + " " + s2
print(full_name)
print()
print('*'*5)
print()

#Searching a character or string

#search_str = input("Enter a string/character: ")

#print(search_str in full_name)
print()

s9 = 'bye'

print(s8 is s9)        #is → Compares object identity (memory address)
print()

print("Min: ",min(s9))
print("Max: ",max(s9))
print()

#num = [10, 20, 30]

print("Type: ",type(s9))
#print("Type: ",type(num))
print()

print("Memory Address of S8: ",id(s8))  #Functions -----> Do-not need Object Reference
print("Memory Address of S9: ",id(s9))
print()

print("s8.isupper(): ",s8.isupper())    #Methods ----> Called by Object Reference
print("s8.islower(): ",s8.islower())
print("s8.isnumeric(): ",s8.isdigit())
print("s8.isalpha(): ",s8.isalpha())
print("s8.startswith(): ",s8.startswith('by'))
print("s8.endswith(): ",s8.endswith('ye'))

s5 = "this is Kshitij's book"

print("s5.find(): ",s5.find("is"))          # Not Found ---> -1
print("s5.replace(): ",s5.replace("book","Box"))
print("s5.lstrip: ",s5.lstrip())      #Trims leading spaces from the string
print("s5.rstrip(): ",s5.rstrip())
print("S5:",s5)
print("s5.strip(): ",s5.strip())
print("s5.split(): ",s5.split("s"))          #Returns List
print("s5.rsplit(): ",s5.rsplit("s"))
print("s5.partition(): ",s5.partition("s"))  #Returns Tuple
print("s5.rpartition(): ",s5.rpartition("s"))
print("s5.join(): ",s5.join("hello"))
print("-".join(s5))
print("S5 in Upper Case: ",s5.upper())
print("S5 in Lower Case: ",s5.lower())
print("S5 Swap Case: ",s5.swapcase())
print("S5 Capitalize: ",s5.capitalize())
print("S5.title()",s5.title())

num = 567
num1 = str(num)

print("type(num)",type(num))
print("str(num): ",num1)
print("type(str(num)): ",type(str(num)))            #TypeCast's the variable num
print("type(num): ",type(num))                 #TypeCasting ---> one datatype to another

s9 = "1234"
s10 = int(s9)

print(s10)
print("type(int(s9)): ",type(int(s9)))
print("float(s9): ",float(s9))
print("float(num): ",float(num))
print("int(123.57): ",int(123.57))
print("complex(s9): ",complex(s9))
print("complex(2,3): ",complex(2,3))
print("complex(2,3).real: ",complex(2,3).real)  #Returns Real number
print("complex(s9).real: ",complex(s9).real)
print("complex(2,3).imag: ",complex(2,3).imag)  #Return Imaginary Part
print("chr(65): ",chr(65))
print("ord('A'): ",ord('A'))

