# Finding whether a number is Even or Odd using Flag

n = int(input("Enter a number: "))
flag = 0

if n % 2 == 0:
    flag = 1

if flag == 0:
    print("Odd Number")
else:
    print("Even Number")